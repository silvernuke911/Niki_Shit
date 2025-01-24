import numpy as np
import matplotlib.pyplot as plt

# Parameters
r_values = np.linspace(1, 5.0, 5000)  # Range of r values
iterations = 1000  # Number of iterations for each r
last = 200  # Number of iterations to plot after transients
x = 1e-5 * np.ones(len(r_values))  # Initial condition for x (small non-zero value)

# Prepare the plot
plt.figure(figsize=(10, 6))

# Generate the bifurcation diagram
for i in range(iterations):
    x = r_values * x * (1 - x)  # Logistic map equation
    if i >= (iterations - last):  # Plot only the last few iterations
        plt.plot(r_values, x, 'k,', alpha=0.5)  # ',' is a small marker

# Customize the plot
plt.title("Bifurcation Diagram of the Logistic Map")
plt.xlabel("$r$")
plt.ylabel("$x$")
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Show the plot
plt.show()
