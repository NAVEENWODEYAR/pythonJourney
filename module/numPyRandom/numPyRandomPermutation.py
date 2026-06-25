# ==========================================================
# NumPy random.permutation() - Complete Demonstration
# ==========================================================
#
# Definition:
#   np.random.permutation() returns a random permutation
#   (random arrangement) of numbers or array elements.
#
# Key Points:
#   1. Returns a NEW shuffled array.
#   2. Does NOT modify the original array.
#   3. Works with integers and arrays.
#   4. Useful for data shuffling, sampling,
#      train-test splitting, games, simulations, etc.
#
# ==========================================================

import numpy as np

print("=" * 60)
print("NUMPY RANDOM PERMUTATION DEMO")
print("=" * 60)

# ----------------------------------------------------------
# 1. Integer Input
# ----------------------------------------------------------
# When an integer n is provided, NumPy creates:
# [0, 1, 2, ..., n-1]
# and then shuffles it.
# ----------------------------------------------------------

print("\n1. INTEGER INPUT EXAMPLE")

n = 10

random_numbers = np.random.permutation(n)

print("Original sequence :", np.arange(n))
print("Random permutation:", random_numbers)

# ----------------------------------------------------------
# 2. Array Input
# ----------------------------------------------------------
# When an array is provided, the array elements
# are shuffled randomly.
# ----------------------------------------------------------

print("\n2. ARRAY INPUT EXAMPLE")

arr = np.array([10, 20, 30, 40, 50])

shuffled_arr = np.random.permutation(arr)

print("Original array :", arr)
print("Permuted array :", shuffled_arr)

# ----------------------------------------------------------
# 3. Original Array Remains Unchanged
# ----------------------------------------------------------
# permutation() returns a new array and keeps
# the original array intact.
# ----------------------------------------------------------

print("\n3. ORIGINAL ARRAY CHECK")

print("Original array after permutation:", arr)
print("Original array unchanged:", np.array_equal(
    arr, np.array([10, 20, 30, 40, 50])
))

# ----------------------------------------------------------
# 4. 2D Array Example
# ----------------------------------------------------------
# For multidimensional arrays, permutation()
# shuffles rows (first axis).
# ----------------------------------------------------------

print("\n4. 2D ARRAY EXAMPLE")

matrix = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

permuted_matrix = np.random.permutation(matrix)

print("Original Matrix:")
print(matrix)

print("\nPermuted Matrix:")
print(permuted_matrix)

# ----------------------------------------------------------
# 5. Reproducible Results Using Seed
# ----------------------------------------------------------
# Setting a seed generates the same random output
# every time the program runs.
# ----------------------------------------------------------

print("\n5. RANDOM SEED EXAMPLE")

np.random.seed(42)

seed_result = np.random.permutation(10)

print("Permutation with seed 42:")
print(seed_result)

# ----------------------------------------------------------
# 6. Dataset Shuffling Use Case
# ----------------------------------------------------------
# Commonly used in Machine Learning to shuffle
# training data before model training.
# ----------------------------------------------------------

print("\n6. DATASET SHUFFLING")

dataset = np.array([
    "Record-1",
    "Record-2",
    "Record-3",
    "Record-4",
    "Record-5"
])

shuffled_dataset = np.random.permutation(dataset)

print("Original Dataset:")
print(dataset)

print("\nShuffled Dataset:")
print(shuffled_dataset)

# ----------------------------------------------------------
# 7. Random Sampling Without Replacement
# ----------------------------------------------------------
# Since permutation contains each element only once,
# selecting the first few elements gives a random
# sample without duplicates.
# ----------------------------------------------------------

print("\n7. RANDOM SAMPLING")

students = np.array([
    "John",
    "Alice",
    "David",
    "Emma",
    "Sophia"
])

random_order = np.random.permutation(students)

selected_students = random_order[:3]

print("Random Order:")
print(random_order)

print("\nSelected 3 Students:")
print(selected_students)

# ----------------------------------------------------------
# 8. Train-Test Split Example
# ----------------------------------------------------------
# Frequently used in Machine Learning projects.
# ----------------------------------------------------------

print("\n8. TRAIN-TEST SPLIT")

data = np.arange(20)

indices = np.random.permutation(len(data))

train_size = int(0.8 * len(data))

train_indices = indices[:train_size]
test_indices = indices[train_size:]

print("Train Indices:")
print(train_indices)

print("\nTest Indices:")
print(test_indices)

# ----------------------------------------------------------
# 9. Card Shuffling Example
# ----------------------------------------------------------
# A simple simulation of shuffling cards.
# ----------------------------------------------------------

print("\n9. CARD SHUFFLING")

cards = np.array([
    "A", "2", "3", "4",
    "5", "6", "7", "8"
])

shuffled_cards = np.random.permutation(cards)

print("Original Cards:")
print(cards)

print("\nShuffled Cards:")
print(shuffled_cards)

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
np.random.permutation()

✔ Creates a random arrangement of elements.
✔ Works with integers and arrays.
✔ Returns a NEW shuffled array.
✔ Does NOT modify the original array.
✔ Useful for:
    - Dataset shuffling
    - Random sampling
    - Train-Test splitting
    - Card shuffling
    - Simulations
    - Machine Learning preprocessing
""")