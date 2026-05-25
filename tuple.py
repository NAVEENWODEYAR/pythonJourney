"""
Python Tuples - Complete Demonstration
--------------------------------------
A tuple is a collection data type in Python.

Tuples are:
1. Ordered
2. Immutable (cannot be changed)
3. Allow duplicate values
4. Can store different data types

This program demonstrates:
- Creating tuples
- Accessing elements
- Tuple methods
- Tuple operations
- Packing and unpacking
- Nested tuples
- Built-in functions
"""

# --------------------------------------------------
# CREATING TUPLES
# --------------------------------------------------

# Empty tuple
empty_tuple = ()

# Tuple with integers
numbers = (10, 20, 30, 40)

# Tuple with mixed data types
mixed = ("Python", 3.14, True, 100)

# Single element tuple
single = (5,)   # Comma is mandatory

print("Empty Tuple:", empty_tuple)
print("Numbers Tuple:", numbers)
print("Mixed Tuple:", mixed)
print("Single Element Tuple:", single)


# --------------------------------------------------
# ACCESSING ELEMENTS
# --------------------------------------------------

print("\nACCESSING ELEMENTS")

# Access using index
print("First element:", numbers[0])

# Negative indexing
print("Last element:", numbers[-1])

# Slicing
print("First 2 elements:", numbers[:2])


# --------------------------------------------------
# IMMUTABILITY OF TUPLES
# --------------------------------------------------

print("\nIMMUTABILITY")

# Tuples cannot be modified
# numbers[0] = 100  # This will give an error

print("Tuples are immutable (cannot be changed)")


# --------------------------------------------------
# TUPLE METHODS
# --------------------------------------------------

# Tuples have only 2 built-in methods:
# 1. count()
# 2. index()

data = (1, 2, 2, 3, 4, 2, 5)

# --------------------------------------------------

# 1. count()
# Counts number of occurrences of an element

print("\n1. count()")

print("Count of 2:", data.count(2))


# --------------------------------------------------

# 2. index()
# Returns first index of the element

print("\n2. index()")

print("Index of 3:", data.index(3))


# --------------------------------------------------
# TUPLE OPERATIONS
# --------------------------------------------------

print("\nTUPLE OPERATIONS")

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation
print("Concatenation:", tuple1 + tuple2)

# Repetition
print("Repetition:", tuple1 * 3)

# Membership
print("Is 2 present?", 2 in tuple1)


# --------------------------------------------------
# LOOPING THROUGH TUPLES
# --------------------------------------------------

print("\nLOOPING THROUGH TUPLES")

for item in tuple1:
    print(item)

# Using index
print("\nUsing index")

for i in range(len(tuple1)):
    print(i, tuple1[i])


# --------------------------------------------------
# BUILT-IN FUNCTIONS WITH TUPLES
# --------------------------------------------------

print("\nBUILT-IN FUNCTIONS")

values = (5, 10, 15, 20)

print("Length:", len(values))
print("Maximum:", max(values))
print("Minimum:", min(values))
print("Sum:", sum(values))


# --------------------------------------------------
# NESTED TUPLES
# --------------------------------------------------

print("\nNESTED TUPLES")

nested = (
    (1, 2),
    (3, 4),
    (5, 6)
)

print(nested)

print("Accessing element:", nested[1][0])


# --------------------------------------------------
# TUPLE PACKING
# --------------------------------------------------

print("\nTUPLE PACKING")

# Packing values into a tuple
person = ("John", 25, "Engineer")

print(person)


# --------------------------------------------------
# TUPLE UNPACKING
# --------------------------------------------------

print("\nTUPLE UNPACKING")

name, age, profession = person

print("Name:", name)
print("Age:", age)
print("Profession:", profession)


# --------------------------------------------------
# CONVERTING LIST TO TUPLE
# --------------------------------------------------

print("\nLIST TO TUPLE")

my_list = [1, 2, 3]

converted_tuple = tuple(my_list)

print(converted_tuple)


# --------------------------------------------------
# CONVERTING TUPLE TO LIST
# --------------------------------------------------

print("\nTUPLE TO LIST")

my_tuple = (10, 20, 30)

converted_list = list(my_tuple)

print(converted_list)


# --------------------------------------------------
# DELETING A TUPLE
# --------------------------------------------------

print("\nDELETING A TUPLE")

temp = (1, 2, 3)

print("Tuple before deletion:", temp)

# Delete entire tuple
del temp

print("Tuple deleted successfully")


# --------------------------------------------------
# COMPARISON OF LIST AND TUPLE
# --------------------------------------------------

print("\nLIST vs TUPLE")

print("LIST: Mutable")
print("TUPLE: Immutable")

print("LIST uses [] brackets")
print("TUPLE uses () brackets")


# --------------------------------------------------
# FINAL OUTPUT
# --------------------------------------------------

print("\nProgram Completed Successfully!")