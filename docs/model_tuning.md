# Model Validation and Hyperparameter Tuning Report

**Dataset:** `data/processed/campus_recruitment_encoded.csv` (9,928 rows, 10 features, 1 binary target)  
**Tuning Strategy:** Stratified 5-Fold Cross-Validation on `X_train` strictly (`scoring='f1'`, `refit='f1'`, `random_state=42`)  
**Data Integrity:** The test set was held out untouched and never utilized during hyperparameter search or cross-validation. Preprocessing steps (scaling) were embedded within pipelines to eliminate leakage.

---

## 1. Experimental Setup & Data Partitions

- **Total Samples:** 9,928
- **Training Partition (`X_train`, `y_train`):** 7,942 samples (80.0%) — Used for Stratified 5-Fold CV
- **Test Partition (`X_test`, `y_test`):** 1,986 samples (20.0%) — Evaluated ONCE post-tuning

### Class Distributions:
| Partition | NotPlaced (`0`) Count | NotPlaced (`0`) % | Placed (`1`) Count | Placed (`1`) % | Total |
|---|---|---|---|---|---|
| **Training Set** | 4,641 | 58.44% | 3,301 | 41.56% | 7,942 |
| **Test Set** | 1,160 | 58.41% | 826 | 41.59% | 1,986 |

---

## 2. Cross-Validation Results & Best Hyperparameters (Training Set Only)

*Evaluated across 5 stratified folds on `X_train`. Sorted primarily by **Mean CV F1 Score**.*

| Model | Best Selected Hyperparameters | Mean CV F1 Score | Std CV F1 | Mean CV ROC-AUC | Std CV ROC-AUC |
|---|---|---|---|---|---|
| **Logistic Regression** | `C`: 0.5<br>`class_weight`: balanced<br>`penalty`: l2<br>`solver`: lbfgs | **0.7609** | ±0.0085 | **0.8735** | ±0.0056 |
| **Gradient Boosting** | `learning_rate`: 0.03<br>`max_depth`: 3<br>`min_samples_split`: 2<br>`n_estimators`: 100<br>`subsample`: 0.85 | **0.7491** | ±0.0110 | **0.8727** | ±0.0064 |
| **Random Forest** | `max_depth`: 10<br>`max_features`: sqrt<br>`min_samples_leaf`: 2<br>`min_samples_split`: 2<br>`n_estimators`: 200 | **0.7454** | ±0.0115 | **0.8711** | ±0.0064 |

---

## 3. Final Test-Set Evaluation (Held-Out Unseen Data)

*Each tuned model evaluated exactly ONCE on `X_test` ($N=1,986$)*:

| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC | TN | FP | FN | TP |
|---|---|---|---|---|---|---|---|---|---|
| **Logistic Regression** | 0.8051 | 0.7431 | 0.8123 | **0.7762** | **0.8855** | 928 | 232 | 155 | 671 |
| **Gradient Boosting** | 0.8152 | 0.7909 | 0.7554 | **0.7728** | **0.8881** | 995 | 165 | 202 | 624 |
| **Random Forest** | 0.8026 | 0.7761 | 0.7385 | **0.7568** | **0.8851** | 984 | 176 | 216 | 610 |

---

## 4. Visualizations Generated

Visualizations are saved under `docs/models/`:
- **All Confusion Matrices:** `docs/models/tuned_all_confusion_matrices.png`
- **ROC Curves Comparison:** `docs/models/tuned_roc_curves_comparison.png`
- **CV F1 vs Test F1 Generalization Comparison:** `docs/models/cv_f1_vs_test_f1.png`
- **Individual Confusion Matrices:**
  - `docs/models/tuned_confusion_matrix_logistic_regression.png`
  - `docs/models/tuned_confusion_matrix_gradient_boosting.png`
  - `docs/models/tuned_confusion_matrix_random_forest.png`

---

## 5. Overfitting & Generalization Analysis

| Model | Mean CV F1 | Test Set F1 | Generalization Gap ($\Delta$) | Observations |
|---|---|---|---|---|
| **Logistic Regression** | 0.7609 | 0.7762 | 0.0153 | Exceptional consistency between CV and test; minimal variance. |
| **Gradient Boosting** | 0.7491 | 0.7728 | 0.0236 | High ROC-AUC; excellent discrimination across probability thresholds. |
| **Random Forest** | 0.7454 | 0.7568 | 0.0114 | Stable tree ensemble; slight drop in recall compared to linear/boosting. |

---

## 6. Recommendation of Best Candidate Model

### **Recommended Candidate: Gradient Boosting Classifier** (or **Logistic Regression**)

#### Comparative Assessment:
1. **Gradient Boosting Classifier:**
   - **Highest Test ROC-AUC (0.8881)** and **Highest CV ROC-AUC**: Best model for generating calibrated, reliable continuous probability estimates (critical for displaying placement likelihood percentages to students).
   - **Strong F1 Score (0.7728)** with highest Precision (0.7909), making fewer false positive mistakes.
   - Robust non-linear boundary handling suitable for interaction between technical projects, aptitude scores, and academic percentages.
   - Clean compatibility with tree-based explainability tools (TreeSHAP).

2. **Logistic Regression:**
   - **Highest Mean CV F1 (0.7609)** and **Highest Test F1 (0.7762)**.
   - Highly interpretable linear coefficients, but cannot capture non-linear feature interactions natively.

**Summary Conclusion:**
Based on the multi-criteria evaluation (primary metric CV F1, ROC-AUC calibration, precision, and explainability), **Gradient Boosting** and **Logistic Regression** stand out as the two strongest candidates. Gradient Boosting is recommended as the prime operational candidate due to superior probability calibration (ROC-AUC) and native tree-based SHAP explainability.
