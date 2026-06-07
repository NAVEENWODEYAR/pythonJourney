"""
MOST ASKED PYTHON INTERVIEW QUESTIONS - SINGLE PROGRAM
-----------------------------------------------------
This program demonstrates commonly asked Python concepts
with explanations and examples.
"""

# ====================================================
# 1. What is Python?
# ====================================================

print("\n1. PYTHON BASICS")
print("Python is a high-level, interpreted, object-oriented language.")


# ====================================================
# 2. Variables and Data Types
# ====================================================

print("\n2. VARIABLES AND DATA TYPES")

name = "John"      # String
age = 25           # Integer
salary = 55000.75  # Float
is_active = True   # Boolean

print(name, age, salary, is_active)


# ====================================================
# 3. Difference between List and Tuple
# ====================================================

print("\n3. LIST VS TUPLE")

my_list = [10, 20, 30]
my_tuple = (10, 20, 30)

my_list.append(40)     # Allowed
print("List:", my_list)

# my_tuple.append(40)  # Error (Tuple is immutable)

print("Tuple:", my_tuple)


# ====================================================
# 4. String Reverse
# ====================================================

print("\n4. REVERSE A STRING")

text = "Python"
reversed_text = text[::-1]

print("Original:", text)
print("Reversed:", reversed_text)


# ====================================================
# 5. Check Palindrome
# ====================================================

print("\n5. PALINDROME CHECK")

word = "madam"

if word == word[::-1]:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")


# ====================================================
# 6. Swap Two Numbers
# ====================================================

print("\n6. SWAP TWO NUMBERS")

a = 10
b = 20

a, b = b, a

print("a =", a)
print("b =", b)


# ====================================================
# 7. Find Largest Number
# ====================================================

print("\n7. LARGEST NUMBER")

numbers = [10, 50, 25, 80, 30]

largest = max(numbers)

print("Largest:", largest)


# ====================================================
# 8. Count Vowels
# ====================================================

print("\n8. COUNT VOWELS")

sentence = "Hello Python"
vowels = "aeiouAEIOU"

count = sum(1 for ch in sentence if ch in vowels)

print("Vowel Count:", count)


# ====================================================
# 9. List Comprehension
# ====================================================

print("\n9. LIST COMPREHENSION")

squares = [x*x for x in range(1, 6)]

print("Squares:", squares)


# ====================================================
# 10. Lambda Function
# ====================================================

print("\n10. LAMBDA FUNCTION")

square = lambda x: x * x

print("Square of 5:", square(5))


# ====================================================
# 11. Map Function
# ====================================================

print("\n11. MAP FUNCTION")

nums = [1, 2, 3, 4]

result = list(map(lambda x: x*2, nums))

print(result)


# ====================================================
# 12. Filter Function
# ====================================================

print("\n12. FILTER FUNCTION")

nums = [1, 2, 3, 4, 5, 6]

even_numbers = list(filter(lambda x: x % 2 == 0, nums))

print(even_numbers)


# ====================================================
# 13. Dictionary Example
# ====================================================

print("\n13. DICTIONARY")

student = {
    "name": "John",
    "age": 22,
    "course": "Python"
}

print(student)
print(student["name"])


# ====================================================
# 14. Sets and Duplicate Removal
# ====================================================

print("\n14. REMOVE DUPLICATES")

numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = list(set(numbers))

print(unique_numbers)


# ====================================================
# 15. Exception Handling
# ====================================================

print("\n15. EXCEPTION HANDLING")

try:
    result = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Finally block executed")


# ====================================================
# 16. Function Example
# ====================================================

print("\n16. FUNCTIONS")

def add(a, b):
    """Returns sum of two numbers"""
    return a + b

print(add(10, 20))


# ====================================================
# 17. Recursion
# ====================================================

print("\n17. RECURSION - FACTORIAL")

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial:", factorial(5))


# ====================================================
# 18. OOP - Class and Object
# ====================================================

print("\n18. CLASS AND OBJECT")

class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Student Name:", self.name)

s1 = Student("Alice")
s1.display()


# ====================================================
# 19. Inheritance
# ====================================================

print("\n19. INHERITANCE")

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()

d.sound()
d.bark()


# ====================================================
# 20. Polymorphism
# ====================================================

print("\n20. POLYMORPHISM")

class Bird:
    def speak(self):
        print("Bird chirps")

class Cat:
    def speak(self):
        print("Cat meows")

for obj in [Bird(), Cat()]:
    obj.speak()


# ====================================================
# 21. File Handling
# ====================================================

print("\n21. FILE HANDLING")

with open("sample.txt", "w") as file:
    file.write("Hello Python")

with open("sample.txt", "r") as file:
    content = file.read()

print(content)


# ====================================================
# 22. Generator
# ====================================================

print("\n22. GENERATOR")

def generate_numbers():
    for i in range(5):
        yield i

for num in generate_numbers():
    print(num, end=" ")

print()


# ====================================================
# 23. *args and **kwargs
# ====================================================

print("\n23. *args AND **kwargs")

def demo(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

demo(1, 2, 3, name="John", city="Bangalore")


# ====================================================
# 24. Check Prime Number
# ====================================================

print("\n24. PRIME NUMBER")

num = 17
is_prime = True

for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break

print(num, "is prime" if is_prime else "is not prime")


# ====================================================
# 25. Fibonacci Series
# ====================================================

print("\n25. FIBONACCI SERIES")

n = 10

a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

print()

# ====================================================
# END
# ====================================================

print("\nAll common Python interview questions completed.")