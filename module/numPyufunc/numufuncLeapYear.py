# Program to check whether a user-given year is a Leap Year using NumPy ufunc

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
# (ufunc) using frompyfunc().
#
# Arguments:
# check_leap : Function to convert
# 1          : Number of input arguments
# 1          : Number of output values
# ---------------------------------------------------------
leap_ufunc = np.frompyfunc(check_leap, 1, 1)

# ---------------------------------------------------------
# Accept the year from the user
# ---------------------------------------------------------
year = int(input("Enter a year: "))

# ---------------------------------------------------------
# Apply the ufunc to the user input
# ---------------------------------------------------------
result = leap_ufunc(year)

# ---------------------------------------------------------
# Display the result
# ---------------------------------------------------------
print("Result:", result)