import random
from algorithms import knn
import time

# Dataset was loaded from http://archive.ics.uci.edu/ml/datasets/Iris
data_file = open('../datasets/fat_iris.data')

data_matrix = []
for i in data_file:
    split_row = i.replace('\n', '').split(',')
    data_list = ([float(k) for k in split_row[:4]], split_row[4])
    data_matrix.append(data_list)

random.seed(42)
random.shuffle(data_matrix)

result_data = []

start_time = time.clock()
res = knn([1.0, 2.0, 1.1, 1.8], data_matrix, 'quadratic')
print time.clock() - start_time
print res