"""
Training and Evaluation Pipeline for Reduced-Feature Placement Model
Uses ONLY 5 features:
1. CGPA
2. AptitudeTestScore
3. SoftSkillsRating
4. SSC_Marks
5. HSC_Marks

Compares performance against the original 10-feature model on the identical test split.
Saves the new model to: models/placement_model_reduced.pkl
Preserves the original model: models/placement_model.pkl
"""

import os
import sys
sys.stdout.reconfigure(encoding='utf-8')
import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix
)


def train_and_evaluate_reduced_model():
    dataset_path = 'data/processed/campus_recruitment_encoded.csv'
    if not os.path.exists(dataset_path):
        raise FileNotFoundError(f"Dataset not found at: {dataset_path}")

    df = pd.read_csv(dataset_path)
    print(f"Loaded dataset: {dataset_path} with {len(df):,} rows.")

    target_col = 'PlacementStatus'
    
    # 1. Original 10 features
    original_feature_cols = [
        'CGPA',
        'Internships',
        'Projects',
        'Workshops_Certifications',
        'AptitudeTestScore',
        'SoftSkillsRating',
        'ExtracurricularActivities',
        'PlacementTraining',
        'SSC_Marks',
        'HSC_Marks'
    ]

    # 2. Reduced 5 features
    reduced_feature_cols = [
        'CGPA',
        'AptitudeTestScore',
        'SoftSkillsRating',
        'SSC_Marks',
        'HSC_Marks'
    ]

    y = df[target_col]

    # Identical 80/20 train/test split (stratified, random_state=42)
    X_train_orig, X_test_orig, y_train, y_test = train_test_split(
        df[original_feature_cols], y, test_size=0.20, random_state=42, stratify=y
    )

    X_train_red = X_train_orig[reduced_feature_cols]
    X_test_red = X_test_orig[reduced_feature_cols]

    print("=" * 70)
    print("EVALUATING EXISTING 10-FEATURE MODEL ON TEST SET")
    print("=" * 70)
    original_model_path = os.path.join('models', 'placement_model.pkl')
    if os.path.exists(original_model_path):
        orig_pipeline = joblib.load(original_model_path)
        y_pred_orig = orig_pipeline.predict(X_test_orig)
        y_proba_orig = orig_pipeline.predict_proba(X_test_orig)[:, 1]

        orig_acc = accuracy_score(y_test, y_pred_orig)
        orig_prec = precision_score(y_test, y_pred_orig, zero_division=0)
        orig_rec = recall_score(y_test, y_pred_orig, zero_division=0)
        orig_f1 = f1_score(y_test, y_pred_orig, zero_division=0)
        orig_auc = roc_auc_score(y_test, y_proba_orig)

        orig_cm = confusion_matrix(y_test, y_pred_orig)
        print(f"Original Model (10 features) - Test Results:")
        print(f"  Accuracy:  {orig_acc:.4f} ({orig_acc*100:.2f}%)")
        print(f"  Precision: {orig_prec:.4f} ({orig_prec*100:.2f}%)")
        print(f"  Recall:    {orig_rec:.4f} ({orig_rec*100:.2f}%)")
        print(f"  F1 Score:  {orig_f1:.4f} ({orig_f1*100:.2f}%)")
        print(f"  ROC-AUC:   {orig_auc:.4f} ({orig_auc*100:.2f}%)")
        print(f"  Confusion Matrix: TN={orig_cm[0,0]}, FP={orig_cm[0,1]}, FN={orig_cm[1,0]}, TP={orig_cm[1,1]}")
    else:
        print("Original model file not found!")
        orig_acc = orig_prec = orig_rec = orig_f1 = orig_auc = None
        orig_cm = None

    print("\n" + "=" * 70)
    print("TRAINING & EVALUATING NEW REDUCED 5-FEATURE MODEL")
    print("=" * 70)

    # Preprocessor for 5 numerical features (all standardized)
    preprocessor_red = ColumnTransformer(
        transformers=[
            ('num_scaler', StandardScaler(), reduced_feature_cols)
        ]
    )

    # Logistic Regression with identical hyperparameters as project baseline
    classifier_red = LogisticRegression(
        C=0.5,
        class_weight='balanced',
        penalty='l2',
        solver='lbfgs',
        random_state=42,
        max_iter=1000
    )

    pipeline_red = Pipeline([
        ('preprocessor', preprocessor_red),
        ('classifier', classifier_red)
    ])

    # Fit pipeline strictly on X_train_red
    pipeline_red.fit(X_train_red, y_train)

    y_pred_red = pipeline_red.predict(X_test_red)
    y_proba_red = pipeline_red.predict_proba(X_test_red)[:, 1]

    red_acc = accuracy_score(y_test, y_pred_red)
    red_prec = precision_score(y_test, y_pred_red, zero_division=0)
    red_rec = recall_score(y_test, y_pred_red, zero_division=0)
    red_f1 = f1_score(y_test, y_pred_red, zero_division=0)
    red_auc = roc_auc_score(y_test, y_proba_red)
    red_cm = confusion_matrix(y_test, y_pred_red)

    print(f"Reduced Model (5 features) - Test Results:")
    print(f"  Accuracy:  {red_acc:.4f} ({red_acc*100:.2f}%)")
    print(f"  Precision: {red_prec:.4f} ({red_prec*100:.2f}%)")
    print(f"  Recall:    {red_rec:.4f} ({red_rec*100:.2f}%)")
    print(f"  F1 Score:  {red_f1:.4f} ({red_f1*100:.2f}%)")
    print(f"  ROC-AUC:   {red_auc:.4f} ({red_auc*100:.2f}%)")
    print(f"  Confusion Matrix: TN={red_cm[0,0]}, FP={red_cm[0,1]}, FN={red_cm[1,0]}, TP={red_cm[1,1]}")

    # Side-by-side comparison table
    print("\n" + "=" * 70)
    print("SIDE-BY-SIDE COMPARISON: ORIGINAL VS REDUCED MODEL")
    print("=" * 70)
    metrics_df = pd.DataFrame({
        "Metric": ["Accuracy", "Precision", "Recall", "F1 Score", "ROC-AUC"],
        "Original (10 Features)": [
            f"{orig_acc:.4f}" if orig_acc else "N/A",
            f"{orig_prec:.4f}" if orig_prec else "N/A",
            f"{orig_rec:.4f}" if orig_rec else "N/A",
            f"{orig_f1:.4f}" if orig_f1 else "N/A",
            f"{orig_auc:.4f}" if orig_auc else "N/A"
        ],
        "Reduced (5 Features)": [
            f"{red_acc:.4f}",
            f"{red_prec:.4f}",
            f"{red_rec:.4f}",
            f"{red_f1:.4f}",
            f"{red_auc:.4f}"
        ],
        "Difference (Diff)": [
            f"{(red_acc - orig_acc):+.4f}" if orig_acc else "N/A",
            f"{(red_prec - orig_prec):+.4f}" if orig_prec else "N/A",
            f"{(red_rec - orig_rec):+.4f}" if orig_rec else "N/A",
            f"{(red_f1 - orig_f1):+.4f}" if orig_f1 else "N/A",
            f"{(red_auc - orig_auc):+.4f}" if orig_auc else "N/A"
        ]
    })
    print(metrics_df.to_string(index=False))

    # Now fit the final reduced pipeline on the full dataset (9,928 samples)
    print("\nFitting final reduced model on full dataset (9,928 samples)...")
    final_reduced_pipeline = Pipeline([
        ('preprocessor', ColumnTransformer(transformers=[('num_scaler', StandardScaler(), reduced_feature_cols)])),
        ('classifier', LogisticRegression(C=0.5, class_weight='balanced', penalty='l2', solver='lbfgs', random_state=42, max_iter=1000))
    ])
    final_reduced_pipeline.fit(df[reduced_feature_cols], y)

    reduced_model_path = os.path.join('models', 'placement_model_reduced.pkl')
    joblib.dump(final_reduced_pipeline, reduced_model_path)
    print(f"Final reduced model saved to: {reduced_model_path}")
    print(f"Reduced model coefficients: {dict(zip(reduced_feature_cols, final_reduced_pipeline.named_steps['classifier'].coef_[0]))}")
    print(f"Reduced model intercept: {final_reduced_pipeline.named_steps['classifier'].intercept_[0]:.4f}")

    return {
        "orig_metrics": {"accuracy": orig_acc, "precision": orig_prec, "recall": orig_rec, "f1": orig_f1, "roc_auc": orig_auc},
        "red_metrics": {"accuracy": red_acc, "precision": red_prec, "recall": red_rec, "f1": red_f1, "roc_auc": red_auc},
        "model_path": reduced_model_path
    }


if __name__ == '__main__':
    train_and_evaluate_reduced_model()
