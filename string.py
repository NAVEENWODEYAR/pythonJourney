# ============================================
# PYTHON STRING DEMO PROGRAM
# ============================================
#
# A string is a sequence of characters.
# Strings are written inside:
#   "double quotes"
#   'single quotes'
#
# Example:
#   name = "Python"
#
# ============================================

print("===== PYTHON STRING DEMO =====\n")


# ------------------------------------------------
# 1. CREATING STRINGS
# ------------------------------------------------

name = "Alice"
city = 'Bangalore'

print("1. CREATING STRINGS")
print("Name:", name)
print("City:", city)
print()


# ------------------------------------------------
# 2. ACCESSING CHARACTERS
# ------------------------------------------------

# Index starts from 0
language = "Python"

print("2. ACCESSING CHARACTERS")
print("String:", language)

print("First character:", language[0])
print("Second character:", language[1])
print("Last character:", language[-1])
print()


# ------------------------------------------------
# 3. STRING LENGTH
# ------------------------------------------------

print("3. STRING LENGTH")

text = "Programming"

# len() gives number of characters
print("String:", text)
print("Length:", len(text))
print()


# ------------------------------------------------
# 4. STRING CONCATENATION
# ------------------------------------------------

print("4. STRING CONCATENATION")

first_name = "John"
last_name = "Doe"

# Joining strings using +
full_name = first_name + " " + last_name

print("Full Name:", full_name)
print()


# ------------------------------------------------
# 5. STRING REPETITION
# ------------------------------------------------

print("5. STRING REPETITION")

word = "Hi! "

# Repeat string 3 times
print(word * 3)
print()


# ------------------------------------------------
# 6. STRING SLICING
# ------------------------------------------------

print("6. STRING SLICING")

message = "Hello Python"

print("Original String:", message)

# Extract part of string
print("message[0:5] =", message[0:5])   # Hello
print("message[6:] =", message[6:])     # Python
print("message[:5] =", message[:5])     # Hello
print()


# ------------------------------------------------
# 7. STRING METHODS
# ------------------------------------------------

print("7. STRING METHODS")

sentence = "python programming"

print("Original:", sentence)

# Convert to uppercase
print("Uppercase:", sentence.upper())

# Convert to lowercase
print("Lowercase:", sentence.lower())

# Capitalize first letter
print("Capitalize:", sentence.capitalize())

# Replace word
print("Replace:", sentence.replace("python", "Java"))

print()


# ------------------------------------------------
# 8. CHECKING STRING CONTENT
# ------------------------------------------------

print("8. CHECKING STRING CONTENT")

data = "Python123"

print("String:", data)

# Check if all characters are alphabet
print("isalpha():", data.isalpha())

# Check if all characters are digits
print("isdigit():", data.isdigit())

# Check if alphanumeric
print("isalnum():", data.isalnum())

print()


# ------------------------------------------------
# 9. SEARCHING IN STRINGS
# ------------------------------------------------

print("9. SEARCHING IN STRINGS")

text = "I love Python programming"

# find() returns index position
print("Index of Python:", text.find("Python"))

# Check word existence
print("Contains 'love'?", "love" in text)

print()


# ------------------------------------------------
# 10. TAKING STRING INPUT
# ------------------------------------------------

print("10. USER INPUT")

user_name = input("Enter your name: ")

print("Welcome,", user_name)
print()


# ------------------------------------------------
# 11. LOOPING THROUGH STRING
# ------------------------------------------------

print("11. LOOPING THROUGH STRING")

sample = "Python"

for ch in sample:
    print(ch)

print()


# ------------------------------------------------
# 12. STRING COMPARISON
# ------------------------------------------------

print("12. STRING COMPARISON")

str1 = "apple"
str2 = "apple"
str3 = "banana"

print("str1 == str2 :", str1 == str2)
print("str1 == str3 :", str1 == str3)

print()


# ============================================
# END OF PROGRAM
# ============================================

print("===== END OF STRING DEMO =====")