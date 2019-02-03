import numpy as np 
import time 

# finds the multiples of a number x

def get_multiples(x, max):
	counter = []
	primes = [2, 3, 5, 7, 11, 13, 17, 19]
	for i in range(len(primes)):
		counter.append(0)
	
	for i in primes:
		number = x
		condition = True
		while condition:
			if number%i==0:
				counter[i] = counter[i]+1
				number = number/i
			else:
				condition = False
	return counter

# find maximum factors, 1-20
def find_max_number():
	numbers = []
	max_numbers = []
	for i in range(2, 21):
		numbers.append(get_multiples(i, 21))
	for i in range(len(numbers[0])):
		maximum = 0
		for j in range(len(numbers)):
			if numbers[j][i] > maximum:
				maximum = numbers[j][i]
		max_numbers.append(maximum)
	return max_numbers

primes = [2, 3, 5, 7, 11, 13, 17, 19]
numbers = find_max_number()
x = 1
for i in primes:
	x = x*(i**numbers[i])
print(x)