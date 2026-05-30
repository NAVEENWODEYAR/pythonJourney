# Python Program to Demonstrate Lists

# Creating a list
fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Original List:")
print(fruits)

# Accessing elements
print("\nFirst element:", fruits[0])
print("Last element:", fruits[-1])

# Adding elements
fruits.append("Grapes")
print("\nAfter append():")
print(fruits)

# Inserting elements
fruits.insert(1, "Pineapple")
print("\nAfter insert():")
print(fruits)

# Removing elements
fruits.remove("Banana")
print("\nAfter remove():")
print(fruits)

# Popping elements
removed_item = fruits.pop()
print("\nAfter pop():")
print("Removed item:", removed_item)
print(fruits)

# Updating elements
fruits[2] = "Kiwi"
print("\nAfter updating an element:")
print(fruits)

# List length
print("\nLength of list:", len(fruits))

# Sorting list
fruits.sort()
print("\nAfter sort():")
print(fruits)

# Reversing list
fruits.reverse()
print("\nAfter reverse():")
print(fruits)

# Looping through list
print("\nLooping through the list:")
for fruit in fruits:
    print(fruit)

# Checking element existence
if "Apple" in fruits:
    print("\nApple is in the list")

# List slicing
print("\nSliced List (first 2 elements):")
print(fruits[:2])

# Clearing the list
fruits.clear()
print("\nAfter clear():")
print(fruits)