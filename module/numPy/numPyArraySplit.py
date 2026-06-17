# ---------------------------------------------------------
# Program: Split a NumPy Array into N Parts
# Author : Example
# Purpose: Demonstrate the use of numpy.array_split()
# ---------------------------------------------------------

# Step 1: Import NumPy library
import numpy as np

# Step 2: Create an array
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# Step 3: Display the original array
print("Original Array:")
print(arr)

# Step 4: Specify the number of parts
n = 3

# Step 5: Split the array into n parts
parts = np.array_split(arr, n)

# Step 6: Display the split arrays
print("\nArray after splitting into", n, "parts:")

for i, part in enumerate(parts, start=1):
    print(f"\nPart {i}:")
    print(part)

# Step 7: Display size of each part
print("\nInformation about each split:")

for i, part in enumerate(parts, start=1):
    print(f"Part {i} contains {len(part)} elements")