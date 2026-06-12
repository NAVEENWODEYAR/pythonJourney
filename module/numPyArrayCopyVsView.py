import numpy as np

print("=" * 50)
print("NUMPY COPY VS VIEW DEMONSTRATION")
print("=" * 50)

# Original Array
arr = np.array([10, 20, 30, 40, 50])

print("\nOriginal Array:")
print(arr)

# --------------------------------------------------
# VIEW
# --------------------------------------------------
print("\n1. VIEW EXAMPLE")

view_arr = arr[1:4]  # Creates a view

print("View Array:", view_arr)

# Modify view
view_arr[0] = 999

print("\nAfter modifying view_arr[0] = 999")
print("Original Array:", arr)
print("View Array:", view_arr)

print("\nExplanation:")
print("A view shares the same memory as the original array.")
print("Changing the view also changes the original array.")

# --------------------------------------------------
# COPY
# --------------------------------------------------
print("\n" + "=" * 50)
print("2. COPY EXAMPLE")

arr2 = np.array([10, 20, 30, 40, 50])

copy_arr = arr2[1:4].copy()  # Creates a copy

print("Copy Array:", copy_arr)

# Modify copy
copy_arr[0] = 888

print("\nAfter modifying copy_arr[0] = 888")
print("Original Array:", arr2)
print("Copy Array:", copy_arr)

print("\nExplanation:")
print("A copy creates a separate memory location.")
print("Changing the copy does NOT affect the original array.")

# --------------------------------------------------
# CHECK USING .base
# --------------------------------------------------
print("\n" + "=" * 50)
print("3. CHECK MEMORY OWNERSHIP")

print("view_arr.base is arr  :", view_arr.base is arr)
print("copy_arr.base is arr2 :", copy_arr.base is arr2)

print("\nInterpretation:")
print("True  -> Shares memory (View)")
print("False -> Separate memory (Copy)")

print("\n" + "=" * 50)
print("SUMMARY")
print("=" * 50)
print("View  : Shares memory with original array.")
print("Copy  : Creates independent array.")
print("View  : Changes affect original.")
print("Copy  : Changes do not affect original.")