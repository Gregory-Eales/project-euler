import numpy as np
import time

def find_sum_proper_divisors(x):
	number = 1
	for i in range(2, int(x/2) + 1):
		if x%i == 0:
			number = number + i
	return [number, x]

# find all amicable numbers under n
def find_sum_amical_numbers(n):
	amicables = []

	for i in range(1, n):
		sum_n_div = find_sum_proper_divisors(i)
		sum_sum = find_sum_proper_divisors(sum_n_div[0])
		if i == sum_sum[0] and i != sum_n_div[0]:
			if sum_n_div[0] not in amicables:
				amicables.append(sum_n_div[0])

			if i not in amicables:
				amicables.append(i)

	return np.sum(amicables)

print(find_sum_amical_numbers(10000))


