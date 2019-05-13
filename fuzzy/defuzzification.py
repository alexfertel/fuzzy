import numpy

def centroid(domain, aggregation):
    a, b = domain
    numerator, denominator = 0, 0
    for x in numpy.arange(a, b, (b - a) / 10):
        numerator += x * aggregation(x)
        denominator += aggregation(x)

    return numerator / denominator
