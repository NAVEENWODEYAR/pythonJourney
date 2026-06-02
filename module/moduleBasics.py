# =====================================================
# PYTHON MODULES - COMPLETE DEMONSTRATION
# =====================================================

# -----------------------------------------------------
# PART 1: CREATING A MODULE (SIMULATED HERE)
# -----------------------------------------------------
# Normally, this code would be in a separate file:
# file name: mymodule.py

# Module content (functions + variables)

def add(a, b):
    """Function to add two numbers"""
    return a + b

def multiply(a, b):
    """Function to multiply two numbers"""
    return a * b

pi = 3.14  # variable inside module


# -----------------------------------------------------
# PART 2: USING MODULE FUNCTIONS (NORMAL USAGE)
# -----------------------------------------------------

print("1. Using module functions:")

print("Addition:", add(10, 5))
print("Multiplication:", multiply(4, 3))


# -----------------------------------------------------
# PART 3: IMPORTING MODULE (SIMULATED IMPORT TYPES)
# -----------------------------------------------------

print("\n2. Different ways of using modules:")

# (A) import module_name
# Syntax: import module
# Usage: module.function()

import math  # built-in module

print("Square root of 16:", math.sqrt(16))


# (B) from module import function
from math import factorial

print("Factorial of 5:", factorial(5))


# (C) import module as alias
import math as m

print("Power using alias:", m.pow(2, 3))


# (D) from module import *
from math import *

print("Value of pi (built-in module):", pi)
print("Cos 0:", cos(0))


# -----------------------------------------------------
# PART 4: CUSTOM MODULE USAGE (REAL CONCEPT)
# -----------------------------------------------------
print("\n3. Concept of custom module:")

print("""
If this code was saved as 'mymodule.py',
we could use it in another file like:

import mymodule
print(mymodule.add(10, 20))
""")


print()
print('\n next session- RegEx')