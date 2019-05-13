__all__ = ['centroid', 'meanofmaximum', 'smallestofmaximum', 'largestofmaximum']

import numpy

def centroid(domain, aggregation):
    a, b = domain
    numerator, denominator = 0, 0
    for x in numpy.arange(a, b, (b - a) / 100):
        numerator += x * aggregation(x)
        denominator += aggregation(x)

    return numerator / denominator

def meanofmaximum(domain, aggregation):
    a, b = domain
    x_val = [x for x in numpy.arange(a, b, (b - a) / 100)]
    y_val = [aggregation(x) for x in x_val]
    m = max(y_val)

    maxs = list(filter(lambda x: aggregation(x) == m, x_val))
    print("MAXS:", maxs)
    return sum(maxs) / len(maxs)

def smallestofmaximum(domain, aggregation):
    a, b = domain
    x_val = [x for x in numpy.arange(a, b, (b - a) / 100)]
    y_val = [aggregation(x) for x in x_val]
    m = max(y_val)

    maxs = filter(lambda x: aggregation(x) == m, x_val)
    print("MAXS:", maxs)
    return min(maxs)

def largestofmaximum(domain, aggregation):
    a, b = domain
    x_val = [x for x in numpy.arange(a, b, (b - a) / 100)]
    y_val = [aggregation(x) for x in x_val]
    m = max(y_val)

    maxs = filter(lambda x: aggregation(x) == m, x_val)
    print("MAXS:", maxs)
    return max(maxs)
