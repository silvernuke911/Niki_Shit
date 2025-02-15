import numpy as np
import matplotlib.pyplot as plt

def persistence(N, counter=0):
    # print(N)
    if len(str(N)) == 1:
        # print(f'number of times: {counter}')
        return int(counter)
    digits = [int(char) for char in str(N)]
    prod = 1
    for digit in digits:
        prod *= digit
    return persistence(prod, counter = counter + 1)

nums = 10000000
numbers      = range(nums)
persis = np.zeros(nums) 
for number in numbers:
    persis[number] = persistence(number)
plt.scatter(numbers,persis, marker = '.')
max_index = np.argmax(persis)
max_value = persis[max_index]

print(f"Number with maximum persistence: {max_index}, Persistence value: {max_value}")
plt.show()
