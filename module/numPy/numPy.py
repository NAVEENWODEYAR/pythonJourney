"""
=========================================================
NUMPY BASICS - COMPLETE BEGINNER GUIDE
=========================================================

Definition:
NumPy (Numerical Python) is a powerful Python library
used for numerical computing, mathematical operations,
scientific calculations, and data analysis.

Why use NumPy?
--------------
1. Faster than Python lists
2. Uses less memory
3. Supports multi-dimensional arrays
4. Provides mathematical and statistical functions
5. Widely used in Data Science, AI, Machine Learning,
   Scientific Computing, Finance, and Engineering

Installation:
-------------
pip install numpy

Import Syntax:
--------------
import numpy as np

Real World Applications:
------------------------
1. Machine Learning
2. Data Analysis
3. Image Processing
4. Financial Forecasting
5. Scientific Simulations
6. Robotics
7. Weather Prediction
"""

# Import NumPy
import numpy as np

print("\n========== NUMPY INTRODUCTION ==========\n")

# ---------------------------------------------------
# 1. Creating NumPy Arrays
# ---------------------------------------------------
print("1. Creating Arrays")

# Python List
python_list = [10, 20, 30, 40]

# Convert list to NumPy Array
arr = np.array(python_list)

print("Python List:", python_list)
print("NumPy Array:", arr)

"""
Syntax:
np.array(iterable)

iterable can be:
- list
- tuple
- nested list
"""

# ---------------------------------------------------
# 2. Array Properties
# ---------------------------------------------------
print("\n2. Array Properties")

arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])

print("Array:\n", arr2)

print("Shape:", arr2.shape)
print("Dimensions:", arr2.ndim)
print("Data Type:", arr2.dtype)
print("Size:", arr2.size)

"""
shape  -> rows and columns
ndim   -> number of dimensions
dtype  -> data type
size   -> total elements
"""

# ---------------------------------------------------
# 3. Special Arrays
# ---------------------------------------------------
print("\n3. Special Arrays")

zeros = np.zeros((2, 3))
ones = np.ones((2, 3))
identity = np.eye(3)

print("Zeros Array:\n", zeros)
print("Ones Array:\n", ones)
print("Identity Matrix:\n", identity)

"""
Useful in:
- Machine Learning
- Matrix calculations
- Data initialization
"""

# ---------------------------------------------------
# 4. Creating Range of Values
# ---------------------------------------------------
print("\n4. Creating Range of Values")

a = np.arange(1, 11, 2)

print("arange(1,11,2):", a)

# evenly spaced numbers
b = np.linspace(0, 10, 5)

print("linspace(0,10,5):", b)

"""
arange(start, stop, step)
linspace(start, stop, number_of_values)
"""

# ---------------------------------------------------
# 5. Array Indexing
# ---------------------------------------------------
print("\n5. Array Indexing")

arr = np.array([100, 200, 300, 400, 500])

print("First Element:", arr[0])
print("Last Element:", arr[-1])

# slicing
print("Elements 1 to 3:", arr[1:4])

"""
Indexing works similar to Python lists
"""

# ---------------------------------------------------
# 6. Mathematical Operations
# ---------------------------------------------------
print("\n6. Mathematical Operations")

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print("x =", x)
print("y =", y)

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)

"""
NumPy performs element-wise operations
"""

# ---------------------------------------------------
# 7. Statistical Functions
# ---------------------------------------------------
print("\n7. Statistical Functions")

data = np.array([10, 20, 30, 40, 50])

print("Data:", data)

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Maximum:", np.max(data))
print("Minimum:", np.min(data))
print("Sum:", np.sum(data))
print("Standard Deviation:", np.std(data))

"""
Used in:
- Data Analytics
- Business Intelligence
- Machine Learning
"""

# ---------------------------------------------------
# 8. Reshaping Arrays
# ---------------------------------------------------
print("\n8. Reshaping Arrays")

numbers = np.arange(1, 13)

matrix = numbers.reshape(3, 4)

print("Original:", numbers)
print("Reshaped Matrix:\n", matrix)

"""
reshape(rows, columns)

Very useful for:
- Image Processing
- Machine Learning datasets
"""

# ---------------------------------------------------
# 9. Random Numbers
# ---------------------------------------------------
print("\n9. Random Numbers")

random_numbers = np.random.randint(1, 100, size=5)

print("Random Numbers:", random_numbers)

"""
Used in:
- Simulations
- Machine Learning
- Testing
"""

# ---------------------------------------------------
# 10. Matrix Operations
# ---------------------------------------------------
print("\n10. Matrix Operations")

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

# Matrix multiplication
result = np.dot(A, B)

print("Matrix Multiplication:\n", result)

"""
Used in:
- Artificial Intelligence
- Computer Graphics
- Engineering
"""

# ---------------------------------------------------
# 11. Real World Example - Student Marks Analysis
# ---------------------------------------------------
print("\n11. Real World Example: Student Marks")

marks = np.array([78, 85, 92, 67, 88])

print("Student Marks:", marks)

print("Average Marks:", np.mean(marks))
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))

# Students scoring above 80
top_students = marks[marks > 80]

print("Marks Above 80:", top_students)

"""
Real-world use:
School Management Systems
Performance Analysis
Educational Analytics
"""

# ---------------------------------------------------
# 12. Real World Example - Sales Analysis
# ---------------------------------------------------
print("\n12. Real World Example: Sales Analysis")

sales = np.array([12000, 15000, 18000, 21000, 25000])

print("Monthly Sales:", sales)

growth = sales[1:] - sales[:-1]

print("Month-to-Month Growth:", growth)

print("Average Sales:", np.mean(sales))

"""
Used in:
- Business Reporting
- Financial Analysis
- Sales Forecasting
"""

# ---------------------------------------------------
# Summary
# ---------------------------------------------------
print("\n========== SUMMARY ==========")

print("""
NumPy Key Concepts:
------------------
1. np.array()      -> Create arrays
2. np.zeros()      -> Create zero-filled arrays
3. np.ones()       -> Create one-filled arrays
4. np.arange()     -> Range of values
5. np.linspace()   -> Evenly spaced values
6. reshape()       -> Change dimensions
7. mean(), sum()   -> Statistics
8. dot()           -> Matrix multiplication
9. random          -> Random number generation

NumPy is the foundation for:
- Pandas
- Scikit-Learn
- TensorFlow
- PyTorch
- Data Science
- Machine Learning
""")