# ==========================================
# DECORATOR EXAMPLE IN PYTHON
# ==========================================

# A decorator is a function that takes another function as an argument,
# adds extra functionality to it, and returns the modified function.

# Step 1: Create a decorator function
def my_decorator(func):

    # Step 2: Create a wrapper function
    # This function adds extra behavior before and after the original function.
    def wrapper():
        print("Before calling the function")

        # Call the original function
        func()

        print("After calling the function")

    # Return the wrapper function
    return wrapper


# Step 3: Apply the decorator using @
@my_decorator
def greet():
    print("Hello, Welcome to Python Decorators!")


# Step 4: Call the function
greet()