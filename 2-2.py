import numpy as np
import matplotlib.pyplot as plt

# Set seed for reproducibility
np.random.seed(0)

# Generate random data
x_data = np.random.rand(100)
y_data = 2 * x_data + np.random.normal(0, 0.1, 100)

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(x_data, y_data, alpha=0.7)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot of X vs. Y')
plt.grid(True)
plt.show()
