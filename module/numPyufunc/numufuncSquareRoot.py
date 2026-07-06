# Python program to find Square Root or Cube Root
# using User-Defined Functions (UDF)

import math

def display_definition():
    """
    Displays the definition of square root and cube root.
    """
    print("Definition")
    print("----------")
    print("Square Root: A number which, when multiplied by itself,")
    print("gives the original number.")
    print("Example: Square root of 25 is 5 because 5 × 5 = 25.\n")

    print("Cube Root: A number which, when multiplied by itself")
    print("three times, gives the original number.")
    print("Example: Cube root of 27 is 3 because 3 × 3 × 3 = 27.\n")


def square_root(num):
    """
    Returns the square root of the given number.
    """
    return math.sqrt(num)


def cube_root(num):
    """
    Returns the cube root of the given number.
    """
    return num ** (1 / 3)


# ---------------- Main Program ----------------

# Display the definitions
display_definition()

# Read the number from the user
number = float(input("Enter a number: "))

# Display menu
print("\nChoose an option:")
print("1. Square Root")
print("2. Cube Root")

choice = int(input("Enter your choice (1 or 2): "))

# Perform the selected operation
if choice == 1:
    if number >= 0:
        print("Square Root =", square_root(number))
    else:
        print("Square root of a negative number is not a real number.")
elif choice == 2:
    print("Cube Root =", cube_root(number))
else:
    print("Invalid choice!")