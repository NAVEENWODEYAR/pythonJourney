# ============================================================
# PYTHON LIST DEMONSTRATION PROGRAM
# ============================================================
# A list in Python is:
# - Ordered
# - Mutable (can be changed)
# - Allows duplicate values
# - Can store different data types
#
# Lists are created using square brackets []
# ============================================================

# ------------------------------------------------------------
# 1. CREATING LISTS
# ------------------------------------------------------------

# List of integers
numbers = [10, 20, 30, 40, 50]

# List of strings
fruits = ["apple", "banana", "mango"]

# Mixed data type list
mixed = [1, "hello", 3.5, True]

print("Numbers List:", numbers)
print("Fruits List:", fruits)
print("Mixed List:", mixed)

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 2. ACCESSING ELEMENTS
# ------------------------------------------------------------

# Indexing starts from 0
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])

# Negative indexing starts from the end
print("Last fruit:", fruits[-1])

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 3. SLICING LISTS
# ------------------------------------------------------------

# Syntax: list[start:end]

print("First 3 numbers:", numbers[0:3])
print("Numbers from index 2:", numbers[2:])
print("All numbers:", numbers[:])

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 4. MODIFYING LIST ELEMENTS
# ------------------------------------------------------------

# Lists are mutable, so values can be changed
fruits[1] = "orange"

print("Modified Fruits List:", fruits)

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 5. ADDING ELEMENTS
# ------------------------------------------------------------

# append() adds one item at the end
fruits.append("grapes")
print("After append:", fruits)

# insert(index, value) adds item at specific position
fruits.insert(1, "kiwi")
print("After insert:", fruits)

# extend() adds multiple elements
fruits.extend(["pineapple", "papaya"])
print("After extend:", fruits)

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 6. REMOVING ELEMENTS
# ------------------------------------------------------------

# remove(value) removes first matching value
fruits.remove("orange")
print("After remove:", fruits)

# pop() removes last element and returns it
removed_item = fruits.pop()
print("Removed using pop:", removed_item)
print("List after pop:", fruits)

# del keyword removes by index
del fruits[0]
print("After del:", fruits)

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 7. LIST LENGTH
# ------------------------------------------------------------

print("Length of numbers list:", len(numbers))

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 8. CHECKING MEMBERSHIP
# ------------------------------------------------------------

print("Is apple present?", "apple" in fruits)
print("Is mango present?", "mango" in fruits)

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 9. LOOPING THROUGH A LIST
# ------------------------------------------------------------

print("Printing all numbers:")

for num in numbers:
    print(num)

print("\nUsing index with loop:")

for i in range(len(numbers)):
    print("Index:", i, "Value:", numbers[i])

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 10. LIST SORTING
# ------------------------------------------------------------

marks = [75, 40, 98, 65, 87]

# Sort ascending
marks.sort()
print("Ascending order:", marks)

# Sort descending
marks.sort(reverse=True)
print("Descending order:", marks)

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 11. REVERSING A LIST
# ------------------------------------------------------------

numbers.reverse()
print("Reversed numbers:", numbers)

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 12. COPYING A LIST
# ------------------------------------------------------------

# copy() creates a new independent list
new_numbers = numbers.copy()

print("Original list:", numbers)
print("Copied list:", new_numbers)

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 13. LIST CONCATENATION
# ------------------------------------------------------------

list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined = list1 + list2

print("Combined List:", combined)

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 14. NESTED LISTS
# ------------------------------------------------------------

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Nested List (Matrix):", matrix)

# Accessing nested elements
print("Element at row 2 column 3:", matrix[1][2])

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 15. LIST COMPREHENSION
# ------------------------------------------------------------

# Create a list of squares
squares = [x * x for x in range(1, 6)]

print("Squares:", squares)

# Even numbers only
even_numbers = [x for x in range(1, 11) if x % 2 == 0]

print("Even Numbers:", even_numbers)

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 16. IMPORTANT LIST METHODS
# ------------------------------------------------------------

sample = [3, 1, 5, 1, 9]

print("Sample List:", sample)

# count() counts occurrences
print("Count of 1:", sample.count(1))

# index() finds first occurrence
print("Index of 5:", sample.index(5))

# clear() removes all elements
sample.clear()
print("After clear:", sample)

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 17. PRACTICAL EXAMPLE
# ------------------------------------------------------------

# Store student marks
student_marks = [85, 90, 78, 92, 88]

# Calculate total marks
total = sum(student_marks)

# Calculate average
average = total / len(student_marks)

print("Student Marks:", student_marks)
print("Total Marks:", total)
print("Average Marks:", average)

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 18. FINAL SUMMARY
# ------------------------------------------------------------

print("Python Lists Summary")
print("---------------------")
print("1. Lists are ordered collections")
print("2. Lists are mutable")
print("3. Lists allow duplicate values")
print("4. Lists can store multiple data types")
print("5. Lists support indexing and slicing")
print("6. Lists support many useful built-in methods")