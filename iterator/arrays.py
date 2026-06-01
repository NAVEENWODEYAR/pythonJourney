# =====================================================
# ARRAYS (LISTS) IN PYTHON - DEMONSTRATION
# =====================================================

# Creating an array (list)
numbers = [10, 20, 30, 40, 50]

# -----------------------------------------------------
# 1. Accessing elements using index
# -----------------------------------------------------
print("First element:", numbers[0])
print("Third element:", numbers[2])

# -----------------------------------------------------
# 2. Modifying elements
# -----------------------------------------------------
numbers[1] = 25   # changing 20 to 25
print("Updated array:", numbers)

# -----------------------------------------------------
# 3. Traversing (looping through array)
# -----------------------------------------------------
print("All elements in array:")
for num in numbers:
    print(num)

# -----------------------------------------------------
# 4. Adding elements
# -----------------------------------------------------
numbers.append(60)
print("After adding 60:", numbers)

# -----------------------------------------------------
# 5. Removing elements
# -----------------------------------------------------
numbers.remove(30)
print("After removing 30:", numbers)

# -----------------------------------------------------
# 6. Length of array
# -----------------------------------------------------
print("Length of array:", len(numbers))