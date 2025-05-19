# Reverse Polish Notation calculator 

import operator
import re 
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*call_args, **call_kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*call_args, **call_kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_yield_from_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*call_args, **call_kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*call_args, **call_kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg:
        # call to a class method where self is not bound
        result = yield from mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = yield from mutants[mutant_name](*call_args, **call_kwargs)
    return result

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
    def xǁRPNǁ__init____mutmut_orig(self):
        self.stack = []
    def xǁRPNǁ__init____mutmut_1(self):
        self.stack = None
    
    xǁRPNǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁRPNǁ__init____mutmut_1': xǁRPNǁ__init____mutmut_1
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRPNǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁRPNǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁRPNǁ__init____mutmut_orig)
    xǁRPNǁ__init____mutmut_orig.__name__ = 'xǁRPNǁ__init__'

    def xǁRPNǁenter__mutmut_orig(self, val):
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

    def xǁRPNǁenter__mutmut_1(self, val):
        if val.upper() == "c":
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

    def xǁRPNǁenter__mutmut_2(self, val):
        if val.lower() != "c":
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

    def xǁRPNǁenter__mutmut_3(self, val):
        if val.lower() == "XXcXX":
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

    def xǁRPNǁenter__mutmut_4(self, val):
        if val.lower() == "C":
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

    def xǁRPNǁenter__mutmut_5(self, val):
        if val.lower() == "C":
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

    def xǁRPNǁenter__mutmut_6(self, val):
        if val.lower() == "c":
            self.stack = None   
        elif re.match(r"[\d]", val): 
            self.stack.append(str(float(val)))
        elif re.match(r"[+\-*/%Pp]+", val):
            operand_2 = float(self.stack.pop())
            operand_1 = float(self.stack.pop())
            self.stack.append(str(self.ops[val](operand_1, operand_2)))
        else: 
            raise ValueError("Invalid input")
        return self.stack[-1]

    def xǁRPNǁenter__mutmut_7(self, val):
        if val.lower() == "c":
            self.stack = ["XXXX"]   
        elif re.match(r"[\d]", val): 
            self.stack.append(str(float(val)))
        elif re.match(r"[+\-*/%Pp]+", val):
            operand_2 = float(self.stack.pop())
            operand_1 = float(self.stack.pop())
            self.stack.append(str(self.ops[val](operand_1, operand_2)))
        else: 
            raise ValueError("Invalid input")
        return self.stack[-1]

    def xǁRPNǁenter__mutmut_8(self, val):
        if val.lower() == "c":
            self.stack = [""]   
        elif re.match(None, val): 
            self.stack.append(str(float(val)))
        elif re.match(r"[+\-*/%Pp]+", val):
            operand_2 = float(self.stack.pop())
            operand_1 = float(self.stack.pop())
            self.stack.append(str(self.ops[val](operand_1, operand_2)))
        else: 
            raise ValueError("Invalid input")
        return self.stack[-1]

    def xǁRPNǁenter__mutmut_9(self, val):
        if val.lower() == "c":
            self.stack = [""]   
        elif re.match(r"[\d]", None): 
            self.stack.append(str(float(val)))
        elif re.match(r"[+\-*/%Pp]+", val):
            operand_2 = float(self.stack.pop())
            operand_1 = float(self.stack.pop())
            self.stack.append(str(self.ops[val](operand_1, operand_2)))
        else: 
            raise ValueError("Invalid input")
        return self.stack[-1]

    def xǁRPNǁenter__mutmut_10(self, val):
        if val.lower() == "c":
            self.stack = [""]   
        elif re.match(val): 
            self.stack.append(str(float(val)))
        elif re.match(r"[+\-*/%Pp]+", val):
            operand_2 = float(self.stack.pop())
            operand_1 = float(self.stack.pop())
            self.stack.append(str(self.ops[val](operand_1, operand_2)))
        else: 
            raise ValueError("Invalid input")
        return self.stack[-1]

    def xǁRPNǁenter__mutmut_11(self, val):
        if val.lower() == "c":
            self.stack = [""]   
        elif re.match(r"[\d]", ): 
            self.stack.append(str(float(val)))
        elif re.match(r"[+\-*/%Pp]+", val):
            operand_2 = float(self.stack.pop())
            operand_1 = float(self.stack.pop())
            self.stack.append(str(self.ops[val](operand_1, operand_2)))
        else: 
            raise ValueError("Invalid input")
        return self.stack[-1]

    def xǁRPNǁenter__mutmut_12(self, val):
        if val.lower() == "c":
            self.stack = [""]   
        elif re.match(r"XX[\d]XX", val): 
            self.stack.append(str(float(val)))
        elif re.match(r"[+\-*/%Pp]+", val):
            operand_2 = float(self.stack.pop())
            operand_1 = float(self.stack.pop())
            self.stack.append(str(self.ops[val](operand_1, operand_2)))
        else: 
            raise ValueError("Invalid input")
        return self.stack[-1]

    def xǁRPNǁenter__mutmut_13(self, val):
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

    def xǁRPNǁenter__mutmut_14(self, val):
        if val.lower() == "c":
            self.stack = [""]   
        elif re.match(r"[\D]", val): 
            self.stack.append(str(float(val)))
        elif re.match(r"[+\-*/%Pp]+", val):
            operand_2 = float(self.stack.pop())
            operand_1 = float(self.stack.pop())
            self.stack.append(str(self.ops[val](operand_1, operand_2)))
        else: 
            raise ValueError("Invalid input")
        return self.stack[-1]

    def xǁRPNǁenter__mutmut_15(self, val):
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

    def xǁRPNǁenter__mutmut_16(self, val):
        if val.lower() == "c":
            self.stack = [""]   
        elif re.match(r"[\d]", val): 
            self.stack.append(None)
        elif re.match(r"[+\-*/%Pp]+", val):
            operand_2 = float(self.stack.pop())
            operand_1 = float(self.stack.pop())
            self.stack.append(str(self.ops[val](operand_1, operand_2)))
        else: 
            raise ValueError("Invalid input")
        return self.stack[-1]

    def xǁRPNǁenter__mutmut_17(self, val):
        if val.lower() == "c":
            self.stack = [""]   
        elif re.match(r"[\d]", val): 
            self.stack.append(str(None))
        elif re.match(r"[+\-*/%Pp]+", val):
            operand_2 = float(self.stack.pop())
            operand_1 = float(self.stack.pop())
            self.stack.append(str(self.ops[val](operand_1, operand_2)))
        else: 
            raise ValueError("Invalid input")
        return self.stack[-1]

    def xǁRPNǁenter__mutmut_18(self, val):
        if val.lower() == "c":
            self.stack = [""]   
        elif re.match(r"[\d]", val): 
            self.stack.append(str(float(None)))
        elif re.match(r"[+\-*/%Pp]+", val):
            operand_2 = float(self.stack.pop())
            operand_1 = float(self.stack.pop())
            self.stack.append(str(self.ops[val](operand_1, operand_2)))
        else: 
            raise ValueError("Invalid input")
        return self.stack[-1]

    def xǁRPNǁenter__mutmut_19(self, val):
        if val.lower() == "c":
            self.stack = [""]   
        elif re.match(r"[\d]", val): 
            self.stack.append(str(float(val)))
        elif re.match(None, val):
            operand_2 = float(self.stack.pop())
            operand_1 = float(self.stack.pop())
            self.stack.append(str(self.ops[val](operand_1, operand_2)))
        else: 
            raise ValueError("Invalid input")
        return self.stack[-1]

    def xǁRPNǁenter__mutmut_20(self, val):
        if val.lower() == "c":
            self.stack = [""]   
        elif re.match(r"[\d]", val): 
            self.stack.append(str(float(val)))
        elif re.match(r"[+\-*/%Pp]+", None):
            operand_2 = float(self.stack.pop())
            operand_1 = float(self.stack.pop())
            self.stack.append(str(self.ops[val](operand_1, operand_2)))
        else: 
            raise ValueError("Invalid input")
        return self.stack[-1]

    def xǁRPNǁenter__mutmut_21(self, val):
        if val.lower() == "c":
            self.stack = [""]   
        elif re.match(r"[\d]", val): 
            self.stack.append(str(float(val)))
        elif re.match(val):
            operand_2 = float(self.stack.pop())
            operand_1 = float(self.stack.pop())
            self.stack.append(str(self.ops[val](operand_1, operand_2)))
        else: 
            raise ValueError("Invalid input")
        return self.stack[-1]

    def xǁRPNǁenter__mutmut_22(self, val):
        if val.lower() == "c":
            self.stack = [""]   
        elif re.match(r"[\d]", val): 
            self.stack.append(str(float(val)))
        elif re.match(r"[+\-*/%Pp]+", ):
            operand_2 = float(self.stack.pop())
            operand_1 = float(self.stack.pop())
            self.stack.append(str(self.ops[val](operand_1, operand_2)))
        else: 
            raise ValueError("Invalid input")
        return self.stack[-1]

    def xǁRPNǁenter__mutmut_23(self, val):
        if val.lower() == "c":
            self.stack = [""]   
        elif re.match(r"[\d]", val): 
            self.stack.append(str(float(val)))
        elif re.match(r"XX[+\-*/%Pp]+XX", val):
            operand_2 = float(self.stack.pop())
            operand_1 = float(self.stack.pop())
            self.stack.append(str(self.ops[val](operand_1, operand_2)))
        else: 
            raise ValueError("Invalid input")
        return self.stack[-1]

    def xǁRPNǁenter__mutmut_24(self, val):
        if val.lower() == "c":
            self.stack = [""]   
        elif re.match(r"[\d]", val): 
            self.stack.append(str(float(val)))
        elif re.match(r"[+\-*/%pp]+", val):
            operand_2 = float(self.stack.pop())
            operand_1 = float(self.stack.pop())
            self.stack.append(str(self.ops[val](operand_1, operand_2)))
        else: 
            raise ValueError("Invalid input")
        return self.stack[-1]

    def xǁRPNǁenter__mutmut_25(self, val):
        if val.lower() == "c":
            self.stack = [""]   
        elif re.match(r"[\d]", val): 
            self.stack.append(str(float(val)))
        elif re.match(r"[+\-*/%PP]+", val):
            operand_2 = float(self.stack.pop())
            operand_1 = float(self.stack.pop())
            self.stack.append(str(self.ops[val](operand_1, operand_2)))
        else: 
            raise ValueError("Invalid input")
        return self.stack[-1]

    def xǁRPNǁenter__mutmut_26(self, val):
        if val.lower() == "c":
            self.stack = [""]   
        elif re.match(r"[\d]", val): 
            self.stack.append(str(float(val)))
        elif re.match(r"[+\-*/%pp]+", val):
            operand_2 = float(self.stack.pop())
            operand_1 = float(self.stack.pop())
            self.stack.append(str(self.ops[val](operand_1, operand_2)))
        else: 
            raise ValueError("Invalid input")
        return self.stack[-1]

    def xǁRPNǁenter__mutmut_27(self, val):
        if val.lower() == "c":
            self.stack = [""]   
        elif re.match(r"[\d]", val): 
            self.stack.append(str(float(val)))
        elif re.match(r"[+\-*/%Pp]+", val):
            operand_2 = None
            operand_1 = float(self.stack.pop())
            self.stack.append(str(self.ops[val](operand_1, operand_2)))
        else: 
            raise ValueError("Invalid input")
        return self.stack[-1]

    def xǁRPNǁenter__mutmut_28(self, val):
        if val.lower() == "c":
            self.stack = [""]   
        elif re.match(r"[\d]", val): 
            self.stack.append(str(float(val)))
        elif re.match(r"[+\-*/%Pp]+", val):
            operand_2 = float(None)
            operand_1 = float(self.stack.pop())
            self.stack.append(str(self.ops[val](operand_1, operand_2)))
        else: 
            raise ValueError("Invalid input")
        return self.stack[-1]

    def xǁRPNǁenter__mutmut_29(self, val):
        if val.lower() == "c":
            self.stack = [""]   
        elif re.match(r"[\d]", val): 
            self.stack.append(str(float(val)))
        elif re.match(r"[+\-*/%Pp]+", val):
            operand_2 = float(self.stack.pop())
            operand_1 = None
            self.stack.append(str(self.ops[val](operand_1, operand_2)))
        else: 
            raise ValueError("Invalid input")
        return self.stack[-1]

    def xǁRPNǁenter__mutmut_30(self, val):
        if val.lower() == "c":
            self.stack = [""]   
        elif re.match(r"[\d]", val): 
            self.stack.append(str(float(val)))
        elif re.match(r"[+\-*/%Pp]+", val):
            operand_2 = float(self.stack.pop())
            operand_1 = float(None)
            self.stack.append(str(self.ops[val](operand_1, operand_2)))
        else: 
            raise ValueError("Invalid input")
        return self.stack[-1]

    def xǁRPNǁenter__mutmut_31(self, val):
        if val.lower() == "c":
            self.stack = [""]   
        elif re.match(r"[\d]", val): 
            self.stack.append(str(float(val)))
        elif re.match(r"[+\-*/%Pp]+", val):
            operand_2 = float(self.stack.pop())
            operand_1 = float(self.stack.pop())
            self.stack.append(None)
        else: 
            raise ValueError("Invalid input")
        return self.stack[-1]

    def xǁRPNǁenter__mutmut_32(self, val):
        if val.lower() == "c":
            self.stack = [""]   
        elif re.match(r"[\d]", val): 
            self.stack.append(str(float(val)))
        elif re.match(r"[+\-*/%Pp]+", val):
            operand_2 = float(self.stack.pop())
            operand_1 = float(self.stack.pop())
            self.stack.append(str(None))
        else: 
            raise ValueError("Invalid input")
        return self.stack[-1]

    def xǁRPNǁenter__mutmut_33(self, val):
        if val.lower() == "c":
            self.stack = [""]   
        elif re.match(r"[\d]", val): 
            self.stack.append(str(float(val)))
        elif re.match(r"[+\-*/%Pp]+", val):
            operand_2 = float(self.stack.pop())
            operand_1 = float(self.stack.pop())
            self.stack.append(str(self.ops[val](None, operand_2)))
        else: 
            raise ValueError("Invalid input")
        return self.stack[-1]

    def xǁRPNǁenter__mutmut_34(self, val):
        if val.lower() == "c":
            self.stack = [""]   
        elif re.match(r"[\d]", val): 
            self.stack.append(str(float(val)))
        elif re.match(r"[+\-*/%Pp]+", val):
            operand_2 = float(self.stack.pop())
            operand_1 = float(self.stack.pop())
            self.stack.append(str(self.ops[val](operand_1, None)))
        else: 
            raise ValueError("Invalid input")
        return self.stack[-1]

    def xǁRPNǁenter__mutmut_35(self, val):
        if val.lower() == "c":
            self.stack = [""]   
        elif re.match(r"[\d]", val): 
            self.stack.append(str(float(val)))
        elif re.match(r"[+\-*/%Pp]+", val):
            operand_2 = float(self.stack.pop())
            operand_1 = float(self.stack.pop())
            self.stack.append(str(self.ops[val](operand_2)))
        else: 
            raise ValueError("Invalid input")
        return self.stack[-1]

    def xǁRPNǁenter__mutmut_36(self, val):
        if val.lower() == "c":
            self.stack = [""]   
        elif re.match(r"[\d]", val): 
            self.stack.append(str(float(val)))
        elif re.match(r"[+\-*/%Pp]+", val):
            operand_2 = float(self.stack.pop())
            operand_1 = float(self.stack.pop())
            self.stack.append(str(self.ops[val](operand_1, )))
        else: 
            raise ValueError("Invalid input")
        return self.stack[-1]

    def xǁRPNǁenter__mutmut_37(self, val):
        if val.lower() == "c":
            self.stack = [""]   
        elif re.match(r"[\d]", val): 
            self.stack.append(str(float(val)))
        elif re.match(r"[+\-*/%Pp]+", val):
            operand_2 = float(self.stack.pop())
            operand_1 = float(self.stack.pop())
            self.stack.append(str(self.ops[val](operand_1, operand_2)))
        else: 
            raise ValueError(None)
        return self.stack[-1]

    def xǁRPNǁenter__mutmut_38(self, val):
        if val.lower() == "c":
            self.stack = [""]   
        elif re.match(r"[\d]", val): 
            self.stack.append(str(float(val)))
        elif re.match(r"[+\-*/%Pp]+", val):
            operand_2 = float(self.stack.pop())
            operand_1 = float(self.stack.pop())
            self.stack.append(str(self.ops[val](operand_1, operand_2)))
        else: 
            raise ValueError("XXInvalid inputXX")
        return self.stack[-1]

    def xǁRPNǁenter__mutmut_39(self, val):
        if val.lower() == "c":
            self.stack = [""]   
        elif re.match(r"[\d]", val): 
            self.stack.append(str(float(val)))
        elif re.match(r"[+\-*/%Pp]+", val):
            operand_2 = float(self.stack.pop())
            operand_1 = float(self.stack.pop())
            self.stack.append(str(self.ops[val](operand_1, operand_2)))
        else: 
            raise ValueError("invalid input")
        return self.stack[-1]

    def xǁRPNǁenter__mutmut_40(self, val):
        if val.lower() == "c":
            self.stack = [""]   
        elif re.match(r"[\d]", val): 
            self.stack.append(str(float(val)))
        elif re.match(r"[+\-*/%Pp]+", val):
            operand_2 = float(self.stack.pop())
            operand_1 = float(self.stack.pop())
            self.stack.append(str(self.ops[val](operand_1, operand_2)))
        else: 
            raise ValueError("INVALID INPUT")
        return self.stack[-1]

    def xǁRPNǁenter__mutmut_41(self, val):
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
        return self.stack[+1]

    def xǁRPNǁenter__mutmut_42(self, val):
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
        return self.stack[-2]
    
    xǁRPNǁenter__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁRPNǁenter__mutmut_1': xǁRPNǁenter__mutmut_1, 
        'xǁRPNǁenter__mutmut_2': xǁRPNǁenter__mutmut_2, 
        'xǁRPNǁenter__mutmut_3': xǁRPNǁenter__mutmut_3, 
        'xǁRPNǁenter__mutmut_4': xǁRPNǁenter__mutmut_4, 
        'xǁRPNǁenter__mutmut_5': xǁRPNǁenter__mutmut_5, 
        'xǁRPNǁenter__mutmut_6': xǁRPNǁenter__mutmut_6, 
        'xǁRPNǁenter__mutmut_7': xǁRPNǁenter__mutmut_7, 
        'xǁRPNǁenter__mutmut_8': xǁRPNǁenter__mutmut_8, 
        'xǁRPNǁenter__mutmut_9': xǁRPNǁenter__mutmut_9, 
        'xǁRPNǁenter__mutmut_10': xǁRPNǁenter__mutmut_10, 
        'xǁRPNǁenter__mutmut_11': xǁRPNǁenter__mutmut_11, 
        'xǁRPNǁenter__mutmut_12': xǁRPNǁenter__mutmut_12, 
        'xǁRPNǁenter__mutmut_13': xǁRPNǁenter__mutmut_13, 
        'xǁRPNǁenter__mutmut_14': xǁRPNǁenter__mutmut_14, 
        'xǁRPNǁenter__mutmut_15': xǁRPNǁenter__mutmut_15, 
        'xǁRPNǁenter__mutmut_16': xǁRPNǁenter__mutmut_16, 
        'xǁRPNǁenter__mutmut_17': xǁRPNǁenter__mutmut_17, 
        'xǁRPNǁenter__mutmut_18': xǁRPNǁenter__mutmut_18, 
        'xǁRPNǁenter__mutmut_19': xǁRPNǁenter__mutmut_19, 
        'xǁRPNǁenter__mutmut_20': xǁRPNǁenter__mutmut_20, 
        'xǁRPNǁenter__mutmut_21': xǁRPNǁenter__mutmut_21, 
        'xǁRPNǁenter__mutmut_22': xǁRPNǁenter__mutmut_22, 
        'xǁRPNǁenter__mutmut_23': xǁRPNǁenter__mutmut_23, 
        'xǁRPNǁenter__mutmut_24': xǁRPNǁenter__mutmut_24, 
        'xǁRPNǁenter__mutmut_25': xǁRPNǁenter__mutmut_25, 
        'xǁRPNǁenter__mutmut_26': xǁRPNǁenter__mutmut_26, 
        'xǁRPNǁenter__mutmut_27': xǁRPNǁenter__mutmut_27, 
        'xǁRPNǁenter__mutmut_28': xǁRPNǁenter__mutmut_28, 
        'xǁRPNǁenter__mutmut_29': xǁRPNǁenter__mutmut_29, 
        'xǁRPNǁenter__mutmut_30': xǁRPNǁenter__mutmut_30, 
        'xǁRPNǁenter__mutmut_31': xǁRPNǁenter__mutmut_31, 
        'xǁRPNǁenter__mutmut_32': xǁRPNǁenter__mutmut_32, 
        'xǁRPNǁenter__mutmut_33': xǁRPNǁenter__mutmut_33, 
        'xǁRPNǁenter__mutmut_34': xǁRPNǁenter__mutmut_34, 
        'xǁRPNǁenter__mutmut_35': xǁRPNǁenter__mutmut_35, 
        'xǁRPNǁenter__mutmut_36': xǁRPNǁenter__mutmut_36, 
        'xǁRPNǁenter__mutmut_37': xǁRPNǁenter__mutmut_37, 
        'xǁRPNǁenter__mutmut_38': xǁRPNǁenter__mutmut_38, 
        'xǁRPNǁenter__mutmut_39': xǁRPNǁenter__mutmut_39, 
        'xǁRPNǁenter__mutmut_40': xǁRPNǁenter__mutmut_40, 
        'xǁRPNǁenter__mutmut_41': xǁRPNǁenter__mutmut_41, 
        'xǁRPNǁenter__mutmut_42': xǁRPNǁenter__mutmut_42
    }
    
    def enter(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRPNǁenter__mutmut_orig"), object.__getattribute__(self, "xǁRPNǁenter__mutmut_mutants"), args, kwargs, self)
        return result 
    
    enter.__signature__ = _mutmut_signature(xǁRPNǁenter__mutmut_orig)
    xǁRPNǁenter__mutmut_orig.__name__ = 'xǁRPNǁenter'






