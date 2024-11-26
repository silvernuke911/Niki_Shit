import numpy as np
import scipy
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import pandas as pd


def t_test_independent(group1, group2):
    """
    Perform an independent samples t-test to compare the means of two unrelated groups.

    Parameters:
    group1 (array-like): Data from the first group.
    group2 (array-like): Data from the second group.

    Returns:
    tuple: t-statistic and p-value of the test.

    Usage:
    Use this test when comparing two independent groups to determine if their means are significantly different.
    """
    t_stat, p_val = scipy.stats.ttest_ind(group1, group2)
    return t_stat, p_val


def t_test_related(group_before, group_after):
    """
    Perform a paired samples t-test to compare the means of two related groups.

    Parameters:
    group_before (array-like): Data from the first measurement (e.g., pre-treatment).
    group_after (array-like): Data from the second measurement (e.g., post-treatment).

    Returns:
    tuple: t-statistic and p-value of the test.

    Usage:
    Use this test when comparing two related groups (e.g., measurements from the same subjects).
    """
    t_stat, p_val = scipy.stats.ttest_rel(group_before, group_after)
    return t_stat, p_val


def t_test_single_sample(sample, expected_mean):
    """
    Perform a one-sample t-test to compare the mean of a sample to a known or expected mean.

    Parameters:
    sample (array-like): Data from the sample.
    expected_mean (float): The expected or known population mean to compare against.

    Returns:
    tuple: t-statistic and p-value of the test.

    Usage:
    Use this test when determining if the sample mean differs significantly from a specified value.
    """
    t_stat, p_val = scipy.stats.ttest_1samp(sample, expected_mean)
    return t_stat, p_val

def anova_oneway(*groups):
    """
    Perform a one-way Analysis of Variance (ANOVA) test to compare the means of two or more groups.

    This test is used to determine if there is a statistically significant difference 
    between the means of the given groups.

    Parameters:
    -----------
    *groups : array-like
        One or more arrays representing the different groups to be compared. Each array contains the data 
        for one group. All groups must have the same underlying measurement.

    Returns:
    --------
    F-statistic : float
        The test statistic calculated from the ratio of variance between the group means and within-group variance.

    p-value : float
        The p-value associated with the test statistic, which helps in determining statistical significance.

    Notes:
    ------
    The null hypothesis for this test is that all group means are equal.
    The alternative hypothesis is that at least one group mean is different from the others.

    If the p-value is less than the significance level (typically 0.05), we reject the null hypothesis and 
    conclude that there is a significant difference between at least one of the groups.
    """

    f_stat, p_value = scipy.stats.f_oneway(*groups)
    return f_stat, p_value



def tukey_posthoc_test(data, groups):
    """
    Perform Tukey's Honest Significant Difference (HSD) post hoc test.

    Tukey's test is used to determine which specific group means are different 
    after finding a significant result in ANOVA.

    Parameters:
    -----------
    data : array-like
        The dependent variable values (e.g., performance scores, measurements, etc.).
    groups : array-like
        The group labels corresponding to the data. Each element in `groups` indicates 
        the group to which the corresponding value in `data` belongs.

    Returns:
    --------
    summary : statsmodels.iolib.table.SimpleTable
        A table summarizing the pairwise comparisons, including group pairs, 
        mean difference, p-value, confidence intervals, and whether the difference is significant.

    Example:
    --------
    >>> data = [23, 25, 22, 30, 28, 31, 35, 33, 32, 30, 20, 19, 21, 22, 23]
    >>> groups = ['group1'] * 5 + ['group2'] * 5 + ['group3'] * 5
    >>> summary = tukey_posthoc_test(data, groups)
    >>> print(summary)
    """
    # Perform Tukey's HSD post hoc test
    tukey_result = pairwise_tukeyhsd(endog=data, groups=groups, alpha=0.05)
    return tukey_result.summary()