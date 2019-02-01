import numpy as np
import time

nums = []
for i in range(101):
	nums.append(i)

num_sum = np.sum(nums)

nums_squared = []
for i in range(101):
	nums_squared.append(i**2)

nums_squared_sum = np.sum(nums_squared)


print(num_sum**2 - nums_squared_sum)

