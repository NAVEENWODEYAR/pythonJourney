"""
NumPy reshape() - Complete Explanation in One Program

reshape() is used to change the shape (dimensions) of an array
without changing its data.

Syntax:
    array.reshape(new_shape)

or

    np.reshape(array, new_shape)

Rules:
1. Total number of elements must remain the same.
2. reshape() returns a new view/copy with a different shape.
3. Use -1 to let NumPy automatically calculate one dimension.

Common Uses:
- Converting 1D arrays to 2D matrices.
- Preparing data for Machine Learning models.
- Transforming rows and columns for analysis.
- Restructuring image and numerical datasets.
"""

import numpy as np

print("=" * 60)
print("NUMPY RESHAPE() DEMONSTRATION")
print("=" * 60)

# ------------------------------------------------------------------
# Example 1: Create a 1D array
# ------------------------------------------------------------------
arr = np.arange(1, 13)  # Creates numbers from 1 to 12

print("\nOriginal Array:")
print(arr)

print("\nShape of Original Array:")
print(arr.shape)  # (12,) => 12 elements in one dimension

# ------------------------------------------------------------------
# Example 2: Reshape 1D array into 3 rows and 4 columns
# ------------------------------------------------------------------
arr_3x4 = arr.reshape(3, 4)

print("\nReshaped Array (3 x 4):")
print(arr_3x4)

print("Shape:", arr_3x4.shape)

# ------------------------------------------------------------------
# Example 3: Reshape into 4 rows and 3 columns
# ------------------------------------------------------------------
arr_4x3 = arr.reshape(4, 3)

print("\nReshaped Array (4 x 3):")
print(arr_4x3)

print("Shape:", arr_4x3.shape)

# ------------------------------------------------------------------
# Example 4: Using -1 (automatic dimension calculation)
# ------------------------------------------------------------------
auto_shape = arr.reshape(2, -1)

print("\nReshape using -1:")
print(auto_shape)

print("Shape:", auto_shape.shape)
# NumPy automatically calculates columns as 6

# ------------------------------------------------------------------
# Example 5: Convert 2D array back to 1D
# ------------------------------------------------------------------
back_to_1d = arr_3x4.reshape(-1)

print("\nConvert Back to 1D:")
print(back_to_1d)

print("Shape:", back_to_1d.shape)

# ------------------------------------------------------------------
# Example 6: Practical Usage
# ------------------------------------------------------------------
# Suppose we have marks of 3 students in 4 subjects

marks = np.array([85, 90, 88,
                  76, 80, 79,
                  92, 95, 91])

print("\nStudent Marks (1D):")
print(marks)

# Reshape into 3 students × 3 subjects
student_marks = marks.reshape(3, 3)

print("\nStudent Marks Matrix (3 Students x 3 Subjects):")
print(student_marks)

# ------------------------------------------------------------------
# Important Note
# ------------------------------------------------------------------
print("\nImportant Rule:")
print("Total elements before and after reshape must be equal.")

print("\nExample:")
print("12 elements can be reshaped into:")
print("  3 x 4  = 12")
print("  2 x 6  = 12")
print("  1 x 12 = 12")

# ------------------------------------------------------------------
# Invalid Reshape Example
# ------------------------------------------------------------------
try:
    arr.reshape(5, 3)  # 15 positions needed, only 12 elements exist
except ValueError as e:
    print("\nInvalid Reshape Example:")
    print("Error:", e)

print("\nProgram Completed Successfully!")