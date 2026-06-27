"""
===========================================================
            UNIFORM DISTRIBUTION - COMPLETE BASICS
===========================================================

Definition:
-----------
A Uniform Distribution is a probability distribution in
which every value within a given interval has an equal
chance of occurring.

There are two types:
1. Discrete Uniform Distribution
   - A finite number of values.
   - Example: Rolling a fair die.

2. Continuous Uniform Distribution
   - Any value within an interval [a, b].
   - Example: A random number between 10 and 20.

-----------------------------------------------------------
Continuous Uniform Distribution Formula
-----------------------------------------------------------

            1
f(x) = -------------
        (b - a)

Where,
------
a = Lower limit
b = Upper limit
x = Any value between a and b

Condition:
----------
a <= x <= b

Otherwise,
f(x) = 0

-----------------------------------------------------------
Probability Formula
-----------------------------------------------------------

Probability that X lies between c and d:

          d - c
P(c<X<d)=-------
          b - a

-----------------------------------------------------------
Properties
-----------------------------------------------------------

Mean      = (a + b) / 2

Variance  = (b - a)^2 / 12

Standard Deviation = √Variance

===========================================================
"""

import math
import random

# ---------------------------------------------------------
# Function to calculate probability density function (PDF)
# ---------------------------------------------------------
def uniform_pdf(a, b, x):
    """
    Calculates the PDF of a continuous uniform distribution.

    Parameters:
    a : Lower limit
    b : Upper limit
    x : Value

    Returns:
    PDF value
    """

    if a <= x <= b:
        return 1 / (b - a)
    else:
        return 0


# ---------------------------------------------------------
# Function to calculate probability between two values
# ---------------------------------------------------------
def uniform_probability(a, b, c, d):
    """
    Calculates probability P(c < X < d)

    Parameters:
    a, b : Distribution limits
    c, d : Required interval

    Returns:
    Probability
    """

    return (d - c) / (b - a)


# =========================================================
# Example
# =========================================================

print("=" * 60)
print("          UNIFORM DISTRIBUTION EXAMPLE")
print("=" * 60)

# Distribution limits
a = 10
b = 20

# Value whose PDF is required
x = 15

pdf = uniform_pdf(a, b, x)

print(f"\nLower Limit (a) : {a}")
print(f"Upper Limit (b) : {b}")
print(f"Selected Value  : {x}")

print(f"\nProbability Density f({x}) = {pdf:.2f}")


# =========================================================
# Probability Example
# =========================================================

c = 12
d = 18

prob = uniform_probability(a, b, c, d)

print("\n")
print("=" * 60)
print("Probability Example")
print("=" * 60)

print(f"P({c} < X < {d}) = {prob:.2f}")

# =========================================================
# Mean, Variance, Standard Deviation
# =========================================================

mean = (a + b) / 2
variance = ((b - a) ** 2) / 12
std = math.sqrt(variance)

print("\n")
print("=" * 60)
print("Properties")
print("=" * 60)

print(f"Mean                = {mean:.2f}")
print(f"Variance            = {variance:.2f}")
print(f"Standard Deviation  = {std:.2f}")


# =========================================================
# Generate Random Numbers
# =========================================================

print("\n")
print("=" * 60)
print("Random Numbers from Uniform Distribution")
print("=" * 60)

for i in range(10):
    value = random.uniform(a, b)
    print(f"Random Number {i+1}: {value:.2f}")


# =========================================================
# Real-life Applications
# =========================================================

print("\n")
print("=" * 60)
print("Applications of Uniform Distribution")
print("=" * 60)

applications = [
    "1. Random number generation.",
    "2. Computer simulations.",
    "3. Online games and lotteries.",
    "4. Random sampling in statistics.",
    "5. Monte Carlo simulations.",
    "6. Testing algorithms with random inputs.",
    "7. Selecting random passwords or IDs.",
    "8. Load balancing in computer networks.",
    "9. Randomized machine learning algorithms.",
    "10. Probability modeling when all outcomes are equally likely."
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
The random variable X is uniformly distributed
between {a} and {b}.

Every value between {a} and {b}
has the same probability density.

The probability that X lies between
{c} and {d} is {prob:.2f}.

Uniform Distribution is useful whenever
all outcomes within a range are equally likely.
""")

print("=" * 60)
print("End of Program")
print("=" * 60)