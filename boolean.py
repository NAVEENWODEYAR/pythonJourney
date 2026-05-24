# ==========================================================
# PYTHON BOOLEAN DEMO PROGRAM
# ==========================================================
#
# Boolean is a data type that has only two values:
#
# True
# False
#
# Booleans are mainly used in:
# - Conditions
# - Decision making
# - Comparisons
# - Loops
#
# ==========================================================

print("===== PYTHON BOOLEAN DEMO =====\n")


# ----------------------------------------------------------
# 1. CREATING BOOLEAN VALUES
# ----------------------------------------------------------

print("1. CREATING BOOLEAN VALUES")

a = True
b = False

print("Value of a:", a)
print("Value of b:", b)

print("Type of a:", type(a))
print("Type of b:", type(b))
print()


# ----------------------------------------------------------
# 2. BOOLEAN USING COMPARISON OPERATORS
# ----------------------------------------------------------

print("2. COMPARISON OPERATORS")

x = 10
y = 20

# Comparison returns True or False
print("x == y :", x == y)
print("x != y :", x != y)
print("x > y  :", x > y)
print("x < y  :", x < y)
print("x >= y :", x >= y)
print("x <= y :", x <= y)

print()


# ----------------------------------------------------------
# 3. BOOLEAN USING LOGICAL OPERATORS
# ----------------------------------------------------------

print("3. LOGICAL OPERATORS")

a = True
b = False

# AND operator
print("a and b :", a and b)

# OR operator
print("a or b :", a or b)

# NOT operator
print("not a :", not a)

print()


# ----------------------------------------------------------
# 4. BOOLEAN IN IF CONDITION
# ----------------------------------------------------------

print("4. BOOLEAN IN IF CONDITION")

age = 18

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

print()


# ----------------------------------------------------------
# 5. BOOLEAN USING bool() FUNCTION
# ----------------------------------------------------------

print("5. bool() FUNCTION")

print("bool(1) =", bool(1))
print("bool(0) =", bool(0))

print("bool('Python') =", bool("Python"))
print("bool('') =", bool(""))

print("bool(100) =", bool(100))
print("bool(None) =", bool(None))

print()


# ----------------------------------------------------------
# 6. BOOLEAN WITH STRINGS
# ----------------------------------------------------------

print("6. BOOLEAN WITH STRINGS")

username = "admin"

print("username == 'admin' :", username == "admin")
print("username == 'guest' :", username == "guest")

print()


# ----------------------------------------------------------
# 7. BOOLEAN WITH LISTS
# ----------------------------------------------------------

print("7. BOOLEAN WITH LISTS")

numbers = [1, 2, 3]
empty_list = []

# Non-empty list = True
print("bool(numbers) =", bool(numbers))

# Empty list = False
print("bool(empty_list) =", bool(empty_list))

print()


# ----------------------------------------------------------
# 8. BOOLEAN WITH LOOPS
# ----------------------------------------------------------

print("8. BOOLEAN WITH LOOP")

count = 1

while count <= 5:
    print("Count =", count)
    count += 1

print()


# ----------------------------------------------------------
# 9. BOOLEAN EXAMPLE PROGRAM
# ----------------------------------------------------------

print("9. LOGIN CHECK EXAMPLE")

password = "python123"

user_password = input("Enter password: ")

if user_password == password:
    print("Login Successful")
else:
    print("Wrong Password")

print()


# ----------------------------------------------------------
# 10. BOOLEAN EXPRESSIONS
# ----------------------------------------------------------

print("10. BOOLEAN EXPRESSIONS")

num = 15

# Checking range using boolean expression
result = num > 10 and num < 20

print("Is number between 10 and 20?", result)

print()


# ----------------------------------------------------------
# 11. BOOLEAN USING in OPERATOR
# ----------------------------------------------------------

print("11. BOOLEAN USING 'in' OPERATOR")

text = "Python Programming"

print("'Python' in text :", "Python" in text)
print("'Java' in text :", "Java" in text)

print()


# ----------------------------------------------------------
# 12. BOOLEAN USING is OPERATOR
# ----------------------------------------------------------

print("12. BOOLEAN USING 'is' OPERATOR")

a = True
b = True

print("a is b :", a is b)

print()


# ==========================================================
# END OF PROGRAM
# ==========================================================

print("===== END OF BOOLEAN DEMO =====")