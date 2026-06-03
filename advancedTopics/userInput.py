"""
===============================================================================
PYTHON STRING FORMATTING WITH USER INPUT
===============================================================================

Definition:
-----------
String formatting is the process of inserting variables, user inputs, or
expressions into a string in a readable and controlled format.

This program demonstrates:
1. Taking user input
2. Converting input data types
3. Different string formatting methods
4. Formatting numbers, currency, and percentages
===============================================================================
"""

# -----------------------------------------------------------------------------
# STEP 1: GET INPUT FROM USER
# -----------------------------------------------------------------------------

print("===== USER INFORMATION FORM =====")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
salary = float(input("Enter your monthly salary: "))

# -----------------------------------------------------------------------------
# STEP 2: DISPLAY USING NORMAL PRINT
# -----------------------------------------------------------------------------

print("\n===== NORMAL PRINT =====")

print("Name:", name)
print("Age:", age)
print("City:", city)
print("Salary:", salary)

# -----------------------------------------------------------------------------
# STEP 3: STRING CONCATENATION
# -----------------------------------------------------------------------------

print("\n===== STRING CONCATENATION =====")

# Numbers must be converted to string using str()
print("Name: " + name)
print("Age: " + str(age))
print("City: " + city)

# -----------------------------------------------------------------------------
# STEP 4: OLD STYLE (%) FORMATTING
# -----------------------------------------------------------------------------

print("\n===== OLD STYLE (%) FORMATTING =====")

print("Name: %s" % name)
print("Age: %d" % age)
print("Salary: %.2f" % salary)

# Multiple variables
print("Name: %s | Age: %d | City: %s" % (name, age, city))

# -----------------------------------------------------------------------------
# STEP 5: str.format() METHOD
# -----------------------------------------------------------------------------

print("\n===== str.format() METHOD =====")

print("Name: {}".format(name))
print("Age: {}".format(age))

print(
    "Name: {} | Age: {} | City: {}".format(
        name,
        age,
        city
    )
)

# Named placeholders
print(
    "Name: {n} | Age: {a} | City: {c}".format(
        n=name,
        a=age,
        c=city
    )
)

# -----------------------------------------------------------------------------
# STEP 6: F-STRINGS (RECOMMENDED)
# -----------------------------------------------------------------------------

print("\n===== F-STRINGS =====")

print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print(f"Salary: {salary}")

# Expression inside f-string
print(f"Age After 5 Years: {age + 5}")

# -----------------------------------------------------------------------------
# STEP 7: FLOAT FORMATTING
# -----------------------------------------------------------------------------

print("\n===== FLOAT FORMATTING =====")

print(f"Salary: {salary:.2f}")      # 2 decimal places
print(f"Salary: {salary:.3f}")      # 3 decimal places

# -----------------------------------------------------------------------------
# STEP 8: CURRENCY FORMAT
# -----------------------------------------------------------------------------

print("\n===== CURRENCY FORMAT =====")

print(f"Monthly Salary : ₹{salary:,.2f}")
print(f"Annual Salary  : ₹{salary * 12:,.2f}")

# -----------------------------------------------------------------------------
# STEP 9: ALIGNMENT FORMAT
# -----------------------------------------------------------------------------

print("\n===== ALIGNMENT =====")

print(f"|{name:<20}|")   # Left Align
print(f"|{name:>20}|")   # Right Align
print(f"|{name:^20}|")   # Center Align

# -----------------------------------------------------------------------------
# STEP 10: TABLE FORMAT
# -----------------------------------------------------------------------------

print("\n===== FORMATTED TABLE =====")

print("-" * 50)
print(f"{'NAME':<15}{'AGE':<10}{'CITY':<15}")
print("-" * 50)

print(f"{name:<15}{age:<10}{city:<15}")

print("-" * 50)

# -----------------------------------------------------------------------------
# STEP 11: PERCENTAGE FORMAT
# -----------------------------------------------------------------------------

print("\n===== PERCENTAGE FORMAT =====")

attendance = float(
    input("Enter attendance percentage as decimal (e.g. 0.85): ")
)

print(f"Attendance: {attendance:.2%}")

# -----------------------------------------------------------------------------
# STEP 12: DEBUG FORMAT (Python 3.8+)
# -----------------------------------------------------------------------------

print("\n===== DEBUG FORMAT =====")

print(f"{name=}")
print(f"{age=}")
print(f"{salary=}")

# -----------------------------------------------------------------------------
# STEP 13: MULTILINE FORMATTED REPORT
# -----------------------------------------------------------------------------

print("\n===== EMPLOYEE REPORT =====")

report = f"""
----------------------------------------
EMPLOYEE DETAILS
----------------------------------------
Name          : {name}
Age           : {age}
City          : {city}
Monthly Salary: ₹{salary:,.2f}
Annual Salary : ₹{salary * 12:,.2f}
----------------------------------------
"""

print(report)

# -----------------------------------------------------------------------------
# SUMMARY
# -----------------------------------------------------------------------------

print("""
================ SUMMARY ================

1. Concatenation
   "Name: " + name

2. Old Style Formatting
   "Age: %d" % age

3. format() Method
   "Age: {}".format(age)

4. f-Strings (Best Method)
   f"Age: {age}"

Useful Specifiers:
------------------
%s      -> String
%d      -> Integer
%f      -> Float
:.2f    -> 2 Decimal Places
:,      -> Comma Separator
:<10    -> Left Align
:>10    -> Right Align
:^10    -> Center Align
:.2%    -> Percentage

Recommended:
-------------
Use f-Strings because they are easier to read,
faster, and more powerful.
=========================================
""")