
from cmath import sqrt
import numpy as np
import pandas as pd

def z_score_normalization(data: pd.DataFrame)-> pd.DataFrame:
    normalized_data = {}
    mean_values = {}
    standard_deviation_values = {}

    for column in data.columns:
        normalized_data[column] = []
        mean_values[column] = np.mean(data[column].tolist())
        standard_deviation_values[column] = np.std(data[column].tolist())

    for index, row in data.iterrows():
        for column in data.columns:
            result = (row[column] - mean_values[column]) / standard_deviation_values[column]
            normalized_data[column].append(result)
    return pd.DataFrame(normalized_data)

def calc_pearson_correlation_coefficient(X: list,Y: list)-> float:
    N = len(X)
    x_mean, y_mean = np.mean(X), np.mean(Y)
    s_xy, s_xx, s_yy = 0, 0, 0
    for i in range(N):
        s_xy += (X[i]-x_mean)*(Y[i]-y_mean)
        s_xx += (X[i]-x_mean)**2
        s_yy += (Y[i]-y_mean)**2
    result = s_xy / (s_xx*s_yy)**0.5
    return result


data = pd.read_csv("data.csv", names = ["Age", "Fat"])
normalized_data = z_score_normalization(data)
print(f"Normalized data based on Z-score : \n{normalized_data}")
res = calc_pearson_correlation_coefficient( normalized_data["Age"].tolist(), normalized_data["Fat"].tolist() )
print(f"\nPearson Coefficient between Age and Fat is : { res } ")


