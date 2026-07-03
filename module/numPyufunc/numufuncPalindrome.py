import numpy as np

# -------------------------------------------------------
# Function to check whether a string is a palindrome
# -------------------------------------------------------
def is_palindrome(word):
    # Convert to lowercase to make the comparison case-insensitive
    word = str(word).lower()

    # Compare the string with its reverse
    if word == word[::-1]:
        return True
    else:
        return False

# -------------------------------------------------------
# Create a NumPy universal function (ufunc)
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
print("Words:", words)
print("Palindrome Check:", result)