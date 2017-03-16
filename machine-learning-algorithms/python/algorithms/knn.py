from test_math import euclidian_knn


def knn(input_array, input_matrix, type):
    def_k = (len(input_matrix) / 3)
    # Calculate and sort distance
    distance_array = []
    for i in input_matrix:
        distance_array.append(euclidian_knn(input_array, i, type))

    # sorted Function Uses Timsort for ordering the data
    # https://en.wikipedia.org/wiki/Timsort
    distance_array.sort()

    dict_result = {}
    for i in range(1, def_k + 1):
        try:
            dict_result[distance_array[i][1]] += distance_array[i][0] * (1.0 / float(i))
        except KeyError:
            dict_result[distance_array[i][1]] = 0
            dict_result[distance_array[i][1]] += distance_array[i][0] * (1.0 / float(i))

    # Get the max value at the knn analysis
    return max(dict_result, key=dict_result.get)