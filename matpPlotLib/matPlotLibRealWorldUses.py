"""
===========================================================
MATPLOTLIB REAL-WORLD BUSINESS ANALYTICS DASHBOARD
===========================================================

This program demonstrates how Matplotlib is used in real
companies to visualize and analyze business data.

Real-world scenarios covered:
1. Monthly Sales Analysis
2. Website Traffic Monitoring
3. Customer Satisfaction Analysis

Charts used:
- Line Chart
- Bar Chart
- Pie Chart

Required Installation:
pip install matplotlib
===========================================================
"""

# Import Matplotlib library
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# DATASET 1: MONTHLY SALES DATA
# ---------------------------------------------------------
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

# Sales revenue in thousands of dollars
sales = [45, 52, 48, 61, 67, 72]

# ---------------------------------------------------------
# DATASET 2: WEBSITE TRAFFIC DATA
# ---------------------------------------------------------
website_visitors = [1200, 1350, 1280, 1600, 1750, 1900]

# ---------------------------------------------------------
# DATASET 3: CUSTOMER FEEDBACK DATA
# ---------------------------------------------------------
feedback_labels = [
    "Excellent",
    "Good",
    "Average",
    "Poor"
]

feedback_counts = [50, 30, 15, 5]

# ---------------------------------------------------------
# BUSINESS ANALYSIS
# ---------------------------------------------------------

# Calculate total sales
total_sales = sum(sales)

# Calculate average sales
average_sales = total_sales / len(sales)

# Find highest sales month
max_sales = max(sales)
max_sales_month = months[sales.index(max_sales)]

# Find highest website traffic
max_visitors = max(website_visitors)
max_visitor_month = months[
    website_visitors.index(max_visitors)
]

# ---------------------------------------------------------
# PRINT BUSINESS REPORT
# ---------------------------------------------------------

print("\n========== BUSINESS REPORT ==========")

print(f"Total Sales: ${total_sales}K")
print(f"Average Monthly Sales: ${average_sales:.2f}K")

print(
    f"Best Sales Month: "
    f"{max_sales_month} (${max_sales}K)"
)

print(
    f"Highest Website Traffic: "
    f"{max_visitor_month} ({max_visitors} visitors)"
)

print("=====================================\n")

# ---------------------------------------------------------
# CREATE DASHBOARD WINDOW
# 1 row and 3 columns of charts
# ---------------------------------------------------------

plt.figure(figsize=(18, 5))

# =========================================================
# CHART 1: SALES TREND (LINE CHART)
# =========================================================

plt.subplot(1, 3, 1)

plt.plot(
    months,
    sales,
    color="blue",
    marker="o",
    linewidth=3
)

plt.title("Monthly Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales ($K)")
plt.grid(True)

# Highlight highest sales point
plt.annotate(
    f"Highest = {max_sales}K",
    xy=(max_sales_month, max_sales),
    xytext=(max_sales_month, max_sales + 8),
    arrowprops=dict(
        facecolor="red",
        arrowstyle="->"
    )
)

# =========================================================
# CHART 2: WEBSITE VISITORS (BAR CHART)
# =========================================================

plt.subplot(1, 3, 2)

bars = plt.bar(
    months,
    website_visitors,
    color="green"
)

plt.title("Website Traffic")
plt.xlabel("Months")
plt.ylabel("Visitors")

# Display values on top of bars
for bar in bars:
    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width()/2,
        height + 20,
        str(height),
        ha='center'
    )

# =========================================================
# CHART 3: CUSTOMER FEEDBACK (PIE CHART)
# =========================================================

plt.subplot(1, 3, 3)

plt.pie(
    feedback_counts,
    labels=feedback_labels,
    autopct='%1.1f%%',
    startangle=90
)

plt.title("Customer Satisfaction")

# ---------------------------------------------------------
# AUTOMATICALLY ADJUST SPACING
# ---------------------------------------------------------
plt.tight_layout()

# ---------------------------------------------------------
# DISPLAY DASHBOARD
# ---------------------------------------------------------
plt.show()