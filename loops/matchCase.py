# -----------------------------------------
# Python Match-Case Demo Program
# -----------------------------------------
# The match-case statement is similar to
# switch-case in other programming languages.
#
# It helps compare a value against multiple
# possible patterns.
#
# Available from Python 3.10 and above.
# -----------------------------------------

# Taking user input
day_number = int(input("Enter a number (1-7): "))

# Using match-case
match day_number:

    # Case for Monday
    case 1:
        print("Monday")

    # Case for Tuesday
    case 2:
        print("Tuesday")

    # Case for Wednesday
    case 3:
        print("Wednesday")

    # Case for Thursday
    case 4:
        print("Thursday")

    # Case for Friday
    case 5:
        print("Friday")

    # Case for Saturday
    case 6:
        print("Saturday")

    # Case for Sunday
    case 7:
        print("Sunday")

    # Default case if input does not match
    case _:
        print("Invalid input! Please enter 1 to 7.")