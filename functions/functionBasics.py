"""
Program: Understanding Python Functions
Purpose: To explain Python functions with examples.
"""

# ---------------------------------------------------------
# WHAT IS A FUNCTION?
# ---------------------------------------------------------
# A function is a block of reusable code that performs
# a specific task. Functions help reduce code repetition,
# improve readability, and make programs easier to maintain.
# ---------------------------------------------------------


# Function without parameters
def greet():
    """This function displays a welcome message."""
    print("Hello! Welcome to Python Functions.")


# Function with parameters
def add_numbers(num1, num2):
    """
    This function accepts two numbers as arguments
    and displays their sum.
    """
    result = num1 + num2
    print(f"Sum of {num1} and {num2} = {result}")


# Function with a return value
def multiply_numbers(num1, num2):
    """
    This function multiplies two numbers
    and returns the result.
    """
    return num1 * num2


# Function with a default parameter
def introduce(name="Guest"):
    """
    If no name is provided, 'Guest' is used
    as the default value.
    """
    print(f"Hello, {name}!")


# Main program
print("=" * 60)
print("PYTHON FUNCTIONS - EXPLANATION AND DEMONSTRATION")
print("=" * 60)

# Definition of a function
print("\nWhat is a Function?")
print("A function is a reusable block of code that performs a specific task.")

# Advantages of functions
print("\nAdvantages of Functions:")
print("1. Code Reusability")
print("2. Better Organization")
print("3. Easy Maintenance")
print("4. Reduced Code Duplication")
print("5. Improved Readability")

# Calling a function without parameters
print("\nExample 1: Function without Parameters")
greet()

# Calling a function with parameters
print("\nExample 2: Function with Parameters")
add_numbers(10, 20)

# Calling a function with return value
print("\nExample 3: Function with Return Value")
product = multiply_numbers(5, 4)
print("Product =", product)

# Calling a function with default parameter
print("\nExample 4: Function with Default Parameter")
introduce()
introduce("Alice")

# Types of functions
print("\nTypes of Functions in Python:")
print("1. Built-in Functions (print(), len(), input())")
print("2. User-defined Functions")
print("3. Anonymous (Lambda) Functions")
print("4. Recursive Functions")

print("\nConclusion:")
print("Functions make programs modular, reusable, and easier to understand.")