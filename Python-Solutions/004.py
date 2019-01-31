import numpy as np
import time


# checks to see if number is palindrome
def is_palindrome(x):
	x = str(x)
	length = len(x)
	condition = True
	if length%2 == 0:
		iterations = length/2
	else:
		iterations = (length-1) / 2
	for i in range(int(iterations)):
		if x[i] != x[-i-1]:
			condition = False
			break
	return condition

# finds the largest pallendrome that is a product
# of two 3-digit numbers
def find_panlindrome():
	x = 999
	y = 999

	for i in range(100):
		y = 999
		x = 999 - i
		for j in range(100):
			z = x*y
			if is_palindrome(z):
				return z
			else:
				y = y-1
	return None

print(find_panlindrome())