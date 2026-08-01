"""
==============================================================
          Python for Loop vs while Loop Demonstration
==============================================================

Definition
----------
Python provides two looping statements:

1. for loop
2. while loop

--------------------------------------------------------------
1. for Loop
--------------------------------------------------------------
Definition:
    A 'for' loop is used when the number of iterations is known
    or when iterating over a collection such as a list, tuple,
    string, dictionary, or range.

Syntax:
    for variable in iterable:
        statements

Example:
    for i in range(5):
        print(i)

Best Used When:
✔ Number of iterations is known.
✔ Traversing collections.
✔ Reading files line by line.
✔ Processing arrays/lists.

Time Complexity:
O(n)

--------------------------------------------------------------
2. while Loop
--------------------------------------------------------------
Definition:
    A 'while' loop executes as long as the given condition
    remains True.

Syntax:
    while condition:
        statements

Example:
    i = 1
    while i <= 5:
        print(i)
        i += 1

Best Used When:
✔ Number of iterations is unknown.
✔ Waiting for user input.
✔ Menu-driven programs.
✔ Games.
✔ Reading data until EOF.

Time Complexity:
O(n)

--------------------------------------------------------------
Difference
--------------------------------------------------------------

for Loop
---------
• Iterates over an iterable.
• Number of iterations usually known.
• Automatically moves to next element.
• Less chance of infinite loop.

while Loop
-----------
• Executes until condition becomes False.
• Number of iterations may be unknown.
• Programmer updates loop variable manually.
• Can become an infinite loop if condition
  never changes.

Author : Naveen K Wodeyar
Date   : 31-Jul-2026
==============================================================
"""


# ----------------------------------------------------------
# FOR LOOP DEMO
# ----------------------------------------------------------

print("=" * 60)
print("FOR LOOP DEMONSTRATION")
print("=" * 60)

# range(1,6) generates numbers from 1 to 5
print("\nPrinting numbers using for loop:\n")

for number in range(1, 6):
    print(number)


# ----------------------------------------------------------
# Traversing a List using for loop
# ----------------------------------------------------------

print("\nTraversing a List:\n")

languages = ["Java", "Python", "C", "C++", "JavaScript"]

for language in languages:
    print(language)


# ----------------------------------------------------------
# Traversing a String
# ----------------------------------------------------------

print("\nTraversing a String:\n")

word = "PYTHON"

for character in word:
    print(character)


# ----------------------------------------------------------
# WHILE LOOP DEMO
# ----------------------------------------------------------

print("\n" + "=" * 60)
print("WHILE LOOP DEMONSTRATION")
print("=" * 60)

print("\nPrinting numbers using while loop:\n")

counter = 1

# Loop continues while condition is True
while counter <= 5:
    print(counter)

    # Without this statement,
    # the loop would run forever (Infinite Loop)
    counter += 1


# ----------------------------------------------------------
# Another while loop example
# ----------------------------------------------------------

print("\nCountdown using while loop:\n")

count = 5

while count > 0:
    print(count)
    count -= 1

print("Blast Off! 🚀")


# ----------------------------------------------------------
# Comparison Summary
# ----------------------------------------------------------

print("\n" + "=" * 60)
print("COMPARISON")
print("=" * 60)

print("""
FOR LOOP
---------
✔ Used when number of iterations is known.
✔ Best for iterating over collections.
✔ Simpler and easier to read.
✔ Automatically moves to next element.

WHILE LOOP
----------
✔ Used when number of iterations is unknown.
✔ Executes until condition becomes False.
✔ Requires manual update of loop variable.
✔ Can become an infinite loop if not handled properly.
""")

print("=" * 60)
print("Program executed successfully.")
print("=" * 60)