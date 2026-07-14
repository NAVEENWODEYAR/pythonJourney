# Real-World Example: Employee Net Salary Calculation using NumPy UFunc

import numpy as np

# ---------------------------------------------------
# Normal Python Function
# Calculates the net salary after deducting 10% tax.
# ---------------------------------------------------
def net_salary(salary):
    tax = salary * 0.10      # 10% tax deduction
    return salary - tax


# ---------------------------------------------------
# Create a User Defined Universal Function (UFunc)
# Input arguments = 1
# Output arguments = 1
# ---------------------------------------------------
net_salary_ufunc = np.frompyfunc(net_salary, 1, 1)


# ---------------------------------------------------
# Employee Gross Salaries
# ---------------------------------------------------
gross_salary = np.array([25000, 30000, 45000, 50000, 60000])

# Calculate Net Salaries
net_salary_result = net_salary_ufunc(gross_salary)

# Display Results
print("========== Employee Net Salary Calculator ==========")
print("User Defined Function using NumPy UFunc")
print("Employee Gross Salaries :", gross_salary)
print("Employee Net Salaries   :", net_salary_result)


# ===================================================
# LeetCode-Style Test Cases
# ===================================================

print("\n========== Test Cases ==========")

test_cases = [
    ([25000, 30000, 45000], [22500.0, 27000.0, 40500.0]),
    ([10000], [9000.0]),
    ([0], [0.0]),
    ([50000, 60000], [45000.0, 54000.0]),
    ([15000, 35000, 75000], [13500.0, 31500.0, 67500.0])
]

for i, (input_salary, expected) in enumerate(test_cases, start=1):
    input_array = np.array(input_salary)
    output = list(net_salary_ufunc(input_array))

    print(f"\nTest Case {i}")
    print("Input    :", input_salary)
    print("Expected :", expected)
    print("Output   :", output)

    if output == expected:
        print("Result   : PASS")
    else:
        print("Result   : FAIL")