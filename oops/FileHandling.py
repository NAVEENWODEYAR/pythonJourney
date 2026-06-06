# ==========================================
# Python Program for File Input
# ==========================================

# This program reads data from a text file
# and displays its contents line by line.

# File name to be read
filename = "sample.txt"

try:
    # Open the file in read mode ('r')
    with open(filename, "r") as file:

        print("Contents of the file:\n")

        # Read file line by line
        for line in file:

            # strip() removes extra newline characters
            print(line.strip())

except FileNotFoundError:
    # Executes if the file does not exist
    print("Error: File not found.")

except Exception as e:
    # Handles any other unexpected errors
    print("An error occurred:", e)