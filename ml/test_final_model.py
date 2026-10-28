"""
Test Script for Final Placement Prediction Model
Verifies loading and inference from models/placement_model.pkl
"""

import os
import joblib
import pandas as pd


def test_saved_model():
    model_path = os.path.join('models', 'placement_model.pkl')
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at: {model_path}")

    print("=" * 70)
    print("TESTING FINAL PLACEMENT PREDICTION MODEL")
    print("=" * 70)
    print(f"Loading model pipeline from: {model_path}")
    pipeline = joblib.load(model_path)
    print("Model pipeline successfully loaded.\n")

    # Define 3 realistic student profiles
    students = [
        {
            'Student_ID': 'Student 1 (High Performer)',
            'CGPA': 8.5,
            'Internships': 2,
            'Projects': 3,
            'Workshops_Certifications': 2,
            'AptitudeTestScore': 88,
            'SoftSkillsRating': 4.6,
            'ExtracurricularActivities': 1,
            'PlacementTraining': 1,
            'SSC_Marks': 85,
            'HSC_Marks': 84
        },
        {
            'Student_ID': 'Student 2 (Average / Moderate)',
            'CGPA': 7.4,
            'Internships': 1,
            'Projects': 1,
            'Workshops_Certifications': 1,
            'AptitudeTestScore': 76,
            'SoftSkillsRating': 4.1,
            'ExtracurricularActivities': 0,
            'PlacementTraining': 1,
            'SSC_Marks': 66,
            'HSC_Marks': 70
        },
        {
            'Student_ID': 'Student 3 (Underprepared / Low)',
            'CGPA': 6.6,
            'Internships': 0,
            'Projects': 0,
            'Workshops_Certifications': 0,
            'AptitudeTestScore': 62,
            'SoftSkillsRating': 3.2,
            'ExtracurricularActivities': 0,
            'PlacementTraining': 0,
            'SSC_Marks': 58,
            'HSC_Marks': 60
        }
    ]

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

    test_df = pd.DataFrame(students)
    X_input = test_df[feature_cols]

    # Perform inference
    predictions = pipeline.predict(X_input)
    probabilities = pipeline.predict_proba(X_input)

    class_names = {0: 'NotPlaced', 1: 'Placed'}

    for idx, student in enumerate(students):
        pred_class = predictions[idx]
        pred_label = class_names[pred_class]
        prob_not_placed = probabilities[idx][0] * 100
        prob_placed = probabilities[idx][1] * 100

        print("-" * 70)
        print(f"Profile: {student['Student_ID']}")
        print(f"  Inputs: CGPA={student['CGPA']}, Internships={student['Internships']}, Projects={student['Projects']}, "
              f"Certifications={student['Workshops_Certifications']}, Aptitude={student['AptitudeTestScore']}, "
              f"SoftSkills={student['SoftSkillsRating']}, Extracurricular={student['ExtracurricularActivities']}, "
              f"Training={student['PlacementTraining']}, SSC={student['SSC_Marks']}, HSC={student['HSC_Marks']}")
        print(f"  Predicted Class:       {pred_class} ({pred_label})")
        print(f"  Placement Probability: {prob_placed:.2f}% (NotPlaced: {prob_not_placed:.2f}%)")

    print("=" * 70)
    print("VERIFICATION CONFIRMATION: The saved model loads and predicts successfully!")
    print("=" * 70)


if __name__ == '__main__':
    test_saved_model()
