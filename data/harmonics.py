import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import math

def latexfont():
    plt.rcParams.update({
        'text.usetex' : True,
        'font.family' : 'serif',
        'font.size'   : 12
    })
latexfont()

def Harmonics():
    xlims = (0,4*np.pi)
    x = np.arange(*xlims, 0.001)
    N = 500
    plt.figure(figsize=(10,4))
    for i in range(1,N+1):
        y = 1/i * np.sin(i * x)
        plt.plot(x,y,'k', linewidth = 0.5)
    plt.xlim(*xlims)
    plt.title(r'\textbf{Harmonic waves}')
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    # plt.grid(True)
    plt.show()

# Body Guard Problem by Ma'am
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

mode = 'mid'  # 'mid' or 'assassin'

if mode == 'mid':
    xlims = (0, 1)
elif mode == 'assassin':
    xlims = (-10, 10)

def anim():
    N = 500
    nsteps = 10
    choices = np.zeros((N, 2), dtype=int)
    positions = np.random.rand(N, 2)
    # Generate random choices
    for i in range(N):
        available_numbers = list(set(range(N)) - {i})
        choice = np.random.choice(available_numbers, 2, replace=False)
        choices[i] = choice

    # Simulate midpoint updates
    plt.figure(figsize=(6, 6))
    for t in range(nsteps + 1):
        if t != 0:
            for i in range(N):
                if mode == 'mid':
                    selection_point = (positions[choices[i][0]] + positions[choices[i][1]]) / 2
                elif mode == 'assassin':
                    selection_point = 2 * positions[choices[i][0]] - positions[choices[i][1]]
                positions[i] = selection_point

        plt.clf()  # Clear the plot for the next frame
        for pos in positions:
            plt.plot(pos[0], pos[1], 'k', marker='.')  # Black dots for positions
        plt.title(f'T = {t}')
        plt.xlim(*xlims)
        plt.ylim(*xlims)
        plt.gca().set_aspect('equal')
        plt.grid(True)
        plt.pause(1)  # Pause to visualize updates
    plt.show()


# Body Guard Problem by Ma'am
def stat():
    mode = 'mid'
    N = 1000
    repeats = 100
    nsteps = 5
    choices = np.zeros((N, 2), dtype=int)
    datas = np.zeros((repeats, nsteps + 1))
    plt.figure(figsize=(8, 6))  # Create a single figure for the area evolution plot
    for j in range(repeats):
        print(j)
        positions = np.random.rand(N, 2)  # Reset positions for each run
        area = np.zeros(nsteps + 1)  # Reset area array for each run

        # Generate random choices
        for i in range(N):
            available_numbers = list(set(range(N)) - {i})
            choice = np.random.choice(available_numbers, 2, replace=False)
            choices[i] = choice

        # Simulate midpoint updates
        for t in range(nsteps + 1):
            if t != 0:
                for i in range(N):
                    if mode == 'mid':
                        selection_point = (positions[choices[i][0]] + positions[choices[i][1]]) / 2
                    elif mode == 'assassin':
                        selection_point = 2 * positions[choices[i][0]] - positions[choices[i][1]]
                    positions[i] = selection_point

            # Calculate the convex hull area if there are more than 2 points
            if len(np.unique(positions, axis=0)) > 2:
                try:
                    hull = ConvexHull(positions)
                    hull_area = hull.volume  # Use .area for 2D
                except sp.spatial.qhull.QhullError:
                    hull_area = 0  # Handle exceptions gracefully
            else:
                hull_area = 0

            area[t] = hull_area
        datas[j] = area
        # Plot the area evolution for this run
        plt.plot(range(nsteps + 1), area)

    # Finalize the area evolution plot
    plt.xlabel('Time Steps')
    plt.ylabel('Convex Hull Area')
    plt.title('Convex Hull Area Evolution Over Time')
    plt.grid(True)
    plt.show()

    # Calculate mean and standard deviation
    means = np.mean(datas, axis=0)
    std_devs = np.std(datas, axis=0)
    # Plot the mean with error bars
    time_steps = np.arange(nsteps + 1)
    plt.figure(figsize = (10,5))
    plt.errorbar(time_steps, means, yerr=std_devs, fmt='o-', color = 'k', ecolor='k', capsize=2)
    # Customize the plot
    plt.xlabel('Time Steps')
    plt.ylabel('Convex Hull Area')
    plt.title('Average Convex Hull Area')
    plt.grid(True)
    plt.show()
# anim()

def Harmonic_sum():
    dx = 0.001
    x = np.arange(dx,10+dx,dx)
    def H_x(x, N=1000):
        k = np.arange(1, N)  # Create an array of k values
        term1 = np.sum(1 / k)  # Harmonic series up to N
        term2 = np.sum(1 / (x[:, None] + k), axis=1)  # Sum over the second term for each x
        return term1 - term2
    y = H_x(x)
    y2 = np.log(x+1)
    y3 = y2/y
    plt.plot(x,y,'r')
    plt.plot(x,y2,'b')
    plt.plot(x,y3,'g')
    plt.grid(True)
    plt.show()

def Gamma(z, dx = 0.005, N = 1000):
# Create integration range
    t = np.arange(dx, N, dx)  # Avoid t=0 to prevent division by zero
    # Precompute exponential term (reused for all z)
    exp_t = np.exp(-t)
    # Handle scalar and array input for z
    if np.isscalar(z):
        # Vectorized computation for scalar z
        integrand = t**(z) * exp_t
        return np.sum(integrand) * dx
    else:
        # Vectorized computation for array z using broadcasting
        z = np.asarray(z).reshape(-1, 1)  # Reshape for broadcasting
        integrand = t**(z) * exp_t  # Broadcasted computation
        return np.sum(integrand, axis=1) * dx

def fact(arr):
    arr = np.asarray(arr)  # Ensure the input is a NumPy array
    if not np.all(np.floor(arr) == arr) or np.any(arr < 0):
        raise ValueError("All elements of the input array must be non-negative integers.")
    return np.array([math.factorial(int(x)) for x in arr])
    
Harmonics()
