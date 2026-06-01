# =====================================================
# ITERATION IN PYTHON - COMPLETE DEMONSTRATION
# =====================================================

# -----------------------------------------------------
# PART 1: ITERATION USING FOR LOOP (EASIEST METHOD)
# -----------------------------------------------------
print("1. Iteration using for loop:")

numbers = [10, 20, 30, 40, 50]

# Syntax:
# for variable in iterable:
#     statement

for num in numbers:
    print(num)


print("\n")  # empty line for separation


# -----------------------------------------------------
# PART 2: ITERATION USING ITERATOR (MANUAL METHOD)
# -----------------------------------------------------
print("2. Iteration using iterator:")

# Step 1: Create iterable (list)
data = ["A", "B", "C"]

# Step 2: Convert iterable into iterator
iterator_obj = iter(data)

# Step 3: Use next() to access elements one by one
print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))


print("\n")


# -----------------------------------------------------
# PART 3: HOW FOR LOOP WORKS INTERNALLY
# -----------------------------------------------------
print("3. Internal working of for loop (using iterator):")

values = [1, 2, 3]

# for loop internally does this:
it = iter(values)

while True:
    try:
        print(next(it))
    except StopIteration:
        break


print("\n")


# -----------------------------------------------------
# PART 4: ITERATION ON STRING
# -----------------------------------------------------
print("4. Iteration on string:")

text = "HELLO"

for ch in text:
    print(ch)