import math
import itertools


def calc_euclidian_distance(vec_a, vec_b):
    # https://en.wikipedia.org/wiki/Euclidean_distance
    sum_data = 0
    for a, b in itertools.izip(vec_a, vec_b):
        sum_data += (a - b) ** 2
    return math.sqrt(sum_data)
