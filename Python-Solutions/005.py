import numpy as np 
import time 

# finds the multiples of a number x

def get_multiples(x, max):
	counter = []
	for i in range(int(max/2) + 1):
		counter.append(0)
	for i in range(2, int(max/2) + 1):
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

numbers = find_max_number()
x = 1
for i in range(len(numbers)):
	x = x*(i**numbers[i])
print(x)