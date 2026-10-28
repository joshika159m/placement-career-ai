"""
Unit Tests for Technical Assessment Module
Covers all 20 required verification criteria.
"""

import unittest
import sys
import os

# Add root directory to python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.technical_questions import TECHNICAL_QUESTIONS
from utils.technical_assessment import (
    IT_TOPICS,
    CORE_TOPICS,
    validate_technical_question,
    validate_technical_question_set,
    select_technical_questions,
    evaluate_technical_assessment
)


class TestTechnicalAssessment(unittest.TestCase):

    def test_01_question_bank_loads_successfully(self):
        """1. Question bank loads successfully."""
        self.assertIsInstance(TECHNICAL_QUESTIONS, list)
        self.assertGreater(len(TECHNICAL_QUESTIONS), 0)

    def test_02_at_least_120_questions_exist(self):
        """2. At least 120 questions exist."""
        self.assertGreaterEqual(len(TECHNICAL_QUESTIONS), 120)

    def test_03_at_least_60_it_questions_exist(self):
        """3. At least 60 IT questions exist."""
        it_qs = [q for q in TECHNICAL_QUESTIONS if q["domain"] == "IT"]
        self.assertGreaterEqual(len(it_qs), 60)

    def test_04_at_least_60_core_questions_exist(self):
        """4. At least 60 Core questions exist."""
        core_qs = [q for q in TECHNICAL_QUESTIONS if q["domain"] == "Core"]
        self.assertGreaterEqual(len(core_qs), 60)

    def test_05_all_required_it_topics_exist(self):
        """5. All required IT topics exist."""
        it_topics_present = {q["topic"] for q in TECHNICAL_QUESTIONS if q["domain"] == "IT"}
        expected_it = set(IT_TOPICS)
        self.assertEqual(it_topics_present, expected_it)

    def test_06_all_required_core_topics_exist(self):
        """6. All required Core topics exist."""
        core_topics_present = {q["topic"] for q in TECHNICAL_QUESTIONS if q["domain"] == "Core"}
        expected_core = set(CORE_TOPICS)
        self.assertEqual(core_topics_present, expected_core)

    def test_07_all_question_schemas_are_valid(self):
        """7. All question schemas are valid."""
        for q in TECHNICAL_QUESTIONS:
            self.assertTrue(validate_technical_question(q))

    def test_08_ids_are_unique(self):
        """8. IDs are unique across entire bank."""
        ids = [q["id"] for q in TECHNICAL_QUESTIONS]
        self.assertEqual(len(ids), len(set(ids)))

    def test_09_it_selection_returns_exactly_15(self):
        """9. IT selection returns exactly 15 questions."""
        for seed in range(3):
            selected = select_technical_questions(domain="IT", random_seed=seed)
            self.assertEqual(len(selected), 15)
            self.assertTrue(all(q["domain"] == "IT" for q in selected))

    def test_10_core_selection_returns_exactly_15(self):
        """10. Core selection returns exactly 15 questions."""
        for seed in range(3):
            selected = select_technical_questions(domain="Core", random_seed=seed)
            self.assertEqual(len(selected), 15)
            self.assertTrue(all(q["domain"] == "Core" for q in selected))

    def test_11_both_selection_returns_exactly_15(self):
        """11. Both selection returns exactly 15 questions."""
        for seed in range(3):
            selected = select_technical_questions(domain="Both", random_seed=seed)
            self.assertEqual(len(selected), 15)

    def test_12_both_selection_contains_8_it_and_7_core(self):
        """12. Both selection contains 8 IT + 7 Core questions."""
        for seed in range(5):
            selected = select_technical_questions(domain="Both", random_seed=seed)
            it_count = sum(1 for q in selected if q["domain"] == "IT")
            core_count = sum(1 for q in selected if q["domain"] == "Core")
            self.assertEqual(it_count, 8)
            self.assertEqual(core_count, 7)

    def test_13_no_duplicate_questions_occur(self):
        """13. No duplicate questions occur in any mode."""
        for domain in ["IT", "Core", "Both"]:
            selected = select_technical_questions(domain=domain, random_seed=42)
            ids = [q["id"] for q in selected]
            self.assertEqual(len(ids), len(set(ids)))

    def test_14_all_correct_scoring_gives_15_of_15(self):
        """14. All-correct scoring gives 15/15 (100%)."""
        selected = select_technical_questions(domain="Both", random_seed=42)
        answers = {q["id"]: q["answer"] for q in selected}
        result = evaluate_technical_assessment(selected, answers)
        self.assertEqual(result["score"], 15)
        self.assertEqual(result["total"], 15)
        self.assertEqual(result["percentage"], 100.0)
        self.assertEqual(len(result["weak_topics"]), 0)

    def test_15_all_incorrect_scoring_gives_0_of_15(self):
        """15. All-incorrect scoring gives 0/15 (0.0%)."""
        selected = select_technical_questions(domain="Both", random_seed=42)
        answers = {q["id"]: "INVALID_OPTION" for q in selected}
        result = evaluate_technical_assessment(selected, answers)
        self.assertEqual(result["score"], 0)
        self.assertEqual(result["total"], 15)
        self.assertEqual(result["percentage"], 0.0)
        self.assertEqual(len(result["strong_topics"]), 0)

    def test_16_partial_scoring_works(self):
        """16. Partial scoring calculates correct score and percentage."""
        selected = select_technical_questions(domain="IT", random_seed=99)
        # Answer first 9 correctly, last 6 wrong
        answers = {q["id"]: (q["answer"] if idx < 9 else "WRONG") for idx, q in enumerate(selected)}
        result = evaluate_technical_assessment(selected, answers)
        self.assertEqual(result["score"], 9)
        self.assertEqual(result["total"], 15)
        expected_pct = round((9 / 15) * 100, 2)  # 60.0%
        self.assertEqual(result["percentage"], expected_pct)

    def test_17_topic_scores_are_correct(self):
        """17. Topic scores are correct and sum up to total score."""
        selected = select_technical_questions(domain="Core", random_seed=12)
        answers = {q["id"]: (q["answer"] if idx % 2 == 0 else "WRONG") for idx, q in enumerate(selected)}
        result = evaluate_technical_assessment(selected, answers)
        sum_topic = sum(t["score"] for t in result["topic_scores"].values())
        self.assertEqual(sum_topic, result["score"])

    def test_18_domain_scores_are_correct(self):
        """18. Domain scores are correct for Both mode."""
        selected = select_technical_questions(domain="Both", random_seed=77)
        answers = {q["id"]: q["answer"] for q in selected}
        result = evaluate_technical_assessment(selected, answers)
        self.assertIn("IT", result["domain_scores"])
        self.assertIn("Core", result["domain_scores"])
        self.assertEqual(result["domain_scores"]["IT"]["total"], 8)
        self.assertEqual(result["domain_scores"]["Core"]["total"], 7)
        sum_domain = result["domain_scores"]["IT"]["score"] + result["domain_scores"]["Core"]["score"]
        self.assertEqual(sum_domain, result["score"])

    def test_19_strong_weak_topic_classification_works(self):
        """19. Strong/weak topic classification with 70% threshold."""
        selected = select_technical_questions(domain="IT", random_seed=42)
        # Select one topic to be 100% and others 0%
        first_topic = selected[0]["topic"]
        answers = {}
        for q in selected:
            if q["topic"] == first_topic:
                answers[q["id"]] = q["answer"]
            else:
                answers[q["id"]] = "WRONG"

        result = evaluate_technical_assessment(selected, answers, threshold=70.0)
        self.assertIn(first_topic, result["strong_topics"])
        for top in result["weak_topics"]:
            self.assertNotEqual(top, first_topic)

    def test_20_invalid_question_data_detected(self):
        """20. Invalid question data is detected properly."""
        # Bad domain
        with self.assertRaises(ValueError):
            validate_technical_question({
                "id": 999, "domain": "Finance", "topic": "DBMS",
                "question": "Q?", "options": ["A", "B", "C", "D"], "answer": "A", "explanation": "E"
            })

        # Mismatched topic and domain
        with self.assertRaises(ValueError):
            validate_technical_question({
                "id": 999, "domain": "IT", "topic": "Digital Electronics",
                "question": "Q?", "options": ["A", "B", "C", "D"], "answer": "A", "explanation": "E"
            })

        # Answer not in options
        with self.assertRaises(ValueError):
            validate_technical_question({
                "id": 999, "domain": "IT", "topic": "SQL",
                "question": "Q?", "options": ["A", "B", "C", "D"], "answer": "Z", "explanation": "E"
            })


if __name__ == '__main__':
    unittest.main()
