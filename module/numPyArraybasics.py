# ==========================================================
# NUMPY ARRAYS - COMPLETE INTRODUCTION WITH EXAMPLES
# ==========================================================

# Import NumPy library
import numpy as np

print("===== NUMPY ARRAYS TUTORIAL =====\n")

# ----------------------------------------------------------
# 1. Creating a 1-D Array
# ----------------------------------------------------------
# A NumPy array is similar to a Python list but is faster
# and supports mathematical operations efficiently.

arr1 = np.array([10, 20, 30, 40, 50])

print("1-D Array:")
print(arr1)
print("Type:", type(arr1))
print()

# ----------------------------------------------------------
# 2. Creating a 2-D Array
# ----------------------------------------------------------
# A 2-D array is like a table with rows and columns.

arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("2-D Array:")
print(arr2)
print()

# ----------------------------------------------------------
# 3. Array Dimensions
# ----------------------------------------------------------
# ndim tells how many dimensions the array has.

print("Dimensions of arr1:", arr1.ndim)
print("Dimensions of arr2:", arr2.ndim)
print()

# ----------------------------------------------------------
# 4. Array Shape
# ----------------------------------------------------------
# shape returns the number of rows and columns.

print("Shape of arr1:", arr1.shape)
print("Shape of arr2:", arr2.shape)
print()

# ----------------------------------------------------------
# 5. Array Data Type
# ----------------------------------------------------------
# dtype shows the type of elements stored in the array.

print("Data type of arr1:", arr1.dtype)
print()

# ----------------------------------------------------------
# 6. Accessing Elements
# ----------------------------------------------------------
# Indexing starts from 0.

print("First element:", arr1[0])
print("Third element:", arr1[2])
print()

# Accessing elements in a 2-D array
print("Element at row 1, column 2:", arr2[0, 1])
print()

# ----------------------------------------------------------
# 7. Slicing Arrays
# ----------------------------------------------------------
# Slicing extracts a portion of the array.

print("Elements from index 1 to 3:")
print(arr1[1:4])
print()

# ----------------------------------------------------------
# 8. Array Operations
# ----------------------------------------------------------
# NumPy performs element-wise operations.

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Array A:", a)
print("Array B:", b)

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print()

# ----------------------------------------------------------
# 9. Mathematical Functions
# ----------------------------------------------------------

print("Sum of elements:", np.sum(a))
print("Mean:", np.mean(a))
print("Maximum:", np.max(a))
print("Minimum:", np.min(a))
print()

# ----------------------------------------------------------
# 10. Creating Special Arrays
# ----------------------------------------------------------

# Array of zeros
zeros_array = np.zeros((2, 3))
print("Zeros Array:")
print(zeros_array)
print()

# Array of ones
ones_array = np.ones((2, 3))
print("Ones Array:")
print(ones_array)
print()

# Sequence of numbers
range_array = np.arange(1, 11)
print("Array using arange():")
print(range_array)
print()

# ----------------------------------------------------------
# 11. Reshaping Arrays
# ----------------------------------------------------------
# Reshape changes the dimensions without changing data.

arr = np.arange(1, 13)

reshaped = arr.reshape(3, 4)

print("Original Array:")
print(arr)

print("Reshaped Array (3 rows, 4 columns):")
print(reshaped)
print()

# ----------------------------------------------------------
# 12. Iterating Through an Array
# ----------------------------------------------------------

print("Looping through array elements:")

for value in arr1:
    print(value)

print()

# ----------------------------------------------------------
# 13. Finding Array Size
# ----------------------------------------------------------

print("Total number of elements:", arr2.size)
print()

# ----------------------------------------------------------
# 14. Converting Python List to NumPy Array
# ----------------------------------------------------------

my_list = [100, 200, 300]

numpy_array = np.array(my_list)

print("Python List:", my_list)
print("Converted NumPy Array:", numpy_array)
print()

# ----------------------------------------------------------
# 15. Why NumPy Arrays?
# ----------------------------------------------------------
# Advantages:
# 1. Faster than Python lists
# 2. Less memory usage
# 3. Supports vectorized operations
# 4. Useful for Data Science and Machine Learning

print("NumPy Arrays are powerful for numerical computing!")