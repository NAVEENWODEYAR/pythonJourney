"""
============================================================
         MULTINOMIAL DISTRIBUTION - COMPLETE BASICS
============================================================

Definition:
-----------
The Multinomial Distribution is an extension of the Binomial
Distribution. It is used when each trial can result in more
than two possible outcomes.

Examples:
---------
1. Rolling a dice (6 possible outcomes)
2. Survey responses (Yes, No, Maybe)
3. Choosing products (Product A, B, C)
4. Voting among multiple candidates
5. Customer preferences for different brands

------------------------------------------------------------
Conditions
------------------------------------------------------------

1. Fixed number of trials (n).
2. Each trial is independent.
3. Every trial has one of k possible outcomes.
4. The probability of each outcome remains constant.
5. Sum of all probabilities equals 1.

------------------------------------------------------------
Formula
------------------------------------------------------------

                  n!
P(X1,X2,...,Xk)= -------------------------------
                x1!x2!...xk!

                × p1^x1 × p2^x2 × ... × pk^xk

Where:
-------
n  = Total number of trials
x1, x2, ..., xk = Number of occurrences of each outcome
p1, p2, ..., pk = Probability of each outcome

============================================================
"""

# Import required libraries
import math

# ----------------------------------------------------------
# Function to calculate factorial
# ----------------------------------------------------------
def factorial(n):
    """Returns the factorial of a number."""
    return math.factorial(n)

# ----------------------------------------------------------
# Function to calculate Multinomial Probability
# ----------------------------------------------------------
def multinomial_probability(n, counts, probabilities):
    """
    Calculates the multinomial probability.

    Parameters:
    n             : Total number of trials
    counts        : List containing occurrences of each outcome
    probabilities : List containing probabilities of each outcome

    Returns:
    Probability value
    """

    # Calculate numerator (n!)
    numerator = factorial(n)

    # Calculate denominator (x1! * x2! * ...)
    denominator = 1
    for count in counts:
        denominator *= factorial(count)

    # Calculate probability term
    probability_term = 1
    for count, probability in zip(counts, probabilities):
        probability_term *= probability ** count

    # Final multinomial probability
    probability = (numerator / denominator) * probability_term

    return probability

# ==========================================================
# Example
# ==========================================================

print("=" * 60)
print("          MULTINOMIAL DISTRIBUTION EXAMPLE")
print("=" * 60)

# Number of trials
n = 10

# Probabilities of outcomes
# Example:
# Red   = 0.5
# Blue  = 0.3
# Green = 0.2

probabilities = [0.5, 0.3, 0.2]

# Observed outcomes
# Red = 4
# Blue = 3
# Green = 3

counts = [4, 3, 3]

prob = multinomial_probability(n, counts, probabilities)

print("\nNumber of Trials :", n)

print("\nProbabilities")
print("----------------")
print("Red   :", probabilities[0])
print("Blue  :", probabilities[1])
print("Green :", probabilities[2])

print("\nObserved Counts")
print("----------------")
print("Red   :", counts[0])
print("Blue  :", counts[1])
print("Green :", counts[2])

print(f"\nMultinomial Probability = {prob:.6f}")

# ==========================================================
# Mean of each category
# ==========================================================

print("\n")
print("=" * 60)
print("Expected Counts (Mean)")
print("=" * 60)

colors = ["Red", "Blue", "Green"]

for color, probability in zip(colors, probabilities):
    mean = n * probability
    print(f"{color:<6}: {mean:.2f}")

# ==========================================================
# Applications
# ==========================================================

print("\n")
print("=" * 60)
print("Applications")
print("=" * 60)

applications = [
    "1. Market research (customer preferences).",
    "2. Election result analysis.",
    "3. Machine Learning (classification problems).",
    "4. Quality control in manufacturing.",
    "5. Medical research.",
    "6. Survey data analysis.",
    "7. Genetics and DNA analysis.",
    "8. Natural Language Processing (word frequencies)."
]

for app in applications:
    print(app)

# ==========================================================
# Interpretation
# ==========================================================

print("\n")
print("=" * 60)
print("Interpretation")
print("=" * 60)

print(f"""
There are {n} independent trials.

Possible outcomes:
Red   : Probability = {probabilities[0]}
Blue  : Probability = {probabilities[1]}
Green : Probability = {probabilities[2]}

Observed:
Red   = {counts[0]}
Blue  = {counts[1]}
Green = {counts[2]}

The probability of observing exactly this combination
of outcomes is {prob:.6f}.

The Multinomial Distribution is useful whenever each
trial has more than two possible outcomes.
""")

print("=" * 60)
print("End of Program")
print("=" * 60)