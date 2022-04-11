from collections import defaultdict
import pandas as pd

def getState(x):
    if x == "P" or x == "Y":
        return "True"
    return "False"

def get_binary_attribute_dissimilarity(X,Y):
    matched = defaultdict(dict)
    matched["True"]["True"] = 0
    matched["True"]["False"] = 0
    matched["False"]["True"] = 0
    matched["False"]["False"] = 0
    for xi,yi in zip(X,Y):
        matched[getState(xi)][getState(yi)] += 1
    # print(matched)
    return (matched["True"]["False"]+matched["False"]["True"]) / (matched["True"]["True"]+matched["True"]["False"]+matched["False"]["True"])


df = pd.read_csv("./data.csv", names=['Name', 'Gender', 'Fever', 'Cough', 'Test-1', 'Test-2', 'Test-3', 'Test-4'])
similarity_results = defaultdict(dict)
del df['Gender']

for i,x in df.iterrows():
    for j,y in df.iterrows():
        if x['Name'] != y['Name']:
            similarity_results[x['Name']][y['Name']] = get_binary_attribute_dissimilarity([ x[k] for k in x.keys() if k != 'Name'], [ y[k] for k in y.keys() if k != 'Name'])

print(f"Dissimilarity results")
for key in similarity_results.keys():
    print(f"{key} -> {similarity_results[key]}")
