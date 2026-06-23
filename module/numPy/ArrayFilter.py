"""
===========================================================
NUMPY ARRAY FILTERING - COMPLETE GUIDE
===========================================================

Definition:
-----------
Array filtering in NumPy is the process of selecting elements
from an array that satisfy a specific condition.

Filtering is performed using a Boolean Mask.

Boolean Mask:
-------------
A Boolean mask is an array of True and False values having
the same shape as the original array.

- True  -> Element is selected.
- False -> Element is ignored.

Syntax:
--------
filtered_array = array[condition]

or

mask = array > value
filtered_array = array[mask]

How It Works:
-------------
1. Create a condition.
2. NumPy evaluates the condition for each element.
3. A Boolean array is generated.
4. Elements corresponding to True are returned.

Common Operators Used:
----------------------
>   Greater than
<   Less than
>=  Greater than or equal to
<=  Less than or equal to
==  Equal to
!=  Not equal to

Logical Operators:
------------------
&   AND
|   OR
~   NOT

Important:
-----------
When using multiple conditions, always surround each
condition with parentheses.

Correct:
(arr > 10) & (arr < 50)

Wrong:
arr > 10 & arr < 50

===========================================================
"""

import numpy as np

print("=" * 60)
print("NUMPY ARRAY FILTERING DEMONSTRATION")
print("=" * 60)

# ---------------------------------------------------------
# Example 1: Create an array
# ---------------------------------------------------------
arr = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50])

print("\nOriginal Array:")
print(arr)

# ---------------------------------------------------------
# Example 2: Filter elements greater than 30
# ---------------------------------------------------------
print("\nExample 2: Elements Greater Than 30")

mask = arr > 30

print("Boolean Mask:")
print(mask)

filtered = arr[mask]

print("Filtered Result:")
print(filtered)

# Shortcut version
print("Shortcut Syntax:")
print(arr[arr > 30])

# ---------------------------------------------------------
# Example 3: Filter elements less than 25
# ---------------------------------------------------------
print("\nExample 3: Elements Less Than 25")

filtered = arr[arr < 25]

print(filtered)

# ---------------------------------------------------------
# Example 4: Filter elements equal to 30
# ---------------------------------------------------------
print("\nExample 4: Elements Equal To 30")

filtered = arr[arr == 30]

print(filtered)

# ---------------------------------------------------------
# Example 5: Filter elements not equal to 30
# ---------------------------------------------------------
print("\nExample 5: Elements Not Equal To 30")

filtered = arr[arr != 30]

print(filtered)

# ---------------------------------------------------------
# Example 6: Multiple Conditions using AND (&)
# ---------------------------------------------------------
print("\nExample 6: Values Between 20 and 45")

filtered = arr[(arr > 20) & (arr < 45)]

print(filtered)

# ---------------------------------------------------------
# Example 7: Multiple Conditions using OR (|)
# ---------------------------------------------------------
print("\nExample 7: Values Less Than 20 OR Greater Than 40")

filtered = arr[(arr < 20) | (arr > 40)]

print(filtered)

# ---------------------------------------------------------
# Example 8: Using NOT (~)
# ---------------------------------------------------------
print("\nExample 8: Exclude Values Greater Than 30")

filtered = arr[~(arr > 30)]

print(filtered)

# ---------------------------------------------------------
# Example 9: Filter Even Numbers
# ---------------------------------------------------------
print("\nExample 9: Even Numbers")

filtered = arr[arr % 2 == 0]

print(filtered)

# ---------------------------------------------------------
# Example 10: Filter Odd Numbers
# ---------------------------------------------------------
print("\nExample 10: Odd Numbers")

filtered = arr[arr % 2 != 0]

print(filtered)

# ---------------------------------------------------------
# Example 11: Filtering Strings
# ---------------------------------------------------------
print("\nExample 11: String Filtering")

names = np.array([
    "John",
    "Alice",
    "Bob",
    "David",
    "Alice"
])

print("Original Names:")
print(names)

filtered_names = names[names == "Alice"]

print("Names Equal To 'Alice':")
print(filtered_names)

# ---------------------------------------------------------
# Example 12: Filtering a 2D Array
# ---------------------------------------------------------
print("\nExample 12: Filtering a 2D Array")

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Original Matrix:")
print(matrix)

filtered = matrix[matrix > 50]

print("Elements Greater Than 50:")
print(filtered)

# ---------------------------------------------------------
# Example 13: Count Filtered Elements
# ---------------------------------------------------------
print("\nExample 13: Count Elements Greater Than 30")

count = np.sum(arr > 30)

print("Count =", count)

# ---------------------------------------------------------
# Example 14: Get Index Positions
# ---------------------------------------------------------
print("\nExample 14: Index Positions of Elements > 30")

indices = np.where(arr > 30)

print(indices)

# ---------------------------------------------------------
# Example 15: Real-World Example
# ---------------------------------------------------------
print("\nExample 15: Student Marks Filtering")

marks = np.array([35, 78, 90, 45, 67, 29, 88])

print("Student Marks:")
print(marks)

# Students who passed (>=40)
passed = marks[marks >= 40]

print("Passed Students Marks:")
print(passed)

# Distinction (>=75)
distinction = marks[marks >= 75]

print("Distinction Marks:")
print(distinction)

# ---------------------------------------------------------
# Summary
# ---------------------------------------------------------
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
1. Array filtering selects elements based on conditions.
2. Filtering uses Boolean masks (True/False arrays).
3. Syntax:
      result = array[condition]

4. Common operators:
      >, <, >=, <=, ==, !=

5. Multiple conditions:
      AND -> &
      OR  -> |
      NOT -> ~

6. Useful patterns:
      arr[arr > 10]
      arr[arr % 2 == 0]
      arr[(arr > 10) & (arr < 50)]

7. Filtering works with:
      - 1D arrays
      - 2D arrays
      - String arrays
      - Numerical arrays

Array filtering is one of the most powerful features of NumPy
for data analysis, machine learning, and scientific computing.
""")