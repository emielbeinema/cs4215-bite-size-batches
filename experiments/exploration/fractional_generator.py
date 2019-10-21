import pyDOE2
import numpy as np
import pandas as pd

# batch size: 32, 64, 128, 256, 512, 1024
# num nodes: 1, 2, 3, 4
# memory size: 1024, 1536, 2048

levels = [6, 3, 3]
reduction = 2

df = pd.DataFrame(pyDOE2.gsd(levels, reduction), columns=[
    'batch_size', 'num_nodes', 'memory_size'
])
df['batch_size'] = df['batch_size'].map({0: 32, 1: 64, 2: 128, 3: 256, 4: 512, 5: 1024})
df['num_nodes'] = df['num_nodes'].map({0: 1, 1: 2, 2: 4})
df['memory_size'] = df['memory_size'].map({0: 1024, 1: 1536, 2: 2048})

design_with_repeats = pd.DataFrame(np.repeat(df.values, 5, axis=0))

design_with_repeats.to_csv("gsd3.csv")

