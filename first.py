import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
ar = np.array([1, 2, 3, 4, 5, 67, 41, 0, 89, 75, 41, 25])
np.sum(ar)
len(ar)
np.sum(ar)/len(ar)
np.sort(ar)
np.mean(ar)
dataset = pd.read_csv("Train.csv")
dataset.head(4)
np.mean(dataset["Price"])
mn = dataset['Price'].mean()
sns.histplot(x="Price", data=dataset, bins=[i for  i in range (0, 600, 100)])
plt.plot([mn for i in range (0,4500)],[i for i in range (0,4500)], c="red")
plt.show()