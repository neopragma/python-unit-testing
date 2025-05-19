import pytest
import sys
from rpn import RPN as rpn

class TestRPN():
    def test_returns_the_last_number_entered(self):
        rpn.enter(rpn, "5")
        assert rpn.enter(rpn,"2") == "2.0"

    def test_adds_2_numbers_and_returns_the_result(self):
        rpn.enter(rpn, "5.987")
        rpn.enter(rpn, "2.0005")
        result = rpn.enter(rpn,"+") 
        assert float(result) == pytest.approx(7.9875) 

    def test_subtracts_2_numbers_and_returns_the_result(self):
        rpn.enter(rpn, "5.4")
        rpn.enter(rpn, "3.1")
        result = rpn.enter(rpn,"-") 
        assert float(result) == pytest.approx(2.3) 

    def test_multiplies_2_numbers_and_returns_the_result(self):
        rpn.enter(rpn, "15.01")
        rpn.enter(rpn, "6.4")
        result = rpn.enter(rpn,"*") 
        assert float(result) == pytest.approx(96.064) 

    def test_divides_2_numbers_and_returns_the_result(self):
        rpn.enter(rpn, "15")
        rpn.enter(rpn, "3")
        result = rpn.enter(rpn,"/") 
        assert float(result) == pytest.approx(5) 

    def test_it_returns_the_modulus_of_2_numbers(self):
        rpn.enter(rpn, "100")
        rpn.enter(rpn, "7")
        result = rpn.enter(rpn,"%") 
        assert float(result) == pytest.approx(2) 

    def test_it_performs_exponentiation_and_returns_the_result(self):
        rpn.enter(rpn, "10")
        rpn.enter(rpn, "3")
        result = rpn.enter(rpn,"P") 
        assert float(result) == pytest.approx(1000) 

    def test_it_performs_complex_expressions_1(self):
        rpn.enter(rpn, "4")
        rpn.enter(rpn, "13")
        rpn.enter(rpn, "-") 
        rpn.enter(rpn, "10")
        result = rpn.enter(rpn, "*")
        assert float(result) == pytest.approx(-90)

    def test_it_performs_complex_expressions_2(self):
        rpn.enter(rpn, "4")
        rpn.enter(rpn, "7.5")
        rpn.enter(rpn, "2") 
        rpn.enter(rpn, "-") 
        result = rpn.enter(rpn, "*")
        assert float(result) == pytest.approx(22)

    def test_it_raises_ValueError_when_input_is_not_valid(self):
        with pytest.raises(ValueError) as excp:
            rpn.enter(rpn, "a")
        assert str(excp.value) == "Invalid input"

    def test_C_command_clears_the_calculator_memory(self):
        rpn.enter(rpn, "5")
        rpn.enter(rpn, "2")
        assert rpn.enter(rpn,"C") == ""


if __name__ == '__main__':
    pytest.main()