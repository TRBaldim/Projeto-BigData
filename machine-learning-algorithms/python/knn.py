from test_math import *

# Dataset was loaded from http://archive.ics.uci.edu/ml/datasets/Iris
data_file = open('../datasets/iris.data')

data_matrix = []
for i in data_file:
    split_row = i.replace('\n', '').split(',')
    data_list = ([float(k) for k in split_row[:4]], split_row[4])
    data_matrix.append(data_list)

# Calculate and sort distance
distance_array = []
for i in data_matrix:
    distance_array.append(euclidian_knn([3.5, 4.1, 5.6, 1.4], i))

# sorted Function Uses Timsort for ordering the data
# https://en.wikipedia.org/wiki/Timsort
print sorted(distance_array)
