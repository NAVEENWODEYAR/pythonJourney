import numpy as np
from datetime import datetime

# -----------------------------------------------------
# Step 1: Define a normal Python function
# This function converts a date string into a datetime object.
# -----------------------------------------------------
def parse_datetime(date_str):
    """
    Converts a string in 'YYYY-MM-DD HH:MM:SS' format
    into a Python datetime object.
    """
    return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")


# -----------------------------------------------------
# Step 2: Convert the Python function into a NumPy ufunc
#
# np.frompyfunc(function, number_of_inputs, number_of_outputs)
#
# Here:
#   function = parse_datetime
#   inputs = 1 (one date string)
#   outputs = 1 (one datetime object)
# -----------------------------------------------------
parse_datetime_ufunc = np.frompyfunc(parse_datetime, 1, 1)


# -----------------------------------------------------
# Step 3: Create an array of date-time strings
# -----------------------------------------------------
date_strings = np.array([
    "2025-01-15 10:30:00",
    "2024-12-25 08:45:30",
    "2023-07-01 14:20:10"
])


# -----------------------------------------------------
# Step 4: Apply the ufunc
# The ufunc automatically processes every element
# in the NumPy array.
# -----------------------------------------------------
parsed_dates = parse_datetime_ufunc(date_strings)


# -----------------------------------------------------
# Step 5: Display the results
# -----------------------------------------------------
print("Original Date Strings:")
print(date_strings)

print("\nParsed Datetime Objects:")
print(parsed_dates)

print("\nType of first parsed value:")
print(type(parsed_dates[0]))