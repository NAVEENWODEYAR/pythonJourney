# Python program to find the length of a string
# using a User-Defined Function (UDF)

def display_definition():
    """
    Displays the definition of string length.
    """
    print("Definition")
    print("----------")
    print("String Length: The total number of characters")
    print("present in a string, including letters, digits,")
    print("spaces, and special symbols.\n")


def find_length(text):
    """
    Returns the length of the given string.
    """
    return len(text)


# ---------------- Main Program ----------------

# Display the definition
display_definition()

# Read a string from the user
user_string = input("Enter a string: ")

# Find the length of the string
length = find_length(user_string)

# Display the result
print("The length of the string is:", length)


# ---------------- Test Cases ----------------

print("\n========== Test Cases ==========")

# List of test cases
test_cases = [
    "Python",
    "Hello World",
    "12345",
    "OpenAI GPT",
    "",
    "A",
    "Python@123"
]

# Execute each test case
for i, test in enumerate(test_cases, start=1):

    expected = len(test)          # Expected result
    actual = find_length(test)    # Function output

    print(f"\nTest Case {i}")
    print(f"Input    : '{test}'")
    print(f"Expected : {expected}")
    print(f"Output   : {actual}")

    if expected == actual:
        print("Result   : PASS")
    else:
        print("Result   : FAIL")