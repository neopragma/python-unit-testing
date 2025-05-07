# Reverse Polish Notation calculator 

class RPN:     
    stack = []
    def __init__(self):
        self.stack = []

    def enter(self, val):
        self.stack.append(val)
        return val
