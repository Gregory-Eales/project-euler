# finds the xth factorial
def factorial(x):
	if x!=1:
		x = x*factorial(x-1)
	return x


answer = factorial(40)/(factorial(20)**2)
print(f'{answer:.20f}')