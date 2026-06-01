# =====================================================
# PYTHON FUNCTIONS - EXPLANATION WITH EXAMPLES
# =====================================================

# A function is a reusable block of code that performs
# a specific task. Functions help make programs:
# 1. Easier to read
# 2. Easier to maintain
# 3. Reusable (write once, use many times)

# -----------------------------------------------------
# 1. SIMPLE FUNCTION (No parameters)
# -----------------------------------------------------

def greet():
    """
    This function displays a greeting message.
    It does not take any input (parameters).
    """
    print("Hello! Welcome to Python Functions.")

# Calling the function
greet()

print("-" * 50)


# -----------------------------------------------------
# 2. FUNCTION WITH PARAMETERS
# -----------------------------------------------------

def greet_user(name):
    """
    This function accepts a parameter 'name'
    and prints a personalized greeting.
    """
    print(f"Hello, {name}! Nice to meet you.")

# Calling the function with an argument
greet_user("Alice")
greet_user("John")

print("-" * 50)


# -----------------------------------------------------
# 3. FUNCTION THAT RETURNS A VALUE
# -----------------------------------------------------

def add_numbers(a, b):
    """
    This function takes two numbers,
    adds them, and returns the result.
    """
    return a + b

# Store the returned value in a variable
result = add_numbers(10, 20)

print("Sum =", result)

print("-" * 50)


# -----------------------------------------------------
# 4. FUNCTION WITH DEFAULT PARAMETER
# -----------------------------------------------------

def country(name="India"):
    """
    If no argument is provided,
    the default value 'India' is used.
    """
    print("Country:", name)

country()          # Uses default value
country("Japan")   # Uses supplied value

print("-" * 50)


# -----------------------------------------------------
# 5. FUNCTION RETURNING MULTIPLE VALUES
# -----------------------------------------------------

def calculate(a, b):
    """
    Returns multiple values:
    sum, difference, and product.
    """
    return a + b, a - b, a * b

sum_value, diff_value, product_value = calculate(15, 5)

print("Sum:", sum_value)
print("Difference:", diff_value)
print("Product:", product_value)

print("-" * 50)


# -----------------------------------------------------
# 6. FUNCTION USING LOOP
# -----------------------------------------------------

def print_numbers(n):
    """
    Prints numbers from 0 to n.
    """
    for i in range(0, n + 1):
        print(i, end=" ")
    print()  # Move to next line

print_numbers(5)

print("-" * 50)


# -----------------------------------------------------
# 7. FUNCTION TO CHECK EVEN OR ODD
# -----------------------------------------------------

def check_even_odd(number):
    """
    Determines whether a number is even or odd number.
    """
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("7 is", check_even_odd(7))
print("10 is", check_even_odd(10))

print("-" * 50)


# -----------------------------------------------------
# 8. MAIN FUNCTION
# -----------------------------------------------------

def main():
    """
    Main function acts as the entry point
    of the program.
    """
    print("Program executed from main function.")

# This ensures the code runs only when
# the file is executed directly.
if __name__ == "__main__":
    main()