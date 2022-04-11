import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = [17, 23, 35, 36, 51, 53, 54, 55, 60, 77, 110]
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
