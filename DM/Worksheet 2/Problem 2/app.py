from collections import defaultdict
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

def minkowski_distance(X,Y):
    distance = 0
    for i in range(len(X)):
        distance += pow(abs(X[i]-Y[i]), 3)
    return pow(distance, 1/3)

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

df = pd.read_csv("./data.csv", names=['Document', 'Team', 'Coach', 'Hockey', 'Baseball', 'Soccer', 'Penalty', 'Score', 'Win', 'Loss', 'Season'])
manhattan_results, euclidean_results, supremum_results, cosine_results, minkowski_results = defaultdict(dict),defaultdict(dict),defaultdict(dict),defaultdict(dict), defaultdict(dict)

for i,x in df.iterrows():
    for j,y in df.iterrows():
        manhattan_results[x['Document']][y['Document']] = manhattan_distance([ x[k] for k in x.keys() if k != 'Document'], [ y[k] for k in y.keys() if k != 'Document'])
        euclidean_results[x['Document']][y['Document']] = euclidean_distance([ x[k] for k in x.keys() if k != 'Document'], [ y[k] for k in y.keys() if k != 'Document'])
        supremum_results[x['Document']][y['Document']] = supremum_distance([ x[k] for k in x.keys() if k != 'Document'], [ y[k] for k in y.keys() if k != 'Document'])
        cosine_results[x['Document']][y['Document']] = cosine_similarity([ x[k] for k in x.keys() if k != 'Document'], [ y[k] for k in y.keys() if k != 'Document'])
        minkowski_results[x['Document']][y['Document']] = minkowski_distance([ x[k] for k in x.keys() if k != 'Document'], [ y[k] for k in y.keys() if k != 'Document'])


#print(f"{manhattan_results}\n\n{euclidean_results}\n\n{supremum_results}\n\n{cosine_results}\n\n{minkowski_results}")

print(f"\nManhattan results")
for key in manhattan_results.keys():
    print(f"{key} -> {manhattan_results[key]}")

print(f"\nEuclidean results")
for key in euclidean_results.keys():
    print(f"{key} -> {euclidean_results[key]}")

print(f"\nSupremum results")
for key in supremum_results.keys():
    print(f"{key} -> {supremum_results[key]}")

print(f"\nCosine results")
for key in cosine_results.keys():
    print(f"{key} -> {cosine_results[key]}")

print(f"\nMinkowski results")
for key in minkowski_results.keys():
    print(f"{key} -> {minkowski_results[key]}")