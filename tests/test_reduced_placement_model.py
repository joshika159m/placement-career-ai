"""
Unit Tests for Reduced Placement Model (5 Features)
Verifies feature expectations, inference, probability calibration, and pipeline integrity.
"""

import unittest
import os
import sys
import joblib
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

REDUCED_MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'placement_model_reduced.pkl')
ORIGINAL_MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'placement_model.pkl')


class TestReducedPlacementModel(unittest.TestCase):

    def setUp(self):
        self.assertTrue(os.path.exists(REDUCED_MODEL_PATH), "Reduced model file not found!")
        self.pipeline = joblib.load(REDUCED_MODEL_PATH)
        self.expected_features = [
            'CGPA',
            'AptitudeTestScore',
            'SoftSkillsRating',
            'SSC_Marks',
            'HSC_Marks'
        ]

    def test_original_model_preserved_untouched(self):
        """Confirms that the original 10-feature model remains intact."""
        self.assertTrue(os.path.exists(ORIGINAL_MODEL_PATH), "Original model must be preserved!")
        orig_pipe = joblib.load(ORIGINAL_MODEL_PATH)
        self.assertIsNotNone(orig_pipe)

    def test_reduced_model_feature_count(self):
        """Confirms that the reduced model accepts exactly 5 features."""
        preprocessor = self.pipeline.named_steps['preprocessor']
        num_transformer = preprocessor.transformers[0]
        feature_list = num_transformer[2]
        self.assertEqual(len(feature_list), 5)
        self.assertEqual(list(feature_list), self.expected_features)

    def test_reduced_model_prediction_and_probability(self):
        """Verifies prediction and probability output on 5-feature input."""
        sample_df = pd.DataFrame([{
            'CGPA': 8.5,
            'AptitudeTestScore': 85.0,
            'SoftSkillsRating': 4.5,
            'SSC_Marks': 88.0,
            'HSC_Marks': 85.0
        }])[self.expected_features]

        pred = self.pipeline.predict(sample_df)
        proba = self.pipeline.predict_proba(sample_df)

        self.assertIn(pred[0], [0, 1])
        self.assertEqual(proba.shape, (1, 2))
        self.assertAlmostEqual(proba[0][0] + proba[0][1], 1.0, places=5)
        self.assertGreater(proba[0][1], 0.50, "High academic profile should yield placement probability > 50%")

    def test_profile_sensitivity(self):
        """Verifies that high academic profile gets higher placement probability than low profile."""
        high_df = pd.DataFrame([{
            'CGPA': 9.0,
            'AptitudeTestScore': 90.0,
            'SoftSkillsRating': 4.8,
            'SSC_Marks': 92.0,
            'HSC_Marks': 90.0
        }])[self.expected_features]

        low_df = pd.DataFrame([{
            'CGPA': 5.5,
            'AptitudeTestScore': 45.0,
            'SoftSkillsRating': 2.0,
            'SSC_Marks': 50.0,
            'HSC_Marks': 48.0
        }])[self.expected_features]

        high_prob = self.pipeline.predict_proba(high_df)[0][1]
        low_prob = self.pipeline.predict_proba(low_df)[0][1]

        self.assertGreater(high_prob, low_prob)


if __name__ == '__main__':
    unittest.main()
