# Reverse Polish Notation calculator 

import operator
import re 

class RPN:     
    stack = []
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.floordiv,
        "P": operator.pow,
        "p": operator.pow,
        "%": operator.mod}   
    def __init__(self):
        self.stack = []

    def enter(self, val):
        if val.lower() == "c":
            self.stack = [""]   
        elif re.match(r"[\d]", val): 
            self.stack.append(str(float(val)))
        elif re.match(r"[+\-*/%Pp]+", val):
            operand_2 = float(self.stack.pop())
            operand_1 = float(self.stack.pop())
            self.stack.append(str(self.ops[val](operand_1, operand_2)))
        else: 
            raise ValueError("Invalid input")
        return self.stack[-1]






