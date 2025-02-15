import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb


# Binomial Estimation
def binomial_distribution(N, events, p):
    """
    Compute the binomial distribution mathematically.

    Parameters:
    N (int): Number of samples (ignored in deterministic computation).
    events (int): Total number of events (trials).
    p (float): Probability of success.

    Returns:
    tuple: (event_index, probabilities) where event_index are possible outcomes
           and probabilities are the corresponding binomial probabilities.
    """
    event_index = np.arange(events + 1)  # Possible outcomes from 0 to events
    probabilities = comb(events, event_index) * (p ** event_index) * ((1 - p) ** (events - event_index))
    return event_index, probabilities*N

population = 169
pop_labels = np.zeros(population+1, dtype = int)
passes = 10
sample_size = 17
for i in range(passes):
    tags = np.random.choice(np.arange(0, population+1), size=sample_size, replace=False)
    for j in tags:
        pop_labels[j] += 1
unique, counts = np.unique(pop_labels, return_counts=True)
print(counts)
event, probcount = binomial_distribution(population, passes, sample_size/population)
plt.bar(unique,counts, edgecolor = 'k', width = 1, zorder = 1)
plt.grid(zorder = 0)
plt.stairs(probcount, np.array(range(0,passes+2))-0.5, color = 'r', zorder = 2)
plt.xlim(-0.5, passes+ 0.5)
plt.show()

# import numpy as np

# # Capture Recapture Statistics
# population = np.random.randint(1000,10000)
# passes = 2
# sample_size = 500
# sample_counts = 100000
# sample_count_values = np.zeros(sample_counts)

# for k in range(sample_counts):
#     pop_labels = np.zeros(population, dtype=int)  # Fix: Use `population` instead of `population+1`
    
#     # Sampling process
#     for i in range(passes):
#         tags = np.random.choice(np.arange(population), size=sample_size, replace=False)
#         for j in tags:
#             pop_labels[j] += 1
    
#     # Count occurrences (0, 1, 2 times)
#     count_labels = [np.sum(pop_labels == i) for i in range(passes + 1)]

#     # Ensure no division by zero
#     if count_labels[2] > 0:
#         population_estimate = sample_size * sample_size / count_labels[2]
#     else:
#         population_estimate = np.nan  # Handle zero-division case
    
#     sample_count_values[k] = population_estimate

# # Compute statistics
# # print(sample_count_values)
# samp_mean, samp_std = np.nanmean(sample_count_values), np.nanstd(sample_count_values)  # Ignore NaNs
# print(population, samp_mean, samp_std, samp_mean*np.sqrt((sample_size/samp_mean) * (1-(sample_size/samp_mean))))

# plt.hist(sample_count_values, bins = 20, edgecolor = 'k')
# plt.axvline(population, color = 'r')
# plt.axvline(samp_mean, color = 'k', linewidth = 3)
# plt.axvline(samp_mean + samp_std, color = 'gray')
# plt.axvline(samp_mean - samp_std, color = 'gray')
# plt.show()

#FIND A GOOD WAY TO CALCULATE THE ERROR, BUT YEA WE GOOD