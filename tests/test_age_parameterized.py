import unittest
import sys
sys.path.append("..")
from src.age import Age as age

class TestAge(unittest.TestCase):

    def age_has_description(self,personsAge,expected):
        self.assertEqual(
            age.categorize_by_age(int(personsAge)), 
            expected,
            "Age of {} should return {}".format(personsAge,expected))

    def test_age_ranges(self):
        test_values = [1]
        test_values.append("Child")
        test_values.append(1)
        test_values.append("Adolescent")
        for idx, x in enumerate(test_values):
            self.age_has_description(test_values[x],test_values[x+1])

if __name__ == '__main__':
    unittest.main()