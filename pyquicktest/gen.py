#!/usr/bin/env python
# -*- coding: utf-8 *-*


""" ~*~ Docstring ~*~
      PyQuickTest is an experimental python testing
             framework designed to deliver an
    easy-and-quick-to-start python testing mechanism.
      gen.py is the file containing every generator
            functions, useful for the tests.
                                    ~*~ Docstring ~*~

    ~*~ CHANGELOG ~*~
     ____________________________________________________________________________________
    | VERSION |    DATE    |                           CONTENT                           |
    |====================================================================================|
    | 0.0.1   | 2023/07/25 | ..........................................................  |
    |------------------------------------------------------------------------------------|
     ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                                                                         ~*~ CHANGELOG ~*~ """


#=--------------=#
# Import section #
#=--------------=#

from   __future__ import annotations
import typing
import random
from pyquicktest.utils      import get_all_functions
from pyquicktest.decorators import add_flag, add_flags

# =------------------------------= #


#=-----------------=#
# Autorship section #
#=-----------------=#

__author__       = "Quentin Raimbaud"
__maintainer__   = "Quentin Raimbaud"
__contact__      = "quentin.raimbaud.contact@gmail.com"
__organization__ = None
__credits__      = []
__copyright__    = None
__license__      = None
__date__         = "2023/07/25"
__version__      = "0.0.1"
__status__       = "Development"
__filename__     = "gen.py"

# =--------------------------------------------------------= #


#=------------------------------------=#
# Constants & Global variables section #
#=------------------------------------=#

NL     = '\n'
DQUOTE = '"'

# =----------------------------------= #


#=----------------------------=#
# Generators functions section #
#=----------------------------=#

@add_flags("is_gen", "is_gen_value")
def gen_none() -> None:
    """Generate a None value."""
    return None

@add_flags("is_gen", "is_gen_value")
def gen_bool() -> bool:
    """Generate a random boolean."""
    return bool(random.randint(0, 1))

@add_flags("is_gen", "is_gen_value", "is_gen_number", "is_gen_natural_number")
def gen_int(min: int = 0, max: int = 4294967296) -> int:
    """Generate a random integer."""
    return random.randint(min, max)

@add_flags("is_gen", "is_gen_value", "is_gen_number", "is_gen_natural_number")
def gen_signed_int(min: int = -4294967296, max: int = 4294967296) -> int:
    """Generate a random signed integer."""
    return random.randint(min, max)

@add_flags("is_gen", "is_gen_value", "is_gen_number", "is_gen_floating_number")
def gen_float(min: float = 0.0, max: float = 4294967296.0) -> float:
    """Generate a random float."""
    return random.uniform(min, max)

@add_flags("is_gen", "is_gen_value", "is_gen_number", "is_gen_floating_number")
def gen_signed_float(min: float = -4294967296.0, max: float = 4294967296.0) -> float:
    """Generate a random signed float."""
    return random.uniform(min, max)

@add_flags("is_gen", "is_gen_value", "is_gen_str", "is_gen_char")
def gen_ascii_lower_char() -> str:
    """Generate a random ascii lower char."""
    return chr(gen_int(97, 122))

@add_flags("is_gen", "is_gen_value", "is_gen_str", "is_gen_char")
def gen_ascii_upper_char() -> str:
    """Generate a random ascii upper char."""
    return chr(gen_int(65, 90))

@add_flags("is_gen", "is_gen_value", "is_gen_str", "is_gen_char")
def gen_ascii_char() -> str:
    """Generate a random ascii char."""
    return gen_ascii_lower_char() if gen_bool() else gen_ascii_upper_char()

@add_flags("is_gen", "is_gen_value", "is_gen_str")
def gen_ascii_lower_string(length: int = 20) -> str:
    """Generate a random ascii lower string."""
    return "".join(gen_generator(length=length, gen_element=gen_ascii_lower_char))

@add_flags("is_gen", "is_gen_value", "is_gen_str")
def gen_ascii_upper_string(length: int = 20) -> str:
    """Generate a random ascii upper string."""
    return "".join(gen_generator(length=length, gen_element=gen_ascii_upper_char))

@add_flags("is_gen", "is_gen_value", "is_gen_str")
def gen_ascii_string(length: int = 20) -> str:
    """Generate a random ascii string."""
    return "".join(gen_generator(length=length, gen_element=gen_ascii_lower_char if gen_bool() else gen_ascii_upper_char))

@add_flags("is_gen", "is_gen_callable")
def gen_callable(nbr_args: int = 1, gen_return: typing.Optional[typing.Callable] = None, raised_exception: typing.Optional[Exception] = None) -> typing.Callable:
    """Generate a random callable."""
    return eval(f"""lambda {", ".join(f"arg{i}" for i in range(1, nbr_args+1))}: 
               {f"exec({DQUOTE}{DQUOTE}{DQUOTE}raise {type(raised_exception).__name__}({DQUOTE}{raised_exception}{DQUOTE}){DQUOTE}{DQUOTE}{DQUOTE})"
            if raised_exception else f"{gen_return.__name__}()"
            if gen_return else "None"}""".replace(NL, ""))

@add_flags("is_gen", "is_gen_iterable")
def gen_generator(length: int = 20, gen_element: typing.Callable = None) -> typing.Generator:
    """Generate a random generator of a given generator function."""
    return (gen_element() for i in range(length)) if gen_element != None else (gen_random_value() for i in range(length))

@add_flags("is_gen", "is_gen_iterable")
def gen_list(length: int = 20, gen_element: typing.Callable = None) -> typing.List[typing.Any]:
    """Generate a random list of a given generator function."""
    return list(gen_generator(length=length, gen_element=gen_element))

@add_flags("is_gen", "is_gen_iterable") #replace list comprehension by gen_list in tests
def gen_dict(length: int = 20, gen_keys: typing.Callable = None, gen_values: typing.Callable = None) -> typing.Dict:
    """Generate a random list of a given generator function."""
    return dict(zip(gen_list(length=length, gen_element=gen_keys), gen_list(length=length, gen_element=gen_values)))

@add_flag("is_master_gen")
def gen_random_value() -> typing.Any:
    """Generate a random value from a random generator function marked as "is_gen_value"."""
    return random.choice(get_all_functions("is_gen_value", ctx=globals()))()

@add_flag("is_master_gen")
def gen_random_iterable() -> typing.Any:
    """Generate a random iterable from a random generator function marked as "is_gen_iterable"."""
    return random.choice(get_all_functions("is_gen_iterable", ctx=globals()))()

@add_flag("is_master_gen")
def gen_random() -> typing.Any:
    """Generate a random element from a random generator function marked as "is_gen"."""
    return random.choice(get_all_functions("is_gen", ctx=globals()))()

# =-----------------------------------------------------------------------------------------------------------------------------------------------------------= #
