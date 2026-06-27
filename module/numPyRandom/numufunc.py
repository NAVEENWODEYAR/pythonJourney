# Import the NumPy library
import numpy as np

# -------------------------------------------------
# Step 1: Create NumPy Arrays
# -------------------------------------------------
# A NumPy array stores multiple values of the same type.

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])

print("Array 1:", arr1)
print("Array 2:", arr2)


# -------------------------------------------------
# Step 2: Arithmetic Ufuncs
# -------------------------------------------------
# Arithmetic ufuncs perform mathematical operations
# on each corresponding element of the arrays.

print("\n----- Arithmetic Ufuncs -----")

# Adds corresponding elements
print("Addition:", np.add(arr1, arr2))

# Subtracts corresponding elements
print("Subtraction:", np.subtract(arr2, arr1))

# Multiplies corresponding elements
print("Multiplication:", np.multiply(arr1, arr2))

# Divides corresponding elements
print("Division:", np.divide(arr2, arr1))


# -------------------------------------------------
# Step 3: Mathematical Ufuncs
# -------------------------------------------------
# These functions perform mathematical calculations
# on every element of the array.

print("\n----- Mathematical Ufuncs -----")

# Square of each element
print("Square:", np.square(arr1))

# Square root of each element
print("Square Root:", np.sqrt(arr2))

# Exponential value (e^x)
print("Exponential:", np.exp(arr1))


# -------------------------------------------------
# Step 4: Trigonometric Ufuncs
# -------------------------------------------------
# Trigonometric functions work with angles in radians.

angles = np.array([0, np.pi/2, np.pi])

print("\n----- Trigonometric Ufuncs -----")

print("Angles:", angles)

# Sine of each angle
print("Sin:", np.sin(angles))

# Cosine of each angle
print("Cos:", np.cos(angles))


# -------------------------------------------------
# Step 5: Comparison Ufuncs
# -------------------------------------------------
# Comparison ufuncs compare elements and return
# True or False.

print("\n----- Comparison Ufuncs -----")

# Checks whether elements of arr2 are greater than arr1
print("Greater:", np.greater(arr2, arr1))

# Checks whether elements are equal
print("Equal:", np.equal(arr1, arr2))


# -------------------------------------------------
# Step 6: Aggregate Functions
# -------------------------------------------------
# Aggregate functions return a single value
# after processing the entire array.

print("\n----- Aggregate Functions -----")

print("Maximum:", np.max(arr2))
print("Minimum:", np.min(arr2))
print("Sum:", np.sum(arr1))
print("Mean:", np.mean(arr2))