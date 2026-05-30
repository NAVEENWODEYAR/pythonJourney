# Python Program for Number Data Types

print("=== NUMBER DATA TYPES IN PYTHON ===\n")

# Integer Type
integer_num = 100

print("Integer Type: Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.")
print("Value:", integer_num)
print("Data Type:", type(integer_num))
print()

# Float Type
float_num = 99.99

print("Float Type: Float, or floating point number is a number, positive or negative, containing one or more decimals. Float can also be scientific numbers with an (e) to indicate the power of 10.")
print("Value:", float_num)
print("Data Type:", type(float_num))
print()

# Complex Type
complex_num = 4 + 5j

print("Complex Type: Complex numbers are written with a (j) as the imaginary part:")
print("Value:", complex_num)
print("Data Type:", type(complex_num))
print()




# Arithmetic Operations
print("=== ARITHMETIC OPERATIONS ===")

a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)







# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
print("random number using built in module random")
import random

print(random.randrange(1, 10))
print("\n=== END OF PROGRAM ===")
print('next session - Python Casting')