"""
Python Lists - Complete Demonstration
-------------------------------------
A list is a collection data type in Python.
Lists are:
1. Ordered
2. Mutable (can be changed)
3. Allow duplicate values
4. Can store different data types

This program demonstrates:
- Creating lists
- Accessing elements
- Updating elements
- All important list methods
- Operators
- Looping
- List functions
"""

# --------------------------------------------------
# CREATING A LIST
# --------------------------------------------------

fruits = ["apple", "banana", "mango", "orange"]

print("Original List:")
print(fruits)


# --------------------------------------------------
# ACCESSING ELEMENTS
# --------------------------------------------------

print("\nAccessing Elements")

# First element
print("First element:", fruits[0])

# Last element
print("Last element:", fruits[-1])

# Slicing
print("First 2 elements:", fruits[:2])


# --------------------------------------------------
# UPDATING ELEMENTS
# --------------------------------------------------

print("\nUpdating Elements")

fruits[1] = "grapes"
print("Updated list:", fruits)


# --------------------------------------------------
# LIST METHODS
# --------------------------------------------------

# 1. append()
# Adds one item at the end

print("\n1. append()")

fruits.append("kiwi")
print(fruits)


# --------------------------------------------------

# 2. extend()
# Adds multiple items to the list

print("\n2. extend()")

fruits.extend(["papaya", "pineapple"])
print(fruits)


# --------------------------------------------------

# 3. insert()
# Inserts an element at a specific position

print("\n3. insert()")

fruits.insert(1, "watermelon")
print(fruits)


# --------------------------------------------------

# 4. remove()
# Removes first matching element

print("\n4. remove()")

fruits.remove("mango")
print(fruits)


# --------------------------------------------------

# 5. pop()
# Removes element using index
# If no index is given, removes last item

print("\n5. pop()")

removed_item = fruits.pop()
print("Removed item:", removed_item)
print(fruits)

# Remove item at index 2
removed_item = fruits.pop(2)
print("Removed item at index 2:", removed_item)
print(fruits)


# --------------------------------------------------

# 6. clear()
# Removes all elements from list

print("\n6. clear()")

temp_list = [1, 2, 3]
temp_list.clear()
print(temp_list)


# --------------------------------------------------

# 7. index()
# Returns index position of an element

print("\n7. index()")

print("Index of apple:", fruits.index("apple"))


# --------------------------------------------------

# 8. count()
# Counts number of occurrences

print("\n8. count()")

numbers = [1, 2, 2, 3, 2, 4]

print("Count of 2:", numbers.count(2))


# --------------------------------------------------

# 9. sort()
# Sorts list in ascending order

print("\n9. sort()")

numbers.sort()
print(numbers)

# Descending order
numbers.sort(reverse=True)
print("Descending:", numbers)


# --------------------------------------------------

# 10. reverse()
# Reverses the list order

print("\n10. reverse()")

numbers.reverse()
print(numbers)


# --------------------------------------------------

# 11. copy()
# Creates a copy of the list

print("\n11. copy()")

new_numbers = numbers.copy()

print("Copied list:", new_numbers)


# --------------------------------------------------
# LIST OPERATORS
# --------------------------------------------------

print("\nLIST OPERATORS")

# Concatenation (+)
list1 = [1, 2]
list2 = [3, 4]

print("Concatenation:", list1 + list2)

# Repetition (*)
print("Repetition:", list1 * 3)

# Membership operator
print("Is apple in fruits?", "apple" in fruits)


# --------------------------------------------------
# LOOPING THROUGH LIST
# --------------------------------------------------

print("\nLOOPING THROUGH LIST")

for item in fruits:
    print(item)

# Using index
print("\nUsing index")

for i in range(len(fruits)):
    print(i, fruits[i])


# --------------------------------------------------
# BUILT-IN FUNCTIONS USED WITH LISTS
# --------------------------------------------------

print("\nBUILT-IN FUNCTIONS")

numbers = [10, 20, 30, 40]

print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))


# --------------------------------------------------
# NESTED LISTS
# --------------------------------------------------

print("\nNESTED LISTS")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)

print("Element at row 2 column 3:", matrix[1][2])


# --------------------------------------------------
# LIST COMPREHENSION
# --------------------------------------------------

print("\nLIST COMPREHENSION")

# Create squares of numbers
squares = [x**2 for x in range(1, 6)]

print("Squares:", squares)


# --------------------------------------------------
# FINAL OUTPUT
# --------------------------------------------------

print("\nProgram Completed Successfully!")