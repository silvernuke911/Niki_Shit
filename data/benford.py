import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


N_max = 100000000
N_nums = 9000
numbers = np.random.randint(0, N_max, N_nums)
numbers = np.array(range(1,N_nums), dtype=int)
print(len(numbers))
first_digits = np.zeros(3145)

numbers = pd.read_csv(r'C:\Users\verci\Documents\Python Code\Niki_Shit\data\nums.csv', dtype = str)
numbers = numbers.fillna('')
nums = np.zeros(len(numbers), dtype = int)
for i in range(len(numbers)):
    num = numbers['a'][i] + numbers['b'][i] + numbers['c'][i]
    num = int(num)
    # print(num)
    nums[i] = num

for i, num in enumerate(nums):
    numi = str(num)
    first_digits[i] = numi[0]

print(numbers)
print(nums)
print(first_digits)
# for dig in first_digits:
    #print(dig)
unique, counts = np.unique(first_digits, return_counts=True)
plt.xlim(0.5,9.5)
plt.ylim(0,1)
plt.bar(unique,counts/3145, width = 1, edgecolor = 'k')
plt.show()