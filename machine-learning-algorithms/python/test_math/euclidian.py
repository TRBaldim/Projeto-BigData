import math
import itertools


def calc_euclidian_distance(vec_a, vec_b):
    '''
    Calculate the Euclidian Distance of two arrays of the same size
    :param vec_a: Array of Numbers
    :param vec_b: Array of Number
    :return: float value of Euclidian distance
    '''
    # https://en.wikipedia.org/wiki/Euclidean_distance
    sum_data = 0
    for a, b in itertools.izip(vec_a, vec_b):
        sum_data += (a - b) ** 2
    return math.sqrt(sum_data)
