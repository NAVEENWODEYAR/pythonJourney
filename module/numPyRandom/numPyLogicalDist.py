"""
===========================================================
          LOGISTIC DISTRIBUTION - COMPLETE BASICS
===========================================================

Definition:
-----------
The Logistic Distribution is a continuous probability
distribution that is similar in shape to the Normal
Distribution but has heavier tails.

It is commonly used in:
1. Machine Learning (Logistic Regression)
2. Statistics
3. Population Growth Models
4. Binary Classification Problems

-----------------------------------------------------------
Probability Density Function (PDF)
-----------------------------------------------------------

                e^(-(x-μ)/s)
f(x) = -------------------------------
       s * (1 + e^(-(x-μ)/s))²

Where:
------
μ (mu) = Mean (location parameter)
s      = Scale parameter (s > 0)
x      = Random variable

-----------------------------------------------------------
Properties
-----------------------------------------------------------

Mean = μ

Variance = (π² × s²) / 3

Standard Deviation = √Variance

===========================================================
"""

# Import required libraries
import math
import random

# ---------------------------------------------------------
# Function to calculate Logistic PDF
# ---------------------------------------------------------
def logistic_pdf(x, mu, s):
    """
    Calculates the probability density function (PDF)
    of the Logistic Distribution.

    Parameters:
    x  : Value
    mu : Mean (location parameter)
    s  : Scale parameter

    Returns:
    PDF value
    """
    exp_value = math.exp(-(x - mu) / s)
    pdf = exp_value / (s * (1 + exp_value) ** 2)
    return pdf


# =========================================================
# Example
# =========================================================

print("=" * 60)
print("         LOGISTIC DISTRIBUTION EXAMPLE")
print("=" * 60)

# Parameters
mu = 50
s = 5
x = 55

pdf = logistic_pdf(x, mu, s)

print(f"\nMean (μ)           : {mu}")
print(f"Scale (s)          : {s}")
print(f"Selected Value (x) : {x}")

print(f"\nProbability Density f({x}) = {pdf:.5f}")

# =========================================================
# Properties
# =========================================================

variance = (math.pi ** 2 * s ** 2) / 3
std = math.sqrt(variance)

print("\n")
print("=" * 60)
print("Properties")
print("=" * 60)

print(f"Mean                = {mu}")
print(f"Variance            = {variance:.2f}")
print(f"Standard Deviation  = {std:.2f}")

# =========================================================
# Generate Random Numbers
# =========================================================

print("\n")
print("=" * 60)
print("Random Numbers from Logistic Distribution")
print("=" * 60)

for i in range(10):
    value = random.logisticvariate(mu, s)
    print(f"Random Value {i+1}: {value:.2f}")

# =========================================================
# Applications
# =========================================================

print("\n")
print("=" * 60)
print("Applications")
print("=" * 60)

applications = [
    "1. Logistic Regression in Machine Learning.",
    "2. Binary Classification Problems.",
    "3. Population Growth Modeling.",
    "4. Medical Research.",
    "5. Social Science Studies.",
    "6. Risk Analysis.",
    "7. Probability Modeling.",
    "8. Data Science."
]

for app in applications:
    print(app)

# =========================================================
# Interpretation
# =========================================================

print("\n")
print("=" * 60)
print("Interpretation")
print("=" * 60)

print(f"""
The Logistic Distribution has:

Mean = {mu}
Scale = {s}

The probability density at x = {x}
is {pdf:.5f}.

Compared with the Normal Distribution,
the Logistic Distribution has heavier tails,
meaning extreme values are slightly more likely.

It is widely used in machine learning,
especially Logistic Regression for predicting
binary outcomes such as Yes/No or True/False.
""")

print("=" * 60)
print("End of Program")
print("=" * 60)