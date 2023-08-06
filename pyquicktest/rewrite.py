#!/usr/bin/env python
# -*- coding: utf-8 *-*


""" ~*~ Docstring ~*~
      PyQuickTest is an experimental python testing
             framework designed to deliver an
    easy-and-quick-to-start python testing mechanism.
    rewrite.py is the file containing the functions
    that allow smart check/ensure rewriting for adding
       explicit and error message when a test fail.               
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
import re
from pyquicktest.utils import *

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
__filename__     = "rewrite.py"

# =--------------------------------------------------------= #


#=------------------------------------=#
# Constants & Global variables section #
#=------------------------------------=#

BS     = '\\'
DQUOTE = '"'
LBRCKT = '{'
RBRCKT = '}'

# =----------------------------------= #


#=-------------------------------------=#
# Parsing & Rewriting functions section #
#=-------------------------------------=#

def parse_function_call(string: str) -> typing.Optional[str]:
    """Parse a single lowest function call from a given string expression."""
    try:
        res = re.findall(r"([\w.]+\(.*?\))", string)[0]
        while True:
            temp = re.findall(r"([\w.]+\(.*?\))", '('.join(e for e in res.split('(')[1:]))
            if temp:
                res = temp[0]
            else:
                break
        return res
    except IndexError:
        return None

def parse_function_calls(string: str) -> typing.Tuple[typing.Dict[str, str], str]:
    """Parse every function call from a given string expression and returns them, their variable name and the resulting string."""
    counter = 1
    out = {}
    res = parse_function_call(string)
    while res:
        arg = f"__GENERATED_ARG_{counter}__"
        out[arg] = res
        counter +=1
        string = string.replace(res, arg)
        res = parse_function_call(string)
    return (out, string)

def rewrite_check(check: str) -> typing.Tuple[typing.Dict[str, str], str]:
    """rewrite a single check instruction, returning it as well as the core rewritten variables."""
    check = check.replace('\n', "")
    tab = get_str_tab(check)
    func = check.split('(')[0].strip()
    (core, res) = parse_function_calls(check.split(func)[-1])
    out = ""
    for key in core:
        out += f"{tab}{key} = {core[key]}\n"
    return (core, out + f"{tab}{func}{res}")

def rewrite_test(test: typing.Callable, caller_file : typing.Optional[str] = None) -> typing.Callable:
    """Rewrite a test function."""
    caller_lib = __import__(caller_file.split('/')[-1].split('\\')[-1].split('.')[0])
    for name in dir(caller_lib):
        globals()[name] = getattr(caller_lib, name)
    new_func_name = f"rewritten_{test.__name__}"
    src = test.__rewritten_source__
    src = src.replace(test.__name__, new_func_name).split('\n')
    while not src[0].lstrip().startswith("def"):
        src.pop(0)
    src ="\n".join(src)
    res = re.findall(r"(\s*(ensure|check)\s?\(.*\))", src)
    for check in res:
        temp = check[0].replace('\n', "")
        tab = get_str_tab(temp)
        (core, rewritten) = rewrite_check(temp)
        rewritten = rewritten[:-1].rstrip()[:-1] + f"""\\nwhere\\n{(BS + 'n').join(
            f"{tab}{multiple_replace(core[key], *[(k, v) for k, v in core.items()], (DQUOTE, BS + DQUOTE))} = {LBRCKT}{key}{RBRCKT}" for key in core
        )}")"""
        src = src.replace(temp, rewritten)
    exec(src)
    return locals()[new_func_name]

# =----------------------------------------------------------------------------------------------------------------------------------------------= #