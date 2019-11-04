import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

sns.set_style("whitegrid")
df = pd.read_csv("model_accuracies.csv")

ax = sns.barplot(x="score", y="classifier", data=df, color="orange")

ax.set(xlabel='Score', ylabel='Regressor')
# ax.set_xlabels("Score")
# ax.set_ylabels("Regressor")
plt.tight_layout()

ax.get_figure().savefig(f"model_comparison.eps")
plt.show()
