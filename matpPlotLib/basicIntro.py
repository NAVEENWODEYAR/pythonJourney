# ============================================================
# PYTHON MATPLOTLIB DEMONSTRATION PROGRAM
# ============================================================
# Purpose:
# This program explains:
# 1. What is Matplotlib?
# 2. Basic Syntax
# 3. Advantages
# 4. Areas of Usage
# 5. Common Functions
# 6. Creates a sample graph
# ============================================================

# Import Matplotlib library
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# Function: Introduction
# ------------------------------------------------------------
def introduction():
    print("=" * 70)
    print("         PYTHON MATPLOTLIB COMPLETE DEMONSTRATION")
    print("=" * 70)

    print("\n1. WHAT IS MATPLOTLIB?")
    print("-" * 40)
    print("Matplotlib is a Python library used for Data Visualization.")
    print("It converts numerical data into charts, graphs, and plots.")
    print("It helps users understand trends, patterns, and comparisons.")

# ------------------------------------------------------------
# Function: Basic Syntax
# ------------------------------------------------------------
def syntax_demo():
    print("\n2. BASIC SYNTAX")
    print("-" * 40)

    print("""
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.plot(x, y)
plt.show()
""")

    print("Explanation:")
    print("plt.plot() -> Creates a graph")
    print("plt.show() -> Displays the graph")

# ------------------------------------------------------------
# Function: Advantages
# ------------------------------------------------------------
def advantages():
    print("\n3. ADVANTAGES OF MATPLOTLIB")
    print("-" * 40)

    print("1. Easy to Learn")
    print("2. Free and Open Source")
    print("3. Professional Quality Graphs")
    print("4. Supports Multiple Chart Types")
    print("5. Works with NumPy and Pandas")
    print("6. Highly Customizable")

# ------------------------------------------------------------
# Function: Areas of Usage
# ------------------------------------------------------------
def usage_areas():
    print("\n4. PRESENT AREAS OF USAGE")
    print("-" * 40)

    print("1. Data Science")
    print("2. Machine Learning")
    print("3. Business Analytics")
    print("4. Finance and Stock Market Analysis")
    print("5. Engineering")
    print("6. Scientific Research")
    print("7. Healthcare Analytics")
    print("8. Educational Projects")

# ------------------------------------------------------------
# Function: Common Functions
# ------------------------------------------------------------
def functions_demo():
    print("\n5. COMMON MATPLOTLIB FUNCTIONS")
    print("-" * 40)

    functions = {
        "plot()"    : "Line Graph",
        "bar()"     : "Bar Chart",
        "scatter()" : "Scatter Plot",
        "hist()"    : "Histogram",
        "pie()"     : "Pie Chart",
        "title()"   : "Graph Title",
        "xlabel()"  : "X-axis Label",
        "ylabel()"  : "Y-axis Label",
        "legend()"  : "Show Legend",
        "grid()"    : "Display Grid",
        "show()"    : "Display Graph"
    }

    for func, purpose in functions.items():
        print(f"{func:<15} --> {purpose}")

# ------------------------------------------------------------
# Function: Create Sample Graph
# ------------------------------------------------------------
def create_graph():
    print("\n6. CREATING SAMPLE GRAPH...")
    print("-" * 40)

    # Sample Data
    months = ["Jan", "Feb", "Mar", "Apr", "May"]
    sales = [1000, 1500, 1800, 2200, 2800]

    # Create Line Graph
    plt.plot(
        months,
        sales,
        color="blue",
        marker="o",
        linewidth=3,
        label="Sales"
    )

    # Graph Title
    plt.title("Monthly Sales Report")

    # Axis Labels
    plt.xlabel("Months")
    plt.ylabel("Sales Amount")

    # Grid
    plt.grid(True)

    # Legend
    plt.legend()

    # Display Graph
    plt.show()

# ------------------------------------------------------------
# MAIN PROGRAM
# ------------------------------------------------------------
introduction()
syntax_demo()
advantages()
usage_areas()
functions_demo()

input("\nPress Enter to display the sample graph...")

create_graph()

print("\nProgram Completed Successfully!")