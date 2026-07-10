# Program to generate a random newborn baby name

import random

# List of baby boy names
boy_names = [
    "Aarav", "Vivaan", "Aditya", "Arjun", "Vihaan",
    "Krishna", "Ishaan", "Reyansh", "Aryan", "Kabir"
]

# List of baby girl names
girl_names = [
    "Anaya", "Aadhya", "Kiara", "Diya", "Saanvi",
    "Myra", "Anika", "Riya", "Avni", "Meera"
]

# Function to generate a random baby name
def generate_name(gender):
    if gender.lower() == "boy":
        return random.choice(boy_names)
    elif gender.lower() == "girl":
        return random.choice(girl_names)
    else:
        return "Invalid gender! Please enter 'boy' or 'girl'."

# Take user input
gender = input("Enter baby's gender (boy/girl): ")

# Display the generated name
print("\nSuggested Baby Name:")
print(generate_name(gender))