import numpy as np

def get_primes(n, primes=[2]):

    if n < len(primes):
        return primes

    m = primes[-1]

    while len(primes) < n:
        m += 1
        is_prime = True
        for prime in primes:
            if m % prime == 0:
                    is_prime =  False
                    break
            if prime > np.sqrt(m):
                break
        if is_prime == True:
            primes.append(m)

    return primes

print(get_primes(50000)[-1])
