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

def euclidian_knn(vec_a, tup_b):
    '''
    Calculate knn with euclidian Distance using KNN core algorithm
    :param vec_a: Array of Numbers
    :param tup_b: Tuple of Array of Numbers and the Label of the point
    :return: A tuple of Value and Label
    '''
    vec_b, label = tup_b
    return calc_euclidian_distance(vec_a, vec_b), label
