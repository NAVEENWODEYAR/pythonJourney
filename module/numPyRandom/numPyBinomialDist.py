# ==========================================================
# Program: Binomial Distribution using NumPy
# ==========================================================
# Definition:
# A Binomial Distribution is a probability distribution that
# gives the number of successful outcomes in a fixed number
# of independent trials.
#
# Example:
# Tossing a coin 10 times.
# Success = Getting Heads
# Failure = Getting Tails
#
# Conditions:
# 1. Fixed number of trials (n)
# 2. Only two possible outcomes (Success/Failure)
# 3. Probability of success (p) remains constant
# 4. Each trial is independent
#
# NumPy Syntax:
# np.random.binomial(n, p, size)
#
# Parameters:
# n    -> Number of trials
# p    -> Probability of success (0 to 1)
# size -> Number of random experiments to generate
#
# Returns:
# Random values representing the number of successes
# in each experiment.
# ==========================================================

# Import NumPy library
import numpy as np

print("=" * 60)
print("        BINOMIAL DISTRIBUTION USING NUMPY")
print("=" * 60)

# ----------------------------------------------------------
# Step 1: Define the parameters
# ----------------------------------------------------------

n = 10          # Number of trials
p = 0.5         # Probability of success
size = 5        # Number of experiments

# ----------------------------------------------------------
# Step 2: Generate random values using binomial distribution
# ----------------------------------------------------------

result = np.random.binomial(n, p, size)

# ----------------------------------------------------------
# Step 3: Display the generated values
# ----------------------------------------------------------

print("\nInput Values")
print("----------------------------")
print("Number of Trials (n)       :", n)
print("Probability of Success (p) :", p)
print("Number of Experiments      :", size)

print("\nGenerated Binomial Values")
print("----------------------------")
print(result)

# ----------------------------------------------------------
# Step 4: Explain each experiment
# ----------------------------------------------------------

print("\nExplanation of Each Experiment")
print("----------------------------")

for i in range(size):
    successes = result[i]
    failures = n - successes

    print(f"Experiment {i+1}")
    print(f"  Successes : {successes}")
    print(f"  Failures  : {failures}")
    print()

# ----------------------------------------------------------
# Step 5: Display Summary
# ----------------------------------------------------------

print("=" * 60)
print("SUMMARY")
print("=" * 60)

print(f"""
Definition:
A Binomial Distribution calculates the number of successful
outcomes in a fixed number of independent trials.

Syntax:
np.random.binomial(n, p, size)

Where:
n    = Number of trials
p    = Probability of success
size = Number of experiments

Example Used:
Trials               = {n}
Probability          = {p}
Experiments          = {size}

Possible Output:
{result}

Applications:
1. Coin Toss Simulation
2. Exam Pass/Fail Analysis
3. Quality Control
4. Medical Testing
5. Machine Learning
6. Probability Experiments

Conclusion:
Each value in the output represents the number of successful
outcomes obtained in one experiment consisting of {n} trials.
The values can range from 0 to {n}.
""")

print("=" * 60)