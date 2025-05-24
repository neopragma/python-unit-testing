import pytest
from age import Age as age

class TestAge():

    # Sample test case showing the Arrange, Act, Assert pattern 
    def test_an_8_yo_is_a_child(self):
        # Arrange - set up the preconditions for the example
        expected = 'Child'
        
        # Act - invoke the SUT 
        actual = age.categorize_by_age(8)

        # Assert - check the result
        assert actual == expected, f"Expected {expected}, but got {actual}"

    # Sample test case without the comments 
    def test_a_10_yo_is_an_adolescent(self):
        expected = 'Adolescent'
        actual = age.categorize_by_age(10)
        assert actual == expected, f"Expected {expected}, but got {actual}"

    # Sample test case compressed to a single line
    def test_a_70_yo_is_a_golden_age(self): 
        assert age.categorize_by_age(70) == 'Golden age'
        
    def test_a_21_yo_is_an_adult(self): 
        assert age.categorize_by_age(21) == 'Adult'    
        
    # Sample test case showing how to check that an exception is raised
    def test_it_raises_exception_when_age_is_less_than_1(self):
        with pytest.raises(Exception) as excp:
             age.categorize_by_age(0)

    # Sample test case showing how to define multiple examples 
    # that have the same pattern but have different input values 
    # and expected results.
    # This is a parameterized test case 
    @pytest.mark.parametrize(
            "persons_age, expected", 
            [(8, 'Child'), 
             (10, 'Adolescent'),
             (21, 'Adult'),
             (70, 'Golden age')])
    def test_age_ranges(self, persons_age, expected):
        assert age.categorize_by_age(persons_age) == expected
