import pandas as pd
from statsmodels.formula.api import ols

from experiments.exploration.generator import experiment_design

lm = ols("accuracy ~" + "(" + '+'.join(experiment_design.columns) + ")**2",
         data=pd.read_csv("results.csv")).fit()
print(lm.summary2())
