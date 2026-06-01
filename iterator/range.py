# =====================================================
# RANGE FUNCTION DEMONSTRATION IN PYTHON
# =====================================================

# 1. range(stop)
# Generates numbers from 0 to stop-1

print("range(5):")
for i in range(5):
    print(i, end=" ")
print("\n")  # empty line for separation


# 2. range(start, stop)
# Generates numbers from start to stop-1

print("range(2, 8):")
for i in range(2, 8):
    print(i, end=" ")
print("\n")


# 3. range(start, stop, step)
# step defines increment (or decrement if negative)

print("range(1, 10, 2):")
for i in range(1, 10, 2):
    print(i, end=" ")
print("\n")


# 4. Reverse range
print("range(10, 0, -2):")
for i in range(10, 0, -2):
    print(i, end=" ")
print()