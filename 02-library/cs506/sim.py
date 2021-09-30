def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    return sum(abs(x_i - y[i]) for i, x_i in enumerate(x))

def jaccard_dist(x, y):
    if len(x) == 0 and len(y) == 0: raise ValueError("lengths must not be zero")
    x_set = set(x)
    y_set = set(y)
    return 1 - (len(x_set.intersection(y_set)) / len(x_set.union(y_set)))

def cosine_sim(x, y):
    if len(x) == 0 or len(y) == 0: raise ValueError("lengths must not be zero")
    if len(x) != len(y): raise ValueError("lengths must be equal")
    prod = sum(x_i * y[i] for i, x_i in enumerate(x))
    return prod / (norm(x) * norm(y))

# Feel free to add more
def norm(v):
    return sum(v_i ** 2 for v_i in v) ** (1/2)
