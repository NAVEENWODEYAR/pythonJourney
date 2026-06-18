"""
=========================================================
NUMPY ARRAY SEARCHING - COMPLETE EXPLANATION PROGRAM
=========================================================

Definition:
-----------
Array searching in NumPy refers to finding specific values,
positions (indices), conditions, minimum/maximum values,
or matching elements within a NumPy array.

Why Array Searching is Important?
---------------------------------
Searching helps us:
1. Locate specific data quickly.
2. Filter records based on conditions.
3. Find minimum and maximum values.
4. Retrieve positions of matching elements.
5. Perform data analysis and machine learning preprocessing.

Common NumPy Search Functions:
------------------------------
1. np.where()      -> Find indices based on a condition.
2. np.searchsorted() -> Find insertion position in sorted arrays.
3. np.argmax()     -> Find index of maximum value.
4. np.argmin()     -> Find index of minimum value.
5. np.nonzero()    -> Find non-zero element indices.

Real-World Use Cases:
---------------------
1. Finding students who scored above a threshold.
2. Identifying defective products in manufacturing.
3. Detecting anomalies in sensor data.
4. Searching customer records in datasets.
5. Data filtering before machine learning training.

=========================================================
"""

import numpy as np

# -------------------------------------------------------
# STEP 1: Create a NumPy Array
# -------------------------------------------------------
print("\n========== Original Array ==========")

arr = np.array([10, 25, 30, 45, 50, 65, 70, 85, 90])

print("Array:", arr)

# -------------------------------------------------------
# SEARCH 1: Search for elements greater than 50
# Using np.where()
# -------------------------------------------------------
print("\n========== Search Using np.where() ==========")

# Returns indices where condition is True
indices = np.where(arr > 50)

print("Indices of elements > 50:", indices)
print("Elements > 50:", arr[indices])

# Explanation:
# np.where(condition) returns index positions
# where the condition becomes True.


# -------------------------------------------------------
# SEARCH 2: Find Exact Value Position
# -------------------------------------------------------
print("\n========== Search Exact Value ==========")

value_to_search = 65

position = np.where(arr == value_to_search)

print(f"Position of {value_to_search}:", position)

# Check if value exists
if len(position[0]) > 0:
    print(f"{value_to_search} found at index {position[0][0]}")
else:
    print(f"{value_to_search} not found")


# -------------------------------------------------------
# SEARCH 3: Find Maximum Value Index
# Using np.argmax()
# -------------------------------------------------------
print("\n========== Search Maximum Value ==========")

max_index = np.argmax(arr)

print("Maximum value:", arr[max_index])
print("Index of maximum value:", max_index)

# Explanation:
# argmax() returns the index of the largest element.


# -------------------------------------------------------
# SEARCH 4: Find Minimum Value Index
# Using np.argmin()
# -------------------------------------------------------
print("\n========== Search Minimum Value ==========")

min_index = np.argmin(arr)

print("Minimum value:", arr[min_index])
print("Index of minimum value:", min_index)

# Explanation:
# argmin() returns the index of the smallest element.


# -------------------------------------------------------
# SEARCH 5: Search Insertion Position
# Using np.searchsorted()
# -------------------------------------------------------
print("\n========== Search Sorted Position ==========")

new_value = 55

insert_position = np.searchsorted(arr, new_value)

print(f"Position to insert {new_value}:", insert_position)

# Explanation:
# searchsorted() finds the position where a value
# should be inserted to maintain sorted order.


# -------------------------------------------------------
# SEARCH 6: Find Non-Zero Elements
# Using np.nonzero()
# -------------------------------------------------------
print("\n========== Search Non-Zero Elements ==========")

arr2 = np.array([0, 5, 0, 8, 10, 0, 15])

print("Array:", arr2)

non_zero_indices = np.nonzero(arr2)

print("Non-zero indices:", non_zero_indices)
print("Non-zero values:", arr2[non_zero_indices])

# Explanation:
# nonzero() returns indices of all non-zero elements.


# -------------------------------------------------------
# SEARCH 7: Multiple Condition Search
# -------------------------------------------------------
print("\n========== Search with Multiple Conditions ==========")

result = np.where((arr > 30) & (arr < 80))

print("Indices:", result)
print("Values between 30 and 80:", arr[result])

# Explanation:
# '&' means logical AND.
# Both conditions must be True.


# -------------------------------------------------------
# PRACTICAL USE CASE:
# Student Marks Analysis
# -------------------------------------------------------
print("\n========== Real-World Use Case ==========")

marks = np.array([45, 78, 92, 33, 88, 55, 99, 67])

print("Student Marks:", marks)

# Find students scoring above 75
top_students = np.where(marks > 75)

print("Indices of students scoring > 75:", top_students)
print("Marks of top students:", marks[top_students])

# Highest scorer
highest_index = np.argmax(marks)

print("\nHighest Score:", marks[highest_index])
print("Top Student Index:", highest_index)

# Lowest scorer
lowest_index = np.argmin(marks)

print("Lowest Score:", marks[lowest_index])
print("Lowest Student Index:", lowest_index)


# -------------------------------------------------------
# SUMMARY
# -------------------------------------------------------
print("\n========== SUMMARY ==========")

print("""
NumPy Search Functions:

1. np.where(condition)
   -> Finds indices matching a condition.

2. np.searchsorted(array, value)
   -> Finds insertion position in sorted arrays.

3. np.argmax(array)
   -> Finds index of maximum value.

4. np.argmin(array)
   -> Finds index of minimum value.

5. np.nonzero(array)
   -> Finds indices of non-zero elements.

These functions are widely used in:
- Data Science
- Machine Learning
- Data Analysis
- Scientific Computing
- Business Analytics
""")