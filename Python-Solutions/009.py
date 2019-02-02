import numpy as np
import time


for c in range(1000):
	for b in range(1000-c):
		a = 1000 - b - c
		if a**2 + b**2 == c**2:
			if a != b and b!= c and a != c:
				print(a*b*c)