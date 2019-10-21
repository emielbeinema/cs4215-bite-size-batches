import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

sns.set_style("whitegrid")
df = pd.read_csv("../data/ex-2019-10-06_03:29_exploration.csv")

ax = sns.catplot(x="batch_size", y="accuracy", hue="num_nodes", kind="box", data=df, legend=False)
ax.set_xlabels("Batch size")
ax.set_ylabels("Accuracy")
plt.legend(title="Number of nodes", loc='upper right')
ax.savefig("exploration_plot.eps")
plt.show()

