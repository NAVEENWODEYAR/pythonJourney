# ==========================================================
# High-Paying Python Jobs Explorer
# ==========================================================
# This program:
# 1. Stores a list of high-paying Python jobs and salaries.
# 2. Displays all jobs and salaries.
# 3. Finds the highest-paying job.
# 4. Allows the user to search for a specific job.
# ==========================================================

# Dictionary containing job titles and average annual salaries (USD)
jobs = {
    "Machine Learning Engineer": 150000,
    "AI Research Engineer": 180000,
    "Data Scientist": 130000,
    "Quantitative Developer": 200000,
    "Backend Software Engineer": 120000,
    "Cybersecurity Engineer": 140000,
    "DevOps Engineer": 125000,
    "Cloud Solutions Architect": 170000
}

# Display program title
print("=" * 50)
print("      HIGH-PAYING PYTHON JOBS EXPLORER")
print("=" * 50)

# Display all jobs and salaries
print("\nAvailable Python-related jobs:\n")

for job, salary in jobs.items():
    print(f"{job:<30} : ${salary:,} per year")

# Find the highest-paying job
highest_job = max(jobs, key=jobs.get)
highest_salary = jobs[highest_job]

print("\n" + "=" * 50)
print("Highest-Paying Job")
print("=" * 50)
print(f"Job Title : {highest_job}")
print(f"Salary    : ${highest_salary:,} per year")

# Calculate average salary
average_salary = sum(jobs.values()) / len(jobs)

print("\nAverage Salary Across All Jobs")
print(f"${average_salary:,.2f} per year")

# Search feature
print("\n" + "=" * 50)
print("Job Search")
print("=" * 50)

user_job = input("Enter a job title to search: ")

# Check if job exists in dictionary
if user_job in jobs:
    print(f"\n{user_job}")
    print(f"Average Salary: ${jobs[user_job]:,} per year")
else:
    print("\nJob not found.")
    print("Please check the spelling and try again.")

print("\nThank you for using the Python Jobs Explorer!")