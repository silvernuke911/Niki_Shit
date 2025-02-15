import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
def science_plot(fontsize = 10):
    import scienceplots
    plt.style.use(['science','grid','notebook'])
    plt.rcParams.update({
        'font.size'       : fontsize,    # General font size
        'axes.titlesize'  : fontsize,    # Font size of the axes title
        'axes.labelsize'  : fontsize,    # Font size of the axes labels
        'xtick.labelsize' : fontsize,    # Font size of the x-axis tick labels
        'ytick.labelsize' : fontsize,    # Font size of the y-axis tick labels
        'legend.fontsize' : fontsize,    # Font size of the legend
        'figure.titlesize': fontsize,    # Font size of the figure title
        'legend.fancybox' : False,       # Disable the fancy box for legend
        'legend.edgecolor': 'k',         # Set legend border color to black
        'text.usetex'     : True,        # Use LaTeX for text rendering
        'font.family'     : 'serif'      # Set font family to serif
    })
science_plot()

a = 2
b = 5
x = np.arange(-10, 10)

def wave_func(x, a, b):
    A = np.sqrt(3 / b)
    y = np.zeros_like(x, dtype=float)  # Initialize an array of zeros
    
    # Apply conditions using NumPy's vectorized operations
    y = np.where((x > 0) & (x < a), A * (x / a), y)
    y = np.where((x > a) & (x < b), A * (b - x) / (b - a), y)

    return y
y = wave_func(x, a, b)
plt.plot(x,y)
plt.show()