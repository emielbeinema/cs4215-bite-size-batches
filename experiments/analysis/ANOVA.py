import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols


def format_floats(x, **kwargs):
    if x < 1:
        return "\\num{{{:0.3e}}}".format(x, **kwargs)
    elif x != x: #NaN
        return "---"
    else:
        return "\\num{{{:0.3f}}}".format(x, **kwargs)


def normalize_data(data):
    return (data-data.min())/(data.max()-data.min()) * 2 - 1


def make_latex_anova(file, formula):
    data_exploration = pd.read_csv(file, index_col=0)
    data_exploration = normalize_data(data_exploration)

    lm = ols(formula, data=data_exploration, drop_cols=['Index']).fit()
    anova_table = sm.stats.anova_lm(lm, typ=2)
    return anova_table.to_latex(float_format=format_floats, na_rep='---', escape=False)


# ANOVA of the Exploration Experiment
print(make_latex_anova('../data/ex-2019-10-06_03:29_exploration.csv', 'accuracy ~( batch_size + num_nodes )**2'))

# ANOVA of the Memory Size experiment
print(make_latex_anova('../data/ex-2019-10-14_13:03_factorial-memory.csv', 'accuracy ~( batch_size + num_nodes + memory_size )**2'))

# ANOVA of the Fractional Factorial experiment
print(make_latex_anova('../data/ex-2019-10-18_13:09_gsd.csv', 'accuracy ~( batch_size + num_nodes + memory_size )**2'))
