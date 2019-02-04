import numpy as np
import time

# counts the divisors of number x
def count_divisors(x):
	num_divisors = 0
	for i in range(1, int(x/2 + 1)):
		if x % i == 0:
			num_divisors += 1
	return num_divisors

def divisor_traingle_number(n):
	triangle_num = n*(n+1) / 2

	return count_divisors(triangle_num)



	

print(divisor_traingle_number(100000))






