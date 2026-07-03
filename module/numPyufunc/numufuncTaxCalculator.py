# Program to calculate tax based on salary

# Get annual salary from the user
salary = float(input("Enter your annual salary: "))

# Calculate tax based on salary slabs
if salary <= 250000:
    tax = 0
elif salary <= 500000:
    tax = (salary - 250000) * 0.05
elif salary <= 1000000:
    tax = (250000 * 0.05) + (salary - 500000) * 0.20
else:
    tax = (250000 * 0.05) + (500000 * 0.20) + (salary - 1000000) * 0.30

# Display the result
print("Annual Salary:", salary)
print("Income Tax:", tax)