"""
Real-World Matplotlib Example:
Company Monthly Sales Analysis Dashboard

Objective:
- Visualize monthly sales data.
- Calculate business metrics.
- Identify highest and lowest sales months.
- Display trends using a line chart.

Requirements:
pip install matplotlib
"""

import matplotlib.pyplot as plt

# --------------------------------------------------
# Step 1: Business Data
# Monthly sales revenue (in thousands of dollars)
# --------------------------------------------------
months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

sales = [45, 52, 48, 61, 67, 72, 75, 70, 80, 85, 90, 95]

# --------------------------------------------------
# Step 2: Calculate Business Metrics
# --------------------------------------------------
total_sales = sum(sales)
average_sales = total_sales / len(sales)

highest_sales = max(sales)
highest_month = months[sales.index(highest_sales)]

lowest_sales = min(sales)
lowest_month = months[sales.index(lowest_sales)]

# --------------------------------------------------
# Step 3: Print Business Summary
# --------------------------------------------------
print("\n========== SALES REPORT ==========")
print(f"Total Annual Sales : ${total_sales}K")
print(f"Average Monthly Sales : ${average_sales:.2f}K")
print(f"Highest Sales : ${highest_sales}K ({highest_month})")
print(f"Lowest Sales : ${lowest_sales}K ({lowest_month})")
print("==================================\n")

# --------------------------------------------------
# Step 4: Create Visualization
# --------------------------------------------------
plt.figure(figsize=(12, 6))

# Plot sales trend
plt.plot(
    months,
    sales,
    color="blue",
    marker="o",
    linewidth=3,
    markersize=8,
    label="Monthly Sales"
)

# Highlight highest sales point
plt.scatter(
    highest_month,
    highest_sales,
    color="green",
    s=150,
    label="Highest Sales"
)

# Highlight lowest sales point
plt.scatter(
    lowest_month,
    lowest_sales,
    color="red",
    s=150,
    label="Lowest Sales"
)

# --------------------------------------------------
# Step 5: Add Labels and Title
# --------------------------------------------------
plt.title(
    "Company Monthly Sales Performance - 2025",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Months", fontsize=12)
plt.ylabel("Sales (Thousands of Dollars)", fontsize=12)

# --------------------------------------------------
# Step 6: Add Grid
# --------------------------------------------------
plt.grid(True, linestyle="--", alpha=0.6)

# --------------------------------------------------
# Step 7: Annotate Important Points
# --------------------------------------------------
plt.annotate(
    f"Highest: {highest_sales}K",
    xy=(highest_month, highest_sales),
    xytext=(highest_month, highest_sales + 10),
    arrowprops=dict(facecolor="green", arrowstyle="->"),
)

plt.annotate(
    f"Lowest: {lowest_sales}K",
    xy=(lowest_month, lowest_sales),
    xytext=(lowest_month, lowest_sales + 10),
    arrowprops=dict(facecolor="red", arrowstyle="->"),
)

# --------------------------------------------------
# Step 8: Display Additional Information
# --------------------------------------------------
plt.axhline(
    average_sales,
    color="orange",
    linestyle=":",
    linewidth=2,
    label=f"Average Sales ({average_sales:.1f}K)"
)

# Show legend
plt.legend()

# Adjust layout
plt.tight_layout()

# --------------------------------------------------
# Step 9: Show Chart
# --------------------------------------------------
plt.show()