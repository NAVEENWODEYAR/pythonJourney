"""
Program: Introduction to Python
Purpose: Display information about Python, its advantages,
         uses, and major application areas.
Author: Example Program
"""

# Function to display the introduction
def introduction():
    print("=" * 60)
    print("INTRODUCTION TO PYTHON")
    print("=" * 60)
    print("\nPython is a high-level, interpreted, and")
    print("general-purpose programming language.")
    print("It was created by Guido van Rossum and")
    print("released in 1991.")
    print("\nPython is known for its simplicity,")
    print("readability, and extensive library support.")


# Function to display advantages of Python
def advantages():
    print("\n" + "=" * 60)
    print("ADVANTAGES OF PYTHON")
    print("=" * 60)

    advantages_list = [
        "Easy to Learn and Read",
        "Simple and Clean Syntax",
        "Platform Independent",
        "Large Standard Library",
        "Supports Multiple Programming Paradigms",
        "Open Source and Free",
        "Strong Community Support",
        "Suitable for Rapid Application Development"
    ]

    for num, advantage in enumerate(advantages_list, start=1):
        print(f"{num}. {advantage}")


# Function to display uses of Python
def uses():
    print("\n" + "=" * 60)
    print("USES OF PYTHON")
    print("=" * 60)

    print("""
Python is used for:
- Software Development
- Web Application Development
- Data Analysis
- Artificial Intelligence (AI)
- Machine Learning (ML)
- Automation and Scripting
- Scientific Computing
- Game Development
- Cybersecurity Tools
- Cloud Computing Applications
""")


# Function to display main application areas
def application_areas():
    print("\n" + "=" * 60)
    print("MAIN AREAS OF PYTHON USAGE")
    print("=" * 60)

    areas = {
        "Web Development":
            "Frameworks like Django and Flask are used "
            "to build websites and web applications.",

        "Data Science":
            "Libraries such as NumPy, Pandas, and Matplotlib "
            "help analyze and visualize data.",

        "Machine Learning & AI":
            "TensorFlow, PyTorch, and Scikit-learn are used "
            "to build intelligent systems and predictive models.",

        "Automation":
            "Python automates repetitive tasks such as file "
            "management, report generation, and testing.",

        "Cybersecurity":
            "Python is used for network analysis, penetration "
            "testing, and security automation.",

        "Game Development":
            "Libraries like Pygame help create 2D games.",

        "Scientific Computing":
            "Researchers use Python for simulations, "
            "mathematical calculations, and experiments.",

        "Desktop Applications":
            "GUI libraries such as Tkinter and PyQt are used "
            "to build desktop software."
    }

    for area, description in areas.items():
        print(f"\n{area}:")
        print(f"  {description}")


# Main function
def main():
    introduction()
    advantages()
    uses()
    application_areas()

    print("\n" + "=" * 60)
    print("CONCLUSION")
    print("=" * 60)
    print("Python is one of the most popular programming")
    print("languages due to its simplicity, versatility,")
    print("and wide range of applications across industries.")


# Program execution starts here
if __name__ == "__main__":
    main()