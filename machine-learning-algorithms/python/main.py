from algorithms import knn
import time
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib as mlt

mlt.use('TkAgg')

files = ['5k-iris.data',
         '10k-iris.data',
         '20k-iris.data',
         '100k-iris.data',
         '200k-iris.data',
         '500k-iris.data',
         '2M-iris.data',
         '4M-iris.data']

euclidian_y = []
quadratic_y = []
euclidian_x = [5, 10, 20, 100, 200, 500, 2000, 4000]

for f in files:
    # Dataset was loaded from http://archive.ics.uci.edu/ml/datasets/Iris
    data_file = open('../datasets/' + f)

    data_matrix = []
    for i in data_file:
        split_row = i.replace('\n', '').split(',')
        data_list = ([float(k) for k in split_row[:4]], split_row[4])
        data_matrix.append(data_list)

    #random.seed(42)
    #random.shuffle(data_matrix)

    result_data = []

    start_time = time.time()
    res = knn([5.0, 3.4, 1.6, 0.3], data_matrix, 'quadratic')
    quadratic_y.append(time.time() - start_time)

    start_time = time.time()
    res = knn([5.0, 3.4, 1.6, 0.3], data_matrix, 'euclidian')
    euclidian_y.append(time.time() - start_time)

    print euclidian_y
    print quadratic_y

plt.plot(euclidian_x, euclidian_y, label='Euclidian')
plt.plot(euclidian_x, quadratic_y, label='Quadratic')
plt.ylabel('Time Execution')
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)
plt.show()