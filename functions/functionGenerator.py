# =====================================================
# GENERATOR EXAMPLE IN PYTHON
# =====================================================

# Generator function using 'yield'
# It generates numbers one by one instead of storing them in memory

def simple_generator():

    # First value
    yield 1

    # Function pauses here and resumes later
    yield 2

    yield 3


# Create generator object
gen = simple_generator()

# Fetch values one by one using next()
print("First value:", next(gen))   # runs until first yield
print("Second value:", next(gen))  # resumes from last yield
print("Third value:", next(gen))   # resumes again

# After last value, next(gen) would raise StopIteration error