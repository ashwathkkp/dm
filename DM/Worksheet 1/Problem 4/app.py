import seaborn as sns
import matplotlib.pyplot as plt

# Pblm: Find the time by which 75% of the children in school A had completed the puzzle. 
# Soln: 75% is quartile 3. Its value from the graph is 17. So, 75% of the children complete the puzzle in around 17 minutes.

# Pblm: State what the two crosses (x) represent on the box plot above. Interpret these in context
# Soln: The two crosses are outliers. Two students are taking a longer time to complete the puzzle

# Pblm: Determine if there are any outliers.
# Soln: There are no outliers

sns.boxplot([6,12,15,17,22])
plt.show()