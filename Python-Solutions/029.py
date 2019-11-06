from tqdm import tqdm


def exp(a, b):
    return a**b



def get_distinct_terms():
    distincts = []
    for a in tqdm(range(2, 101)):
        for b in range(2, 101):
            e = exp(a, b)
            if e not in distincts:
                distincts.append(e)

    return distincts


print(len(get_distinct_terms()))
