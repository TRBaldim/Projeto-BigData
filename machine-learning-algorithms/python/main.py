from random import shuffle
from algorithms import knn

# Dataset was loaded from http://archive.ics.uci.edu/ml/datasets/Iris
data_file = open('../datasets/iris.data')

data_matrix = []
for i in data_file:
    split_row = i.replace('\n', '').split(',')
    data_list = ([float(k) for k in split_row[:4]], split_row[4])
    data_matrix.append(data_list)

shuffle(data_matrix)

data_test = data_matrix[105:]
data_matrix = data_matrix[:105]

result_data = []
for t in data_test:
    res = (knn(t[0], data_matrix), t[1])
    result_data.append(res)
    print res

count = 0.0
right = 0.0
for i in result_data:
    count += 1.0
    right += 1.0 if i[0] == i[1] else 0.0
print right / count