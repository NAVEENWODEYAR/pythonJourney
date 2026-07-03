# Program to check whether a user-given number is Prime or Not Prime
# using NumPy ufunc

import numpy as np

# ---------------------------------------------------------
# Function to check if a number is prime
# A prime number is divisible only by 1 and itself.
# ---------------------------------------------------------
def check_prime(num):
    if num <= 1:
        return "Not a Prime Number"

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return "Not a Prime Number"

    return "Prime Number"

# ---------------------------------------------------------
# Convert the Python function into a NumPy Universal Function
# (ufunc) using frompyfunc().
#
# Arguments:
# check_prime : Function to convert
# 1           : Number of input arguments
# 1           : Number of output values
# ---------------------------------------------------------
prime_ufunc = np.frompyfunc(check_prime, 1, 1)

# ---------------------------------------------------------
# Accept a number from the user
# ---------------------------------------------------------
number = int(input("Enter a number: "))

# ---------------------------------------------------------
# Apply the ufunc to the user input
# ---------------------------------------------------------
result = prime_ufunc(number)

# ---------------------------------------------------------
# Display the result
# ---------------------------------------------------------
print("Result:", result)