# ----------------------------------------------------------
# Program: String Concatenation
# Purpose: Concatenate two strings using the '+' operator
# Author : Your Name
# ----------------------------------------------------------

# Function to concatenate two strings
def concatenate_strings(str1, str2):
    """
    This function takes two strings as input
    and returns their concatenation with a space.
    """
    return str1 + " " + str2


# -----------------------------
# User Input
# -----------------------------
print("===== String Concatenation =====")

# Read first string
string1 = input("Enter the first string: ")

# Read second string
string2 = input("Enter the second string: ")

# Call the function
result = concatenate_strings(string1, string2)

# Display the result
print("\nConcatenated String:", result)


# -----------------------------
# LeetCode-Style Test Cases
# -----------------------------
print("\n===== Test Cases =====")

test_cases = [
    ("Hello", "World"),
    ("Python", "Programming"),
    ("OpenAI", "GPT"),
    ("Data", "Science"),
    ("Good", "Morning")
]

# Execute each test case
for i, (s1, s2) in enumerate(test_cases, start=1):
    expected = s1 + " " + s2
    actual = concatenate_strings(s1, s2)

    print(f"\nTest Case {i}")
    print(f"Input    : str1 = '{s1}', str2 = '{s2}'")
    print(f"Expected : '{expected}'")
    print(f"Output   : '{actual}'")

    # Check whether the test case passed
    if actual == expected:
        print("Result   : PASS")
    else:
        print("Result   : FAIL")