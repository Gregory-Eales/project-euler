import time
import numpy as np

# finds multiples of a number
# less than y
def find_multiples(x, y):
	multiples = []
	num_multiples = int(y/x) + 1
	for i in range(1, num_multiples):
		if i*x != y:
			multiples.append(i*x)


	return multiples


ThreeMultiples = find_multiples(3, 1000)
FiveMultiples = find_multiples(5, 1000)

multiples = []

for i in ThreeMultiples:
	if i not in multiples:
		multiples.append(i)


for i in FiveMultiples:
	if i not in multiples:
		multiples.append(i)


print(np.sum(multiples))



