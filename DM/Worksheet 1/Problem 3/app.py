import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = [6, 25, 39, 62, 65, 74, 80, 94, 125, 127, 154, 159, 184, 210, 251]
quartiles = np.percentile(data, [25,50,75])
print(f"Median = {np.median(data)}\nQuartiles = {quartiles}")

inter_quantile_region = quartiles[2] - quartiles[0]
low = quartiles[0] - 1.5*inter_quantile_region
high = quartiles[2] + 1.5*inter_quantile_region
outliers = []
for i in data:
  if i > high or i < low:
    outliers.append(i)
print(f"Outliers in dataset: {outliers}")

sns.boxplot(data)
plt.show()
