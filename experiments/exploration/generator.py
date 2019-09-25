import numpy as np
import pandas as pd
from dexpy import factorial, design

NUM_REPEATS = 5

actual_lows = {
    'batch_size': 64,
    'num_nodes': 1,
    'failure_rate': 0,
    'failure_duration': 0,
}
actual_highs = {
    'batch_size': 256,
    'num_nodes': 4,
    'failure_rate': 0.5,
    'failure_duration': 20,
}
experiment_design = factorial.build_factorial(4, 2 ** 4)
experiment_design.columns = ['batch_size', 'num_nodes', 'failure_rate', 'failure_duration']

actual_design = design.coded_to_actual(experiment_design, actual_lows, actual_highs)
design_with_repeats = pd.DataFrame(np.repeat(actual_design.values, 5, axis=0))
design_with_repeats.columns = actual_design.columns
design_with_repeats.to_csv("design.csv")
