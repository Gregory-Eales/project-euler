
import numpy as np
from tqdm import tqdm
numbers = []
for i in range(1, 10):
    numbers.append(i)


from itertools import permutations

# Get all permutations of [1, 2, 3]
perm = list(permutations(numbers))


numbs = []
for p in perm:
    for i in range(1, 7):
        for j in range(1, 7-i):


            n1 = int(''.join(map(str, p[0:i])))
            n2 = int(''.join(map(str, p[i:j+i])))
            n3 = int(''.join(map(str, p[i+j:9])))

            if n1*n2 == n3:
                numbs.append(n3)

print(np.sum(numbs))
