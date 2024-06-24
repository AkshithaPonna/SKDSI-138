import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate random data
random_data = np.random.normal(loc=0, scale=1, size=1000)

# Create a histogram
plt.figure(figsize=(10, 6))
plt.hist(random_data, bins=30, edgecolor='black', alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Value Frequency')
plt.grid(True)
plt.show()

# Create a density plot
plt.figure(figsize=(10, 6))
sns.kdeplot(random_data, fill=True)
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Density Plot of Continuous Probability Distribution')
plt.grid(True)
plt.show()
