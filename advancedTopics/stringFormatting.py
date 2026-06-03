"""
===============================================================================
PYTHON STRING FORMATTING - COMPLETE GUIDE
===============================================================================

Definition:
-----------
String formatting is the process of inserting variables, values, or expressions
into a string in a readable and controlled manner.

Why String Formatting?
----------------------
1. Makes output more readable.
2. Allows dynamic content inside strings.
3. Controls alignment, spacing, and precision.
4. Commonly used in reports, logs, user messages, and data display.

Python provides several ways to format strings:

1. Concatenation (+ operator)
2. %-Formatting (Old Style)
3. str.format() Method
4. f-Strings (Recommended, Python 3.6+)

===============================================================================
"""


# =============================================================================
# 1. BASIC STRING
# =============================================================================

print("\n" + "=" * 80)
print("1. BASIC STRING")
print("=" * 80)

name = "Alice"

# Simple string
print("Hello World")

# Variable inside string requires formatting
print("Name:", name)


# =============================================================================
# 2. STRING CONCATENATION
# =============================================================================

print("\n" + "=" * 80)
print("2. STRING CONCATENATION")
print("=" * 80)

"""
Concatenation:
--------------
Combining strings using the + operator.

Syntax:
-------
string1 + string2
"""

first_name = "John"
last_name = "Doe"

full_name = first_name + " " + last_name

print("Full Name:", full_name)

# Limitation:
# Cannot directly concatenate string and integer

age = 25

# print("Age: " + age)   # ERROR

# Correct way
print("Age: " + str(age))


# =============================================================================
# 3. OLD STYLE (%) FORMATTING
# =============================================================================

print("\n" + "=" * 80)
print("3. OLD STYLE (%) FORMATTING")
print("=" * 80)

"""
Old Style Formatting:
---------------------
Uses the % operator.

Syntax:
-------
"format string" % values

Common Specifiers:
------------------
%s  -> String
%d  -> Integer
%f  -> Float
%.2f -> Float with 2 decimal places
"""

name = "David"
age = 30
salary = 45678.567

print("Name: %s" % name)
print("Age: %d" % age)
print("Salary: %.2f" % salary)

# Multiple values
print("Name: %s | Age: %d" % (name, age))


# =============================================================================
# 4. str.format() METHOD
# =============================================================================

print("\n" + "=" * 80)
print("4. str.format() METHOD")
print("=" * 80)

"""
Introduced in Python 3.

Syntax:
-------
"{}".format(value)

Advantages:
-----------
1. More readable.
2. Supports positional arguments.
3. Supports named arguments.
"""

name = "Emma"
age = 28

# Basic formatting
print("Name: {}".format(name))

# Multiple values
print("Name: {} Age: {}".format(name, age))

# Positional indexes
print("Age: {1}, Name: {0}".format(name, age))

# Named placeholders
print("Name: {n}, Age: {a}".format(n=name, a=age))


# =============================================================================
# 5. F-STRINGS (BEST METHOD)
# =============================================================================

print("\n" + "=" * 80)
print("5. F-STRINGS")
print("=" * 80)

"""
f-Strings:
----------
Introduced in Python 3.6.

Recommended because:
--------------------
1. Fast
2. Easy to read
3. Allows expressions directly

Syntax:
-------
f"text {variable}"
"""

name = "Sophia"
age = 22

print(f"Name: {name}")
print(f"Age: {age}")

# Expression inside f-string
print(f"Next Year Age: {age + 1}")

x = 10
y = 20

print(f"Sum = {x + y}")


# =============================================================================
# 6. FLOAT FORMATTING
# =============================================================================

print("\n" + "=" * 80)
print("6. FLOAT FORMATTING")
print("=" * 80)

pi = 3.14159265359

# Default
print(f"PI = {pi}")

# 2 decimal places
print(f"PI = {pi:.2f}")

# 4 decimal places
print(f"PI = {pi:.4f}")

# Using format()
print("PI = {:.3f}".format(pi))


# =============================================================================
# 7. WIDTH AND ALIGNMENT
# =============================================================================

print("\n" + "=" * 80)
print("7. WIDTH AND ALIGNMENT")
print("=" * 80)

"""
Alignment Symbols:
------------------
<  Left Align
>  Right Align
^  Center Align

Syntax:
-------
{value:alignment width}
"""

text = "Python"

