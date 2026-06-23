# ==========================================================
# NUMPY RANDOM MODULE - COMPLETE EXPLANATION
# ==========================================================
#
# Definition:
# NumPy Random module is used to generate random numbers,
# random arrays, random selections, and random samples.
#
# Syntax:
# import numpy as np
# np.random.function_name(parameters)
#
# Common Functions:
# 1. np.random.rand()       -> Random float values (0 to 1)
# 2. np.random.randint()   -> Random integers
# 3. np.random.randn()     -> Random values from normal distribution
# 4. np.random.choice()    -> Random selection from a list
# 5. np.random.shuffle()   -> Shuffle elements
# 6. np.random.seed()      -> Generate reproducible random values
#
# Usage:
# - Machine Learning
# - Data Science
# - Simulations
# - Games
# - Testing and Sampling
#
# ==========================================================

import numpy as np

print("========== NUMPY RANDOM MODULE DEMO ==========\n")

# ----------------------------------------------------------
# 1. Seed Function
# ----------------------------------------------------------
# Seed ensures that the same random values are generated
# every time the program runs.

np.random.seed(42)

print("1. Using seed(42) for reproducible results\n")

# ----------------------------------------------------------
# 2. Random Float Numbers using rand()
# ----------------------------------------------------------
# Generates random values between 0 and 1.

print("2. Random Float Numbers using rand()")

single_float = np.random.rand()
print("Single random float:", single_float)

array_float = np.random.rand(3, 4)
print("\n3x4 Random Float Array:")
print(array_float)

# ----------------------------------------------------------
# 3. Random Integers using randint()
# ----------------------------------------------------------
# Syntax:
# np.random.randint(low, high, size)

print("\n3. Random Integers using randint()")

random_int = np.random.randint(1, 100)
print("Single Random Integer:", random_int)

random_int_array = np.random.randint(1, 50, size=(2, 5))
print("\n2x5 Random Integer Array:")
print(random_int_array)

# ----------------------------------------------------------
# 4. Random Numbers from Normal Distribution using randn()
# ----------------------------------------------------------
# Mean = 0
# Standard Deviation = 1

print("\n4. Random Numbers using randn()")

normal_values = np.random.randn(5)
print(normal_values)

# ----------------------------------------------------------
# 5. Random Selection using choice()
# ----------------------------------------------------------
# Select random elements from a list

print("\n5. Random Selection using choice()")

colors = ["Red", "Blue", "Green", "Yellow"]

selected_color = np.random.choice(colors)
print("Selected Color:", selected_color)

multiple_colors = np.random.choice(colors, size=3)
print("Three Random Colors:", multiple_colors)

# ----------------------------------------------------------
# 6. Shuffle Elements using shuffle()
# ----------------------------------------------------------
# Rearranges elements randomly

print("\n6. Shuffle using shuffle()")

numbers = np.array([1, 2, 3, 4, 5])

print("Before Shuffle:", numbers)

np.random.shuffle(numbers)

print("After Shuffle :", numbers)

# ----------------------------------------------------------
# 7. Random Sample using random()
# ----------------------------------------------------------
# Generates random values between 0 and 1

print("\n7. Random Sample using random()")

sample = np.random.random((2, 3))
print(sample)

# ----------------------------------------------------------
# 8. Practical Example
# ----------------------------------------------------------
# Simulating marks of 10 students

print("\n8. Practical Example - Student Marks")

marks = np.random.randint(35, 101, size=10)

print("Marks:", marks)

print("Highest Mark :", marks.max())
print("Lowest Mark  :", marks.min())
print("Average Mark :", marks.mean())

# ----------------------------------------------------------
# End of Program
# ----------------------------------------------------------

print("\n========== PROGRAM COMPLETED ==========")