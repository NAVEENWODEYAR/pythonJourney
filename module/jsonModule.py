# ============================================
# Python JSON Module Demonstration Program
# ============================================

# Import JSON module
import json

# ------------------------------------------------
# 1. Python Dictionary
# ------------------------------------------------

student = {
    "id": 101,
    "name": "Rahul",
    "age": 21,
    "course": "Python",
    "is_active": True
}

print("1. Original Python Dictionary")
print(student)

print()


# ------------------------------------------------
# 2. Convert Python Object to JSON String
# ------------------------------------------------

json_data = json.dumps(student)

print("2. Python Dictionary to JSON String")
print(json_data)

print()


# ------------------------------------------------
# 3. Convert JSON String Back to Python Object
# ------------------------------------------------

python_data = json.loads(json_data)

print("3. JSON String to Python Dictionary")
print(python_data)

print()


# ------------------------------------------------
# 4. Pretty Printing JSON
# ------------------------------------------------

print("4. Formatted JSON Output")

formatted_json = json.dumps(
    student,
    indent=4
)

print(formatted_json)

print()


# ------------------------------------------------
# 5. Sorting Keys
# ------------------------------------------------

print("5. Sorted JSON Keys")

sorted_json = json.dumps(
    student,
    indent=4,
    sort_keys=True
)

print(sorted_json)

print()


# ------------------------------------------------
# 6. Writing JSON Data to a File
# ------------------------------------------------

with open("student.json", "w") as file:

    json.dump(
        student,
        file,
        indent=4
    )

print("6. JSON Written to student.json")

print()


# ------------------------------------------------
# 7. Reading JSON Data from File
# ------------------------------------------------

with open("student.json", "r") as file:

    data = json.load(file)

print("7. Data Read from File")
print(data)

print()


# ------------------------------------------------
# 8. Working with JSON Array
# ------------------------------------------------

students = [
    {"id": 1, "name": "Amit"},
    {"id": 2, "name": "Neha"},
    {"id": 3, "name": "Priya"}
]

json_students = json.dumps(
    students,
    indent=4
)

print("8. JSON Array")

print(json_students)

print()


# ------------------------------------------------
# 9. Access JSON Data
# ------------------------------------------------

print("9. Access Individual Values")

print("Name:", data["name"])
print("Course:", data["course"])

print()


# ------------------------------------------------
# 10. Update JSON Data
# ------------------------------------------------

data["age"] = 22

print("10. Updated Data")

print(data)

print()


# ------------------------------------------------
# Program End
# ------------------------------------------------

print("JSON Module Demonstration Completed!")