print(f"|{text:<15}|")   # Left
print(f"|{text:>15}|")   # Right
print(f"|{text:^15}|")   # Center


# =============================================================================
# 8. NUMBER FORMATTING
# =============================================================================

print("\n" + "=" * 80)
print("8. NUMBER FORMATTING")
print("=" * 80)

number = 1234567890

# Comma separator
print(f"{number:,}")

# Underscore separator
print(f"{number:_}")

# Binary
print(f"{number:b}")

# Octal
print(f"{number:o}")

# Hexadecimal
print(f"{number:x}")

# Uppercase Hexadecimal
print(f"{number:X}")


# =============================================================================
# 9. PADDING WITH ZEROS
# =============================================================================

print("\n" + "=" * 80)
print("9. ZERO PADDING")
print("=" * 80)

num = 42

# Width 5 with leading zeros
print(f"{num:05}")

# Width 10 with leading zeros
print(f"{num:010}")


# =============================================================================
# 10. PERCENTAGE FORMAT
# =============================================================================

print("\n" + "=" * 80)
print("10. PERCENTAGE FORMAT")
print("=" * 80)

score = 0.875

# Convert to percentage
print(f"{score:.2%}")

# Output: 87.50%


# =============================================================================
# 11. SCIENTIFIC NOTATION
# =============================================================================

print("\n" + "=" * 80)
print("11. SCIENTIFIC NOTATION")
print("=" * 80)

value = 123456789

print(f"{value:e}")
print(f"{value:.2e}")


# =============================================================================
# 12. STRING REPETITION
# =============================================================================

print("\n" + "=" * 80)
print("12. STRING REPETITION")
print("=" * 80)

print("-" * 30)
print("*" * 50)


# =============================================================================
# 13. MULTI-LINE FORMATTED STRINGS
# =============================================================================

print("\n" + "=" * 80)
print("13. MULTI-LINE FORMATTED STRINGS")
print("=" * 80)

name = "Robert"
age = 35
city = "New York"

message = f"""
Employee Information
--------------------
Name : {name}
Age  : {age}
City : {city}
"""

print(message)


# =============================================================================
# 14. FORMATTING TABLE OUTPUT
# =============================================================================

print("\n" + "=" * 80)
print("14. TABLE FORMAT OUTPUT")
print("=" * 80)

print(f"{'Name':<15}{'Age':<10}{'Salary':<15}")
print("-" * 40)

print(f"{'John':<15}{25:<10}{50000:<15}")
print(f"{'Emma':<15}{30:<10}{70000:<15}")
print(f"{'David':<15}{28:<10}{65000:<15}")


# =============================================================================
# 15. DEBUGGING WITH F-STRINGS
# =============================================================================

print("\n" + "=" * 80)
print("15. DEBUGGING FEATURE")
print("=" * 80)

"""
Python 3.8+ Feature

Syntax:
-------
{variable=}
"""

x = 100
y = 50

print(f"{x=}")
print(f"{y=}")
print(f"{x + y=}")


# =============================================================================
# 16. PRACTICAL REAL-WORLD EXAMPLE
# =============================================================================

print("\n" + "=" * 80)
print("16. REAL-WORLD EXAMPLE")
print("=" * 80)

employee_name = "Michael"
employee_id = 1001
salary = 75643.789

print(
    f"Employee ID: {employee_id}\n"
    f"Employee Name: {employee_name}\n"
    f"Monthly Salary: ₹{salary:,.2f}"
)


# =============================================================================
# SUMMARY
# =============================================================================

print("\n" + "=" * 80)
print("SUMMARY")
print("=" * 80)

print("""
1. Concatenation (+)
   Example:
       "Hello " + name

2. Old Style (%)
   Example:
       "Age: %d" % age

3. format()
   Example:
       "Age: {}".format(age)

4. f-Strings (Recommended)
   Example:
       f"Age: {age}"

Formatting Options:
-------------------
:.2f      -> 2 decimal places
:,        -> Comma separator
:05       -> Zero padding
:<10      -> Left alignment
:>10      -> Right alignment
:^10      -> Center alignment
:.2%      -> Percentage
:e        -> Scientific notation

Best Practice:
--------------
Use f-Strings whenever possible because they are:
✔ Readable
✔ Fast
✔ Powerful
✔ Modern Python Standard
""")

print("\nEnd of Complete String Formatting Tutorial")