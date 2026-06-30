"""
============================================================
            ZIPF DISTRIBUTION - COMPLETE BASICS
============================================================

Definition:
-----------
The Zipf Distribution is a discrete probability distribution
where the frequency of an item is inversely proportional to
its rank.

Simply put:
- The highest-ranked item occurs most frequently.
- The second-ranked item occurs about half as often.
- The third-ranked item occurs about one-third as often.

Examples:
---------
1. Word frequencies in books.
2. Website popularity.
3. City population rankings.
4. Income rankings.
5. Product sales rankings.

------------------------------------------------------------
Formula
------------------------------------------------------------

              1 / r^s
P(r) = -----------------------
       Σ (1 / k^s)

Where:
-------
r = Rank of the item (1,2,3,...)
s = Exponent (shape parameter)
N = Total number of ranked items

Denominator:
------------
Σ (1 / k^s) for k = 1 to N
This is called the normalization constant.

------------------------------------------------------------
Conditions
------------------------------------------------------------

1. Rank starts from 1.
2. Shape parameter (s) > 0.
3. Total probabilities must sum to 1.

------------------------------------------------------------
Properties
------------------------------------------------------------

• Discrete probability distribution.
• Higher-ranked items have higher probabilities.
• Lower-ranked items become increasingly rare.
• Probability decreases as rank increases.

============================================================
"""

import math
import random

# ----------------------------------------------------------
# Function to calculate normalization constant
# ----------------------------------------------------------
def normalization_constant(N, s):
    """
    Calculates the denominator:
    Σ (1 / k^s)
    """
    total = 0
    for k in range(1, N + 1):
        total += 1 / (k ** s)
    return total


# ----------------------------------------------------------
# Function to calculate Zipf Probability
# ----------------------------------------------------------
def zipf_probability(rank, N, s):
    """
    Calculates probability of a given rank.

    Parameters:
    rank : Item rank
    N    : Total number of items
    s    : Shape parameter

    Returns:
    Probability
    """
    H = normalization_constant(N, s)
    probability = (1 / (rank ** s)) / H
    return probability


# ==========================================================
# Example
# ==========================================================

print("=" * 60)
print("             ZIPF DISTRIBUTION EXAMPLE")
print("=" * 60)

N = 10          # Total ranked items
s = 1.2         # Shape parameter

print(f"\nTotal Items (N): {N}")
print(f"Shape Parameter (s): {s}")

print("\nRank\tProbability")
print("-" * 30)

for rank in range(1, N + 1):
    prob = zipf_probability(rank, N, s)
    print(f"{rank}\t{prob:.4f}")

# ==========================================================
# Verify Total Probability
# ==========================================================

total_probability = 0

for rank in range(1, N + 1):
    total_probability += zipf_probability(rank, N, s)

print("\n")
print("=" * 60)
print("Verification")
print("=" * 60)

print(f"Sum of Probabilities = {total_probability:.4f}")

# ==========================================================
# Random Zipf Samples
# ==========================================================

print("\n")
print("=" * 60)
print("Random Zipf Samples")
print("=" * 60)

for i in range(10):
    sample = random.zipf(s)
    print(f"Sample {i+1}: Rank {sample}")

# ==========================================================
# Applications
# ==========================================================

print("\n")
print("=" * 60)
print("Applications")
print("=" * 60)

applications = [
    "1. Word frequency analysis.",
    "2. Search engine ranking.",
    "3. Website popularity.",
    "4. City population studies.",
    "5. Library book usage.",
    "6. Product sales ranking.",
    "7. Social media popularity.",
    "8. Natural Language Processing (NLP)."
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
The Zipf Distribution assigns probabilities based
on an item's rank.

Rank 1 has the highest probability.

As the rank increases,
the probability decreases.

For N = {N} items and s = {s},
the probabilities sum to approximately 1.

This distribution is widely used in language
processing, web search, economics, and
population studies.
""")

print("=" * 60)
print("End of Program")
print("=" * 60)


print("next session-- ufunc")