import unittest
import sys
sys.path.append("..")
from src.age import Age as age

class TestAge2(unittest.TestCase):

    def age_under_9_is_a_child(self):
        self.assertEqual(
            age.categorize_by_age(3), 
            "Child",
            "Should have returned 'Child'")

    def test_age_21_is_an_adult(self):
        
        # Arrange
        persons_age = 21
        expected_result = "Adult"

        # Act
        actual_result = age.categorize_by_age(persons_age)

        # Assert
        self.assertEqual(actual_result, expected_result,
            "Should have returned \'{}\'".format(expected_result))
        
    def test_it_raises_exception_when_age_is_less_than_1(self):
        self.assertRaises(Exception, age.categorize_by_age(0))

if __name__ == '__main__':
    unittest.main()