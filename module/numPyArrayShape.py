import numpy as np

print("=" * 50)
print("NUMPY ARRAY SHAPE DEMONSTRATION")
print("=" * 50)

# ------------------------------------
# 1D Array
# ------------------------------------
arr1 = np.array([10, 20, 30, 40, 50])

print("\n1D Array:")
print(arr1)

print("Shape:", arr1.shape)
print("Meaning: 5 elements in one dimension")

# ------------------------------------
# 2D Array
# ------------------------------------
arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\n2D Array:")
print(arr2)

print("Shape:", arr2.shape)
print("Meaning: 2 rows and 3 columns")

# ------------------------------------
# 3D Array
# ------------------------------------
arr3 = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print("\n3D Array:")
print(arr3)

print("Shape:", arr3.shape)
print("Meaning: 2 blocks, 2 rows, 2 columns")

# ------------------------------------
# Reshape Example
# ------------------------------------
arr = np.array([1, 2, 3, 4, 5, 6])

print("\nOriginal Array:")
print(arr)

print("Original Shape:", arr.shape)

new_arr = arr.reshape(2, 3)

print("\nAfter Reshape (2,3):")
print(new_arr)

print("New Shape:", new_arr.shape)

print("\nProgram Completed!")