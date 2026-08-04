# Simple calculator using match-case

# Read two numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Read the operator
operator = input("Enter operator (+, -, *, /): ")

# Match the operator
match operator:
    case "+":
        print("Result =", num1 + num2)

    case "-":
        print("Result =", num1 - num2)

    case "*":
        print("Result =", num1 * num2)

    case "/":
        # Check for division by zero
        if num2 != 0:
            print("Result =", num1 / num2)
        else:
            print("Error: Division by zero is not allowed.")

    case _:
        # Runs if the operator is invalid
        print("Invalid operator!")