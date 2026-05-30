# ============================================================
# PYTHON IF-ELSE DEMONSTRATION PROGRAM
# ============================================================
# if-else statements are used for decision making.
#
# They allow the program to:
# - Check conditions
# - Execute different blocks of code
# - Make logical decisions
#
# Syntax:
#
# if condition:
#     code
# else:
#     code
# ============================================================

# ------------------------------------------------------------
# 1. SIMPLE if STATEMENT
# ------------------------------------------------------------

age = 20

# Check if age is greater than or equal to 18
if age >= 18:
    print("You are eligible to vote")

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 2. if-else STATEMENT
# ------------------------------------------------------------

number = 10

# Check whether number is even or odd
if number % 2 == 0:
    print("The number is EVEN")
else:
    print("The number is ODD")

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 3. if-elif-else STATEMENT
# ------------------------------------------------------------

marks = 85

# Check grade based on marks
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 4. NESTED if STATEMENT
# ------------------------------------------------------------

username = "admin"
password = "1234"

# First check username
if username == "admin":

    # Then check password
    if password == "1234":
        print("Login Successful")
    else:
        print("Incorrect Password")

else:
    print("Invalid Username")

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 5. CHECK POSITIVE, NEGATIVE, OR ZERO
# ------------------------------------------------------------

num = -5

if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 6. LARGEST OF TWO NUMBERS
# ------------------------------------------------------------

a = 15
b = 25

if a > b:
    print(a, "is greater")
else:
    print(b, "is greater")

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 7. LARGEST OF THREE NUMBERS
# ------------------------------------------------------------

x = 10
y = 50
z = 30

if x >= y and x >= z:
    print(x, "is the largest")

elif y >= x and y >= z:
    print(y, "is the largest")

else:
    print(z, "is the largest")

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 8. CHECK LEAP YEAR
# ------------------------------------------------------------

year = 2024

# Leap year condition
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is NOT a Leap Year")

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 9. SIMPLE LOGIN SYSTEM
# ------------------------------------------------------------

saved_username = "python"
saved_password = "12345"

entered_username = "python"
entered_password = "12345"

if entered_username == saved_username and entered_password == saved_password:
    print("Login Successful")
else:
    print("Login Failed")

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 10. ELIGIBLE FOR DRIVING LICENSE
# ------------------------------------------------------------

person_age = 17

if person_age >= 18:
    print("Eligible for Driving License")
else:
    print("Not Eligible")

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 11. CHECK DIVISIBILITY
# ------------------------------------------------------------

n = 15

if n % 3 == 0 and n % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both")

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 12. TERNARY if-else (SHORT FORM)
# ------------------------------------------------------------

value = 7

# Short form of if-else
result = "Even" if value % 2 == 0 else "Odd"

print("The number is:", result)

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 13. PRACTICAL EXAMPLE - ATM WITHDRAWAL
# ------------------------------------------------------------

balance = 5000
withdraw = 2000

if withdraw <= balance:
    balance = balance - withdraw
    print("Withdrawal Successful")
    print("Remaining Balance:", balance)
else:
    print("Insufficient Balance")

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 14. FINAL SUMMARY
# ------------------------------------------------------------

print("IF-ELSE SUMMARY")
print("----------------")
print("1. if is used to check conditions")
print("2. else runs when condition is False")
print("3. elif checks multiple conditions")
print("4. Nested if means if inside another if")
print("5. if-else helps in decision making")
print("nest session :- match")