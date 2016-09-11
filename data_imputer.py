#!.venv/bin/python
"""
This is to impute values in the train_numeric from a pickled dictionary of values
"""
import pandas as pd
import pickle

cols = pd.read_csv("./data/train_numeric.csv",nrows=5).columns.tolist()

# Create a blank file to later append to 
pd.DataFrame(columns=col).to_csv("./data/train_numeric_imputed.csv",index=False)
k = pickle.load( open( "train_numeric_mean_dictionary.pkl", "rb" ) )

i = 0; nrows = 10000;
while (i*nrows) < 1183748:
    print "Now reading lines %d through %d" % (i*nrows,nrows);
    df = pd.read_csv("./data/train_numeric.csv",skiprows=(i*nrows),nrows=nrows);
    df.fillna(k)  # this should be able to take a dictionary
    
    with open("./data/train_numeric_imputed.csv",'a') as f:
        df.to_csv(f,headers=False)
