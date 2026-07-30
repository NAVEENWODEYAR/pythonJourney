# Program to calculate Provident Fund (PF) contribution
# and estimate the total amount after retirement

# Function to calculate PF details
def calculate_pf(monthly_salary, pf_percent, years):
    # Monthly PF contribution
    monthly_pf = (monthly_salary * pf_percent) / 100

    # Employee and Employer contribute the same amount
    total_monthly_contribution = monthly_pf * 2

    # Total contribution (without interest)
    total_amount = total_monthly_contribution * 12 * years

    return monthly_pf, total_monthly_contribution, total_amount


# Take input from the user
salary = float(input("Enter your monthly salary: ₹"))
pf_percentage = float(input("Enter PF contribution percentage (e.g., 12): "))
retirement_years = int(input("Enter number of years until retirement: "))

# Call the function
employee_pf, total_monthly, retirement_amount = calculate_pf(
    salary, pf_percentage, retirement_years
)

# Display the results
print("\n------ PF Calculation ------")
print(f"Monthly Employee PF Contribution : ₹{employee_pf:.2f}")
print(f"Monthly Total Contribution       : ₹{total_monthly:.2f}")
print(f"Total Amount at Retirement       : ₹{retirement_amount:.2f}")   