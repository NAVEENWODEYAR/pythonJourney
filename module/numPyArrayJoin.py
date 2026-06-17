# NumPy Array Joining Methods Demonstration
# -----------------------------------------
# This program explains and demonstrates:
# 1. concatenate()
# 2. hstack()
# 3. vstack()
# 4. stack()
# 5. column_stack()
# 6. row_stack()
# 7. dstack()

import numpy as np

# ------------------------------------------------------------------
# STEP 1: Create sample arrays
# ------------------------------------------------------------------

# 1-D arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print("=" * 60)
print("ORIGINAL ARRAYS")
print("=" * 60)

print("Array 1:", arr1)
print("Array 2:", arr2)

# ------------------------------------------------------------------
# 1. concatenate()
# ------------------------------------------------------------------
# Purpose:
# Joins arrays along an existing axis.
# No new dimension is created.

print("\n" + "=" * 60)
print("1. concatenate()")
print("=" * 60)

result = np.concatenate((arr1, arr2))

print("Result:", result)

# Output:
# [1 2 3 4 5 6]

# ------------------------------------------------------------------
# 2. hstack()
# ------------------------------------------------------------------
# Purpose:
# Horizontally stack arrays (side-by-side).
# For 1-D arrays, it behaves similar to concatenate().

print("\n" + "=" * 60)
print("2. hstack()")
print("=" * 60)

result = np.hstack((arr1, arr2))

print("Result:", result)

# Output:
# [1 2 3 4 5 6]

# ------------------------------------------------------------------
# 3. vstack()
# ------------------------------------------------------------------
# Purpose:
# Vertically stack arrays.
# Creates rows from input arrays.

print("\n" + "=" * 60)
print("3. vstack()")
print("=" * 60)

result = np.vstack((arr1, arr2))

print("Result:\n", result)

# Output:
# [[1 2 3]
#  [4 5 6]]

# ------------------------------------------------------------------
# 4. stack()
# ------------------------------------------------------------------
# Purpose:
# Joins arrays along a NEW axis.
# Unlike concatenate(), a new dimension is created.

print("\n" + "=" * 60)
print("4. stack()")
print("=" * 60)

result = np.stack((arr1, arr2))

print("Result:\n", result)

# Output:
# [[1 2 3]
#  [4 5 6]]

# Shape helps us understand dimensions
print("Shape:", result.shape)

# ------------------------------------------------------------------
# 5. column_stack()
# ------------------------------------------------------------------
# Purpose:
# Combines 1-D arrays as columns.

print("\n" + "=" * 60)
print("5. column_stack()")
print("=" * 60)

result = np.column_stack((arr1, arr2))

print("Result:\n", result)

# Output:
# [[1 4]
#  [2 5]
#  [3 6]]

# ------------------------------------------------------------------
# 6. row_stack()
# ------------------------------------------------------------------
# Purpose:
# Combines arrays as rows.
# Similar to vstack().

print("\n" + "=" * 60)
print("6. row_stack()")
print("=" * 60)

result = np.row_stack((arr1, arr2))

print("Result:\n", result)

# Output:
# [[1 2 3]
#  [4 5 6]]

# ------------------------------------------------------------------
# 7. dstack()
# ------------------------------------------------------------------
# Purpose:
# Stacks arrays along the third dimension (depth).
# Commonly used in image processing and 3D data.

print("\n" + "=" * 60)
print("7. dstack()")
print("=" * 60)

result = np.dstack((arr1, arr2))

print("Result:\n", result)

# Output:
# [[[1 4]
#   [2 5]
#   [3 6]]]

print("Shape:", result.shape)

# ------------------------------------------------------------------
# Working with 2-D Arrays
# ------------------------------------------------------------------

print("\n" + "=" * 60)
print("2-D ARRAY EXAMPLES")
print("=" * 60)

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

# Join row-wise (axis=0)
print("\nConcatenate along rows (axis=0):")
print(np.concatenate((A, B), axis=0))

# Join column-wise (axis=1)
print("\nConcatenate along columns (axis=1):")
print(np.concatenate((A, B), axis=1))

# ------------------------------------------------------------------
# Summary
# ------------------------------------------------------------------

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
concatenate()  -> Join arrays along an existing axis
hstack()       -> Horizontal join (side-by-side)
vstack()       -> Vertical join (top-to-bottom)
stack()        -> Join arrays and create a new axis
column_stack() -> Convert arrays into columns
row_stack()    -> Convert arrays into rows
dstack()       -> Join arrays along depth (3rd dimension)
""")