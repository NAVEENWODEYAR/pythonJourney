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

    # Check divisibility from 2 to √num
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return "Not a Prime Number"

    return "Prime Number"


# ---------------------------------------------------------
# Convert the Python function into a NumPy Universal Function
# (ufunc) using frompyfunc()
# ---------------------------------------------------------
prime_ufunc = np.frompyfunc(check_prime, 1, 1)


# ---------------------------------------------------------
# Accept a number from the user
# ---------------------------------------------------------
number = int(input("Enter a number: "))

# Apply the ufunc
result = prime_ufunc(number)

# Display the result
print("Result:", result)


# ---------------------------------------------------------
# LeetCode-Style Test Cases
# ---------------------------------------------------------
print("\n========== Test Cases ==========")

# Test cases: (Input, Expected Output)
test_cases = [
    (2, "Prime Number"),
    (3, "Prime Number"),
    (4, "Not a Prime Number"),
    (5, "Prime Number"),
    (10, "Not a Prime Number"),
    (17, "Prime Number"),
    (25, "Not a Prime Number"),
    (29, "Prime Number"),
    (1, "Not a Prime Number"),
    (0, "Not a Prime Number"),
    (-5, "Not a Prime Number")
]

# Execute test cases
for i, (num, expected) in enumerate(test_cases, start=1):

    actual = prime_ufunc(num)

    print(f"\nTest Case {i}")
    print(f"Input    : {num}")
    print(f"Expected : {expected}")
    print(f"Output   : {actual}")

    if actual == expected:
        print("Result   : PASS")
    else:
        print("Result   : FAIL")