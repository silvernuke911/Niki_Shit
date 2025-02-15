import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import numpy as np
from itertools import product

def dicer0(n, num_dice, density=False):
    """
    Simulates rolling multiple dice and computes the distribution of sums.

    Parameters:
    -----------
    n : int
        Number of sides on each die.
    num_dice : int
        Number of dice to roll.
    density : bool, optional (default=False)
        If True, returns the probability distribution instead of raw counts.

    Returns:
    --------
    tuple
        - ranges : np.array
            Possible sum values from rolling `num_dice` dice.
        - counts : np.array
            Count of occurrences for each sum (or probability if `density=True`).
    """
    total = n**num_dice  # Total possible outcomes
    ranges = np.arange(num_dice, num_dice * n + 1)  # Possible sum values
    counts = np.zeros_like(ranges, dtype=int)  # Store sum frequencies

    # Generate all possible outcomes
    for outcome in product(range(1, n + 1), repeat=num_dice):
        counts[sum(outcome) - num_dice] += 1

    if density:
        return ranges, counts / total  # Return probability distribution
    return ranges, counts  # Return raw counts

import numpy as np
from scipy.special import comb  # For binomial coefficients

def dicer(n, num_dice, density=True):
    """
    Computes the probability mass function (PMF) for the sum of `num_dice` fair dice.
    
    Parameters:
    -----------
    n : int
        Number of sides per die.
    num_dice : int
        Number of dice rolled.
    density : bool, optional (default=True)
        If True, returns the probability distribution instead of raw counts.

    Returns:
    --------
    tuple
        - ranges : np.array
            Possible sum values from rolling `num_dice` dice.
        - counts : np.array
            Count of occurrences for each sum (or probability if `density=True`).
    """
    ranges = np.arange(num_dice, num_dice * n + 1, dtype = int)  # Possible sum values
    total = n**num_dice  # Total number of outcomes
    counts = np.zeros_like(ranges, dtype=np.float64)  # Store frequencies

    # Compute probabilities using the explicit formula
    for i, S in enumerate(ranges):
        sum_term = 0
        for j in range((S - num_dice) // n + 1):
            sum_term += (-1)**j * comb(num_dice, j) * comb(S - j * n - 1, num_dice - 1)
    # P(S) = \frac{1}{n^{\text{num_dice}}} \sum_{j=0}^{\lfloor \frac{S - \text{num_dice}}{n} \rfloor} (-1)^j \binom{\text{num_dice}}{j} \binom{S - j n - 1}{\text{num_dice} - 1}
        counts[i] = sum_term

    if density:
        return ranges, counts / total, (ranges[0], ranges[-1])   # Normalize to get probabilities
    return ranges, counts.astype(int)  # Convert counts to integers if density=False

x,y,lims = dicer(20,10, density = True)
plt.figure(figsize=(6,6))
plt.xlim(lims[0]-0.5, lims[1]+0.5)
plt.bar(x,y, width = 1, color = 'r', edgecolor = 'k')
plt.show()