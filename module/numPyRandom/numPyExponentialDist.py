"""
============================================================
        EXPONENTIAL DISTRIBUTION - COMPLETE BASICS
============================================================

Definition:
-----------
The Exponential Distribution is a continuous probability
distribution used to model the time between independent
events that occur at a constant average rate.

Examples:
---------
1. Time between customer arrivals.
2. Time until a machine fails.
3. Time between phone calls.
4. Waiting time for a bus.
5. Time between earthquakes.

------------------------------------------------------------
Conditions
------------------------------------------------------------

1. Events occur independently.
2. Average event rate (λ) remains constant.
3. Time between events is continuous.
4. Events follow a Poisson process.

------------------------------------------------------------
Probability Density Function (PDF)
------------------------------------------------------------

          f(x) = λe^(-λx)

Where:
-------
λ (lambda) = Rate parameter (λ > 0)
x = Time (x ≥ 0)
e = Euler's number (2.71828)

------------------------------------------------------------
Cumulative Distribution Function (CDF)
------------------------------------------------------------

          F(x) = 1 - e^(-λx)

------------------------------------------------------------
Properties
------------------------------------------------------------

Mean               = 1 / λ
Variance           = 1 / λ²
Standard Deviation = 1 / λ

============================================================
"""

# Import required libraries
import math
import random

# ----------------------------------------------------------
# Function to calculate PDF
# ----------------------------------------------------------
def exponential_pdf(rate, x):
    """
    Calculates the Probability Density Function (PDF).

    Parameters:
    rate : Lambda (event rate)
    x    : Time

    Returns:
    PDF value
    """
    if x < 0:
        return 0
    return rate * math.exp(-rate * x)


# ----------------------------------------------------------
# Function to calculate CDF
# ----------------------------------------------------------
def exponential_cdf(rate, x):
    """
    Calculates the Cumulative Distribution Function (CDF).

    Parameters:
    rate : Lambda (event rate)
    x    : Time

    Returns:
    CDF value
    """
    if x < 0:
        return 0
    return 1 - math.exp(-rate * x)


# ==========================================================
# Example
# ==========================================================

print("=" * 60)
print("        EXPONENTIAL DISTRIBUTION EXAMPLE")
print("=" * 60)

# Rate parameter
rate = 0.5

# Time
x = 3

pdf = exponential_pdf(rate, x)
cdf = exponential_cdf(rate, x)

print(f"\nRate (λ) : {rate}")
print(f"Time (x) : {x}")

print(f"\nProbability Density (PDF) = {pdf:.5f}")
print(f"Cumulative Probability (CDF) = {cdf:.5f}")

# ==========================================================
# Properties
# ==========================================================

mean = 1 / rate
variance = 1 / (rate ** 2)
std = 1 / rate

print("\n")
print("=" * 60)
print("Properties")
print("=" * 60)

print(f"Mean                = {mean:.2f}")
print(f"Variance            = {variance:.2f}")
print(f"Standard Deviation  = {std:.2f}")

# ==========================================================
# Generate Random Values
# ==========================================================

print("\n")
print("=" * 60)
print("Random Waiting Times")
print("=" * 60)

for i in range(10):
    value = random.expovariate(rate)
    print(f"Sample {i+1}: {value:.2f}")

# ==========================================================
# Applications
# ==========================================================

print("\n")
print("=" * 60)
print("Applications")
print("=" * 60)

applications = [
    "1. Waiting time between customer arrivals.",
    "2. Predicting machine failures.",
    "3. Queueing systems.",
    "4. Network packet arrival times.",
    "5. Reliability engineering.",
    "6. Survival analysis.",
    "7. Telecommunication systems.",
    "8. Service center waiting times."
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
The average event rate is λ = {rate} events per unit time.

The probability density at time x = {x}
is {pdf:.5f}.

The probability that an event occurs within
{x} time units is {cdf:.5f}.

The Exponential Distribution is widely used
to model waiting times between random events.
""")

print("=" * 60)
print("End of Program")
print("=" * 60)