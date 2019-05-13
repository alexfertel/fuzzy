__all__ = ['truncate', 'aggregate', 'scale']

def truncate(curried, value, x):
    y = curried(x)
    return value if value < y else y

def scale(curried, value, x):
    y = curried(x)
    return y * value

def aggregate(functions, x):
    return max(map(lambda fn: fn(x), functions))

