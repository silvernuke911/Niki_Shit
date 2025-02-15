# Fabrications

fab_data_path = 'step_means.csv'
fab_data = pd.read_csv(fab_data_path)
print(fab_data)
np.random.seed(42)

# # Generate random numbers within the range [-0.1, 0.1] and scale them by the cell's value
# random_adjustments = fab_data.iloc[:, 1:] * np.random.uniform(-0.1, 0.1, fab_data.iloc[:, 1:].shape)

# # Add the random adjustments to the numeric columns
# fab_data.iloc[:, 1:] += random_adjustments

# Print the updated DataFrame
print(fab_data)
# Number of datasets to generate
N = 5

# Randomizer function
def randomizer(n, average, stddev):
    samples = np.random.normal(loc=average, scale=stddev, size=n)
    return samples
codes = ['C', 'P', 'N', 'S']
for code in codes:
    # Extract the mean (ending with 'M') and standard deviation (ending with 'S') rows
    mean_row = fab_data[fab_data['TYPE'] == f'{code}M']
    stddev_row = fab_data[fab_data['TYPE'] == f'{code}S']

    # Extract mean and standard deviation values for each feature
    mean_ets, stdev_ets = mean_row['ETS'].values[0], stddev_row['ETS'].values[0]
    mean_eit, stdev_eit = mean_row['EIT'].values[0], stddev_row['EIT'].values[0]
    mean_epl, stdev_epl = mean_row['EPL'].values[0], stddev_row['EPL'].values[0]
    mean_nts, stdev_nts = mean_row['NTS'].values[0], stddev_row['NTS'].values[0]
    mean_nit, stdev_nit = mean_row['NIT'].values[0], stddev_row['NIT'].values[0]
    mean_npl, stdev_npl = mean_row['NPL'].values[0], stddev_row['NPL'].values[0]

    # Outer loop over levels
    for i in range(1, 6):  # Iterate over levels 1 to 5
        # Generate new random samples for each feature
        ets = randomizer(5, mean_ets, stdev_ets)
        eit = randomizer(5, mean_eit, stdev_eit)
        epl = randomizer(5, mean_epl, stdev_epl)
        nts = randomizer(5, mean_nts, stdev_nts)
        nit = randomizer(5, mean_nit, stdev_nit)
        npl = randomizer(5, mean_npl, stdev_npl)

        # Inner loop over columns
        for j in range(1, 6):  # Iterate over columns 1 to 5
            print(f'{code}{i}W6,{code}W6,{j},'
                  f'{ets[j-1]:.2f},{eit[j-1]:.2f},{epl[j-1]:.2f},'
                  f'{nts[j-1]:.2f},{nit[j-1]:.2f},{npl[j-1]:.2f}')

import pandas as pd
import numpy as np

# Load the data
fab_data = 'rdth_means.csv'
fabdata = pd.read_csv(fab_data)
np.random.seed(42)

def randomizer(n, average, stddev):
    return np.random.normal(loc=average, scale=stddev, size=n)

codes = ['C', 'P', 'N', 'S']
entries = []

for code in codes:
    mean_row = fabdata[fabdata['TYPE'] == f'{code}M'].iloc[0]
    stddev_row = fabdata[fabdata['TYPE'] == f'{code}S'].iloc[0]
    
    mean_v = mean_row['D'] / mean_row['T'] 
    stddev_v = 0.1
    
    for i in range(1, 6):  # C1 to C5, P1 to P5, etc.
        sample_d = randomizer(3, mean_row['D'], stddev_row['D']/2) + 5
        sample_v = randomizer(3, mean_v, stddev_v)
        sample_t = sample_d / sample_v
        sample_r = randomizer(3, mean_row['R'], stddev_row['R'])
        sample_h = randomizer(3, mean_row['H'], stddev_row['H']/2)
        for j in range(1, 4):  # 3 samples per type
            entry = [f"{code}{i}W6", f"{code}W6", j, round(sample_r[j-1], 2), round(sample_d[j-1]), round(sample_t[j-1], 2), round(sample_h[j-1], 2)]
            entries.append(entry)

# Convert to DataFrame and save
output_df = pd.DataFrame(entries, columns=["ID", "Group", "Sample", "R", "D", "T", "H"])
output_df.to_csv("generated_w6_data.csv", index=False, sep=',')
print(output_df)