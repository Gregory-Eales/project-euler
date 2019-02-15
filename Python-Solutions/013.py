import numpy as np 
from matplotlib import pyplot as plt

# finds the xth factorial
def factorial(x):

	if x!=1:
		x = x*factorial(x-1)

	return x


print(factorial(3))