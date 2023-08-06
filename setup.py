#!/usr/bin/env python
# -*- coding: utf-8 *-*


""" ~*~ Docstring ~*~
      PyQuickTest is an experimental python testing
             framework designed to deliver an
    easy-and-quick-to-start python testing mechanism.           
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
import os
from setuptools import setup

# =------------------------------= #


#=-----------------=#
# Autorship section #
#=-----------------=#

__author__       = "Quentin Raimbaud"
__maintainer__   = "Quentin Raimbaud"
__contact__      = "quentin.raimbaud.contact@gmail.com"
__organization__ = "Airbus Defense & Space"
__credits__      = []
__copyright__    = None
__license__      = None
__date__         = "2023/07/25"
__version__      = "0.0.1"
__status__       = "Development"
__filename__     = "pqt.py"

# =--------------------------------------------------------= #


#=----------------------=#
# Setup function section #
#=----------------------=#

setup(
    name             = "PyQuickTest",
    version          = "0.0.1",
    author           = "Quentin Raimbaud",
    author_email     = "quentin.raimbaud.contact@gmail.com",
    description      = "PyQuickTest is an experimental python testing framework designed to \
                           deliver an easy-and-quick-to-start python testing mechanism.",
    license          = "PSFL",
    entry_points={
        "console_scripts": [
            "pqt = pyquicktest.cli:cli",
        ]
    },
    keywords         = "Python test experimental framework",
    url              = "http://packages.python.org/an_example_pypi_project",
    packages         = ["pyquicktest", "tests"],
    long_description = open(os.path.join(os.path.dirname(__file__), "README")).read(),
    classifiers      = [
        "Development Status :: 3 - Alpha",
        "Topic              :: Utilities",
        "License            :: OSI Approved :: PSF License",
    ],
)

# =---------------------------------------------------------------------------------= #