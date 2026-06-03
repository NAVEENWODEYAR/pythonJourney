# ============================================
# Python Exception Handling Demonstration
# ============================================

# ------------------------------------------------
# 1. Basic Try-Except
# ------------------------------------------------

print("1. Basic Try-Except")

try:
    num = int(input("Enter a number: "))
    
    result = 100 / num
    
    print("Result:", result)

except ZeroDivisionError:
    
    print("Error: Division by zero is not allowed.")

print()


# ------------------------------------------------
# 2. Handling Multiple Exceptions
# ------------------------------------------------

print("2. Multiple Exceptions")

try:
    
    number = int(input("Enter a number: "))
    
    result = 50 / number
    
    print(result)

except ZeroDivisionError:
    
    print("Cannot divide by zero.")

except ValueError:
    
    print("Please enter a valid integer.")

print()


# ------------------------------------------------
# 3. Using Else Block
# ------------------------------------------------

print("3. Else Block")

try:
    
    num = int(input("Enter a number: "))
    
    result = 20 / num

except ZeroDivisionError:
    
    print("Division by zero error.")

else:
    
    print("Result:", result)
    
    print("No exception occurred.")

print()


# ------------------------------------------------
# 4. Using Finally Block
# ------------------------------------------------

print("4. Finally Block")

try:
    
    file = open("sample.txt", "r")
    
    content = file.read()
    
    print(content)

except FileNotFoundError:
    
    print("File does not exist.")

finally:
    
    print("Finally block executed.")

print()


# ------------------------------------------------
# 5. Catching All Exceptions
# ------------------------------------------------

print("5. Generic Exception")

try:
    
    x = int(input("Enter number: "))
    
    print(100 / x)

except Exception as error:
    
    print("Error:", error)

print()


# ------------------------------------------------
# 6. Raising Custom Exceptions
# ------------------------------------------------

print("6. Raise Exception")

try:
    
    age = int(input("Enter age: "))
    
    if age < 18:
        
        raise ValueError(
            "Age must be 18 or above."
        )
    
    print("Eligible")

except ValueError as e:
    
    print("Error:", e)

print()


# ------------------------------------------------
# Program End
# ------------------------------------------------

print("Exception Handling Demonstration Completed!")
print("\n next session- OOP \n")