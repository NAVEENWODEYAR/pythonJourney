"""
============================================================
          CHI-SQUARE DISTRIBUTION - COMPLETE BASICS
============================================================

Definition:
-----------
The Chi-Square (χ²) Distribution is a continuous probability
distribution used mainly in hypothesis testing and statistics.

It is obtained by adding the squares of independent standard
normal random variables.

Examples:
---------
1. Chi-Square Test of Independence
2. Goodness-of-Fit Test
3. Test of Population Variance
4. Feature Selection in Machine Learning

------------------------------------------------------------
Conditions
------------------------------------------------------------

1. Data should be randomly selected.
2. Observations should be independent.
3. Expected frequency in each category should usually be ≥ 5.
4. Degrees of Freedom (df) must be greater than 0.

------------------------------------------------------------
Chi-Square Test Statistic
------------------------------------------------------------

            χ² = Σ ((O - E)² / E)

Where:
-------
O = Observed Frequency
E = Expected Frequency
Σ = Sum over all categories

------------------------------------------------------------
Properties
------------------------------------------------------------

Mean               = Degrees of Freedom (df)

Variance           = 2 × df

Standard Deviation = √(2 × df)

The distribution is:
• Continuous
• Positively skewed
• Becomes more symmetric as df increases

============================================================
"""

# Import required libraries
import math
import random

# ----------------------------------------------------------
# Function to calculate Chi-Square statistic
# ----------------------------------------------------------
def chi_square(observed, expected):
    """
    Calculates the Chi-Square statistic.

    Parameters:
    observed : List of observed frequencies
    expected : List of expected frequencies

    Returns:
    Chi-Square value
    """
    chi = 0

    for o, e in zip(observed, expected):
        chi += ((o - e) ** 2) / e

    return chi


# ==========================================================
# Example
# ==========================================================

print("=" * 60)
print("         CHI-SQUARE DISTRIBUTION EXAMPLE")
print("=" * 60)

# Observed frequencies
observed = [18, 22, 20, 40]

# Expected frequencies
expected = [25, 25, 25, 25]

chi = chi_square(observed, expected)

print("\nObserved Frequencies :", observed)
print("Expected Frequencies :", expected)

print(f"\nChi-Square Statistic = {chi:.2f}")

# ==========================================================
# Degrees of Freedom
# ==========================================================

df = len(observed) - 1

print("\n")
print("=" * 60)
print("Distribution Properties")
print("=" * 60)

print("Degrees of Freedom :", df)
print("Mean               :", df)
print("Variance           :", 2 * df)
print("Standard Deviation :", round(math.sqrt(2 * df), 2))

# ==========================================================
# Random Chi-Square Samples
# ==========================================================

print("\n")
print("=" * 60)
print("Random Chi-Square Samples")
print("=" * 60)

for i in range(10):
    sample = random.gammavariate(df / 2, 2)
    print(f"Sample {i+1}: {sample:.2f}")

# ==========================================================
# Applications
# ==========================================================

print("\n")
print("=" * 60)
print("Applications")
print("=" * 60)

applications = [
    "1. Goodness-of-Fit Test.",
    "2. Test of Independence.",
    "3. Test of Homogeneity.",
    "4. Population Variance Testing.",
    "5. Machine Learning Feature Selection.",
    "6. Medical Research.",
    "7. Survey Data Analysis.",
    "8. Quality Control."
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
Observed Frequencies : {observed}
Expected Frequencies : {expected}

Chi-Square Statistic = {chi:.2f}

Degrees of Freedom = {df}

A larger Chi-Square value indicates a greater difference
between the observed and expected frequencies.

The Chi-Square Distribution is widely used in hypothesis
testing to determine whether observed data differs
significantly from expected data.
""")

print("=" * 60)
print("End of Program")
print("=" * 60)