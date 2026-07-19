# ==========================================================
# OBJECT ORIENTED PROGRAMMING SYSTEM (OOPS) IN PYTHON
# ==========================================================

"""
DEFINITION:
OOPS (Object-Oriented Programming System) is a programming
paradigm that uses Classes and Objects to organize code.

BASIC SYNTAX:

class ClassName:

    def __init__(self):
        # attributes

    def method_name(self):
        # functionality

obj = ClassName()
obj.method_name()

USE CASES:
1. Banking Systems
2. Student Management Systems
3. Hospital Management Systems
4. E-Commerce Applications
5. Game Development

ADVANTAGES:
1. Code Reusability
2. Better Security
3. Easy Maintenance
4. Reduced Code Duplication
5. Real-World Modeling

DISADVANTAGES:
1. More Memory Usage
2. Increased Complexity
3. Longer Development Time
4. Difficult for Beginners
"""

# ==========================================================
# PARENT CLASS
# ==========================================================

class Person:

    # Constructor
    # Automatically called when object is created
    def __init__(self, name, age):

        # Public Attribute
        self.name = name

        # Private Attribute (Encapsulation)
        self.__age = age

    # Method
    def display(self):

        print("Name :", self.name)
        print("Age  :", self.__age)

    # Method for Polymorphism
    def role(self):

        print("I am a Person")


# ==========================================================
# CHILD CLASS (INHERITANCE)
# Student inherits Person class
# ==========================================================

class Student(Person):

    # Constructor
    def __init__(self, name, age, roll_no):

        # Calling Parent Constructor
        super().__init__(name, age)

        # Additional Attribute
        self.roll_no = roll_no

    # Method Overriding (Polymorphism)
    def role(self):

        print("I am a Student")

    # Student Method
    def show_details(self):

        # Calling Parent Method
        self.display()

        print("Roll Number :", self.roll_no)


# ==========================================================
# OBJECT CREATION
# ==========================================================

s1 = Student("Rahul", 20, 101)

# ==========================================================
# METHOD CALLS
# ==========================================================

print("===== STUDENT DETAILS =====")

s1.show_details()

print()

print("===== POLYMORPHISM =====")

s1.role()

print()

print("===== OOPS CONCEPTS USED =====")

print("1. Class          -> Person, Student")
print("2. Object         -> s1")
print("3. Constructor    -> __init__()")
print("4. Attributes/Variables    -> name, age, roll_no")
print("5. Methods        -> display(), role()")
print("6. Encapsulation  -> __age")
print("7. Inheritance    -> Student(Person)")
print("8. Polymorphism   -> role() overridden")

print()

print("===== ADVANTAGES OF OOPS =====")
print("1. Code Reusability")
print("2. Better Security")
print("3. Easy Maintenance")
print("4. Reduced Code Duplication")
print("5. Real World Modeling")

print()

print("===== DISADVANTAGES OF OOPS =====")
print("1. More Memory Usage")
print("2. Increased Complexity")
print("3. Longer Development Time")
print("4. Difficult for Beginners")