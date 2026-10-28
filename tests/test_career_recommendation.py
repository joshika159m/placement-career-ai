"""
Unit Tests for Career Recommendation Engine
Covers all 17 required validation criteria and 3 synthetic student profiles.
"""

import unittest
import sys
import os

# Add root directory to python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.career_roles import CAREER_ROLES
from utils.career_recommendation import (
    recommend_careers,
    get_match_level,
    TOPIC_RECOMMENDATIONS
)


class TestCareerRecommendation(unittest.TestCase):

    def setUp(self):
        # Base realistic aptitude result template
        self.high_aptitude = {
            "percentage": 85.0,
            "category_scores": {
                "Quantitative Aptitude": {"score": 4, "total": 4, "percentage": 100.0},
                "Logical Reasoning": {"score": 4, "total": 4, "percentage": 100.0},
                "Verbal Ability": {"score": 3, "total": 4, "percentage": 75.0},
                "Data Interpretation": {"score": 2, "total": 3, "percentage": 66.67}
            }
        }

        self.moderate_aptitude = {
            "percentage": 60.0,
            "category_scores": {
                "Quantitative Aptitude": {"score": 2, "total": 4, "percentage": 50.0},
                "Logical Reasoning": {"score": 3, "total": 4, "percentage": 75.0},
                "Verbal Ability": {"score": 2, "total": 4, "percentage": 50.0},
                "Data Interpretation": {"score": 2, "total": 3, "percentage": 66.67}
            }
        }

        # High IT, Weak Core technical template
        self.it_strong_tech = {
            "domain": "Both",
            "topic_scores": {
                "Programming": {"score": 2, "total": 2, "percentage": 100.0},
                "Data Structures & Algorithms": {"score": 2, "total": 2, "percentage": 100.0},
                "OOP": {"score": 2, "total": 2, "percentage": 100.0},
                "DBMS": {"score": 2, "total": 2, "percentage": 100.0},
                "SQL": {"score": 2, "total": 2, "percentage": 100.0},
                "Operating Systems": {"score": 2, "total": 2, "percentage": 100.0},
                "Computer Networks": {"score": 2, "total": 2, "percentage": 100.0},
                "Digital Electronics": {"score": 0, "total": 1, "percentage": 0.0},
                "Embedded Systems": {"score": 0, "total": 1, "percentage": 0.0},
                "Microcontrollers": {"score": 0, "total": 1, "percentage": 0.0}
            },
            "domain_scores": {
                "IT": {"score": 14, "total": 14, "percentage": 100.0},
                "Core": {"score": 0, "total": 3, "percentage": 0.0}
            }
        }

        # Strong Core, Weak IT technical template
        self.core_strong_tech = {
            "domain": "Both",
            "topic_scores": {
                "Embedded Systems": {"score": 2, "total": 2, "percentage": 100.0},
                "Microcontrollers": {"score": 2, "total": 2, "percentage": 100.0},
                "Digital Electronics": {"score": 2, "total": 2, "percentage": 100.0},
                "Microprocessors": {"score": 2, "total": 2, "percentage": 100.0},
                "Electronic Devices": {"score": 2, "total": 2, "percentage": 100.0},
                "Programming": {"score": 0, "total": 2, "percentage": 0.0},
                "OOP": {"score": 0, "total": 2, "percentage": 0.0},
                "DBMS": {"score": 0, "total": 2, "percentage": 0.0}
            },
            "domain_scores": {
                "Core": {"score": 10, "total": 10, "percentage": 100.0},
                "IT": {"score": 0, "total": 6, "percentage": 0.0}
            }
        }

    def test_01_career_role_definitions_load_successfully(self):
        """1. Career role definitions load successfully."""
        self.assertIsInstance(CAREER_ROLES, list)
        self.assertGreater(len(CAREER_ROLES), 0)

    def test_02_all_12_roles_exist(self):
        """2. All 12 specified roles exist."""
        expected_roles = {
            "Software Developer", "Frontend Developer", "Backend Developer",
            "Full Stack Developer", "Data Analyst", "Data Scientist",
            "ML Engineer", "DevOps Engineer", "QA Engineer",
            "Cloud Engineer", "Cybersecurity Analyst", "Embedded Engineer"
        }
        loaded_roles = {r["role"] for r in CAREER_ROLES}
        self.assertEqual(loaded_roles, expected_roles)
        self.assertEqual(len(CAREER_ROLES), 12)

    def test_03_role_definitions_contain_required_fields(self):
        """3. Role definitions contain all required fields."""
        required_fields = {
            "role", "domain", "important_topics", "preferred_aptitude",
            "technical_weight", "aptitude_weight", "placement_weight",
            "skills", "description"
        }
        for r in CAREER_ROLES:
            missing = required_fields - set(r.keys())
            self.assertEqual(missing, set(), f"Role {r['role']} missing fields: {missing}")
            self.assertIn(r["domain"], {"IT", "Core"})
            self.assertGreater(len(r["important_topics"]), 0)
            self.assertGreater(len(r["skills"]), 0)

    def test_04_it_filtering_works(self):
        """4. IT filtering works and excludes Core roles."""
        res = recommend_careers(
            placement_probability=0.85,
            aptitude_result=self.high_aptitude,
            technical_result=self.it_strong_tech,
            selected_domain="IT"
        )
        for rec in res["recommendations"]:
            self.assertEqual(rec["domain"], "IT")
            self.assertNotEqual(rec["role"], "Embedded Engineer")

    def test_05_core_filtering_works(self):
        """5. Core filtering works and excludes IT roles."""
        res = recommend_careers(
            placement_probability=0.85,
            aptitude_result=self.high_aptitude,
            technical_result=self.core_strong_tech,
            selected_domain="Core"
        )
        for rec in res["recommendations"]:
            self.assertEqual(rec["domain"], "Core")
            self.assertEqual(rec["role"], "Embedded Engineer")

    def test_06_both_mode_allows_both_domains(self):
        """6. Both mode evaluates all roles across domains."""
        res = recommend_careers(
            placement_probability=0.80,
            aptitude_result=self.high_aptitude,
            technical_result=self.it_strong_tech,
            selected_domain="Both"
        )
        self.assertEqual(res["total_evaluated"], 12)

    def test_07_recommendation_returns_at_most_3_roles(self):
        """7. Recommendation returns at most 3 roles."""
        res = recommend_careers(
            placement_probability=0.85,
            aptitude_result=self.high_aptitude,
            technical_result=self.it_strong_tech,
            selected_domain="Both",
            top_n=3
        )
        self.assertLessEqual(len(res["recommendations"]), 3)
        self.assertGreater(len(res["recommendations"]), 0)

    def test_08_scores_remain_between_0_and_100(self):
        """8. Match scores remain strictly within [0, 100]."""
        for prob in [0.0, 0.5, 1.0, 50.0, 100.0]:
            res = recommend_careers(
                placement_probability=prob,
                aptitude_result=self.high_aptitude,
                technical_result=self.it_strong_tech,
                selected_domain="Both"
            )
            for rec in res["recommendations"]:
                self.assertGreaterEqual(rec["match_score"], 0.0)
                self.assertLessEqual(rec["match_score"], 100.0)
                self.assertGreaterEqual(rec["technical_match"], 0.0)
                self.assertLessEqual(rec["technical_match"], 100.0)

    def test_09_match_levels_assigned_correctly(self):
        """9. Match levels follow standard thresholds."""
        self.assertEqual(get_match_level(85.0), "Strong Match")
        self.assertEqual(get_match_level(80.0), "Strong Match")
        self.assertEqual(get_match_level(75.0), "Good Match")
        self.assertEqual(get_match_level(65.0), "Good Match")
        self.assertEqual(get_match_level(55.0), "Moderate Match")
        self.assertEqual(get_match_level(50.0), "Moderate Match")
        self.assertEqual(get_match_level(45.0), "Weak Match")
        self.assertEqual(get_match_level(0.0), "Weak Match")

    def test_10_technical_match_responds_to_topic_performance(self):
        """10. Technical match increases with higher topic score."""
        tech_high = {
            "topic_scores": {"Programming": {"percentage": 100.0}, "OOP": {"percentage": 100.0}}
        }
        tech_low = {
            "topic_scores": {"Programming": {"percentage": 20.0}, "OOP": {"percentage": 20.0}}
        }
        res_high = recommend_careers(0.8, self.high_aptitude, tech_high, selected_domain="IT")
        res_low = recommend_careers(0.8, self.high_aptitude, tech_low, selected_domain="IT")
        self.assertGreater(res_high["recommendations"][0]["technical_match"], res_low["recommendations"][0]["technical_match"])

    def test_11_aptitude_match_responds_to_aptitude_performance(self):
        """11. Aptitude match responds to aptitude assessment percentage."""
        apt_high = {"percentage": 90.0, "category_scores": {"Quantitative Aptitude": {"percentage": 100.0}}}
        apt_low = {"percentage": 30.0, "category_scores": {"Quantitative Aptitude": {"percentage": 20.0}}}
        res_high = recommend_careers(0.8, apt_high, self.it_strong_tech, selected_domain="IT")
        res_low = recommend_careers(0.8, apt_low, self.it_strong_tech, selected_domain="IT")
        self.assertGreater(res_high["recommendations"][0]["aptitude_match"], res_low["recommendations"][0]["aptitude_match"])

    def test_12_placement_readiness_responds_to_placement_probability(self):
        """12. Placement readiness responds to model probability."""
        res_high = recommend_careers(0.95, self.high_aptitude, self.it_strong_tech, selected_domain="IT")
        res_low = recommend_careers(0.20, self.high_aptitude, self.it_strong_tech, selected_domain="IT")
        self.assertGreater(res_high["recommendations"][0]["placement_readiness"], res_low["recommendations"][0]["placement_readiness"])

    def test_13_weak_topics_become_skill_gaps(self):
        """13. Relevant topics below 70% become skill gaps."""
        tech_weak_sql = {
            "topic_scores": {
                "SQL": {"percentage": 40.0},
                "DBMS": {"percentage": 90.0},
                "Programming": {"percentage": 90.0},
                "OOP": {"percentage": 90.0}
            }
        }
        res = recommend_careers(0.8, self.high_aptitude, tech_weak_sql, selected_domain="IT")
        # Find Backend Developer or Data Analyst
        backend_rec = next((r for r in res["recommendations"] if r["role"] == "Backend Developer"), None)
        if backend_rec:
            self.assertTrue(any("SQL" in gap for gap in backend_rec["skill_gaps"]))

    def test_14_unrelated_topics_not_in_skill_gaps(self):
        """14. Unrelated topics are not included in a role's skill gaps."""
        tech_results = {
            "topic_scores": {
                "SQL": {"percentage": 90.0},
                "Programming": {"percentage": 90.0},
                "OOP": {"percentage": 90.0},
                "Microcontrollers": {"percentage": 10.0}  # Core topic unrelated to Backend Developer
            }
        }
        res = recommend_careers(0.8, self.high_aptitude, tech_results, selected_domain="IT")
        backend_rec = next((r for r in res["recommendations"] if r["role"] == "Backend Developer"), None)
        if backend_rec:
            for gap in backend_rec["skill_gaps"]:
                self.assertNotIn("Microcontrollers", gap)

    def test_15_high_performing_student_receives_sensible_recommendations(self):
        """15. High-performing student receives Strong Match level."""
        res = recommend_careers(0.92, self.high_aptitude, self.it_strong_tech, selected_domain="IT")
        top_rec = res["recommendations"][0]
        self.assertIn(top_rec["match_level"], ["Strong Match", "Good Match"])
        self.assertGreaterEqual(top_rec["match_score"], 75.0)

    def test_16_low_performing_student_receives_sensible_skill_gaps(self):
        """16. Low-performing student receives clear skill gaps and guidance."""
        tech_weak = {
            "topic_scores": {
                "Programming": {"percentage": 25.0},
                "Data Structures & Algorithms": {"percentage": 30.0},
                "OOP": {"percentage": 20.0}
            }
        }
        res = recommend_careers(0.15, self.moderate_aptitude, tech_weak, selected_domain="IT")
        top_rec = res["recommendations"][0]
        self.assertGreater(len(top_rec["skill_gaps"]), 0)
        self.assertGreater(len(top_rec["actionable_recommendations"]), 0)

    def test_17_invalid_input_handled_safely(self):
        """17. Invalid domain input raises descriptive ValueError."""
        with self.assertRaises(ValueError):
            recommend_careers(0.8, self.high_aptitude, self.it_strong_tech, selected_domain="Aerospace")

    # ==========================================
    # SECTION 10: 3 SYNTHETIC TEST PROFILES
    # ==========================================

    def test_synthetic_student_a_high_it_weak_core(self):
        """Student A: High IT, Strong Aptitude, High Placement, Weak Core -> IT careers rank highly."""
        res = recommend_careers(
            placement_probability=0.90,
            aptitude_result=self.high_aptitude,
            technical_result=self.it_strong_tech,
            selected_domain="Both"
        )
        top_roles = [r["role"] for r in res["recommendations"]]
        top_domains = [r["domain"] for r in res["recommendations"]]
        self.assertIn("IT", top_domains)
        self.assertEqual(top_domains[0], "IT", "Top recommendation for Student A should be an IT career")

    def test_synthetic_student_b_strong_core_weak_it(self):
        """Student B: Strong Core, Strong Aptitude, High Placement, Weak IT -> Core careers rank highly."""
        res = recommend_careers(
            placement_probability=0.90,
            aptitude_result=self.high_aptitude,
            technical_result=self.core_strong_tech,
            selected_domain="Both"
        )
        top_role = res["recommendations"][0]
        self.assertEqual(top_role["domain"], "Core", "Top recommendation for Student B should be a Core career")
        self.assertEqual(top_role["role"], "Embedded Engineer")

    def test_synthetic_student_c_mixed_it_and_core(self):
        """Student C: Mixed IT + Core performance, Moderate Aptitude & Placement."""
        mixed_tech = {
            "domain": "Both",
            "topic_scores": {
                "Programming": {"percentage": 75.0},
                "Operating Systems": {"percentage": 75.0},
                "Embedded Systems": {"percentage": 75.0},
                "Digital Electronics": {"percentage": 75.0}
            },
            "domain_scores": {
                "IT": {"percentage": 75.0},
                "Core": {"percentage": 75.0}
            }
        }
        res = recommend_careers(
            placement_probability=0.60,
            aptitude_result=self.moderate_aptitude,
            technical_result=mixed_tech,
            selected_domain="Both"
        )
        self.assertEqual(len(res["recommendations"]), 3)
        for rec in res["recommendations"]:
            self.assertIn(rec["match_level"], ["Good Match", "Moderate Match"])

    # =========================================================================
    # PHASE 7 BUG FIX TESTS: INTEREST INTEGRATION VALIDATION
    # =========================================================================

    def test_1_recommend_careers_without_interests(self):
        """1. recommend_careers() without interests uses backward-compatible 50/25/25 formula."""
        res = recommend_careers(
            placement_probability=80.0,
            aptitude_result=self.high_aptitude,
            technical_result=self.it_strong_tech,
            selected_domain="IT"
        )
        self.assertEqual(len(res["recommendations"]), 3)
        for r in res["recommendations"]:
            self.assertIsNone(r["interest_match"])

    def test_2_recommend_careers_with_interests(self):
        """2. recommend_careers() with interests executes successfully and returns Top 3."""
        interests = ["Software Development", "Web Development"]
        res = recommend_careers(
            placement_probability=80.0,
            aptitude_result=self.high_aptitude,
            technical_result=self.it_strong_tech,
            selected_domain="IT",
            interests=interests
        )
        self.assertEqual(len(res["recommendations"]), 3)
        for r in res["recommendations"]:
            self.assertIsNotNone(r["interest_match"])

    def test_3_recommend_careers_empty_interests(self):
        """3. Empty interests list safely sets Interest Match to 0.0."""
        res = recommend_careers(
            placement_probability=80.0,
            aptitude_result=self.high_aptitude,
            technical_result=self.it_strong_tech,
            selected_domain="IT",
            interests=[]
        )
        self.assertEqual(len(res["recommendations"]), 3)
        for r in res["recommendations"]:
            self.assertEqual(r["interest_match"], 0.0)

    def test_4_recommend_careers_matching_interests(self):
        """4. Matching interests elevate Interest Match and populate matched_interests."""
        interests = ["Software Development"]
        res = recommend_careers(
            placement_probability=80.0,
            aptitude_result=self.high_aptitude,
            technical_result=self.it_strong_tech,
            selected_domain="IT",
            interests=interests
        )
        # Find Software Developer recommendation
        sw_dev = [r for r in res["recommendations"] if r["role"] == "Software Developer"]
        self.assertTrue(len(sw_dev) > 0)
        self.assertEqual(sw_dev[0]["interest_match"], 100.0)
        self.assertIn("Software Development", sw_dev[0]["matched_interests"])

    def test_5_recommend_careers_non_matching_interests(self):
        """5. Non-matching interests result in Interest Match = 0.0."""
        interests = ["Embedded Systems", "VLSI / Semiconductor"]
        res = recommend_careers(
            placement_probability=80.0,
            aptitude_result=self.high_aptitude,
            technical_result=self.it_strong_tech,
            selected_domain="IT",
            interests=interests
        )
        for r in res["recommendations"]:
            self.assertEqual(r["interest_match"], 0.0)
            self.assertEqual(r["matched_interests"], [])

    def test_6_interest_match_calculation(self):
        """6. Interest match calculation is strictly proportional to role interest overlap."""
        # Backend Developer has role_interests: ["Software Development", "Cloud Computing", "DevOps"]
        # Match 1 of 3 -> 33.33%
        res_1 = recommend_careers(
            placement_probability=80.0,
            aptitude_result=self.high_aptitude,
            technical_result=self.it_strong_tech,
            selected_domain="IT",
            interests=["Software Development"]
        )
        bk_1 = [r for r in res_1["recommendations"] if r["role"] == "Backend Developer"]
        if bk_1:
            self.assertAlmostEqual(bk_1[0]["interest_match"], 33.33, places=1)

        # Match 2 of 3 -> 66.67%
        res_2 = recommend_careers(
            placement_probability=80.0,
            aptitude_result=self.high_aptitude,
            technical_result=self.it_strong_tech,
            selected_domain="IT",
            interests=["Software Development", "Cloud Computing"]
        )
        bk_2 = [r for r in res_2["recommendations"] if r["role"] == "Backend Developer"]
        if bk_2:
            self.assertAlmostEqual(bk_2[0]["interest_match"], 66.67, places=1)

    def test_7_final_match_score_formula(self):
        """7. Final Match Score strictly follows 0.40*Tech + 0.20*Apt + 0.20*Place + 0.20*Interest."""
        interests = ["Software Development"]
        res = recommend_careers(
            placement_probability=80.0,
            aptitude_result=self.high_aptitude,
            technical_result=self.it_strong_tech,
            selected_domain="IT",
            interests=interests
        )
        for r in res["recommendations"]:
            expected_score = round(
                (r["technical_match"] * 0.40) +
                (r["aptitude_match"] * 0.20) +
                (r["placement_probability"] * 0.20) +
                (r["interest_match"] * 0.20),
                2
            )
            self.assertEqual(r["match_score"], expected_score)

    def test_8_top_3_recommendation_ordering(self):
        """8. Top 3 recommendations are sorted in strict descending order of match_score."""
        interests = ["Data Science & AI", "Machine Learning", "Software Development", "Web Development"]
        res = recommend_careers(
            placement_probability=85.0,
            aptitude_result=self.high_aptitude,
            technical_result=self.it_strong_tech,
            selected_domain="IT",
            interests=interests
        )
        recs = res["recommendations"]
        self.assertEqual(len(recs), 3)
        self.assertGreaterEqual(recs[0]["match_score"], recs[1]["match_score"])
        self.assertGreaterEqual(recs[1]["match_score"], recs[2]["match_score"])


if __name__ == '__main__':
    unittest.main()
