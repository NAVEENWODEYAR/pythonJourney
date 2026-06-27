"""
============================================================
          PARETO DISTRIBUTION - COMPLETE BASICS
============================================================

Definition:
-----------
The Pareto Distribution is a continuous probability
distribution used to describe situations where a small
percentage of causes account for a large percentage of effects.

It is also known as the 80/20 Rule because:
• 80% of the results often come from 20% of the causes.

Examples:
---------
1. 20% of customers generate 80% of sales.
2. 20% of employees produce 80% of the work.
3. Wealth distribution in a country.
4. Website traffic from a few popular pages.
5. File sizes on a computer network.

------------------------------------------------------------
Conditions
------------------------------------------------------------

1. Random variable x must be greater than or equal to xm.
2. Shape parameter α (alpha) must be greater than 0.
3. Scale parameter xm must be positive.

------------------------------------------------------------
Probability Density Function (PDF)
------------------------------------------------------------

                α × xm^α
f(x) = -------------------------------
            x^(α + 1)

Where:
-------
α  = Shape parameter (alpha)
xm = Minimum possible value (scale parameter)
x  = Random variable (x ≥ xm)

------------------------------------------------------------
Cumulative Distribution Function (CDF)
------------------------------------------------------------

               xm
F(x) = 1 - ( ------ )^α
                x

------------------------------------------------------------
Properties
------------------------------------------------------------

Mean = (α × xm) / (α - 1)      (Only if α > 1)

Variance = (α × xm²) /
           ((α - 1)² × (α - 2))   (Only if α > 2)

============================================================
"""

# Import required libraries
import math
import random

# ----------------------------------------------------------
# Function to calculate Pareto PDF
# ----------------------------------------------------------
def pareto_pdf(x, alpha, xm):
    """
    Calculates the Probability Density Function (PDF).

    Parameters:
    x     : Random variable
    alpha : Shape parameter
    xm    : Minimum value (scale parameter)

    Returns:
    PDF value
    """
    if x < xm:
        return 0

    pdf = (alpha * (xm ** alpha)) / (x ** (alpha + 1))
    return pdf


# ----------------------------------------------------------
# Function to calculate Pareto CDF
# ----------------------------------------------------------
def pareto_cdf(x, alpha, xm):
    """
    Calculates the Cumulative Distribution Function (CDF).
    """
    if x < xm:
        return 0

    cdf = 1 - (xm / x) ** alpha
    return cdf


# ==========================================================
# Example
# ==========================================================

print("=" * 60)
print("          PARETO DISTRIBUTION EXAMPLE")
print("=" * 60)

alpha = 3
xm = 2
x = 5

pdf = pareto_pdf(x, alpha, xm)
cdf = pareto_cdf(x, alpha, xm)

print(f"\nShape Parameter (α): {alpha}")
print(f"Minimum Value (xm): {xm}")
print(f"Random Variable (x): {x}")

print(f"\nProbability Density (PDF): {pdf:.5f}")
print(f"Cumulative Probability (CDF): {cdf:.5f}")

# ==========================================================
# Properties
# ==========================================================

print("\n")
print("=" * 60)
print("Properties")
print("=" * 60)

if alpha > 1:
    mean = (alpha * xm) / (alpha - 1)
    print(f"Mean                = {mean:.3f}")
else:
    print("Mean                = Undefined")

if alpha > 2:
    variance = (alpha * xm ** 2) / ((alpha - 1) ** 2 * (alpha - 2))
    print(f"Variance            = {variance:.3f}")
    print(f"Standard Deviation  = {math.sqrt(variance):.3f}")
else:
    print("Variance            = Undefined")

# ==========================================================
# Generate Random Samples
# ==========================================================

print("\n")
print("=" * 60)
print("Random Pareto Samples")
print("=" * 60)

for i in range(10):
    sample = random.paretovariate(alpha) * xm
    print(f"Sample {i+1}: {sample:.3f}")

# ==========================================================
# Applications
# ==========================================================

print("\n")
print("=" * 60)
print("Applications")
print("=" * 60)

applications = [
    "1. Wealth and income distribution.",
    "2. Business sales analysis.",
    "3. Insurance claim analysis.",
    "4. Internet traffic modeling.",
    "5. File size distribution.",
    "6. Population studies.",
    "7. Risk management.",
    "8. Economics and finance."
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
For α = {alpha}, xm = {xm}, and x = {x}:

Probability Density = {pdf:.5f}

Cumulative Probability = {cdf:.5f}

The Pareto Distribution models situations where
a small number of observations contribute to
most of the overall effect (80/20 rule).

It is widely used in economics, finance,
insurance, business, and data analysis.
""")

print("=" * 60)
print("End of Program")
print("=" * 60)