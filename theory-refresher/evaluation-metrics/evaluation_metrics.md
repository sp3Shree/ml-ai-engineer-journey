# Evaluation Metrics in Machine Learning

---

## 🔍 Why Are Evaluation Metrics Important?

The right evaluation metric helps you:

- Select the best model
- Tune hyperparameters effectively
- Align performance with real-world business goals
- Avoid misleading interpretations (e.g., accuracy on imbalanced data)

📌 **Different tasks require different metrics.**  
There’s no universal best metric.

---

## 🧠 Classification Metrics

Used when the output is **categorical** (e.g., spam/not spam, fraud/no fraud).

---

### ✅ 1. Accuracy

**Definition**:  
The proportion of correctly predicted instances out of all instances.

$$
\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}
$$

**Limitation**: Misleading when classes are imbalanced.

---

### ✅ 2. Precision, Recall, F1-Score

| Metric    | Description                          | Formula                                | Use When...                          |
|-----------|--------------------------------------|----------------------------------------|--------------------------------------|
| Precision | How many predicted positives are correct | $$( \frac{TP}{TP + FP} )$$             | False positives are costly (e.g., email spam) |
| Recall    | How many actual positives are caught  | $$( \frac{TP}{TP + FN} )$$             | False negatives are costly (e.g., cancer detection) |
| F1-Score  | Harmonic mean of precision and recall | $$( 2 \cdot \frac{P \cdot R}{P + R} )$$ | Balance between precision & recall |

---

### ✅ 3. Confusion Matrix

|            | Predicted Positive | Predicted Negative |
|------------|--------------------|--------------------|
| Actual Pos | True Positive (TP) | False Negative (FN)|
| Actual Neg | False Positive (FP)| True Negative (TN) |

Used to derive precision, recall, and accuracy.

---

### ✅ 4. ROC Curve & AUC (Area Under Curve)

- Plots True Positive Rate vs False Positive Rate at different thresholds
- AUC = area under this curve
- Closer to 1.0 = better model
- Great for **binary classification** problems

---

## 📊 Regression Metrics

Used when the output is **continuous** (e.g., house price, temperature).

---

### ✅ 1. Mean Squared Error (MSE)

$$
\text{MSE} = \frac{1}{n} \sum (y_{\text{true}} - y_{\text{pred}})^2
$$

- Penalizes **large errors** more heavily
- Sensitive to outliers

---

### ✅ 2. Root Mean Squared Error (RMSE)

$$
\text{RMSE} = \sqrt{\text{MSE}}
$$

- More interpretable in the same units as the target

---

### ✅ 3. Mean Absolute Error (MAE)

$$
\text{MAE} = \frac{1}{n} \sum |y_{\text{true}} - y_{\text{pred}}|
$$

- Less sensitive to outliers than MSE

---

### ✅ 4. R² Score (Coefficient of Determination)

$$
R^2 = 1 - \frac{\text{SS}_{\text{res}}}{\text{SS}_{\text{tot}}}
$$

- Measures proportion of variance explained by the model
- Ranges from 0 (no fit) to 1 (perfect fit)
- Can be **negative** if the model performs worse than the mean

---

## 🔍 Choosing the Right Metric

| Problem Type        | Suggested Metrics                      |
|---------------------|----------------------------------------|
| Binary Classification | Accuracy, F1, ROC-AUC, Confusion Matrix |
| Imbalanced Classification | Precision, Recall, F1, ROC-AUC        |
| Multi-class Classification | Macro-averaged F1, Confusion Matrix   |
| Regression           | MAE, RMSE, R²                          |

---

## 💡 Real-World Analogy

Imagine a medical test:
- **High precision** = When the test says you’re sick, you probably are
- **High recall** = It catches most of the sick people
- **F1 Score** = Balances both (e.g., in critical screening scenarios)
