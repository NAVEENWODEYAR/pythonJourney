"""
============================================================
          RAYLEIGH DISTRIBUTION - COMPLETE BASICS
============================================================

Definition:
-----------
The Rayleigh Distribution is a continuous probability
distribution used to model the magnitude of a two-dimensional
random vector whose components are independent and normally
distributed with equal variance.

Examples:
---------
1. Wind speed analysis.
2. Signal strength in wireless communication.
3. Radar and sonar signal processing.
4. Ocean wave height analysis.
5. Image processing and noise modeling.

------------------------------------------------------------
Conditions
------------------------------------------------------------

1. Random variable x must be non-negative (x ≥ 0).
2. The two underlying variables are independent.
3. Both variables follow a normal distribution with
   mean = 0 and equal variance.

------------------------------------------------------------
Probability Density Function (PDF)
------------------------------------------------------------

                 x
f(x) = ------------------ × e^(-(x²)/(2σ²))
         σ²

Where:
-------
x = Random variable (x ≥ 0)
σ = Scale parameter (σ > 0)

------------------------------------------------------------
Cumulative Distribution Function (CDF)
------------------------------------------------------------

           x²
F(x) = 1 - e^(-(-----))
          2σ²

------------------------------------------------------------
Properties
------------------------------------------------------------

Mean               = σ × √(π / 2)

Variance           = ((4 - π) / 2) × σ²

Standard Deviation = √Variance

============================================================
"""

# Import required libraries
import math
import random

# ----------------------------------------------------------
# Function to calculate Rayleigh PDF
# ----------------------------------------------------------
def rayleigh_pdf(x, sigma):
    """
    Calculates the Probability Density Function (PDF).

    Parameters:
    x     : Random variable
    sigma : Scale parameter

    Returns:
    PDF value
    """
    if x < 0:
        return 0

    pdf = (x / (sigma ** 2)) * math.exp(-(x ** 2) / (2 * sigma ** 2))
    return pdf


# ----------------------------------------------------------
# Function to calculate Rayleigh CDF
# ----------------------------------------------------------
def rayleigh_cdf(x, sigma):
    """
    Calculates the Cumulative Distribution Function (CDF).

    Parameters:
    x     : Random variable
    sigma : Scale parameter

    Returns:
    CDF value
    """
    if x < 0:
        return 0

    cdf = 1 - math.exp(-(x ** 2) / (2 * sigma ** 2))
    return cdf


# ==========================================================
# Example
# ==========================================================

print("=" * 60)
print("          RAYLEIGH DISTRIBUTION EXAMPLE")
print("=" * 60)

sigma = 2
x = 3

pdf = rayleigh_pdf(x, sigma)
cdf = rayleigh_cdf(x, sigma)

print(f"\nScale Parameter (σ): {sigma}")
print(f"Value (x): {x}")

print(f"\nProbability Density (PDF): {pdf:.5f}")
print(f"Cumulative Probability (CDF): {cdf:.5f}")

# ==========================================================
# Properties
# ==========================================================

mean = sigma * math.sqrt(math.pi / 2)
variance = ((4 - math.pi) / 2) * sigma ** 2
std = math.sqrt(variance)

print("\n")
print("=" * 60)
print("Properties")
print("=" * 60)

print(f"Mean                = {mean:.3f}")
print(f"Variance            = {variance:.3f}")
print(f"Standard Deviation  = {std:.3f}")

# ==========================================================
# Generate Random Samples
# ==========================================================

print("\n")
print("=" * 60)
print("Random Rayleigh Samples")
print("=" * 60)

for i in range(10):
    sample = random.weibullvariate(sigma, 2)
    print(f"Sample {i+1}: {sample:.3f}")

# ==========================================================
# Applications
# ==========================================================

print("\n")
print("=" * 60)
print("Applications")
print("=" * 60)

applications = [
    "1. Wireless communication signal strength.",
    "2. Wind speed modeling.",
    "3. Ocean wave height analysis.",
    "4. Radar systems.",
    "5. Sonar systems.",
    "6. Image processing.",
    "7. Medical imaging.",
    "8. Reliability engineering."
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
For σ = {sigma} and x = {x}:

Probability Density = {pdf:.5f}

Cumulative Probability = {cdf:.5f}

The Rayleigh Distribution is useful for modeling
non-negative measurements such as signal amplitudes,
wind speeds, and wave heights.
""")

print("=" * 60)
print("End of Program")
print("=" * 60)