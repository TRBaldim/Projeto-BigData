import random
from algorithms import knn
import matplotlib.pyplot as plt
import matplotlib as mlt
import time

mlt.use('TkAgg')

# Dataset was loaded from http://archive.ics.uci.edu/ml/datasets/Iris
data_file = open('../datasets/big_iris.data')

data_matrix = []
for i in data_file:
    split_row = i.replace('\n', '').split(',')
    data_list = ([float(k) for k in split_row[:4]], split_row[4])
    data_matrix.append(data_list)

random.seed(54654)
random.shuffle(data_matrix)

size = len(data_matrix)

data_test = data_matrix[int(size * 0.3):]
data_matrix = data_matrix[:int(size * 0.7)]

# Euclidian
result_data = []
c = 0
start_time = time.clock()
for t in data_test:
    res = (knn(t[0], data_matrix, 'euclidian'), t[1])
    result_data.append(res)
    c += 1
    if c % 100 == 0:
        print c
print str(time.clock() - start_time) + ' Seconds'

count = 0.0
right = 0.0
graph_res = []
for i in result_data:
    count += 1.0
    right += 1.0 if i[0] == i[1] else 0.0
    graph_res.append(right / count)
print right / count


# Quadratic
result_data = []
start_time = time.clock()
c = 0
for t in data_test:
    res = (knn(t[0], data_matrix, 'quadratic'), t[1])
    result_data.append(res)
    c += 1
    if c % 100 == 0:
        print c
print str(time.clock() - start_time) + ' Seconds'

count = 0.0
right = 0.0
graph_res_qudratic = []
for i in result_data:
    count += 1.0
    right += 1.0 if i[0] == i[1] else 0.0
    graph_res_qudratic.append(right / count)
print right / count

axes = plt.gca()
axes.set_ylim([0.5, 1.0])
plt.plot(graph_res)
plt.plot(graph_res_qudratic)
plt.ylabel('Precision')
plt.show()
