# ==================================================
# NORMAL DISTRIBUTION DEMONSTRATION
# ==================================================

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Mean and Standard Deviation
mean = 50
std_dev = 10

# Generate random samples
data = np.random.normal(
    loc=mean,
    scale=std_dev,
    size=1000
)

# Display basic statistics
print("Generated Data Statistics")
print("-" * 30)

print("Mean :", np.mean(data))
print("Standard Deviation :", np.std(data))
print("Minimum :", np.min(data))
print("Maximum :", np.max(data))

# Plot histogram and density curve
plt.figure(figsize=(8,5))

sns.histplot(
    data,
    kde=True,
    color="skyblue"
)

plt.axvline(
    np.mean(data),
    color="red",
    linestyle="--",
    label="Mean"
)

plt.title("Normal Distribution")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.legend()

plt.show()


print("next session - numPy ufunc");