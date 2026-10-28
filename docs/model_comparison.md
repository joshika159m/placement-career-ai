# Baseline Machine Learning Model Evaluation Report

**Dataset:** `data/processed/campus_recruitment_encoded.csv` (9,928 rows, 10 features, 1 binary target)  
**Evaluation Protocol:** 80/20 Stratified Split (`random_state=42`)  
**Data Leakage Prevention:** Preprocessing pipelines fitted strictly on the training set (`X_train`); test set remained completely unseen until final evaluation.

---

## 1. Experimental Setup & Data Partitioning

- **Total Samples:** 9,928
- **Training Set Size:** 7,942 samples (80.0%)
- **Test Set Size:** 1,986 samples (20.0%)

### Class Balance Across Splits:
| Split | NotPlaced (`0`) Count | NotPlaced (`0`) % | Placed (`1`) Count | Placed (`1`) % | Total |
|---|---|---|---|---|---|
| **Training Set** | 4,641 | 58.44% | 3,301 | 41.56% | 7,942 |
| **Test Set** | 1,160 | 58.41% | 826 | 41.59% | 1,986 |

*Stratification guaranteed exact preservation of the ~58.43% unplaced vs ~41.57% placed ratio across both partitions.*

---

## 2. Models & Preprocessing Architecture

1. **Logistic Regression:**
   - Numerical features (`CGPA`, `Internships`, `Projects`, `Workshops_Certifications`, `AptitudeTestScore`, `SoftSkillsRating`, `SSC_Marks`, `HSC_Marks`) scaled via `StandardScaler()`.
   - Binary features (`ExtracurricularActivities`, `PlacementTraining`) passed through unscaled.
   - Scaler fitted strictly on `X_train`.
2. **Decision Tree Classifier:**
   - Default CART baseline (`random_state=42`), unscaled.
3. **Random Forest Classifier:**
   - Ensemble of 100 decision trees (`random_state=42`), unscaled.
4. **Gradient Boosting Classifier:**
   - Sequential gradient boosted trees (`random_state=42`), unscaled.

---

## 3. Baseline Performance Comparison Table

*Sorted primarily by **F1 Score** and secondarily by **ROC-AUC**.*

| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC | TN | FP | FN | TP |
|---|---|---|---|---|---|---|---|---|---|
| **Logistic Regression** | 0.8097 | 0.7732 | 0.7676 | **0.7704** | **0.8854** | 974 | 186 | 192 | 634 |
| **Gradient Boosting** | 0.8072 | 0.7772 | 0.7518 | **0.7643** | **0.8858** | 982 | 178 | 205 | 621 |
| **Random Forest** | 0.7966 | 0.7755 | 0.7191 | **0.7462** | **0.8747** | 988 | 172 | 232 | 594 |
| **Decision Tree** | 0.7266 | 0.6758 | 0.6586 | **0.6671** | **0.7187** | 899 | 261 | 282 | 544 |

---

## 4. Confusion Matrix & ROC Curve Visualizations

Confusion matrix plots and ROC curves have been generated and saved under `docs/models/`:
- **All Confusion Matrices:** `docs/models/all_confusion_matrices.png`
- **ROC Curves Comparison:** `docs/models/roc_curves_comparison.png`
- **Individual Plots:**
  - `docs/models/confusion_matrix_logistic_regression.png`
  - `docs/models/confusion_matrix_decision_tree.png`
  - `docs/models/confusion_matrix_random_forest.png`
  - `docs/models/confusion_matrix_gradient_boosting.png`

---

## 5. Detailed Metric Analysis

### A. F1 Score Leader
- **Model:** **Logistic Regression**
- **F1 Score:** **0.7704**
- **Precision:** 0.7732 | **Recall:** 0.7676
- Balances False Positives (FP = 186) and False Negatives (FN = 192), making it highly suitable for placement recommendation where both over-promising and under-promising are costly.

### B. ROC-AUC Leader
- **Model:** **Gradient Boosting**
- **ROC-AUC:** **0.8858**
- Measures discrimination threshold quality across all potential probability decision thresholds, critical for extracting continuous placement probability percentages in the web app.

### C. Decision Tree vs Ensemble Methods
- The unconstrained Decision Tree displays the expected high-variance behavior, achieving lower generalization scores due to greedy splitting on unpruned leaves.
- Random Forest and Gradient Boosting substantially improve precision, recall, and stability by reducing tree variance and bias respectively.

---

## 6. Model Selection Governance & Guidelines

> **Important Boundary Rule:**
> In accordance with project standards:
> - **No final model is selected automatically based purely on accuracy.**
> - Accuracy can be deceptive on tabular datasets and does not account for the trade-off between Precision (confidence in predicting placed) and Recall (identifying placed students without missing them).
> - Hyperparameter tuning has **not** been performed yet.
> - The test set was strictly held out and was **not** used for tuning or greedy iterative selection.
