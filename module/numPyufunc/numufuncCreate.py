# ==========================================================
#           NUMPY USER DEFINED UNIVERSAL FUNCTION (UFUNC)
# ==========================================================

import numpy as np

print("=" * 70)
print("        NUMPY USER DEFINED UNIVERSAL FUNCTION (UFUNC)")
print("=" * 70)

# ----------------------------------------------------------
# 1. Definition
# ----------------------------------------------------------
print("\n1. DEFINITION")
print("-" * 70)
print("""
A Universal Function (ufunc) is a function that operates on NumPy arrays
element by element.

NumPy provides many built-in ufuncs such as:
np.add(), np.subtract(), np.multiply(), np.sin(), np.sqrt() etc.

We can also create our own ufunc using:
np.frompyfunc()
""")

# ----------------------------------------------------------
# 2. Syntax
# ----------------------------------------------------------
print("\n2. SYNTAX")
print("-" * 70)
print("""
ufunc_name = np.frompyfunc(function_name,
                           number_of_inputs,
                           number_of_outputs)

Parameters:
function_name      -> Normal Python function
number_of_inputs   -> Number of input arguments
number_of_outputs  -> Number of returned values
""")

# ----------------------------------------------------------
# 3. Creating a Normal Python Function
# ----------------------------------------------------------
print("\n3. CREATING A NORMAL PYTHON FUNCTION")
print("-" * 70)

def square(x):
    return x * x

print("Normal Function Created:")
print("def square(x):")
print("    return x * x")

# ----------------------------------------------------------
# 4. Creating User Defined UFunc
# ----------------------------------------------------------
print("\n4. CREATING A USER DEFINED UFUNC")
print("-" * 70)

square_ufunc = np.frompyfunc(square, 1, 1)

print("UFunc Created Successfully!")
print("square_ufunc = np.frompyfunc(square, 1, 1)")

# ----------------------------------------------------------
# 5. Usage
# ----------------------------------------------------------
print("\n5. USAGE")
print("-" * 70)

numbers = np.array([1, 2, 3, 4, 5])

print("Input Array :", numbers)

result = square_ufunc(numbers)

print("Squared Array :", result)

# ----------------------------------------------------------
# 6. Real World Example
# ----------------------------------------------------------
print("\n6. REAL WORLD EXAMPLE")
print("-" * 70)

print("""
Problem:
A company stores employee daily working hours.
Payroll requires calculating daily salary.

Formula:
Salary = Hours Worked × ₹500
""")

def salary(hours):
    return hours * 500

salary_ufunc = np.frompyfunc(salary, 1, 1)

hours = np.array([8, 9, 7, 10, 6])

salary_result = salary_ufunc(hours)

print("Working Hours :", hours)
print("Daily Salary  :", salary_result)

# ----------------------------------------------------------
# 7. Another Example (Temperature Conversion)
# ----------------------------------------------------------
print("\n7. ANOTHER EXAMPLE - CELSIUS TO FAHRENHEIT")
print("-" * 70)

def celsius_to_fahrenheit(c):
    return (9/5) * c + 32

temp_ufunc = np.frompyfunc(celsius_to_fahrenheit, 1, 1)

celsius = np.array([0, 20, 30, 40])

fahrenheit = temp_ufunc(celsius)

print("Celsius    :", celsius)
print("Fahrenheit :", fahrenheit)

# ----------------------------------------------------------
# 8. Advantages
# ----------------------------------------------------------
print("\n8. ADVANTAGES OF USER DEFINED UFUNCS")
print("-" * 70)

advantages = [
    "Works element by element on arrays.",
    "Code becomes reusable.",
    "Handles entire arrays without writing loops.",
    "Easy to apply custom operations.",
    "Can process multiple values efficiently."
]

for i, item in enumerate(advantages, 1):
    print(f"{i}. {item}")

# ----------------------------------------------------------
# 9. Summary
# ----------------------------------------------------------
print("\n9. SUMMARY")
print("-" * 70)

print("""
Definition:
A ufunc performs element-wise operations on NumPy arrays.

Function Used:
np.frompyfunc()

Syntax:
np.frompyfunc(function_name, inputs, outputs)

Examples Covered:
✓ Square of numbers
✓ Employee salary calculation
✓ Celsius to Fahrenheit conversion

Applications:
✓ Data Analysis
✓ Scientific Computing
✓ Machine Learning
✓ Financial Calculations
✓ Image Processing
""")

print("=" * 70)
print("        END OF PROGRAM")
print("=" * 70)