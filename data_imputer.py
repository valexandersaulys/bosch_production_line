#!.venv/bin/python
"""
This is to impute values in the train_numeric from a pickled dictionary of values
"""
import pandas as pd
import pickle

cols = pd.read_csv("./data/train_numeric.csv",nrows=5).columns.tolist()

# Create a blank file to later append to
SAVENAME = "./data/train_numeric_imputed_mean.csv"
pd.DataFrame(columns=cols).to_csv(SAVENAME,index=False)
k = pickle.load( open( "train_numeric_mean_dictionary.pkl", "rb" ) )

i = 0; nrows = 100000;
while (i*nrows) < 1183748:
    print "Now reading lines %d through %d" % (i*nrows,(i+1)*nrows);
    df = pd.read_csv("./data/train_numeric.csv",skiprows=(i*nrows),nrows=nrows);
    df = df.fillna(k)  # this should be able to take a dictionary
    
    with open(SAVENAME,'a') as f:
        df.to_csv(f,headers=False)

    i += 1;
