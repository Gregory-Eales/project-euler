from tqdm import tqdm
import numpy as np

def get_power_digits(n):
    n = str(n)
    n = [int(char)**5 for char in n]
    n = np.sum(n)
    return n


def get_pow_nums(n):
    nums = []
    for i in range(2, n):
        if i == get_power_digits(i):
            nums.append(i)
            print(len(nums))
    return np.sum(nums)

print(get_pow_nums(1000000))
