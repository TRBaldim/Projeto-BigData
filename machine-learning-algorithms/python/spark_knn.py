from pyspark import SparkContext
from algorithms import spark_knn
import time

sc = SparkContext(appName='My Test')

rdd = sc.textFile('/home/thiago/Mestrado/topicos-BigData/Projeto-BigData/machine-learning-algorithms/datasets/big_iris.data')\
            .map(lambda x: x.split(','))\
            .map(lambda x: ([float(k) for k in x[:4]], x[4]))


# 5.1,3.5,1.4,0.2,Iris-setosa
start_time = time.time()
print spark_knn([5.0, 3.4, 1.6, 0.3], rdd, 'euclidian')
print time.time() - start_time


# 5.1,3.5,1.4,0.2,Iris-setosa
start_time = time.time()
print spark_knn([5.0, 3.4, 1.6, 0.3], rdd, 'quadratic')
print time.time() - start_time

