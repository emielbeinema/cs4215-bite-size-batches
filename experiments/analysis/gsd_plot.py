import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

sns.set_style("whitegrid")
df = pd.read_csv("../data/ex-2019-10-18_13:09_gsd.csv")

real_names = {
    "batch_size": "Batch size",
    "num_nodes": "Number of nodes",
    "memory_size": "Memory size",
}

for p1, p2 in (("batch_size", "num_nodes"), ("batch_size", "memory_size"), ("num_nodes", "memory_size")):
    ax = sns.catplot(x=p1, y="accuracy", hue=p2, markers=["x", "o", "s"],
                     height=6, aspect=.75, capsize=.2,
                     kind="point", data=df, legend=False)

    ax.set_xlabels(real_names[p1])
    ax.set_ylabels("accuracy")
    plt.legend(title=real_names[p2], loc='upper right')

    ax.savefig(f"gsd_plot_{p1}_{p2}.eps")
    plt.show()

