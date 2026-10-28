"""
Final Placement Prediction Model Training Pipeline
Placement Prediction and Career Recommendation System
"""

import os
import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression


def train_final_model():
    dataset_path = 'data/processed/campus_recruitment_encoded.csv'
    if not os.path.exists(dataset_path):
        raise FileNotFoundError(f"Dataset not found at: {dataset_path}")

    df = pd.read_csv(dataset_path)
    print(f"Loaded dataset: {dataset_path} with {len(df):,} rows and {len(df.columns)} columns.")

    target_col = 'PlacementStatus'
    feature_cols = [
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

    num_cols = [
        'CGPA',
        'Internships',
        'Projects',
        'Workshops_Certifications',
        'AptitudeTestScore',
        'SoftSkillsRating',
        'SSC_Marks',
        'HSC_Marks'
    ]
    binary_cols = ['ExtracurricularActivities', 'PlacementTraining']

    X = df[feature_cols]
    y = df[target_col]

    # Preprocessor: standardize numerical features, passthrough binary features
    preprocessor = ColumnTransformer(
        transformers=[
            ('num_scaler', StandardScaler(), num_cols),
            ('cat_pass', 'passthrough', binary_cols)
        ]
    )

    # Tuned Logistic Regression classifier
    classifier = LogisticRegression(
        C=0.5,
        class_weight='balanced',
        penalty='l2',
        solver='lbfgs',
        random_state=42,
        max_iter=1000
    )

    # Complete pipeline
    pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('classifier', classifier)
    ])

    print("Training final model on the complete cleaned dataset (9,928 samples)...")
    pipeline.fit(X, y)

    # Save trained pipeline
    os.makedirs('models', exist_ok=True)
    model_path = os.path.join('models', 'placement_model.pkl')
    joblib.dump(pipeline, model_path)

    print(f"Final model successfully trained and saved to: {model_path}")
    print(f"Model coefficients: {pipeline.named_steps['classifier'].coef_[0]}")
    print(f"Model intercept: {pipeline.named_steps['classifier'].intercept_[0]}")

    return pipeline, model_path


if __name__ == '__main__':
    train_final_model()
