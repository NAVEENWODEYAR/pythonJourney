"""
=========================================================
        NUMPY ARRAY ITERATION - COMPLETE EXPLANATION
=========================================================

DEFINITION:
Array iteration is the process of visiting each element
of a NumPy array one by one to access, process, or modify
its values.

WHY ITERATION IS USED?
1. To read array elements individually.
2. To perform operations on each element.
3. To traverse multi-dimensional arrays.
4. To apply custom logic to array values.

SYNTAX:

1. Iterating a 1-D array:
   for element in array:
       print(element)

2. Iterating a 2-D array:
   for row in array:
       print(row)

3. Iterating each element of a multi-dimensional array:
   for element in np.nditer(array):
       print(element)

4. Iterating with index:
   for index, value in np.ndenumerate(array):
       print(index, value)

=========================================================
"""

import numpy as np

print("\n========== NUMPY ARRAY ITERATION ==========\n")

# -------------------------------------------------------
# 1. Creating a 1-D Array
# -------------------------------------------------------
print("1. ONE-DIMENSIONAL ARRAY")

arr1 = np.array([10, 20, 30, 40, 50])

print("Array:", arr1)

print("\nIterating through each element:")
for element in arr1:
    print(element)

# -------------------------------------------------------
# 2. Creating a 2-D Array
# -------------------------------------------------------
print("\n\n2. TWO-DIMENSIONAL ARRAY")

arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("Array:\n", arr2)

print("\nIterating row by row:")
for row in arr2:
    print(row)

# -------------------------------------------------------
# 3. Iterating each element of a 2-D Array
# -------------------------------------------------------
print("\n3. ITERATING EACH ELEMENT USING np.nditer()")

for element in np.nditer(arr2):
    print(element)

# -------------------------------------------------------
# 4. Three-Dimensional Array Iteration
# -------------------------------------------------------
print("\n4. THREE-DIMENSIONAL ARRAY")

arr3 = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print("Array:\n", arr3)

print("\nIterating all elements using np.nditer():")
for element in np.nditer(arr3):
    print(element)

# -------------------------------------------------------
# 5. Iteration with Index Values
# -------------------------------------------------------
print("\n5. ITERATION WITH INDEX USING np.ndenumerate()")

for index, value in np.ndenumerate(arr2):
    print(f"Index: {index}  Value: {value}")

# -------------------------------------------------------
# 6. Practical Example
# -------------------------------------------------------
print("\n6. PRACTICAL EXAMPLE - SQUARE OF EACH ELEMENT")

numbers = np.array([1, 2, 3, 4, 5])

for num in numbers:
    print(f"Square of {num} = {num**2}")

# -------------------------------------------------------
# SUMMARY
# -------------------------------------------------------
print("\n========== SUMMARY ==========")
print("""
1. Use 'for element in array' for 1-D arrays.
2. Use nested loops or np.nditer() for multi-dimensional arrays.
3. Use np.nditer() to access every element efficiently.
4. Use np.ndenumerate() when index positions are required.
5. Array iteration is useful for processing elements individually.
""")