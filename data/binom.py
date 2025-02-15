import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
def binomial_pmf(n, p, k = 0, scale = 1, array = True, cdf = False, stat = False):
    """
    Computes the probability mass function (PMF) of the binomial distribution.

    Parameters:
    -----------
    n : int
        The number of trials.
    p : float
        The probability of success in each trial.
    k : int, optional (default=0)
        The number of successful events. Ignored if `array=True` or `cdf=True`.
    scale : float, optional (default=1)
        A scaling factor applied to the probability.
    array : bool, optional (default=True)
        If True, returns the PMF for all values of k (0 to n).
    cdf : bool, optional (default=False)
        If True, returns the k values and cumulative distribution function (CDF).
    stat : bool, optional (default=False)
        If True, returns statistical properties of the binomial distribution. Overrides cmf and cdf

    Returns:
    --------
    - If `array` is True: Returns two arrays (k values and PMF values).
    - If `cdf` is True: Returns two arrays of k and  cumulative probabilities.
    - If `stat` is True: Returns a tuple (PMF, dictionary of statistics).
    - Otherwise: Returns the probability mass function for a single `k`.

    Raises:
    -------
    ValueError:
        - If `n` or `k` are negative.
        - If `k` is greater than `n`.
        - If `p` is greater than 1

    Notes:
    ------
    - Uses a custom factorial and combination function.
    - The binomial PMF is given by:

      .. math::
         P(X = k) = \binom{n}{k} p^k (1 - p)^{n-k}
    """
    def fact(n):
        if n < 0:
            raise ValueError("n must be non-negative")
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    def choose(n, k):
        if k > n:
            raise ValueError("k must not be greater than n")
        return fact(n) / (fact(k) * fact(n - k))
    if p > 1 or p < 0:
        raise ValueError('p cannot be greater than 1 or lesser than 0')
    q = 1 - p  # Probability of failure
    k_vals = np.arange(0, n + 1)
    pmf_vals = np.array([choose(n, k) * p**k * q**(n - k) * scale for k in k_vals])
    if stat:
        stats = {
            "mean": n * p,
            "variance": n * p * q,
            "standard deviation": np.sqrt(n * p * q),
            "skewness": (q - p) / np.sqrt(n * p * q),
            "kurtosis": (1 - 6 * p * q) / (n * p * q) if n * p * q > 0 else float("inf"),
            'total area': np.sum(pmf_vals)
        }
        stats = pd.DataFrame.from_dict(stats, orient="index", columns=["Value"])
        return stats
    if array or cdf:
        if cdf:
            return k_vals, np.cumsum(pmf_vals)
        return k_vals, pmf_vals
    pmf = choose(n, k) * p**k * q**(n - k) * scale
    return pmf

import numpy as np
from scipy.stats import norm

def normal_pdf(x, mu, sigma, scale=1, cdf=False, stat=False):
    """
    Computes the probability density function (PDF) of the normal (Gaussian) distribution.

    Parameters:
    -----------
    x : float or array-like
        The value(s) at which to evaluate the normal distribution.
    mu : float
        The mean (center) of the distribution.
    sigma : float
        The standard deviation of the distribution.
    scale : float, optional (default=1)
        A scaling factor applied to the probability density.
    cdf : bool, optional (default=False)
        If True, returns the cumulative distribution function (CDF) instead of the PDF.
    stat : bool, optional (default=False)
        If True, returns additional statistical properties of the normal distribution.

    Returns:
    --------
    - If `cdf` is True: Returns the cumulative distribution function values.
    - If `stat` is True: Returns a tuple (PDF, dictionary of statistics).
    - Otherwise: Returns the normal probability density function.

    Raises:
    -------
    ValueError:
        If `sigma` is non-positive.

    Notes:
    ------
    - The normal PDF is given by:
    - The function also provides the 1σ and 2σ confidence intervals.

    Example:
    --------
    >>> normal_pdf(0, 0, 1)
    0.3989422804014327

    >>> normal_pdf(np.array([-1, 0, 1]), 0, 1, cdf=True)
    array([0.15865525, 0.5, 0.84134475])

    >>> normal_pdf(0, 0, 1, stat=True)
    (0.3989422804014327, {'mean': 0, 'stddev': 1, '1sigma': (-1, 1), '2sigma': (-2, 2)})
    """
    if sigma <= 0:
        raise ValueError("sigma must be positive")

    coeff = 1 / (sigma * np.sqrt(2 * np.pi))
    exponent = np.exp(-((x - mu) ** 2) / (2 * sigma ** 2))
    result = coeff * exponent * scale
    if cdf:
        return norm.cdf(x, mu, sigma) * scale  # Corrected cumulative distribution function
    if stat:
        stats = {
            "mean": mu,
            "stddev": sigma,
            "1sigma": (mu - sigma, mu + sigma),
            "2sigma": (mu - 2 * sigma, mu + 2 * sigma),
        }
        stats = pd.DataFrame.from_dict(stats)
        return result, stats
    return result

# n, k = 20, 0.5
# x, y = binomial_pmf(n, k)
# print(binomial_pmf(n, k, stat = True))
# plt.bar(x,y,width=1,edgecolor = 'k')
# # i,j = binomial_pmf(20, 0.2, cdf = True)
# # plt.bar(i,j)
# plt.show()

# IMPORTANT, PUT IN LIBRARY SOMEWHERE