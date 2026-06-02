# ============================================
# Python Math Module Demonstration Program
# ============================================

# Import math module
import math

# ------------------------------------------------
# 1. Mathematical Constants
# ------------------------------------------------

print("1. Mathematical Constants")

print("Value of PI:", math.pi)
print("Value of Euler's Number (e):", math.e)

print()


# ------------------------------------------------
# 2. Square Root
# ------------------------------------------------

number = 25

print("2. Square Root")

sqrt_value = math.sqrt(number)

print("Square Root of", number, "=", sqrt_value)

print()


# ------------------------------------------------
# 3. Power Function
# ------------------------------------------------

print("3. Power Function")

power_value = math.pow(2, 3)

print("2^3 =", power_value)

print()


# ------------------------------------------------
# 4. Absolute Value
# ------------------------------------------------

print("4. Absolute Value")

print(math.fabs(-50))

print()


# ------------------------------------------------
# 5. Ceiling Function
# ------------------------------------------------

print("5. Ceiling Function")

print(math.ceil(4.2))

print()


# ------------------------------------------------
# 6. Floor Function
# ------------------------------------------------

print("6. Floor Function")

print(math.floor(4.9))

print()


# ------------------------------------------------
# 7. Factorial
# ------------------------------------------------

print("7. Factorial")

print("Factorial of 5 =", math.factorial(5))

print()


# ------------------------------------------------
# 8. Greatest Common Divisor
# ------------------------------------------------

print("8. GCD")

print("GCD of 24 and 36 =", math.gcd(24, 36))

print()


# ------------------------------------------------
# 9. Trigonometric Functions
# ------------------------------------------------

print("9. Trigonometric Functions")

angle = 30

# Convert degree to radian
radian = math.radians(angle)

print("Sin(30) =", math.sin(radian))
print("Cos(30) =", math.cos(radian))
print("Tan(30) =", math.tan(radian))

print()


# ------------------------------------------------
# 10. Logarithms
# ------------------------------------------------

print("10. Logarithms")

print("Natural Log of 10 =", math.log(10))
print("Log Base 10 of 100 =", math.log10(100))

print()


# ------------------------------------------------
# 11. Exponential Function
# ------------------------------------------------

print("11. Exponential")

print("e^2 =", math.exp(2))

print()


# ------------------------------------------------
# 12. Degree and Radian Conversion
# ------------------------------------------------

print("12. Conversion")

print("180 Degrees =", math.radians(180), "Radians")
print("PI Radians =", math.degrees(math.pi), "Degrees")

print()


# ------------------------------------------------
# 13. Hypotenuse Calculation
# ------------------------------------------------

print("13. Hypotenuse")

side1 = 3
side2 = 4

hypotenuse = math.hypot(side1, side2)

print("Hypotenuse =", hypotenuse)

print()


# ------------------------------------------------
# 14. Sum of Multiple Numbers
# ------------------------------------------------

print("14. Product of Numbers")

numbers = [2, 3, 4]

result = math.prod(numbers)

print("Product =", result)

print()


# ------------------------------------------------
# 15. Distance Between Two Points
# ------------------------------------------------

print("15. Distance Calculation")

distance = math.dist([1, 2], [4, 6])

print("Distance =", distance)

print()


# ------------------------------------------------
# Program End
# ------------------------------------------------

print("Math Module Demonstration Completed!")