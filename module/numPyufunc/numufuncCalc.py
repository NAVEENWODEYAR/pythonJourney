# Calculator using NumPy Universal Functions (ufunc)

import numpy as np

# Take two numbers as input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Display the menu
print("\nChoose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1-4): ")

# Perform the selected operation using NumPy ufuncs
if choice == "1":
    result = np.add(num1, num2)          # Adds two numbers
    print("Result =", result)

elif choice == "2":
    result = np.subtract(num1, num2)     # Subtracts second number from first
    print("Result =", result)

elif choice == "3":
    result = np.multiply(num1, num2)     # Multiplies two numbers
    print("Result =", result)

elif choice == "4":
    if num2 != 0:
        result = np.divide(num1, num2)   # Divides first number by second
        print("Result =", result)
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Invalid choice! Please select a number between 1 and 4.")