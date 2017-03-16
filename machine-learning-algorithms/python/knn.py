from test_math import *

# Dataset was loaded from http://archive.ics.uci.edu/ml/datasets/Iris
data_file = open('../datasets/iris.data')

data_matrix = []
for i in data_file:
    data_list = [float(k) for k in i.split(',')[:3]]
    data_matrix.append(data_list)

# Calculate and sort distance
distance_array = []
for i in data_matrix:
    distance_array.append(calc_euclidian_distance(i, [3.5, 4.1, 5.6]))

# sorted Function Uses Timsort for ordering the data
# https://en.wikipedia.org/wiki/Timsort
print sorted(distance_array)
