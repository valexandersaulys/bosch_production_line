#!/.venv/bin/python
"""
This script imputes the missing data that is present to some degree  in train_numeric.
"""
import pandas as pd
import numpy as np

# Going to read in the data column by column
cols = pd.read_csv("./data/train_numeric.csv",nrows=5).columns.tolist()
del cols[0];  # first is ID

for col in cols:
    df = pd.read_csv("./data/train_numeri.csv",usecols=[col])

    df.fillna(df.mean())  # maybe median?
    
    with open("./data/train_numeric_imputed.csv",'a') as f:
        df.to_csv(f,header=False);

