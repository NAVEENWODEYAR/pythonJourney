# ==========================================================
# COMPLETE PYTHON OPERATORS PROGRAM
# ==========================================================
#
# Operators are special symbols used to perform
# operations on variables and values.
#
# Python Operators:
#
# 1. Arithmetic Operators
# 2. Assignment Operators
# 3. Comparison Operators
# 4. Logical Operators
# 5. Identity Operators
# 6. Membership Operators
# 7. Bitwise Operators
#
# ==========================================================

print("===== COMPLETE PYTHON OPERATORS DEMO =====\n")


# ==========================================================
# 1. ARITHMETIC OPERATORS
# ==========================================================
#
# Used for mathematical calculations
#
# +   Addition
# -   Subtraction
# *   Multiplication
# /   Division
# %   Modulus
# **  Exponent
# //  Floor Division
#
# ==========================================================

print("1. ARITHMETIC OPERATORS")

a = 15
b = 4

print("a =", a)
print("b =", b)

print("Addition (a + b) =", a + b)
print("Subtraction (a - b) =", a - b)
print("Multiplication (a * b) =", a * b)
print("Division (a / b) =", a / b)
print("Modulus (a % b) =", a % b)
print("Exponent (a ** b) =", a ** b)
print("Floor Division (a // b) =", a // b)

print()


# ==========================================================
# 2. ASSIGNMENT OPERATORS
# ==========================================================
#
# Used to assign values to variables
#
# =    Assign
# +=   Add and assign
# -=   Subtract and assign
# *=   Multiply and assign
# /=   Divide and assign
# %=   Modulus and assign
# //=  Floor divide and assign
# **=  Exponent and assign
#
# ==========================================================

print("2. ASSIGNMENT OPERATORS")

x = 10

print("Initial value:", x)

x += 5
print("After x += 5 :", x)

x -= 3
print("After x -= 3 :", x)

x *= 2
print("After x *= 2 :", x)

x /= 4
print("After x /= 4 :", x)

x %= 3
print("After x %= 3 :", x)

x **= 2
print("After x **= 2 :", x)

print()


# ==========================================================
# 3. COMPARISON OPERATORS
# ==========================================================
#
# Used to compare two values
# Returns True or False
#
# ==   Equal
# !=   Not Equal
# >    Greater Than
# <    Less Than
# >=   Greater Than or Equal
# <=   Less Than or Equal
#
# ==========================================================

print("3. COMPARISON OPERATORS")

p = 20
q = 10

print("p == q :", p == q)
print("p != q :", p != q)
print("p > q  :", p > q)
print("p < q  :", p < q)
print("p >= q :", p >= q)
print("p <= q :", p <= q)

print()


# ==========================================================
# 4. LOGICAL OPERATORS
# ==========================================================
#
# and   -> True if both conditions are True
# or    -> True if at least one condition is True
# not   -> Reverses the result
#
# ==========================================================

print("4. LOGICAL OPERATORS")

a = True
b = False

print("a and b :", a and b)
print("a or b  :", a or b)
print("not a   :", not a)

print()


# ==========================================================
# 5. IDENTITY OPERATORS
# ==========================================================
#
# is       -> True if same object
# is not   -> True if not same object
#
# ==========================================================

print("5. IDENTITY OPERATORS")

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print("list1 is list2 :", list1 is list2)
print("list1 is list3 :", list1 is list3)
print("list1 is not list3 :", list1 is not list3)

print()


# ==========================================================
# 6. MEMBERSHIP OPERATORS
# ==========================================================
#
# in        -> True if value exists
# not in    -> True if value does not exist
#
# ==========================================================

print("6. MEMBERSHIP OPERATORS")

text = "Python Programming"

print("'Python' in text :", "Python" in text)
print("'Java' in text :", "Java" in text)
print("'Java' not in text :", "Java" not in text)

print()


# ==========================================================
# 7. BITWISE OPERATORS
# ==========================================================
#
# Performs operations on binary values
#
# &   AND
# |   OR
# ^   XOR
# ~   NOT
# <<  Left Shift
# >>  Right Shift
#
# ==========================================================

print("7. BITWISE OPERATORS")

x = 5      # Binary = 0101
y = 3      # Binary = 0011

print("x =", x)
print("y =", y)

print("x & y =", x & y)
print("x | y =", x | y)
print("x ^ y =", x ^ y)
print("~x =", ~x)
print("x << 1 =", x << 1)
print("x >> 1 =", x >> 1)

print()


# ==========================================================
# 8. OPERATOR PRECEDENCE
# ==========================================================
#
# Python follows mathematical priority rules
#
# Example:
# Multiplication happens before addition
#
# ==========================================================

print("8. OPERATOR PRECEDENCE")

result1 = 10 + 5 * 2
print("10 + 5 * 2 =", result1)

result2 = (10 + 5) * 2
print("(10 + 5) * 2 =", result2)

print()


# ==========================================================
# 9. RELATIONAL EXAMPLE
# ==========================================================

print("9. RELATIONAL EXAMPLE")

age = 20

if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible")

print()


# ==========================================================
# 10. LOGICAL CONDITION EXAMPLE
# ==========================================================

print("10. LOGICAL CONDITION EXAMPLE")

username = "admin"
password = "1234"

user = input("Enter username: ")
pwd = input("Enter password: ")

if user == username and pwd == password:
    print("Login Successful")
else:
    print("Invalid Username or Password")

print()


# ==========================================================
# 11. MEMBERSHIP EXAMPLE
# ==========================================================

print("11. MEMBERSHIP EXAMPLE")

fruits = ["apple", "banana", "mango"]

print("'apple' in fruits :", "apple" in fruits)
print("'grapes' in fruits :", "grapes" in fruits)

print()


# ==========================================================
# 12. IDENTITY EXAMPLE
# ==========================================================

print("12. IDENTITY EXAMPLE")

a = [1, 2]
b = a
c = [1, 2]

print("a is b :", a is b)
print("a is c :", a is c)

print()


# ==========================================================
# 13. COMBINED OPERATORS EXAMPLE
# ==========================================================

print("13. COMBINED OPERATORS EXAMPLE")

num = 25

# Checking range using logical and comparison operators
result = num > 10 and num < 50

print("Is number between 10 and 50?", result)

print()


# ==========================================================
# END OF PROGRAM
# ==========================================================

print("===== END OF COMPLETE OPERATORS PROGRAM =====")
print("next session - python list")