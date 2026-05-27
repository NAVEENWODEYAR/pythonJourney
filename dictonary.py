# ============================================================
# PYTHON DICTIONARY DEMONSTRATION PROGRAM
# ============================================================
# A Dictionary in Python is:
# - Unordered collection (before Python 3.7)
# - Ordered collection (Python 3.7+)
# - Mutable (can be changed)
# - Stores data in key:value pairs
# - Keys must be unique
#
# Dictionaries are created using curly braces {}
# ============================================================

# ------------------------------------------------------------
# 1. CREATING DICTIONARIES
# ------------------------------------------------------------

# Simple dictionary
student = {
    "name": "Rahul",
    "age": 21,
    "course": "Python"
}

print("Student Dictionary:")
print(student)

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 2. ACCESSING VALUES
# ------------------------------------------------------------

# Access values using keys
print("Student Name:", student["name"])
print("Student Age:", student["age"])

# Using get() method (safer)
print("Student Course:", student.get("course"))

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 3. ADDING NEW ITEMS
# ------------------------------------------------------------

# Add a new key:value pair
student["city"] = "Bangalore"

print("After Adding City:")
print(student)

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 4. MODIFYING VALUES
# ------------------------------------------------------------

# Change existing value
student["age"] = 22

print("After Modifying Age:")
print(student)

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 5. REMOVING ITEMS
# ------------------------------------------------------------

# pop() removes item using key
removed_value = student.pop("course")

print("Removed Course:", removed_value)
print("Dictionary After pop():")
print(student)

# del keyword removes key:value pair
del student["city"]

print("After del:")
print(student)

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 6. DICTIONARY LENGTH
# ------------------------------------------------------------

print("Number of Items:", len(student))

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 7. CHECKING KEYS
# ------------------------------------------------------------

print("Is 'name' present?", "name" in student)
print("Is 'marks' present?", "marks" in student)

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 8. LOOPING THROUGH DICTIONARY
# ------------------------------------------------------------

print("Printing Keys:")

for key in student:
    print(key)

print("\nPrinting Values:")

for value in student.values():
    print(value)

print("\nPrinting Key-Value Pairs:")

for key, value in student.items():
    print(key, ":", value)

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 9. IMPORTANT DICTIONARY METHODS
# ------------------------------------------------------------

employee = {
    "id": 101,
    "name": "Amit",
    "salary": 50000
}

# keys() method
print("Keys:", employee.keys())

# values() method
print("Values:", employee.values())

# items() method
print("Items:", employee.items())

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 10. COPYING A DICTIONARY
# ------------------------------------------------------------

new_employee = employee.copy()

print("Original Dictionary:")
print(employee)

print("Copied Dictionary:")
print(new_employee)

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 11. NESTED DICTIONARY
# ------------------------------------------------------------

students = {
    "student1": {
        "name": "Arjun",
        "marks": 85
    },
    "student2": {
        "name": "Sneha",
        "marks": 92
    }
}

print("Nested Dictionary:")
print(students)

# Access nested values
print("Student1 Name:", students["student1"]["name"])
print("Student2 Marks:", students["student2"]["marks"])

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 12. DICTIONARY WITH MIXED DATA TYPES
# ------------------------------------------------------------

data = {
    "name": "Ravi",
    "age": 25,
    "skills": ["Python", "Java"],
    "is_employee": True
}

print("Mixed Data Dictionary:")
print(data)

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 13. USING update() METHOD
# ------------------------------------------------------------

employee.update({
    "department": "IT",
    "salary": 60000
})

print("After update():")
print(employee)

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 14. CLEARING A DICTIONARY
# ------------------------------------------------------------

temp = {
    "a": 1,
    "b": 2
}

print("Before clear():", temp)

temp.clear()

print("After clear():", temp)

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 15. PRACTICAL EXAMPLE
# ------------------------------------------------------------

# Store marks of students
marks = {
    "Rahul": 85,
    "Priya": 90,
    "Kiran": 78
}

# Calculate total marks
total = sum(marks.values())

# Calculate average
average = total / len(marks)

print("Student Marks:")
print(marks)

print("Total Marks:", total)
print("Average Marks:", average)

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 16. DICTIONARY COMPREHENSION
# ------------------------------------------------------------

# Create dictionary of squares
squares = {x: x*x for x in range(1, 6)}

print("Dictionary Comprehension:")
print(squares)

print("\n--------------------------------------------------")

# ------------------------------------------------------------
# 17. FINAL SUMMARY
# ------------------------------------------------------------

print("Python Dictionary Summary")
print("-------------------------")
print("1. Dictionaries store data as key:value pairs")
print("2. Keys must be unique")
print("3. Dictionaries are mutable")
print("4. Values can be any data type")
print("5. Dictionaries support fast searching")
print("6. Useful methods: keys(), values(), items(), update()")