import numpy as np

# -------------------------------------------------------
# Function to check whether a string is a palindrome
# -------------------------------------------------------
def is_palindrome(word):
    """
    Checks whether the given string is a palindrome.
    Returns True if it is a palindrome, otherwise False.
    """

    # Convert to lowercase for case-insensitive comparison
    word = str(word).lower()

    # Compare the string with its reverse
    return word == word[::-1]


# -------------------------------------------------------
# Create a NumPy Universal Function (ufunc)
# Input arguments = 1
# Output arguments = 1
# -------------------------------------------------------
palindrome_ufunc = np.frompyfunc(is_palindrome, 1, 1)


# -------------------------------------------------------
# Input array of words
# -------------------------------------------------------
words = np.array(["madam", "python", "level", "hello", "racecar"])

# Apply the ufunc to every element in the array
result = palindrome_ufunc(words)

# Display the results
print("Words            :", words)
print("Palindrome Check :", result)


# -------------------------------------------------------
# LeetCode-Style Test Cases
# -------------------------------------------------------
print("\n========== Test Cases ==========")

test_cases = [
    ("madam", True),
    ("python", False),
    ("level", True),
    ("hello", False),
    ("racecar", True),
    ("Radar", True),      # Case-insensitive
    ("12321", True),
    ("OpenAI", False)
]

for i, (word, expected) in enumerate(test_cases, start=1):

    # Apply the ufunc to a single-element NumPy array
    actual = palindrome_ufunc(np.array([word]))[0]

    print(f"\nTest Case {i}")
    print(f"Input    : '{word}'")
    print(f"Expected : {expected}")
    print(f"Output   : {actual}")

    if actual == expected:
        print("Result   : PASS")
    else:
        print("Result   : FAIL")