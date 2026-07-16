import numpy as np

# ---------------------------------------------------------
# Function to check if a year is a leap year
# Rules:
# 1. Year divisible by 400  -> Leap Year
# 2. Year divisible by 4 but not by 100 -> Leap Year
# 3. Otherwise -> Not a Leap Year
# ---------------------------------------------------------
def check_leap(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return "Leap Year"
    else:
        return "Not a Leap Year"


# ---------------------------------------------------------
# Convert the Python function into a NumPy Universal Function
# (ufunc) using frompyfunc()
# ---------------------------------------------------------
leap_ufunc = np.frompyfunc(check_leap, 1, 1)


# ---------------------------------------------------------
# Main Program
# ---------------------------------------------------------
year = int(input("Enter a year: "))

# Apply ufunc
result = leap_ufunc(year)

# Display result
print("Result:", result)


# =========================================================
# LeetCode-Style Test Cases
# =========================================================
print("\n" + "=" * 50)
print("Running Test Cases")
print("=" * 50)

test_cases = [
    # (Input, Expected Output)
    (2000, "Leap Year"),      # Divisible by 400
    (1900, "Not a Leap Year"),# Divisible by 100 but not 400
    (2024, "Leap Year"),      # Divisible by 4 but not 100
    (2023, "Not a Leap Year"),# Normal year
    (2400, "Leap Year"),      # Divisible by 400
    (2100, "Not a Leap Year"),# Century year
    (1996, "Leap Year"),      # Divisible by 4
    (1999, "Not a Leap Year"),# Not divisible by 4
    (1600, "Leap Year"),      # Old leap year
    (1700, "Not a Leap Year") # Century not divisible by 400
]

passed = 0

for i, (year, expected) in enumerate(test_cases, start=1):
    result = leap_ufunc(year)

    if result == expected:
        status = "PASS"
        passed += 1
    else:
        status = "FAIL"

    print(f"Test Case {i}")
    print(f"Input    : {year}")
    print(f"Expected : {expected}")
    print(f"Output   : {result}")
    print(f"Status   : {status}")
    print("-" * 50)

print(f"Summary: {passed}/{len(test_cases)} Test Cases Passed")