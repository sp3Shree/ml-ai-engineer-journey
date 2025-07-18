# Regression vs Classification

---

## 🔍 What is Regression?

**Regression** is a type of supervised learning used when the target output is a **continuous numerical value**.

**Use Cases**:
- Predicting house prices
- Estimating customer lifetime value
- Forecasting sales

**Common Algorithms**:
- Linear Regression
- Ridge/Lasso Regression
- Random Forest Regressor
- Gradient Boosting Regressor

---

## 🔍 What is Classification?

**Classification** is used when the target output is a **discrete category or label**.

**Use Cases**:
- Email spam detection (spam or not)
- Medical diagnosis (disease present or not)
- Image recognition (cat, dog, etc.)

**Common Algorithms**:
- Logistic Regression
- Random Forest Classifier
- Support Vector Machine (SVM)
- XGBoost Classifier

---

## 📊 Comparison Table

| Feature         | Regression                   | Classification              |
|-----------------|-------------------------------|------------------------------|
| Output          | Continuous value              | Discrete category            |
| Evaluation      | MSE, RMSE, R²                 | Accuracy, Precision, F1      |
| Examples        | Predict price, temperature    | Predict labels, categories   |
| Models          | Linear Regression, GBM        | Logistic Regression, SVM     |

---

## 🧪 Code Examples

See the runnable code examples:

- [Regression Example: Predict Boston Housing Prices](./code-examples/regression_example.py)
- [Classification Example: Predict Iris Species](./code-examples/classification_example.py)
- [Notebook: Regression vs Classification](./code-examples/regression_vs_classification.ipynb)

To run the `.py` versions:

```bash
python theory-refresher/code-examples/regression_example.py
python theory-refresher/code-examples/classification_example.py
