"""
Program: Random Data Distribution Demonstration

Objective:
----------
This program generates random numbers and analyzes how they are distributed.

A distribution describes how data values are spread across a range.
In this example, we use a Uniform Distribution, where every value
between 0 and 1 has an equal probability of being generated.

Requirements:
-------------
Install matplotlib if not already installed:

pip install matplotlib
"""

# Import the random module for generating random numbers
import random

# Import matplotlib for creating graphs
import matplotlib.pyplot as plt


# --------------------------------------------------
# STEP 1: Generate Random Data
# --------------------------------------------------

# Number of random values to generate
sample_size = 1000

# Create an empty list to store random values
random_data = []

# Generate 1000 random numbers between 0 and 1
for i in range(sample_size):
    value = random.random()   # Generates a value from 0.0 to 1.0
    random_data.append(value)


# --------------------------------------------------
# STEP 2: Calculate Basic Statistics
# --------------------------------------------------

# Total number of values
count = len(random_data)

# Smallest value in the dataset
minimum = min(random_data)

# Largest value in the dataset
maximum = max(random_data)

# Average (Mean) value
mean = sum(random_data) / count


# --------------------------------------------------
# STEP 3: Display Statistical Information
# --------------------------------------------------

print("RANDOM DATA DISTRIBUTION ANALYSIS")
print("-" * 40)

print("Total Values Generated :", count)
print("Minimum Value          :", round(minimum, 4))
print("Maximum Value          :", round(maximum, 4))
print("Average (Mean)         :", round(mean, 4))

print("\nExpected Mean for Uniform Distribution = 0.5")
print("Observed Mean =", round(mean, 4))


# --------------------------------------------------
# STEP 4: Create Histogram
# --------------------------------------------------

"""
Histogram Explanation:
----------------------
A histogram divides data into intervals called bins.

Example:

0.0 - 0.1
0.1 - 0.2
0.2 - 0.3
...
0.9 - 1.0

The height of each bar represents how many values
fall within that range.

For a Uniform Distribution, the bars should be
approximately equal in height.
"""

plt.figure(figsize=(8, 5))

plt.hist(
    random_data,
    bins=10,             # Divide into 10 intervals
    color="skyblue",
    edgecolor="black"
)

plt.title("Random Data Distribution (Uniform Distribution)")
plt.xlabel("Value Range")
plt.ylabel("Frequency")

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()