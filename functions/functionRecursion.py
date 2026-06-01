# =====================================================
# RECURSION PROGRAM - FACTORIAL OF A NUMBER
# =====================================================

# Factorial of n (written as n!) means:
# n! = n × (n-1) × (n-2) × ... × 1
# Example: 5! = 5 × 4 × 3 × 2 × 1 = 120

# We will solve this using RECURSION
# Recursion means a function calling itself

def factorial(n):

    # -------------------------------
    # BASE CONDITION (VERY IMPORTANT)
    # -------------------------------
    # This stops the recursion.
    # Without this, function will run forever.
    if n == 0 or n == 1:
        return 1

    # -------------------------------
    # RECURSIVE CASE
    # -------------------------------
    # Function calls itself with smaller value (n - 1)
    # This breaks the problem into smaller subproblems
    return n * factorial(n - 1)


# -------------------------------
# MAIN PROGRAM
# -------------------------------

# Take input from user
num = int(input("Enter a number: "))

# Call recursive function
result = factorial(num)

# Print final result
print("Factorial of", num, "is", result)