import random
from algorithms import knn
import matplotlib.pyplot as plt
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

size = len(data_matrix)

data_test = data_matrix[int(size * 0.3):]
data_matrix = data_matrix[:int(size * 0.7)]

for _ in range(10):
    result_data = []
    start_time = time.clock()
    for t in data_test:
        res = (knn(t[0], data_matrix, 'quadratic'), t[1])
        result_data.append(res)
    print str(time.clock() - start_time) + ' Seconds'

count = 0.0
right = 0.0
graph_res = []
for i in result_data:
    count += 1.0
    right += 1.0 if i[0] == i[1] else 0.0
    graph_res.append(right / count)
print right / count

axes = plt.gca()
axes.set_ylim([0.5, 1.0])
plt.plot(graph_res)
plt.ylabel('Precision')
plt.show()
