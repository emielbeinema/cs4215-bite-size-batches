import pandas as pd
from sklearn.linear_model import BayesianRidge, LinearRegression, Ridge, Lasso, ElasticNet, Lars, \
    LassoLars, OrthogonalMatchingPursuit, ARDRegression
from sklearn.model_selection import cross_val_score

df = pd.read_csv("../data/ex-2019-10-18_13:09_gsd.csv")

# ax = sns.lineplot(x="batch_size", y="accuracy", hue="memory_size", data=df)
#
# ax.get_figure().savefig("test.png")
# plt.show()

X = df.values[:, [2, 3, 4]]
y = df.values[:, 5]
classifiers = []

for alpha in (0.1, 1, 10, 100, 1000):
    for solver in ("auto", "svd", "cholesky", "lsqr", "sparse_cg", "sag", "saga"):
        for tol in (1e-6, 1e-5, 1e-4, 1e-3, 1e-2):
            classifiers.append([alpha, solver, tol])

FOLDS = 5
results = pd.DataFrame(columns=["alpha", "solver", "tolerance", "score"])

for i, params in enumerate(classifiers):
    print(f"Classifier: {params}")

    classifier = Ridge(alpha=params[0], solver=params[1], tol=params[2])
    scores = -1 * cross_val_score(classifier, X, y, scoring="neg_mean_squared_error", cv=FOLDS)
    print(f"Mean score: {scores.mean()}")

    for j, score in enumerate(scores):
        results.loc[i * FOLDS + j] = [*params, score]

    model = classifier.fit(X, y)

    batch_sizes = [2 ** i for i in range(6, 11)]

    projected_accuracies = model.predict(list([[batch_size, 1, 3] for batch_size in batch_sizes]))

    model_df = pd.DataFrame({"batch_size": batch_sizes, "projected_accuracy": projected_accuracies})
    print(model_df.to_latex())

    # ax = sns.lineplot(x="batch_size", y="projected_accuracy", data=model_df)

    # ax.get_figure().savefig("test.png")
    # plt.show()

results.to_csv("ridge_accuracies.csv")
