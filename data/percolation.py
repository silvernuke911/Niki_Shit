import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import measurements

def generate_grid(L, p):
    """Generate an LxL grid where each site is occupied with probability p."""
    grid = np.random.rand(L, L) < p
    return grid

def check_percolation(grid):
    """Check if the grid has a percolating cluster."""
    # Label clusters
    labeled_grid, num_clusters = measurements.label(grid)
    
    # Find clusters that touch the top row
    top_labels = np.unique(labeled_grid[0])
    
    # Check if any of these clusters touch the bottom row
    bottom_labels = np.unique(labeled_grid[-1])
    
    # Intersection of top and bottom labels indicates percolation
    percolating_clusters = np.intersect1d(top_labels, bottom_labels)
    
    return len(percolating_clusters) > 1  # Ignore label 0 (background)

def plot_grid(grid, title):
    """Plot the grid with occupied and unoccupied sites."""
    plt.figure(figsize=(6, 6))
    plt.imshow(grid, cmap="binary", origin="upper")
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

# Simulation parameters
L = 50  # Grid size
p = 0.8  # Occupation probability

# Generate and analyze grid
grid = generate_grid(L, p)
percolates = check_percolation(grid)

# Plot results
title = f"Percolation: {'Yes' if percolates else 'No'} (p = {p})"
plot_grid(grid, title)
