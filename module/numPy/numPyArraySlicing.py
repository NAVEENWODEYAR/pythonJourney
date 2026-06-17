import numpy as np

print("=" * 50)
print("NUMPY ARRAY SLICING DEMONSTRATION")
print("=" * 50)

# --------------------------------------------------
# 1. Creating a 1D Array
# --------------------------------------------------
arr = np.array([10, 20, 30, 40, 50, 60, 70])

print("\nOriginal Array:")
print(arr)

# --------------------------------------------------
# 2. Basic Slicing
# Syntax: array[start:stop]
# start -> included
# stop  -> excluded
# --------------------------------------------------
print("\narr[1:5]")
print("Elements from index 1 to 4")
print(arr[1:5])

# --------------------------------------------------
# 3. From Beginning
# --------------------------------------------------
print("\narr[:4]")
print("From start up to index 3")
print(arr[:4])

# --------------------------------------------------
# 4. Till End
# --------------------------------------------------
print("\narr[3:]")
print("From index 3 to end")
print(arr[3:])

# --------------------------------------------------
# 5. Step Size
# Syntax: array[start:stop:step]
# --------------------------------------------------
print("\narr[::2]")
print("Every 2nd element")
print(arr[::2])

# --------------------------------------------------
# 6. Reverse Array
# --------------------------------------------------
print("\narr[::-1]")
print("Reverse order")
print(arr[::-1])

# --------------------------------------------------
# 7. Negative Indexing
# --------------------------------------------------
print("\narr[-4:-1]")
print("From 4th element from end to 2nd element from end")
print(arr[-4:-1])

# --------------------------------------------------
# 8. 2D Array
# --------------------------------------------------
arr2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("\n2D Array:")
print(arr2d)

# --------------------------------------------------
# 9. Access Single Element
# Syntax: array[row, column]
# --------------------------------------------------
print("\narr2d[1,2]")
print("Row 1, Column 2")
print(arr2d[1, 2])

# --------------------------------------------------
# 10. Entire Row
# --------------------------------------------------
print("\narr2d[1,:]")
print("Second row")
print(arr2d[1, :])

# --------------------------------------------------
# 11. Entire Column
# --------------------------------------------------
print("\narr2d[:,1]")
print("Second column")
print(arr2d[:, 1])

# --------------------------------------------------
# 12. Submatrix
# --------------------------------------------------
print("\narr2d[0:2,1:3]")
print("Rows 0-1 and Columns 1-2")
print(arr2d[0:2, 1:3])

# --------------------------------------------------
# 13. Last Two Rows
# --------------------------------------------------
print("\narr2d[-2:,:]")
print("Last two rows")
print(arr2d[-2:, :])

# --------------------------------------------------
# 14. Every Alternate Column
# --------------------------------------------------
print("\narr2d[:,::2]")
print("All rows, alternate columns")
print(arr2d[:, ::2])

# --------------------------------------------------
# 15. Modify Using Slicing
# --------------------------------------------------
print("\nBefore Modification:")
print(arr)

arr[2:5] = 100

print("After arr[2:5] = 100")
print(arr)

# --------------------------------------------------
# 16. Copy vs View
# --------------------------------------------------
print("\nCopy vs View Example")

original = np.array([1, 2, 3, 4, 5])

view = original[1:4]      # View
view[0] = 999

print("Original after modifying view:")
print(original)

copy = original[1:4].copy()
copy[0] = 555

print("Original after modifying copy:")
print(original)

print("\nModified Copy:")
print(copy)

print("\nProgram Completed Successfully!")