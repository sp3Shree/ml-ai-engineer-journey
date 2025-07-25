import os
import json
import argparse
import requests
import shutil
from pathlib import Path
from git import Repo
from dotenv import load_dotenv

# Load from .env file into environment
load_dotenv()

EXCLUDED_DIRS = {"venv", "__pycache__", ".git", "node_modules", "build", "dist"}
CHUNK_SIZE = 400
OVERLAP = 50

LANGUAGE_EXTENSIONS = {
    "Python": [".py", ".ipynb", ".md", ".txt", ".rst", ".yml", ".yaml", ".json", ".toml"],
    "JavaScript": [".js", ".jsx", ".json", ".md", ".yml"],
    "TypeScript": [".ts", ".tsx", ".json", ".md", ".yml"],
    "Java": [".java", ".xml", ".md", ".properties", ".json"],
    "Go": [".go", ".mod", ".sum", ".md", ".yml"],
    "Rust": [".rs", ".toml", ".md"],
    "C++": [".cpp", ".h", ".hpp", ".md"],
    "C": [".c", ".h", ".md"],
    "Shell": [".sh", ".md", ".env"],
    "HTML": [".html", ".css", ".js", ".md"],
    "Dockerfile": ["Dockerfile", ".env", ".md"],
}


def get_primary_language(repo_url: str, token: str = None) -> str:
    parts = repo_url.rstrip("/").split("/")
    user, repo = parts[-2], parts[-1]
    api_url = f"https://api.github.com/repos/{user}/{repo}"
    headers = {"Authorization": f"token {token}"} if token else {}
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        return response.json().get("language", "Python")
    except Exception as e:
        print(f"⚠️ Error fetching language from GitHub API: {e}")
        return "Python"


def get_allowed_extensions(language: str) -> list:
    return LANGUAGE_EXTENSIONS.get(language, [".py", ".md", ".txt"])


def should_include(path: Path, allowed_exts) -> bool:
    if path.name == "Dockerfile":
        return True
    return (
            path.suffix in allowed_exts and
            not any(part in EXCLUDED_DIRS for part in path.parts)
    )


def chunk_text(text, chunk_size=CHUNK_SIZE, overlap=OVERLAP):
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        chunk = words[start:start + chunk_size]
        chunks.append(" ".join(chunk))
        start += chunk_size - overlap
    return chunks


def extract_text_from_repo(repo_path: Path, allowed_exts):
    all_chunks = []
    for path in repo_path.rglob("*"):
        if not path.is_file() or not should_include(path, allowed_exts):
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
            chunks = chunk_text(text)
            for i, chunk in enumerate(chunks):
                all_chunks.append({
                    "file_path": str(path.relative_to(repo_path)),
                    "chunk_id": i,
                    "text": chunk
                })
        except Exception as e:
            print(f"⚠️ Failed to read {path}: {e}")
    return all_chunks


def save_chunks(chunks, output_path="data/chunks/chunks.jsonl"):
    os.makedirs(Path(output_path).parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        for chunk in chunks:
            f.write(json.dumps(chunk) + "\n")
    print(f"✅ Saved {len(chunks)} chunks to {output_path}")


def clone_repo(repo_url: str, dest_path: Path, force: bool = False):
    if dest_path.exists():
        if force:
            print(f"🧹 Removing existing repo at {dest_path}")
            shutil.rmtree(dest_path)
        else:
            print(f"📂 Using existing repo at {dest_path}")
            return
    print(f"🔄 Cloning {repo_url} into {dest_path}")
    Repo.clone_from(repo_url, dest_path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True, help="GitHub repo URL (e.g., https://github.com/user/repo)")
    parser.add_argument("--token", help="GitHub token (or set GITHUB_TOKEN env var)")
    parser.add_argument("--force_clone", action="store_true", help="Delete and re-clone repo")
    parser.add_argument("--local_path", default="data/raw", help="Local path to clone repo")
    parser.add_argument("--output", default="data/chunks/chunks.jsonl", help="Where to write output chunks")

    args = parser.parse_args()
    github_token = args.token or os.getenv("GITHUB_TOKEN")

    # Clone the repo
    repo_path = Path(args.local_path)
    clone_repo(args.repo, repo_path, force=args.force_clone)

    # Detect primary language and get allowed extensions
    language = get_primary_language(args.repo, github_token)
    print(f"🔍 Primary language detected: {language}")
    allowed_exts = get_allowed_extensions(language)

    # Extract and save chunks
    chunks = extract_text_from_repo(repo_path, allowed_exts)
    save_chunks(chunks, args.output)


if __name__ == "__main__":
    main()