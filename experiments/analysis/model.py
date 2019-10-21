import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import sklearn
from sklearn.linear_model import BayesianRidge, LinearRegression, Ridge, Lasso, MultiTaskLasso, \
    ElasticNet, Lars, LassoLars, OrthogonalMatchingPursuit, ARDRegression, LogisticRegression, \
    SGDRegressor
from sklearn.model_selection import cross_val_score

df = pd.read_csv("../data/ex-2019-10-18_13:09_gsd.csv")

# ax = sns.lineplot(x="batch_size", y="accuracy", hue="memory_size", data=df)
#
# ax.get_figure().savefig("test.png")
# plt.show()

X = df.values[:, [2, 3, 4]]
y = df.values[:, 5]

classifiers = (
    ("linear_regression", LinearRegression()),
    ("ridge", Ridge()),
    ("lasso", Lasso()),
    ("elastic_net", ElasticNet()),
    ("lars", Lars()),
    ("lasso_lars", LassoLars()),
    ("orthogonal_mp", OrthogonalMatchingPursuit()),
    ("bayesian_ridge", BayesianRidge()),
    ("ard_regression", ARDRegression()),
)

FOLDS = 5
results = pd.DataFrame(columns=["classifier", "score"])

for i, classifier_pair in enumerate(classifiers):
    name, classifier = classifier_pair

    print(f"Classifier: {name}")

    scores = -1 * cross_val_score(classifier, X, y, scoring="neg_mean_squared_error", cv=FOLDS)
    print(f"Mean score: {scores.mean()}")

    for j, score in enumerate(scores):
        results.loc[i * FOLDS + j] = [name, score]

    model = classifier.fit(X, y)

    batch_sizes = [2**i for i in range(6, 11)]

    projected_accuracies = model.predict(list([[batch_size, 1, 3] for batch_size in batch_sizes]))

    model_df = pd.DataFrame({"batch_size": batch_sizes, "projected_accuracy": projected_accuracies})
    print(model_df.to_latex())

    # ax = sns.lineplot(x="batch_size", y="projected_accuracy", data=model_df)

    # ax.get_figure().savefig("test.png")
    # plt.show()

results.to_csv("model_accuracies.csv")
