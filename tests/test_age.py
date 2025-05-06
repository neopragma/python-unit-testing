import unittest
import sys
sys.path.append("..")
from src.age import Age as age

class TestCalc(unittest.TestCase):

    def age_under_9_is_a_child(self):
        self.assertEqual(
            age.categorize_by_age(8), 
            "Child",
            "Should have returned 'Child'")

    def test_age_between_9_and_12_is_an_adolescent(self):
        self.assertEqual(
            age.categorize_by_age(1), 
            "Adolescent",
            "Should have returned 'Adolescent'")

if __name__ == '__main__':
    unittest.main()