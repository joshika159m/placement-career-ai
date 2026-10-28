"""
Unit Tests for Live Aptitude Assessment Module
Verifies question bank integrity, random selection, scoring, and validation.
"""

import unittest
import sys
import os

# Add root directory to python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.aptitude_questions import APTITUDE_QUESTIONS
from utils.aptitude_assessment import (
    CATEGORY_QUOTA,
    VALID_CATEGORIES,
    validate_question,
    validate_question_set,
    select_assessment_questions,
    evaluate_assessment
)


class TestAptitudeAssessment(unittest.TestCase):

    def test_question_bank_loading(self):
        """Verify question bank loads and contains at least 60 questions."""
        self.assertIsInstance(APTITUDE_QUESTIONS, list)
        self.assertGreaterEqual(len(APTITUDE_QUESTIONS), 60, "Question bank must contain at least 60 questions")
        print(f"\n[PASS] Loaded {len(APTITUDE_QUESTIONS)} questions from question bank.")

    def test_categories_exist_and_balanced(self):
        """Verify all 4 required categories exist with sufficient questions."""
        categories = [q["category"] for q in APTITUDE_QUESTIONS]
        unique_categories = set(categories)

        expected_categories = {"Quantitative Aptitude", "Logical Reasoning", "Verbal Ability", "Data Interpretation"}
        self.assertEqual(unique_categories, expected_categories, "Question bank must contain exactly the 4 required categories")

        for cat in expected_categories:
            count = categories.count(cat)
            self.assertGreaterEqual(count, 15, f"Category '{cat}' should have at least 15 questions in the bank")
            print(f"  - {cat}: {count} questions")

    def test_all_questions_valid(self):
        """Verify every single question in the bank passes validation."""
        seen_ids = set()
        for q in APTITUDE_QUESTIONS:
            self.assertNotIn(q["id"], seen_ids, f"Duplicate ID {q['id']} in question bank")
            seen_ids.add(q["id"])
            self.assertTrue(validate_question(q))

    def test_selection_count_and_uniqueness(self):
        """Verify exactly 15 unique questions are selected with no duplicate IDs."""
        for seed in range(5):
            selected = select_assessment_questions(random_seed=seed)
            self.assertEqual(len(selected), 15, "Must select exactly 15 questions")

            ids = [q["id"] for q in selected]
            self.assertEqual(len(ids), len(set(ids)), "Selected questions must have no duplicates")

    def test_category_distribution_in_selection(self):
        """Verify quota distribution: 4 Quant, 4 Logical, 4 Verbal, 3 DI."""
        for seed in range(5):
            selected = select_assessment_questions(random_seed=seed)
            cat_counts = {cat: 0 for cat in VALID_CATEGORIES}
            for q in selected:
                cat_counts[q["category"]] += 1

            self.assertEqual(cat_counts["Quantitative Aptitude"], 4)
            self.assertEqual(cat_counts["Logical Reasoning"], 4)
            self.assertEqual(cat_counts["Verbal Ability"], 4)
            self.assertEqual(cat_counts["Data Interpretation"], 3)

    def test_scoring_all_correct(self):
        """Verify scoring when all 15 questions are answered correctly."""
        selected = select_assessment_questions(random_seed=42)
        answers = {q["id"]: q["answer"] for q in selected}

        result = evaluate_assessment(selected, answers)

        self.assertEqual(result["score"], 15)
        self.assertEqual(result["total"], 15)
        self.assertEqual(result["percentage"], 100.0)
        self.assertEqual(len(result["weak_topics"]), 0)
        self.assertEqual(len(result["strong_topics"]), 4)

        for cat, stats in result["category_scores"].items():
            self.assertEqual(stats["score"], stats["total"])
            self.assertEqual(stats["percentage"], 100.0)

    def test_scoring_all_incorrect(self):
        """Verify scoring when all answers are incorrect or unattempted."""
        selected = select_assessment_questions(random_seed=42)
        answers = {q["id"]: "WRONG_ANSWER" for q in selected}

        result = evaluate_assessment(selected, answers)

        self.assertEqual(result["score"], 0)
        self.assertEqual(result["total"], 15)
        self.assertEqual(result["percentage"], 0.0)
        self.assertEqual(len(result["strong_topics"]), 0)
        self.assertEqual(len(result["weak_topics"]), 4)

        for cat, stats in result["category_scores"].items():
            self.assertEqual(stats["score"], 0)
            self.assertEqual(stats["percentage"], 0.0)

    def test_scoring_partial_and_category_sum(self):
        """Verify partial scoring and that category scores sum up to total score."""
        selected = select_assessment_questions(random_seed=101)
        # Answer first 10 correctly, last 5 incorrectly
        answers = {}
        for idx, q in enumerate(selected):
            answers[q["id"]] = q["answer"] if idx < 10 else "WRONG"

        result = evaluate_assessment(selected, answers)

        self.assertEqual(result["score"], 10)
        self.assertEqual(result["total"], 15)
        expected_pct = round((10 / 15) * 100, 2)  # 66.67%
        self.assertEqual(result["percentage"], expected_pct)

        # Check category scores sum up to total
        cat_sum = sum(s["score"] for s in result["category_scores"].values())
        self.assertEqual(cat_sum, result["score"])

    def test_invalid_question_data_detected(self):
        """Verify validation catches malformed question dictionaries."""
        # 1. Missing keys
        with self.assertRaises(ValueError):
            validate_question({"id": 999, "question": "Incomplete?"})

        # 2. Options count not 4
        with self.assertRaises(ValueError):
            validate_question({
                "id": 999,
                "category": "Logical Reasoning",
                "question": "Test?",
                "options": ["A", "B", "C"],  # Only 3
                "answer": "A",
                "explanation": "Exp"
            })

        # 3. Answer not in options
        with self.assertRaises(ValueError):
            validate_question({
                "id": 999,
                "category": "Logical Reasoning",
                "question": "Test?",
                "options": ["A", "B", "C", "D"],
                "answer": "Z",  # Not in options
                "explanation": "Exp"
            })

        # 4. Invalid category
        with self.assertRaises(ValueError):
            validate_question({
                "id": 999,
                "category": "Astronomy",  # Invalid
                "question": "Test?",
                "options": ["A", "B", "C", "D"],
                "answer": "A",
                "explanation": "Exp"
            })

    def test_invalid_question_set_detected(self):
        """Verify validation catches malformed question sets (e.g. wrong count or duplicates)."""
        selected = select_assessment_questions(random_seed=12)

        # 14 questions instead of 15
        with self.assertRaises(ValueError):
            validate_question_set(selected[:14])

        # Duplicate questions
        duplicate_set = selected[:14] + [selected[0]]
        with self.assertRaises(ValueError):
            validate_question_set(duplicate_set)


if __name__ == '__main__':
    unittest.main()
