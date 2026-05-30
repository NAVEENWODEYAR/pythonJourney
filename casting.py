# ============================================
# PYTHON TYPE CASTING EXAMPLE PROGRAM
# ============================================
#
# Type Casting means converting one data type
# into another data type.
#
# Example:
# int -> float
# string -> int
# float -> string
#
# Python provides built-in functions for casting:
# int()    -> converts to integer
# float()  -> converts to float
# str()    -> converts to string
# bool()   -> converts to boolean
#
# ============================================

print("===== PYTHON TYPE CASTING DEMO =====\n")


# ------------------------------------------------
# 1. INTEGER TO FLOAT
# ------------------------------------------------

# Integer value
num_int = 10

# Convert integer to float
num_float = float(num_int)

print("1. INTEGER TO FLOAT")
print("Original Integer:", num_int)
print("After Casting to Float:", num_float)
print("Type of num_int:", type(num_int))
print("Type of num_float:", type(num_float))
print()


# ------------------------------------------------
# 2. FLOAT TO INTEGER
# ------------------------------------------------

# Float value
price = 99.99

# Convert float to integer
# int() removes the decimal part
price_int = int(price)

print("2. FLOAT TO INTEGER")
print("Original Float:", price)
print("After Casting to Integer:", price_int)
print("Type of price:", type(price))
print("Type of price_int:", type(price_int))
print()


# ------------------------------------------------
# 3. STRING TO INTEGER
# ------------------------------------------------

# String containing a number
age_str = "25"

# Convert string to integer
age_int = int(age_str)

print("3. STRING TO INTEGER")
print("Original String:", age_str)
print("After Casting to Integer:", age_int)
print("Type of age_str:", type(age_str))
print("Type of age_int:", type(age_int))
print()


# ------------------------------------------------
# 4. INTEGER TO STRING
# ------------------------------------------------

# Integer value
marks = 95

# Convert integer to string
marks_str = str(marks)

print("4. INTEGER TO STRING")
print("Original Integer:", marks)
print("After Casting to String:", marks_str)
print("Type of marks:", type(marks))
print("Type of marks_str:", type(marks_str))
print()


# ------------------------------------------------
# 5. STRING TO FLOAT
# ------------------------------------------------

# String containing decimal number
height_str = "5.9"

# Convert string to float
height_float = float(height_str)

print("5. STRING TO FLOAT")
print("Original String:", height_str)
print("After Casting to Float:", height_float)
print("Type of height_str:", type(height_str))
print("Type of height_float:", type(height_float))
print()


# ------------------------------------------------
# 6. BOOLEAN CASTING
# ------------------------------------------------

# Boolean conversion examples
print("6. BOOLEAN CASTING")

print("bool(1) =", bool(1))       # True
print("bool(0) =", bool(0))       # False
print("bool('Hello') =", bool("Hello"))  # True
print("bool('') =", bool(""))    # False
print()


# ------------------------------------------------
# 7. USER INPUT CASTING
# ------------------------------------------------

# input() always takes data as STRING
# So we must cast it if we need numbers

print("7. USER INPUT CASTING")

# Take input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Add numbers
sum_result = num1 + num2

print("Sum =", sum_result)
print()


# ------------------------------------------------
# 8. INVALID CASTING EXAMPLE
# ------------------------------------------------

print("8. INVALID CASTING EXAMPLE")

try:
    # This string cannot be converted to integer
    value = int("Python")
    print(value)

except ValueError:
    print("Error: Cannot convert 'Python' into integer")

print()


# ============================================
# END OF PROGRAM
# ============================================

print("===== END OF TYPE CASTING PROGRAM =====")