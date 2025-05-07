import unittest
import sys
sys.path.append("..")
from src.rpn import RPN as rpn

class TestRPN(unittest.TestCase):
    def test_enter(self):
        self.assertEqual(rpn.enter(rpn,"2"), "2")
