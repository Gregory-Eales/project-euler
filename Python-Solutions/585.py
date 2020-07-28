import math
from tqdm import tqdm


# calculate nested root
def get_nested_root(x,y,z):
    return math.sqrt(x + math.sqrt(y) + math.sqrt(z))

# get all non perfect squares
def get_non_squares(n):
    non_squares = []
    for i in tqdm(range(n+1), "Getting Non-Squares"):
        num = math.sqrt(i)
        if num != int(num):
            non_squares.append(i)

    return non_squares


# give the number of denested roots up to n
def f(n):
    
    num_denested = 0

    # get non squares
    non_squares = get_non_squares(n)

    # check each x for denested roots
    for x in tqdm(range(n+1), "Finding Denested Roots"):
        
        # can't check every non-square!
        # how to bound the search?

        for z in non_squares:
            for y in non_squares:
                nested_root = get_nested_root(x, y, z)

    print(nested_root)
    print(num_denested)

if __name__ == "__main__":
    f(100)
    #f(5000000)

