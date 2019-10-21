import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

sns.set_style("whitegrid")
df = pd.read_csv("ridge_accuracies.csv")

means = df.groupby(["alpha", "solver", "tolerance"]).mean().reset_index()
# print(means.reset_index().min())
# print(means.iloc[means.idxmin()["score"]])
print(means.iloc[means["score"].idxmin()])

print(means[(means["alpha"] == 1) & (means["solver"] == "auto") & (means["tolerance"] == 0.001)])

ax = sns.barplot(x="score", y="solver", hue="alpha", data=df[df["tolerance"] == 1e-6])

ax.set(xlabel='Score', ylabel='Solver')
# ax.set_xlabels("Score")
# ax.set_ylabels("Regressor")
plt.tight_layout()

ax.get_figure().savefig(f"ridge_comparison_alpha.eps", bbox_inches='tight')
plt.show()

ax = sns.barplot(x="score", y="solver", hue="tolerance", data=df[df["alpha"] == 10])

ax.set(xlabel='Score', ylabel='Solver')
# ax.set_xlabels("Score")
# ax.set_ylabels("Regressor")
plt.tight_layout()

ax.get_figure().savefig(f"ridge_comparison_tolerance.eps", bbox_inches='tight')
plt.show()
