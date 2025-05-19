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
class Age:

    def xǁAgeǁcategorize_by_age__mutmut_orig(age):
        if 0 < age <= 9:
            return "Child"
        elif 9 < age <= 18:
            return "Adolescent"
        elif 18 < age <= 65:
            return "Adult"
        elif 65 < age <= 150:
            return "Golden age"
        else:
            raise Exception(f"Invalid age: {age}")

    def xǁAgeǁcategorize_by_age__mutmut_1(age):
        if 1 < age <= 9:
            return "Child"
        elif 9 < age <= 18:
            return "Adolescent"
        elif 18 < age <= 65:
            return "Adult"
        elif 65 < age <= 150:
            return "Golden age"
        else:
            raise Exception(f"Invalid age: {age}")

    def xǁAgeǁcategorize_by_age__mutmut_2(age):
        if 0 <= age <= 9:
            return "Child"
        elif 9 < age <= 18:
            return "Adolescent"
        elif 18 < age <= 65:
            return "Adult"
        elif 65 < age <= 150:
            return "Golden age"
        else:
            raise Exception(f"Invalid age: {age}")

    def xǁAgeǁcategorize_by_age__mutmut_3(age):
        if 0 < age < 9:
            return "Child"
        elif 9 < age <= 18:
            return "Adolescent"
        elif 18 < age <= 65:
            return "Adult"
        elif 65 < age <= 150:
            return "Golden age"
        else:
            raise Exception(f"Invalid age: {age}")

    def xǁAgeǁcategorize_by_age__mutmut_4(age):
        if 0 < age <= 10:
            return "Child"
        elif 9 < age <= 18:
            return "Adolescent"
        elif 18 < age <= 65:
            return "Adult"
        elif 65 < age <= 150:
            return "Golden age"
        else:
            raise Exception(f"Invalid age: {age}")

    def xǁAgeǁcategorize_by_age__mutmut_5(age):
        if 0 < age <= 9:
            return "XXChildXX"
        elif 9 < age <= 18:
            return "Adolescent"
        elif 18 < age <= 65:
            return "Adult"
        elif 65 < age <= 150:
            return "Golden age"
        else:
            raise Exception(f"Invalid age: {age}")

    def xǁAgeǁcategorize_by_age__mutmut_6(age):
        if 0 < age <= 9:
            return "child"
        elif 9 < age <= 18:
            return "Adolescent"
        elif 18 < age <= 65:
            return "Adult"
        elif 65 < age <= 150:
            return "Golden age"
        else:
            raise Exception(f"Invalid age: {age}")

    def xǁAgeǁcategorize_by_age__mutmut_7(age):
        if 0 < age <= 9:
            return "CHILD"
        elif 9 < age <= 18:
            return "Adolescent"
        elif 18 < age <= 65:
            return "Adult"
        elif 65 < age <= 150:
            return "Golden age"
        else:
            raise Exception(f"Invalid age: {age}")

    def xǁAgeǁcategorize_by_age__mutmut_8(age):
        if 0 < age <= 9:
            return "Child"
        elif 10 < age <= 18:
            return "Adolescent"
        elif 18 < age <= 65:
            return "Adult"
        elif 65 < age <= 150:
            return "Golden age"
        else:
            raise Exception(f"Invalid age: {age}")

    def xǁAgeǁcategorize_by_age__mutmut_9(age):
        if 0 < age <= 9:
            return "Child"
        elif 9 <= age <= 18:
            return "Adolescent"
        elif 18 < age <= 65:
            return "Adult"
        elif 65 < age <= 150:
            return "Golden age"
        else:
            raise Exception(f"Invalid age: {age}")

    def xǁAgeǁcategorize_by_age__mutmut_10(age):
        if 0 < age <= 9:
            return "Child"
        elif 9 < age < 18:
            return "Adolescent"
        elif 18 < age <= 65:
            return "Adult"
        elif 65 < age <= 150:
            return "Golden age"
        else:
            raise Exception(f"Invalid age: {age}")

    def xǁAgeǁcategorize_by_age__mutmut_11(age):
        if 0 < age <= 9:
            return "Child"
        elif 9 < age <= 19:
            return "Adolescent"
        elif 18 < age <= 65:
            return "Adult"
        elif 65 < age <= 150:
            return "Golden age"
        else:
            raise Exception(f"Invalid age: {age}")

    def xǁAgeǁcategorize_by_age__mutmut_12(age):
        if 0 < age <= 9:
            return "Child"
        elif 9 < age <= 18:
            return "XXAdolescentXX"
        elif 18 < age <= 65:
            return "Adult"
        elif 65 < age <= 150:
            return "Golden age"
        else:
            raise Exception(f"Invalid age: {age}")

    def xǁAgeǁcategorize_by_age__mutmut_13(age):
        if 0 < age <= 9:
            return "Child"
        elif 9 < age <= 18:
            return "adolescent"
        elif 18 < age <= 65:
            return "Adult"
        elif 65 < age <= 150:
            return "Golden age"
        else:
            raise Exception(f"Invalid age: {age}")

    def xǁAgeǁcategorize_by_age__mutmut_14(age):
        if 0 < age <= 9:
            return "Child"
        elif 9 < age <= 18:
            return "ADOLESCENT"
        elif 18 < age <= 65:
            return "Adult"
        elif 65 < age <= 150:
            return "Golden age"
        else:
            raise Exception(f"Invalid age: {age}")

    def xǁAgeǁcategorize_by_age__mutmut_15(age):
        if 0 < age <= 9:
            return "Child"
        elif 9 < age <= 18:
            return "Adolescent"
        elif 19 < age <= 65:
            return "Adult"
        elif 65 < age <= 150:
            return "Golden age"
        else:
            raise Exception(f"Invalid age: {age}")

    def xǁAgeǁcategorize_by_age__mutmut_16(age):
        if 0 < age <= 9:
            return "Child"
        elif 9 < age <= 18:
            return "Adolescent"
        elif 18 <= age <= 65:
            return "Adult"
        elif 65 < age <= 150:
            return "Golden age"
        else:
            raise Exception(f"Invalid age: {age}")

    def xǁAgeǁcategorize_by_age__mutmut_17(age):
        if 0 < age <= 9:
            return "Child"
        elif 9 < age <= 18:
            return "Adolescent"
        elif 18 < age < 65:
            return "Adult"
        elif 65 < age <= 150:
            return "Golden age"
        else:
            raise Exception(f"Invalid age: {age}")

    def xǁAgeǁcategorize_by_age__mutmut_18(age):
        if 0 < age <= 9:
            return "Child"
        elif 9 < age <= 18:
            return "Adolescent"
        elif 18 < age <= 66:
            return "Adult"
        elif 65 < age <= 150:
            return "Golden age"
        else:
            raise Exception(f"Invalid age: {age}")

    def xǁAgeǁcategorize_by_age__mutmut_19(age):
        if 0 < age <= 9:
            return "Child"
        elif 9 < age <= 18:
            return "Adolescent"
        elif 18 < age <= 65:
            return "XXAdultXX"
        elif 65 < age <= 150:
            return "Golden age"
        else:
            raise Exception(f"Invalid age: {age}")

    def xǁAgeǁcategorize_by_age__mutmut_20(age):
        if 0 < age <= 9:
            return "Child"
        elif 9 < age <= 18:
            return "Adolescent"
        elif 18 < age <= 65:
            return "adult"
        elif 65 < age <= 150:
            return "Golden age"
        else:
            raise Exception(f"Invalid age: {age}")

    def xǁAgeǁcategorize_by_age__mutmut_21(age):
        if 0 < age <= 9:
            return "Child"
        elif 9 < age <= 18:
            return "Adolescent"
        elif 18 < age <= 65:
            return "ADULT"
        elif 65 < age <= 150:
            return "Golden age"
        else:
            raise Exception(f"Invalid age: {age}")

    def xǁAgeǁcategorize_by_age__mutmut_22(age):
        if 0 < age <= 9:
            return "Child"
        elif 9 < age <= 18:
            return "Adolescent"
        elif 18 < age <= 65:
            return "Adult"
        elif 66 < age <= 150:
            return "Golden age"
        else:
            raise Exception(f"Invalid age: {age}")

    def xǁAgeǁcategorize_by_age__mutmut_23(age):
        if 0 < age <= 9:
            return "Child"
        elif 9 < age <= 18:
            return "Adolescent"
        elif 18 < age <= 65:
            return "Adult"
        elif 65 <= age <= 150:
            return "Golden age"
        else:
            raise Exception(f"Invalid age: {age}")

    def xǁAgeǁcategorize_by_age__mutmut_24(age):
        if 0 < age <= 9:
            return "Child"
        elif 9 < age <= 18:
            return "Adolescent"
        elif 18 < age <= 65:
            return "Adult"
        elif 65 < age < 150:
            return "Golden age"
        else:
            raise Exception(f"Invalid age: {age}")

    def xǁAgeǁcategorize_by_age__mutmut_25(age):
        if 0 < age <= 9:
            return "Child"
        elif 9 < age <= 18:
            return "Adolescent"
        elif 18 < age <= 65:
            return "Adult"
        elif 65 < age <= 151:
            return "Golden age"
        else:
            raise Exception(f"Invalid age: {age}")

    def xǁAgeǁcategorize_by_age__mutmut_26(age):
        if 0 < age <= 9:
            return "Child"
        elif 9 < age <= 18:
            return "Adolescent"
        elif 18 < age <= 65:
            return "Adult"
        elif 65 < age <= 150:
            return "XXGolden ageXX"
        else:
            raise Exception(f"Invalid age: {age}")

    def xǁAgeǁcategorize_by_age__mutmut_27(age):
        if 0 < age <= 9:
            return "Child"
        elif 9 < age <= 18:
            return "Adolescent"
        elif 18 < age <= 65:
            return "Adult"
        elif 65 < age <= 150:
            return "golden age"
        else:
            raise Exception(f"Invalid age: {age}")

    def xǁAgeǁcategorize_by_age__mutmut_28(age):
        if 0 < age <= 9:
            return "Child"
        elif 9 < age <= 18:
            return "Adolescent"
        elif 18 < age <= 65:
            return "Adult"
        elif 65 < age <= 150:
            return "GOLDEN AGE"
        else:
            raise Exception(f"Invalid age: {age}")

    def xǁAgeǁcategorize_by_age__mutmut_29(age):
        if 0 < age <= 9:
            return "Child"
        elif 9 < age <= 18:
            return "Adolescent"
        elif 18 < age <= 65:
            return "Adult"
        elif 65 < age <= 150:
            return "Golden age"
        else:
            raise Exception(None)
    
    xǁAgeǁcategorize_by_age__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAgeǁcategorize_by_age__mutmut_1': xǁAgeǁcategorize_by_age__mutmut_1, 
        'xǁAgeǁcategorize_by_age__mutmut_2': xǁAgeǁcategorize_by_age__mutmut_2, 
        'xǁAgeǁcategorize_by_age__mutmut_3': xǁAgeǁcategorize_by_age__mutmut_3, 
        'xǁAgeǁcategorize_by_age__mutmut_4': xǁAgeǁcategorize_by_age__mutmut_4, 
        'xǁAgeǁcategorize_by_age__mutmut_5': xǁAgeǁcategorize_by_age__mutmut_5, 
        'xǁAgeǁcategorize_by_age__mutmut_6': xǁAgeǁcategorize_by_age__mutmut_6, 
        'xǁAgeǁcategorize_by_age__mutmut_7': xǁAgeǁcategorize_by_age__mutmut_7, 
        'xǁAgeǁcategorize_by_age__mutmut_8': xǁAgeǁcategorize_by_age__mutmut_8, 
        'xǁAgeǁcategorize_by_age__mutmut_9': xǁAgeǁcategorize_by_age__mutmut_9, 
        'xǁAgeǁcategorize_by_age__mutmut_10': xǁAgeǁcategorize_by_age__mutmut_10, 
        'xǁAgeǁcategorize_by_age__mutmut_11': xǁAgeǁcategorize_by_age__mutmut_11, 
        'xǁAgeǁcategorize_by_age__mutmut_12': xǁAgeǁcategorize_by_age__mutmut_12, 
        'xǁAgeǁcategorize_by_age__mutmut_13': xǁAgeǁcategorize_by_age__mutmut_13, 
        'xǁAgeǁcategorize_by_age__mutmut_14': xǁAgeǁcategorize_by_age__mutmut_14, 
        'xǁAgeǁcategorize_by_age__mutmut_15': xǁAgeǁcategorize_by_age__mutmut_15, 
        'xǁAgeǁcategorize_by_age__mutmut_16': xǁAgeǁcategorize_by_age__mutmut_16, 
        'xǁAgeǁcategorize_by_age__mutmut_17': xǁAgeǁcategorize_by_age__mutmut_17, 
        'xǁAgeǁcategorize_by_age__mutmut_18': xǁAgeǁcategorize_by_age__mutmut_18, 
        'xǁAgeǁcategorize_by_age__mutmut_19': xǁAgeǁcategorize_by_age__mutmut_19, 
        'xǁAgeǁcategorize_by_age__mutmut_20': xǁAgeǁcategorize_by_age__mutmut_20, 
        'xǁAgeǁcategorize_by_age__mutmut_21': xǁAgeǁcategorize_by_age__mutmut_21, 
        'xǁAgeǁcategorize_by_age__mutmut_22': xǁAgeǁcategorize_by_age__mutmut_22, 
        'xǁAgeǁcategorize_by_age__mutmut_23': xǁAgeǁcategorize_by_age__mutmut_23, 
        'xǁAgeǁcategorize_by_age__mutmut_24': xǁAgeǁcategorize_by_age__mutmut_24, 
        'xǁAgeǁcategorize_by_age__mutmut_25': xǁAgeǁcategorize_by_age__mutmut_25, 
        'xǁAgeǁcategorize_by_age__mutmut_26': xǁAgeǁcategorize_by_age__mutmut_26, 
        'xǁAgeǁcategorize_by_age__mutmut_27': xǁAgeǁcategorize_by_age__mutmut_27, 
        'xǁAgeǁcategorize_by_age__mutmut_28': xǁAgeǁcategorize_by_age__mutmut_28, 
        'xǁAgeǁcategorize_by_age__mutmut_29': xǁAgeǁcategorize_by_age__mutmut_29
    }
    
    def categorize_by_age(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAgeǁcategorize_by_age__mutmut_orig"), object.__getattribute__(self, "xǁAgeǁcategorize_by_age__mutmut_mutants"), args, kwargs, self)
        return result 
    
    categorize_by_age.__signature__ = _mutmut_signature(xǁAgeǁcategorize_by_age__mutmut_orig)
    xǁAgeǁcategorize_by_age__mutmut_orig.__name__ = 'xǁAgeǁcategorize_by_age'