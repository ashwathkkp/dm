# Boxplots
# Quantile plot
# Quantile- Quantile plot
# Histograms
# Scatter Plots 

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm

data = sns.load_dataset("iris")

sns.boxplot(x = data["species"], y = data["sepal_length"])
plt.show()

sns.distplot(x = data["petal_length"], hist=True, kde=False, rug=False)
plt.show()

sns.scatterplot(x = data["sepal_length"], y = data["sepal_width"])
plt.show()

rd = pd.DataFrame(np.array(data["sepal_length"].tolist()))
res = rd.describe().T.drop('count', axis=1)
plt.plot([res["min"], res["25%"], res["50%"], res["75%"], res["max"]], [0,0.25,0.5,0.75,1])
plt.show()

sm.qqplot( data["sepal_length"])
plt.show()
