import sys
#sys.path.append("..")
import pytest
import operator 
import re
from hypothesis import given, strategies as st, settings
from hypothesis.stateful import Bundle, RuleBasedStateMachine, rule
from rpn import RPN as rpn

class TestRPNProps():

    @given(st.from_regex(r"^-?(?:\d+|\d*\.\d+)$"), 
           st.from_regex(r"^-?(?:\d+|\d*\.\d+)$"), 
           st.sampled_from(["+", "-", "*", "/", "%", "P", "p"]))
    def test_calculator_operations(self, operand1, operand2, op):
        rpn.enter(rpn, operand1)
        rpn.enter(rpn, operand2)
        result = rpn.enter(rpn, op) 
        this_op = operator.add if op == "+" else \
                  operator.sub if op == "-" else \
                  operator.mul if op == "*" else \
                  operator.floordiv if op == "/" else \
                  operator.mod if op == "%" else \
                  operator.pow
        assert float(result) == pytest.approx(this_op(float(operand1), float(operand2)))

if __name__ == '__main__':
    pytest.main()   
    