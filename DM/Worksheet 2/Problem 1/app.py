import pandas as pd

def manhattan_distance(X,Y):
    distance = 0
    for i in range(len(X)):
        distance += abs(X[i]-Y[i])
    return distance

def euclidean_distance(X,Y):
    distance = 0
    for i in range(len(X)):
        distance += pow(abs(X[i]-Y[i]), 2)
    return pow(distance, 1/2)

def supremum_distance(X,Y):
    distance = 0
    for i in range(len(X)):
        distance = max(abs(X[i]-Y[i]), distance)
    return distance

def cosine_similarity(X,Y):
    sum_xi_yi = 0
    sum_xi_2 = 0
    sum_yi_2 = 0
    for i in range(len(X)):
        sum_xi_yi += X[i]*Y[i]
        sum_xi_2 += pow(X[i], 2)
        sum_yi_2 += pow(Y[i], 2)
    return sum_xi_yi/(pow(sum_xi_2, 1/2) * pow(sum_yi_2, 1/2))

df = pd.read_csv("./data.csv", names=['Name', 'A1', 'A2'])
data_point = {'Name':'x6', 'A1':1.4, 'A2':1.6}

manhattan_results, euclidean_results, supremum_results, cosine_results = {}, {}, {}, {}

for index, point in df.iterrows():
    manhattan_results[point['Name']] = manhattan_distance( [point['A1'], point['A2']], [data_point['A1'], data_point['A2']])
    euclidean_results[point['Name']] = euclidean_distance( [point['A1'], point['A2']], [data_point['A1'], data_point['A2']])
    supremum_results[point['Name']] = supremum_distance( [point['A1'], point['A2']], [data_point['A1'], data_point['A2']])
    cosine_results[point['Name']] = cosine_similarity( [point['A1'], point['A2']], [data_point['A1'], data_point['A2']])

max_manhattan_result = max(manhattan_results, key= lambda x: manhattan_results[x])
print(f"\nManhattan Results:\n{manhattan_results}\nMax val: {max_manhattan_result}")

max_euclidean_result = max(euclidean_results, key= lambda x: euclidean_results[x])
print(f"\nEuclidean Results:\n{euclidean_results}\nMax val: {max_euclidean_result}")

max_supremum_result = max(supremum_results, key= lambda x: supremum_results[x])
print(f"\nSupremum Results:\n{supremum_results}\nMax val: {max_supremum_result}")

max_cosine_result = max(cosine_results, key= lambda x: cosine_results[x])
print(f"\nCosine Results:\n{cosine_results}\nMax val: {max_cosine_result}\n\n")