import math
import numpy as np
from tqdm import tqdm

def factorial(n):
	if n <= 1:
		return 1
	
	else: return n*factorial(n-1)


def get_curious():
	curious_nums = []
	for i in tqdm(range(3, 1000000), "Getting Curious"):
		fact_num = 0
		for s in range(len(str(i))):
			fact_num += factorial(int(str(i)[s]))

		if fact_num == i:
			curious_nums.append(i)
	
	print(len(curious_nums))
	print(np.sum(curious_nums))

if __name__ == "__main__":
	get_curious()

