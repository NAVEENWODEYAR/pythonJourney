# Sample Program: Creating a User Defined UFunc in NumPy

import numpy as np

# Step 1: Define a normal Python function
def square(x):
    return x * x

# Step 2: Convert the function into a NumPy ufunc
square_ufunc = np.frompyfunc(square, 1, 1)

# Step 3: Create a NumPy array
numbers = np.array([2, 4, 6, 8, 10])

# Step 4: Apply the ufunc to the array
result = square_ufunc(numbers)

# Step 5: Display the results
print("Original Array :", numbers)
print("Squared Array  :", result)