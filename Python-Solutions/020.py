import numpy as np 
from matplotlib import pyplot as pyplot

def factorial(x):

	if x!=1:
		x = x*factorial(x-1)

	return x

def sum_factorial_digits(x):
	f = factorial(x)
	f = str(f)
	number = 0
	for i in range(len(f)):
		number = number + int(f[i])

	return number

print(sum_factorial_digits(100))