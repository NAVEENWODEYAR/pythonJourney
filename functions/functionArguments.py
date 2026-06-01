# Function demonstrating different types of arguments

def student_info(name, age=18, *subjects, **details):
    print("Name:", name)
    print("Age:", age)

    print("Subjects:")
    for subject in subjects:
        print("-", subject)

    print("Additional Details:")
    for key, value in details.items():
        print(f"{key}: {value}")

# Function call
student_info(
    "John",                 # Positional argument
    20,                     # Positional argument
    "Python", "Java",       # Variable-length arguments (*args)
    city="Bangalore",       # Keyword argument (**kwargs)
    college="ABC College"
)