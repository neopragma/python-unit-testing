import pytest
import sys
from age import Age as age

class TestAge():

    def test_age_under_9_is_a_child(self):
        expected = 'Child'
        actual = age.categorize_by_age(8)
        assert actual == expected, f"Expected {expected}, but got {actual}"

    def test_age_between_9_and_12_is_an_adolescent(self):
        expected = 'Adolescent'
        actual = age.categorize_by_age(10)
        assert actual == expected, f"Expected {expected}, but got {actual}"
        
    def test_it_raises_exception_when_age_is_less_than_1(self):
        with pytest.raises(Exception) as excp:
             age.categorize_by_age(0)

    @pytest.mark.parametrize(
            "persons_age, expected", 
            [(8, 'Child'), 
             (10, 'Adolescent'),
             (21, 'Adult'),
             (70, 'Golden age')])
    def test_age_ranges(self, persons_age, expected):
        assert age.categorize_by_age(persons_age) == expected

if __name__ == '__main__':
    pytest.main()