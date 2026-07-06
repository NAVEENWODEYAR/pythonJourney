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