"""
===========================================================
                NUMPY COMPLETE OVERVIEW
===========================================================

What is NumPy?
--------------
NumPy (Numerical Python) is an open-source Python library
used for numerical computing.

It provides:
1. Fast multidimensional arrays
2. Mathematical operations
3. Linear algebra functions
4. Statistical functions
5. Random number generation
6. Data manipulation tools

Why NumPy?
-----------
Python lists are flexible but slower for numerical
computations.

NumPy arrays:
✓ Faster
✓ Less memory usage
✓ Vectorized operations
✓ Suitable for scientific computing
✓ Foundation for Pandas, SciPy, Scikit-Learn, TensorFlow

Installation:
-------------
pip install numpy

Import Statement:
-----------------
import numpy as np

===========================================================
"""

import numpy as np

print("=" * 60)
print("NUMPY COMPLETE DEMONSTRATION")
print("=" * 60)

# =========================================================
# 1. Creating Arrays
# =========================================================

print("\n1. ARRAY CREATION")

# 1D Array
arr1 = np.array([10, 20, 30, 40])

print("1D Array:")
print(arr1)

# 2D Array
arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\n2D Array:")
print(arr2)

# =========================================================
# 2. Array Attributes
# =========================================================

print("\n2. ARRAY ATTRIBUTES")

print("Shape :", arr2.shape)
print("Dimensions :", arr2.ndim)
print("Size :", arr2.size)
print("Data Type :", arr2.dtype)

# =========================================================
# 3. Special Array Creation Functions
# =========================================================

print("\n3. SPECIAL ARRAYS")

print("\nZeros Array:")
print(np.zeros((2, 3)))

print("\nOnes Array:")
print(np.ones((2, 3)))

print("\nIdentity Matrix:")
print(np.eye(3))

print("\nRange Array:")
print(np.arange(1, 11))

print("\nLinspace Array:")
print(np.linspace(0, 100, 5))

# =========================================================
# 4. Indexing and Slicing
# =========================================================

print("\n4. INDEXING AND SLICING")

arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)

print("First Element:", arr[0])
print("Last Element:", arr[-1])

print("Slice [1:4]:", arr[1:4])

# =========================================================
# 5. Mathematical Operations
# =========================================================

print("\n5. MATHEMATICAL OPERATIONS")

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("A =", a)
print("B =", b)

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# =========================================================
# 6. Statistical Functions
# =========================================================

print("\n6. STATISTICAL FUNCTIONS")

data = np.array([10, 20, 30, 40, 50])

print("Data:", data)

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Maximum:", np.max(data))
print("Minimum:", np.min(data))
print("Standard Deviation:", np.std(data))
print("Variance:", np.var(data))
print("Sum:", np.sum(data))

# =========================================================
# 7. Reshaping Arrays
# =========================================================

print("\n7. RESHAPING")

arr = np.arange(1, 13)

print("Original:")
print(arr)

reshaped = arr.reshape(3, 4)

print("\nReshaped (3x4):")
print(reshaped)

# =========================================================
# 8. Filtering Arrays
# =========================================================

print("\n8. FILTERING")

numbers = np.array([10, 15, 20, 25, 30, 35])

filtered = numbers[numbers > 20]

print("Numbers > 20:")
print(filtered)

# =========================================================
# 9. Sorting
# =========================================================

print("\n9. SORTING")

arr = np.array([50, 10, 40, 20, 30])

print("Original:", arr)

print("Sorted:", np.sort(arr))

# =========================================================
# 10. Joining Arrays
# =========================================================

print("\n10. CONCATENATION")

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

joined = np.concatenate((a, b))

print(joined)

# =========================================================
# 11. Splitting Arrays
# =========================================================

print("\n11. SPLITTING")

arr = np.array([1, 2, 3, 4, 5, 6])

parts = np.array_split(arr, 3)

print(parts)

# =========================================================
# 12. Random Numbers
# =========================================================

print("\n12. RANDOM NUMBERS")

print("Random Integer:")
print(np.random.randint(1, 100, 5))

print("Random Float:")
print(np.random.rand(5))

# =========================================================
# 13. Linear Algebra
# =========================================================

print("\n13. LINEAR ALGEBRA")

matrix = np.array([
    [1, 2],
    [3, 4]
])

print("Matrix:")
print(matrix)

print("Transpose:")
print(matrix.T)

print("Determinant:")
print(np.linalg.det(matrix))

# =========================================================
# 14. Universal Functions (ufuncs)
# =========================================================

print("\n14. UNIVERSAL FUNCTIONS")

angles = np.array([0, 30, 45, 60, 90])

radians = np.radians(angles)

print("Sin:")
print(np.sin(radians))

print("Cos:")
print(np.cos(radians))

print("Square Root:")
print(np.sqrt([4, 9, 16, 25]))

# =========================================================
# 15. Practical Example
# =========================================================

print("\n15. STUDENT MARKS ANALYSIS")

marks = np.array([78, 90, 65, 88, 45, 70])

print("Marks:", marks)

print("Average:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))

print("Passed Students:")
print(marks[marks >= 50])

# =========================================================
# USES OF NUMPY
# =========================================================

print("\n" + "=" * 60)
print("USES OF NUMPY")
print("=" * 60)

uses = [
    "Scientific Computing",
    "Data Analysis",
    "Machine Learning",
    "Artificial Intelligence",
    "Deep Learning",
    "Image Processing",
    "Signal Processing",
    "Statistical Analysis",
    "Financial Modeling",
    "Simulation and Research",
    "Computer Vision",
    "Big Data Processing"
]

for i, use in enumerate(uses, start=1):
    print(f"{i}. {use}")

# =========================================================
# ADVANTAGES
# =========================================================

print("\n" + "=" * 60)
print("ADVANTAGES OF NUMPY")
print("=" * 60)

advantages = [
    "High Performance",
    "Memory Efficient",
    "Supports Multidimensional Arrays",
    "Vectorized Operations",
    "Powerful Mathematical Functions",
    "Easy Integration with Other Libraries",
    "Widely Used in Industry and Research"
]

for i, adv in enumerate(advantages, start=1):
    print(f"{i}. {adv}")

# =========================================================
# SUMMARY
# =========================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
NumPy is the core numerical computing library in Python.

Key Concepts:
-------------
1. ndarray (NumPy Array)
2. Array Creation
3. Indexing & Slicing
4. Mathematical Operations
5. Statistical Functions
6. Filtering
7. Sorting
8. Reshaping
9. Random Number Generation
10. Linear Algebra

Major Applications:
-------------------
• Data Science
• Machine Learning
• Artificial Intelligence
• Scientific Research
• Engineering Simulations
• Financial Analytics

NumPy is the foundation of:
- Pandas
- SciPy
- Scikit-Learn
- TensorFlow
- PyTorch

Learning NumPy is essential for modern Python
data science and scientific computing.
""")