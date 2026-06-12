import numpy as np

# ==========================
# 1. Creating Arrays
# ==========================
arr = np.array([10, 20, 30, 40, 50])
print("Original Array:", arr)

# ==========================
# 2. Shape and Size
# ==========================
print("\nShape:", arr.shape)      # Dimensions
print("Size:", arr.size)          # Total elements
print("Data Type:", arr.dtype)

# ==========================
# 3. Reshape
# ==========================
arr2 = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr2.reshape(2, 3)
print("\nReshaped Array (2x3):")
print(reshaped)

# ==========================
# 4. Flatten
# ==========================
flat = reshaped.flatten()
print("\nFlattened Array:", flat)

# ==========================
# 5. Indexing and Slicing
# ==========================
print("\nFirst Element:", arr[0])
print("Last Element:", arr[-1])
print("Slice [1:4]:", arr[1:4])

# ==========================
# 6. Mathematical Operations
# ==========================
print("\nArray + 5:", arr + 5)
print("Array * 2:", arr * 2)
print("Square of Elements:", arr ** 2)

# ==========================
# 7. Aggregate Methods
# ==========================
print("\nSum:", arr.sum())
print("Mean:", arr.mean())
print("Maximum:", arr.max())
print("Minimum:", arr.min())
print("Standard Deviation:", arr.std())

# ==========================
# 8. Sorting
# ==========================
unsorted = np.array([5, 2, 8, 1, 9])
print("\nUnsorted:", unsorted)
print("Sorted:", np.sort(unsorted))

# ==========================
# 9. Unique Values
# ==========================
dup = np.array([1, 2, 2, 3, 3, 4])
print("\nUnique Values:", np.unique(dup))

# ==========================
# 10. Concatenate Arrays
# ==========================
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
combined = np.concatenate((a, b))
print("\nConcatenated Array:", combined)

# ==========================
# 11. Append Elements
# ==========================
new_arr = np.append(arr, [60, 70])
print("\nAfter Append:", new_arr)

# ==========================
# 12. Insert Elements
# ==========================
inserted = np.insert(arr, 2, 25)
print("After Insert:", inserted)

# ==========================
# 13. Delete Elements
# ==========================
deleted = np.delete(arr, 1)
print("After Delete:", deleted)

# ==========================
# 14. Filtering
# ==========================
filtered = arr[arr > 25]
print("\nElements Greater Than 25:", filtered)

# ==========================
# 15. Transpose
# ==========================
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

print("\nOriginal Matrix:")
print(matrix)

print("\nTranspose:")
print(matrix.T)