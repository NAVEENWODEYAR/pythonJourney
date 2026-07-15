# Python program to check whether a number is an Armstrong number
# using a user-defined function (UDF)

def display_definition():
    """
    This function displays the definition of an Armstrong number.
    """
    print("Definition of Armstrong Number")
    print("--------------------------------")
    print("An Armstrong number is a number that is equal to")
    print("the sum of its own digits, where each digit is")
    print("raised to the power of the total number of digits.\n")


def is_armstrong(number):
    """
    This function checks whether the given number is an
    Armstrong number.
    Returns True if it is an Armstrong number,
    otherwise returns False.
    """

    # Store the original number
    original_number = number

    # Handle 0 separately (0 is an Armstrong number)
    if number == 0:
        return True

    # Negative numbers are not Armstrong numbers
    if number < 0:
        return False

    # Find the number of digits
    num_digits = len(str(number))

    # Variable to store the sum of powered digits
    armstrong_sum = 0

    # Calculate the sum of each digit raised to the power of num_digits
    while number > 0:
        digit = number % 10
        armstrong_sum += digit ** num_digits
        number //= 10

    # Compare the calculated sum with the original number
    return armstrong_sum == original_number


# ---------------- LeetCode-Style Test Cases ----------------

def run_test_cases():
    print("\n========== Running Test Cases ==========\n")

    test_cases = [
        (0, True),
        (1, True),
        (5, True),
        (9, True),
        (10, False),
        (153, True),
        (370, True),
        (371, True),
        (407, True),
        (1634, True),
        (8208, True),
        (9474, True),
        (9475, False),
        (123, False),
        (100, False),
        (-153, False),
    ]

    passed = 0

    for i, (num, expected) in enumerate(test_cases, start=1):
        result = is_armstrong(num)
        status = "PASS" if result == expected else "FAIL"

        print(f"Test Case {i}")
        print(f"Input     : {num}")
        print(f"Expected  : {expected}")
        print(f"Output    : {result}")
        print(f"Result    : {status}")
        print("-" * 40)

        if status == "PASS":
            passed += 1

    print(f"\nSummary: {passed}/{len(test_cases)} test cases passed.")


# ---------------- Main Program ----------------

# Display the definition
display_definition()

# Get input from the user
num = int(input("Enter a number: "))

# Check whether the number is an Armstrong number
if is_armstrong(num):
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")

# Run LeetCode-style test cases
run_test_cases()