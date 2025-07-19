# Overfitting vs Underfitting in Machine Learning

Understanding **model generalization** is critical to building robust ML systems. Two common issues arise when a model doesn’t generalize well:

---

## 🎯 Overfitting

Overfitting occurs when a model learns not only the true patterns in the training data but also the noise and random fluctuations. As a result, the model performs **exceptionally well on training data** but fails to generalize to unseen (test) data.

### 📌 Characteristics:
- High accuracy on training data
- Low accuracy on validation/test data
- High variance (model is sensitive to input data)

### 🧠 Why It Happens:
- The model is too complex (too many parameters)
- The training data is limited or noisy
- No regularization or poor regularization
- Model trained too long (e.g., too many epochs in neural nets)

### 🛠️ Remedies:
- **Reduce model complexity**: e.g., shallower trees, fewer layers
- **Use regularization**:
    - L1 (Lasso): Shrinks some weights to zero (feature selection)
    - L2 (Ridge): Penalizes large weights, reduces variance
- **Cross-validation** to catch overfit early
- **Early stopping** (in deep learning)
- **More training data**

---

## 🎯 Underfitting

Underfitting occurs when a model is too simple to capture the underlying pattern in the data. It performs **poorly on both training and test sets**.

### 📌 Characteristics:
- Low training and test accuracy
- High bias (model makes overly simplistic assumptions)

### 🧠 Why It Happens:
- The model is too basic for the data (e.g., linear model for nonlinear problem)
- Not enough features or information in the data
- Features not engineered properly
- Model undertrained (e.g., not enough iterations)

### 🛠️ Remedies:
- **Increase model complexity** (e.g., add layers, use nonlinear models)
- **Improve feature engineering** (add interaction terms, domain knowledge)
- **Reduce regularization strength**
- **Train for longer** (in iterative models)

---

## ⚖️ Bias-Variance Tradeoff

This is a fundamental concept describing the tension between underfitting and overfitting.

| Term       | Description                                                  |
|------------|--------------------------------------------------------------|
| **Bias**   | Error from wrong assumptions (underfitting)                  |
| **Variance** | Error from model being too sensitive to training data (overfitting) |
| **Overfitting** | Low bias, high variance                                |
| **Underfitting** | High bias, low variance                               |

The goal of any model is to find the **sweet spot** with low bias and low variance.

---

## 📊 Real-World Analogy

Think of overfitting like a student who memorizes answers without understanding — they ace practice tests but fail real exams.  
Underfitting is like a student who barely studies — they struggle with both practice and real tests.

---

## 🧪 Code Demonstration

You can view a polynomial regression example that demonstrates both extremes:

- [Notebook: Overfitting vs Underfitting Visualization](./overfitting_vs_underfitting.ipynb)

---

## 📚 Further Reading
- [Bias-Variance Tradeoff – ML Mastery](https://machinelearningmastery.com/gentle-introduction-to-the-bias-variance-trade-off-in-machine-learning/)
- [StatQuest: Overfitting and Underfitting](https://www.youtube.com/watch?v=EuBBz3bI-aA)
