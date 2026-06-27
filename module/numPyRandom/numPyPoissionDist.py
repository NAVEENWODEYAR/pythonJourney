"""
===========================================================
             POISSON DISTRIBUTION - COMPLETE BASICS
===========================================================

Definition:
-----------
The Poisson Distribution is a probability distribution used
to calculate the probability of a certain number of events
occurring within a fixed interval of time or space.

Examples:
---------
1. Number of customer calls received in one hour.
2. Number of accidents at a traffic signal per day.
3. Number of emails received in one minute.
4. Number of typing mistakes on a page.
5. Number of website visitors per minute.

Conditions for Poisson Distribution:
------------------------------------
1. Events occur independently.
2. Average rate (λ) remains constant.
3. Two events cannot occur at exactly the same instant.
4. Number of events can be 0,1,2,3,...

Formula:
--------

            P(X=x) = (e^(-λ) * λ^x) / x!

Where,
-------
P(X=x) = Probability of getting exactly x events
λ (lambda) = Average number of events
e = Euler's constant (2.71828)
x = Number of occurrences
x! = Factorial of x

===========================================================
"""

# Import required libraries
import math

# -------------------------------
# Function to calculate Poisson Probability
# -------------------------------
def poisson_probability(lam, x):
    """
    Calculates the probability of exactly x events
    using the Poisson formula.

    Parameters:
    lam : Average number of events (λ)
    x   : Number of occurrences

    Returns:
    Probability value
    """

    probability = (math.exp(-lam) * (lam ** x)) / math.factorial(x)
    return probability


# ===========================================================
# Example
# ===========================================================

print("=" * 60)
print("           POISSON DISTRIBUTION EXAMPLE")
print("=" * 60)

# Average number of customer arrivals per hour
lambda_value = 4

# Find probability of exactly 2 customers arriving
x = 2

prob = poisson_probability(lambda_value, x)

print(f"\nAverage arrivals (λ) : {lambda_value}")
print(f"Required events (x)  : {x}")

print("\nUsing Formula:")
print("P(X=x) = (e^(-λ) * λ^x) / x!")

print(f"\nProbability of exactly {x} arrivals = {prob:.4f}")


# ===========================================================
# Display probabilities for multiple values
# ===========================================================

print("\n")
print("=" * 60)
print("Probability Table")
print("=" * 60)

print("x\tProbability")
print("-" * 25)

for i in range(11):
    p = poisson_probability(lambda_value, i)
    print(f"{i}\t{p:.4f}")


# ===========================================================
# Mean and Variance
# ===========================================================

print("\n")
print("=" * 60)
print("Important Properties")
print("=" * 60)

print(f"Mean (Expected Value) = λ = {lambda_value}")
print(f"Variance = λ = {lambda_value}")
print(f"Standard Deviation = √λ = {math.sqrt(lambda_value):.2f}")


# ===========================================================
# Real-life Usage
# ===========================================================

print("\n")
print("=" * 60)
print("Where is Poisson Distribution Used?")
print("=" * 60)

uses = [
    "1. Number of phone calls received in a call center.",
    "2. Number of customers entering a supermarket.",
    "3. Number of road accidents at a junction.",
    "4. Number of printing errors in a book.",
    "5. Number of emails received per hour.",
    "6. Number of machine failures in a factory.",
    "7. Number of patients arriving at a hospital.",
    "8. Number of defects in manufactured products.",
    "9. Number of network requests reaching a server.",
    "10. Number of goals scored in some sports analyses."
]

for item in uses:
    print(item)


# ===========================================================
# Interpretation
# ===========================================================

print("\n")
print("=" * 60)
print("Interpretation")
print("=" * 60)

print(f"""
If the average customer arrival rate is {lambda_value} per hour,

The probability of getting exactly {x} customers
in one hour is {prob:.4f}

This means there is approximately {prob*100:.2f}% chance
that exactly {x} customers will arrive.

The Poisson Distribution is especially useful when we
know the average occurrence rate but want to predict
the probability of a specific number of events.
""")

print("=" * 60)
print("End of Program")
print("=" * 60)