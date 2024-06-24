import matplotlib.pyplot as plt
import numpy as np

# Data for the plots
x_values = np.linspace(0, 10, 100)
y_values_sin = np.sin(x_values)
y_values_cos = np.cos(x_values)

# Creating subplots
figure, (axis1, axis2) = plt.subplots(2, 1, figsize=(10, 8))

# Plotting the sine function
axis1.plot(x_values, y_values_sin, label='sin(x)', color='blue', linestyle='-')
axis1.set_title('Sine Function')
axis1.set_xlabel('x-axis')
axis1.set_ylabel('sin(x)')
axis1.grid(True)
axis1.legend(loc='upper right')
axis1.set_xticks(np.arange(0, 11, 1))
axis1.set_yticks(np.arange(-1, 1.5, 0.5))
axis1.set_xticklabels([f'{i}' for i in range(11)])
axis1.set_yticklabels([f'{i:.1f}' for i in np.arange(-1, 1.5, 0.5)])
axis1.annotate('Max Value', xy=(np.pi/2, 1), xytext=(np.pi/2+1, 0.8),
               arrowprops=dict(facecolor='black', shrink=0.05))

# Plotting the cosine function
axis2.plot(x_values, y_values_cos, label='cos(x)', color='red', linestyle='--')
axis2.set_title('Cosine Function')
axis2.set_xlabel('x-axis')
axis2.set_ylabel('cos(x)')
axis2.grid(True)
axis2.legend(loc='upper right')
axis2.set_xticks(np.arange(0, 11, 1))
axis2.set_yticks(np.arange(-1, 1.5, 0.5))
axis2.set_xticklabels([f'{i}' for i in range(11)])
axis2.set_yticklabels([f'{i:.1f}' for i in np.arange(-1, 1.5, 0.5)])
axis2.annotate('Min Value', xy=(np.pi, -1), xytext=(np.pi+1, -0.8),
               arrowprops=dict(facecolor='black', shrink=0.05))

# Adjusting layout and saving the figure
plt.tight_layout()
plt.savefig('line_plot_with_annotations.png')
plt.show()
