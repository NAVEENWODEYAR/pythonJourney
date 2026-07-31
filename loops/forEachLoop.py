"""
===========================================================
            Python forEach Loop Demonstration
===========================================================

Definition:
-----------
A "forEach" loop is a programming concept used to iterate over
every element in a collection (such as a list or tuple) and
perform an operation on each element.

Does Python have a forEach() method?
------------------------------------
No. Unlike Java, Python does NOT provide a built-in forEach()
method for lists.

Instead, Python uses the 'for' loop, which is simpler, more
readable, and is the recommended way to iterate over collections.

Java Example:
-------------
languages.forEach(language -> System.out.println(language));

Python Equivalent:
------------------
for language in languages:
    print(language)

Syntax:
-------
for variable in collection:
    # statements

where
------
variable   -> Current element in the collection
collection -> List, Tuple, Set, Dictionary, String, etc.

Time Complexity : O(n)
Space Complexity: O(1)

Author : Naveen K Wodeyar
Date   : 31-Jul-2026
===========================================================
"""


# -------------------------------
# Main Program
# -------------------------------

# Creating a list
languages = [
    "Java",
    "Python",
    "C",
    "C++",
    "JavaScript"
]

print("=" * 50)
print("Python forEach Loop Demonstration")
print("=" * 50)

# ----------------------------------------------------------
# The for loop automatically visits every element
# one by one from the list.
# ----------------------------------------------------------

print("\nPrinting all programming languages:\n")

for language in languages:
    print(language)

# ----------------------------------------------------------
# Another Example
# ----------------------------------------------------------

numbers = [10, 20, 30, 40, 50]

print("\nPrinting numbers:\n")

for number in numbers:
    print(number)

# ----------------------------------------------------------
# Example with String
# Every character is treated as an element.
# ----------------------------------------------------------

word = "PYTHON"

print("\nPrinting characters of a string:\n")

for character in word:
    print(character)

# ----------------------------------------------------------
# Example with Index
# enumerate() returns both index and value.
# ----------------------------------------------------------

print("\nPrinting index and value:\n")

for index, language in enumerate(languages):
    print(f"Index = {index}, Value = {language}")

print("\nProgram executed successfully.")