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


def calc_quadratic_distance(vec_a, vec_b):
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
    return sum_data


def calc_cos_sim(vec_a, vec_b):
    sum_data_ab = 0
    sum_data_a = 0
    sum_data_b = 0

    for a, b in itertools.izip(vec_a, vec_b):
        sum_data_ab += a * b
        sum_data_a += a ** 2
        sum_data_b += b ** 2

    similarity = sum_data_ab / (math.sqrt(sum_data_a) * math.sqrt(sum_data_b))
    try:
        distance = math.acos(similarity) / math.pi
    except:
        # Handle the precision of float in the math.sqrt that can create number bigger than 1.0 like 1.000000000001
        distance = math.acos(round(similarity)) / math.pi
    return distance


def euclidian_knn(vec_a, tup_b, type):
    '''
    Calculate knn with euclidian Distance using KNN core algorithm
    :param vec_a: Array of Numbers
    :param tup_b: Tuple of Array of Numbers and the Label of the point
    :return: A tuple of Value and Label
    '''
    vec_b, label = tup_b
    if type == 'euclidian':
        return calc_euclidian_distance(vec_a, vec_b), label
    elif type == 'quadratic':
        return calc_quadratic_distance(vec_a, vec_b), label
    elif type == 'cos':
        return calc_cos_sim(vec_a, vec_b), label
    else:
        return 0
