"""
------------------------------------------------------------
                ARRAYS IN PYTHON
------------------------------------------------------------

Introduction:
An array is a data structure used to store multiple values
of the same type in a single variable. Since Python does not
have a built-in array data type like some programming languages,
lists are commonly used as arrays because they are flexible and
easy to use.

Definition:
An array is a collection of elements stored in contiguous
locations and accessed using an index. In Python, lists are
used to represent arrays for most applications.

Uses of Arrays:
1. Store multiple values in a single variable.
2. Access elements quickly using indexes.
3. Perform searching and sorting operations.
4. Store marks, salaries, temperatures, etc.
5. Reduce the need for multiple variables.

------------------------------------------------------------
                PYTHON PROGRAM
------------------------------------------------------------
"""

# Creating an array (list)
numbers = [10, 20, 30, 40, 50]

# Display the complete array
print("Original Array:")
print(numbers)

# Accessing elements using index
print("\nAccessing Elements:")
print("First element :", numbers[0])
print("Third element :", numbers[2])

# Updating an element
numbers[1] = 25
print("\nArray after updating second element:")
print(numbers)

# Adding a new element
numbers.append(60)
print("\nArray after adding an element:")
print(numbers)

# Removing an element
numbers.remove(40)
print("\nArray after removing 40:")
print(numbers)

# Finding the length of the array
print("\nNumber of elements in the array:", len(numbers))

# Traversing the array using a loop
print("\nTraversing the array:")
for item in numbers:
    print(item)

# Calculating the sum of elements
total = sum(numbers)
print("\nSum of all elements:", total)

# Finding the largest and smallest elements
print("Largest element :", max(numbers))
print("Smallest element:", min(numbers))

# Searching for an element
search = 30
if search in numbers:
    print(f"\n{search} is present in the array.")
else:
    print(f"\n{search} is not present in the array.")

# Sorting the array
numbers.sort()
print("\nSorted Array:")
print(numbers)

"""
------------------------------------------------------------
Output (Example)

Original Array:
[10, 20, 30, 40, 50]

Accessing Elements:
First element : 10
Third element : 30

Array after updating second element:
[10, 25, 30, 40, 50]

Array after adding an element:
[10, 25, 30, 40, 50, 60]

Array after removing 40:
[10, 25, 30, 50, 60]

Number of elements in the array: 5

Traversing the array:
10
25
30
50
60

Sum of all elements: 175
Largest element : 60
Smallest element: 10

30 is present in the array.

Sorted Array:
[10, 25, 30, 50, 60]
------------------------------------------------------------
"""