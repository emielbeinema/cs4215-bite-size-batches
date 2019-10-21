import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

sns.set_style("whitegrid")
df = pd.read_csv("../data/ex-2019-10-14_13:03_factorial-memory.csv")

ax = sns.catplot(x="batch_size", y="accuracy", hue="num_nodes", col="memory_size", kind="box", data=df, legend=False, height=6, aspect=.75)
plt.legend(title="Number of nodes", loc='upper right')
ax.map(lambda color: plt.axvline(0.5, color="lightgrey"))
ax.axes[0,0].set_title("Memory size = 1GiB")
ax.axes[0,1].set_title("Memory size = 2GiB")
ax.set_axis_labels("Batch size", "Accuracy")

ax.savefig("memory_plot.eps")
plt.show()
