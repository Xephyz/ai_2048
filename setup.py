#!/usr/bin/env python3

"""
setup.py to build code using cython
"""

from setuptools import setup
from Cython.Build import cythonize
# import numpy  # To get includes

EXTENSIONS = ["logic.pyx", "heuristics.pyx", "expectimax.pyx", "game.pyx"]
# EXTENSIONS = ["logic.pyx", "heuristics.pyx"]

setup(
    name='2048 game AI',
    # include_dirs=[numpy.get_include()],
    ext_modules=cythonize(EXTENSIONS, annotate=True, language_level='3'),
    zip_safe=False,
)
