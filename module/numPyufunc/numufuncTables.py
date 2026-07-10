# Function to print the multiplication table of a given number
def print_table(number):
    # Loop from 1 to 10
    for i in range(1, 11):
        # Display the multiplication result
        print(f"{number} x {i} = {number * i}")


# Take input from the user
num = int(input("Enter a number: "))

# Call the function to print the table
print("\nMultiplication Table:")
print_table(num)