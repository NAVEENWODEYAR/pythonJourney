# =====================================================
# LAMBDA FUNCTION DEMONSTRATION
# =====================================================

# Lambda function to find square of a number
square = lambda x: x * x

# Lambda function to add two numbers
add = lambda a, b: a + b

# List of numbers
numbers = [1, 2, 3, 4, 5, 6]

# Using lambda with map() to find squares
squares = list(map(lambda x: x * x, numbers))

# Using lambda with filter() to get even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# List of students with marks
students = [
    ("John", 80),
    ("Alice", 95),
    ("Bob", 70)
]

# Using lambda with sorted() to sort by marks
sorted_students = sorted(students, key=lambda student: student[1])

# Displaying results
print("Square of 5 =", square(5))
print("Sum of 10 and 20 =", add(10, 20))
print("Squares of numbers =", squares)
print("Even numbers =", even_numbers)
print("Students sorted by marks =", sorted_students)