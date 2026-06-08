# =====================================================
# COMPLETE FILE HANDLING PROGRAM IN PYTHON
# =====================================================

# -----------------------------------------------------
# Function 1: Create and Write to File
# -----------------------------------------------------
def create_and_write():
    """
    Creates a new file and writes data into it.
    If file already exists, content is overwritten.
    """

    with open("student.txt", "w") as file:
        file.write("Name: John\n")
        file.write("Age: 22\n")
        file.write("Course: Python Programming\n")

    print("File created and data written successfully.")


# -----------------------------------------------------
# Function 2: Read Entire File
# -----------------------------------------------------
def read_file():
    """
    Reads entire file content.
    """

    try:
        with open("student.txt", "r") as file:
            content = file.read()

        print("\n----- FILE CONTENT -----")
        print(content)

    except FileNotFoundError:
        print("File does not exist.")


# -----------------------------------------------------
# Function 3: Append Data
# -----------------------------------------------------
def append_data():
    """
    Adds new data at the end of file.
    """

    with open("student.txt", "a") as file:
        file.write("City: Bangalore\n")

    print("New data appended successfully.")


# -----------------------------------------------------
# Function 4: Read Line by Line
# -----------------------------------------------------
def read_line_by_line():
    """
    Reads file one line at a time.
    """

    print("\n----- LINE BY LINE OUTPUT -----")

    with open("student.txt", "r") as file:

        for line in file:
            print(line.strip())


# -----------------------------------------------------
# Function 5: Count Lines
# -----------------------------------------------------
def count_lines():
    """
    Counts total number of lines.
    """

    with open("student.txt", "r") as file:

        lines = file.readlines()

    print("\nTotal Lines =", len(lines))


# -----------------------------------------------------
# Function 6: Count Words
# -----------------------------------------------------
def count_words():
    """
    Counts total words in file.
    """

    with open("student.txt", "r") as file:

        content = file.read()

    words = content.split()

    print("Total Words =", len(words))


# -----------------------------------------------------
# Function 7: Display File Information
# -----------------------------------------------------
def file_info():
    """
    Displays file size.
    """

    import os

    size = os.path.getsize("student.txt")

    print("File Size =", size, "bytes")


# -----------------------------------------------------
# MAIN PROGRAM
# -----------------------------------------------------
print("=" * 50)
print("      PYTHON FILE HANDLING DEMONSTRATION")
print("=" * 50)

# Step 1
create_and_write()

# Step 2
read_file()

# Step 3
append_data()

# Step 4
read_file()

# Step 5
read_line_by_line()

# Step 6
count_lines()

# Step 7
count_words()

# Step 8
file_info()

print("\nProgram Executed Successfully.")