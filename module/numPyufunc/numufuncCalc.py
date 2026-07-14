# Calculator Program Using NumPy Universal Functions (ufunc)

import numpy as np


def calculator(num1, num2, choice):
    """
    Performs arithmetic operations using NumPy ufuncs.

    Parameters:
        num1 (float): First number
        num2 (float): Second number
        choice (int): Operation choice
                      1 - Addition
                      2 - Subtraction
                      3 - Multiplication
                      4 - Division

    Returns:
        Result of the operation or an error message.
    """

    if choice == 1:
        return np.add(num1, num2)

    elif choice == 2:
        return np.subtract(num1, num2)

    elif choice == 3:
        return np.multiply(num1, num2)

    elif choice == 4:
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return np.divide(num1, num2)

    else:
        return "Invalid choice! Please enter a number between 1 and 4."


# ---------------- Main Program ----------------

print("===== NumPy Ufunc Calculator =====")

# Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1-4): "))

# Call the calculator function
result = calculator(num1, num2, choice)

# Display the result
print("\nResult:", result)