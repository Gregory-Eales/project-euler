import time 
import numpy as np

# gets all fibonacci values
# less than y
def get_fibonacci(y):
	fib = [1]
	last = 1
	condition = False
	while not condition:
		fib.append(last)
		last = last + fib[-2]
		if last > y:
			condition = True
	return fib


fib = get_fibonacci(4*10**6)
even_fib = []
for i in fib:
	if (i%2) == 0:
		even_fib.append(i)

print(np.sum(even_fib))

