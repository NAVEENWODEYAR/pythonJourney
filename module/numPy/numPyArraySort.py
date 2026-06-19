"""
=========================================================
NUMPY ARRAY SORTING - COMPLETE EXPLANATION PROGRAM
=========================================================

Definition:
-----------
NumPy sorting is the process of arranging array elements
in ascending or descending order.

NumPy provides the sort() function to sort arrays quickly
and efficiently.

Syntax:
--------
numpy.sort(array, axis=-1)

Parameters:
------------
array : Input NumPy array
axis  : Axis along which to sort
        axis=-1 -> sort last axis (default)
        axis=0  -> sort column-wise
        axis=1  -> sort row-wise

Returns:
---------
A sorted copy of the array.

Real-World Uses:
----------------
1. Ranking student marks.
2. Sorting sales data.
3. Organizing customer records.
4. Data analysis and machine learning preprocessing.
5. Finding minimum and maximum values efficiently.
"""

# Import NumPy library
import numpy as np

print("=" * 60)
print("NUMPY ARRAY SORTING TUTORIAL")
print("=" * 60)

# ---------------------------------------------------------
# BASIC ARRAY CREATION
# ---------------------------------------------------------
print("\n1. Creating a NumPy Array")

arr = np.array([50, 10, 40, 20, 30])

print("Original Array:")
print(arr)

# ---------------------------------------------------------
# BASIC SORTING
# ---------------------------------------------------------
print("\n2. Sorting an Array")

sorted_arr = np.sort(arr)

print("Sorted Array (Ascending Order):")
print(sorted_arr)

# Original array remains unchanged
print("Original Array After Sorting:")
print(arr)

# ---------------------------------------------------------
# DESCENDING SORT
# ---------------------------------------------------------
print("\n3. Sorting in Descending Order")

descending_arr = np.sort(arr)[::-1]

print("Descending Order:")
print(descending_arr)

# ---------------------------------------------------------
# SORTING FLOAT VALUES
# ---------------------------------------------------------
print("\n4. Sorting Floating Point Numbers")

float_arr = np.array([3.5, 1.2, 5.8, 2.1])

print("Original Float Array:")
print(float_arr)

print("Sorted Float Array:")
print(np.sort(float_arr))

# ---------------------------------------------------------
# SORTING STRING VALUES
# ---------------------------------------------------------
print("\n5. Sorting Strings")

names = np.array(["John", "Alice", "David", "Bob"])

print("Original Names:")
print(names)

print("Sorted Names:")
print(np.sort(names))

# ---------------------------------------------------------
# 2D ARRAY SORTING
# ---------------------------------------------------------
print("\n6. Sorting a 2D Array")

matrix = np.array([
    [30, 10, 20],
    [90, 50, 70]
])

print("Original Matrix:")
print(matrix)

# Sort row-wise
print("\nRow-wise Sorting (axis=1):")
print(np.sort(matrix, axis=1))

# Sort column-wise
print("\nColumn-wise Sorting (axis=0):")
print(np.sort(matrix, axis=0))

# ---------------------------------------------------------
# USING argsort()
# ---------------------------------------------------------
print("\n7. Using argsort()")

scores = np.array([85, 60, 95, 70])

print("Scores:")
print(scores)

indices = np.argsort(scores)

print("Indices After Sorting:")
print(indices)

print("Sorted Scores Using Indices:")
print(scores[indices])

# ---------------------------------------------------------
# REAL-WORLD EXAMPLE:
# STUDENT MARKS RANKING SYSTEM
# ---------------------------------------------------------
print("\n8. REAL-WORLD USE CASE: Student Ranking")

student_names = np.array([
    "Rahul",
    "Priya",
    "Amit",
    "Sneha",
    "Kiran"
])

marks = np.array([78, 95, 67, 88, 72])

print("\nStudent Marks:")
for name, mark in zip(student_names, marks):
    print(f"{name:10s} : {mark}")

# Get descending order indices
rank_indices = np.argsort(marks)[::-1]

print("\nStudents Ranked by Marks:")
print("-" * 30)

rank = 1
for i in rank_indices:
    print(
        f"Rank {rank}: "
        f"{student_names[i]:10s} "
        f"Marks = {marks[i]}"
    )
    rank += 1

# ---------------------------------------------------------
# FINDING MINIMUM AND MAXIMUM USING SORTING
# ---------------------------------------------------------
print("\n9. Finding Minimum and Maximum Values")

sorted_marks = np.sort(marks)

minimum = sorted_marks[0]
maximum = sorted_marks[-1]

print("Minimum Marks:", minimum)
print("Maximum Marks:", maximum)

# ---------------------------------------------------------
# SUMMARY
# ---------------------------------------------------------
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
1. np.sort(array)
   -> Sorts array in ascending order.

2. np.sort(array)[::-1]
   -> Sorts array in descending order.

3. np.sort(array, axis=0)
   -> Column-wise sorting.

4. np.sort(array, axis=1)
   -> Row-wise sorting.

5. np.argsort(array)
   -> Returns indices that would sort the array.

Real Applications:
- Student ranking systems
- Sales report analysis
- Data preprocessing
- Machine learning datasets
- Customer record organization
""")

print("\nProgram Completed Successfully!")