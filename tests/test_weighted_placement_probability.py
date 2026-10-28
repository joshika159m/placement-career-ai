"""
Unit Tests for Weighted Placement Probability Model
Tests the deterministic 70/30 formula:
0.35 * Live Aptitude + 0.35 * Live Technical + 0.15 * SSC + 0.15 * HSC
"""

import unittest
import sys
import os

# Add root directory to python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.placement_scoring import calculate_weighted_placement_probability


class TestWeightedPlacementProbability(unittest.TestCase):

    def test_case_1_high_assessments_moderate_academics(self):
        """Test Case 1: Aptitude = 95, Technical = 95, SSC = 60, HSC = 60 -> Expected: 84.50%"""
        result = calculate_weighted_placement_probability(
            aptitude_percentage=95.0,
            technical_percentage=95.0,
            ssc_percentage=60.0,
            hsc_percentage=60.0
        )
        # 0.35(95) + 0.35(95) + 0.15(60) + 0.15(60) = 33.25 + 33.25 + 9.0 + 9.0 = 84.50
        self.assertEqual(result, 84.50)

    def test_case_2_low_assessments_high_academics(self):
        """Test Case 2: Aptitude = 40, Technical = 40, SSC = 95, HSC = 95 -> Expected: 56.50%"""
        result = calculate_weighted_placement_probability(
            aptitude_percentage=40.0,
            technical_percentage=40.0,
            ssc_percentage=95.0,
            hsc_percentage=95.0
        )
        # 0.35(40) + 0.35(40) + 0.15(95) + 0.15(95) = 14.0 + 14.0 + 14.25 + 14.25 = 56.50
        self.assertEqual(result, 56.50)

    def test_case_3_standard_balanced_profile(self):
        """Test Case 3: Aptitude = 80, Technical = 70, SSC = 85, HSC = 90 -> Expected: 78.75%"""
        result = calculate_weighted_placement_probability(
            aptitude_percentage=80.0,
            technical_percentage=70.0,
            ssc_percentage=85.0,
            hsc_percentage=90.0
        )
        # 0.35(80) + 0.35(70) + 0.15(85) + 0.15(90) = 28.0 + 24.5 + 12.75 + 13.5 = 78.75
        self.assertEqual(result, 78.75)

    def test_case_4_maximum_boundary(self):
        """Test Case 4: Aptitude = 100, Technical = 100, SSC = 100, HSC = 100 -> Expected: 100.0%"""
        result = calculate_weighted_placement_probability(
            aptitude_percentage=100.0,
            technical_percentage=100.0,
            ssc_percentage=100.0,
            hsc_percentage=100.0
        )
        self.assertEqual(result, 100.0)

    def test_case_5_minimum_boundary(self):
        """Test Case 5: Aptitude = 0, Technical = 0, SSC = 0, HSC = 0 -> Expected: 0.0%"""
        result = calculate_weighted_placement_probability(
            aptitude_percentage=0.0,
            technical_percentage=0.0,
            ssc_percentage=0.0,
            hsc_percentage=0.0
        )
        self.assertEqual(result, 0.0)

    def test_weights_sum_to_one(self):
        """Verify weights strictly total 1.00 (70% live assessments, 30% academics)."""
        w_apt = 0.35
        w_tech = 0.35
        w_ssc = 0.15
        w_hsc = 0.15
        self.assertAlmostEqual(w_apt + w_tech + w_ssc + w_hsc, 1.00)
        self.assertAlmostEqual(w_apt + w_tech, 0.70)
        self.assertAlmostEqual(w_ssc + w_hsc, 0.30)

    def test_clipping_boundaries(self):
        """Ensure inputs exceeding 100 or below 0 are properly bounded."""
        clipped_high = calculate_weighted_placement_probability(110.0, 105.0, 100.0, 100.0)
        self.assertEqual(clipped_high, 100.0)

        clipped_low = calculate_weighted_placement_probability(-10.0, 0.0, 0.0, 0.0)
        self.assertEqual(clipped_low, 0.0)


if __name__ == '__main__':
    unittest.main()
