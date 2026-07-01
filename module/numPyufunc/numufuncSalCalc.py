# Real-World Example: Employee Net Salary Calculation using NumPy UFunc

import numpy as np

# Normal Python function
def net_salary(salary):
    tax = salary * 0.10      # 10% tax deduction
    return salary - tax

# Create a User Defined UFunc
net_salary_ufunc = np.frompyfunc(net_salary, 1, 1)

# Employee gross salaries
gross_salary = np.array([25000, 30000, 45000, 50000, 60000])

# Calculate net salaries
net_salary_result = net_salary_ufunc(gross_salary)

# Display results
print("Employee Gross Salaries :", gross_salary)
print("Employee Net Salaries   :", net_salary_result)