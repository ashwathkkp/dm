import math
from typing import List
import numpy as np

def cosine_similarity(X: List,Y: List)-> float:
    sum_xi_yi = 0
    sum_xi_2 = 0
    sum_yi_2 = 0
    for i in range(len(X)):
        sum_xi_yi += X[i]*Y[i]
        sum_xi_2 += pow(X[i], 2)
        sum_yi_2 += pow(Y[i], 2)
    return sum_xi_yi/(pow(sum_xi_2, 1/2) * pow(sum_yi_2, 1/2))

def euclidean_distance(X: List,Y: List)-> float:
    distance = 0
    for i in range(len(X)):
        distance += pow(abs(X[i]-Y[i]), 2)
    return pow(distance, 1/2)

def pearson_correlation_coefficient(X: List,Y: List)-> float:
    N = len(X)
    x_mean, y_mean = np.mean(X), np.mean(Y)
    s_xy, s_xx, s_yy = 0, 0, 0
    for i in range(N):
        s_xy += (X[i]-x_mean)*(Y[i]-y_mean)
        s_xx += (X[i]-x_mean)**2
        s_yy += (Y[i]-y_mean)**2
    result = s_xy / (s_xx*s_yy)**0.5
    if math.isnan(result):
        result = 0.0
    return result

def jacardian_distance(X: List,Y: List)-> float:
    return len(set(X).intersection(set(Y)))/len(set(X).union(set(Y)))

q1_1, q1_2 = [1, 1, 1, 1], [2, 2, 2, 2] # cosine, correlation, Euclidean
q2_1, q2_2 = [0, 1, 0, 1], [1, 0, 1, 0] # cosine, correlation, Euclidean, Jaccard
q3_1, q3_2 = [0, -1, 0, 1], [1, 0, -1, 0] # cosine, correlation, Euclidean
q4_1, q4_2 = [1, 1, 0, 1, 0, 1] , [1, 1, 1, 0, 0, 1] # cosine, correlation, Jaccard
q5_1, q5_2 = [2, -1, 0, 2, 0, -3] , [-1, 1, -1, 0, 0, -1] #cosine, correlation

print(cosine_similarity(q1_1, q1_2), pearson_correlation_coefficient(q1_1,q1_2), euclidean_distance(q1_1,q1_2))
print(cosine_similarity(q2_1, q2_2), pearson_correlation_coefficient(q2_1,q2_2), euclidean_distance(q2_1,q2_2), jacardian_distance(q2_1, q2_2))
print(cosine_similarity(q3_1, q3_2), pearson_correlation_coefficient(q3_1,q3_2), euclidean_distance(q3_1,q3_2))
print(cosine_similarity(q4_1, q4_2), pearson_correlation_coefficient(q4_1,q4_2), jacardian_distance(q4_1,q4_2))
print(cosine_similarity(q5_1, q5_2), pearson_correlation_coefficient(q5_1,q5_2))
