def distance(x, y):
    res = 0
    if(len(x) != len(y)):
        raise ValueError
    for ind, el in enumerate(x):
        if(el != y[ind]):
            res += 1
    return(res)
