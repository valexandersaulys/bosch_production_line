"""
This will contain scripts to read in the data and assemble a stitched
together set. Then it splits them into a train/valid/test sets. 

Saving data is taking the longest to compute
"""
import pandas as pd
import time, pickle
from sklearn.cross_validation import train_test_split
import logging

DATALENGTH = 1183748;
TRAIN_NUMERIC = "./data/train_numeric.csv"
TRAIN_CAT = "./data/train_categorical.csv"
TRAIN_DATE = "./data/train_date.csv"

# Setup logging
logging.basicConfig(filename="assemble.log",level=logging.DEBUG);

# helper function to process imputing dictionaries
def load_dicts(x):
    if x=="mean":
        k = pickle.load( open("train_numeric_mean_dictionary.pkl","rb") )
        kk = pickle.load( open("train_date_mean_dictionary.pkl","rb") )
    elif x=="median":
        k = pickle.load( open("train_numeric_median_dictionary.pkl","rb") )
        kk = pickle.load( open("train_date_median_dictionary.pkl","rb") )
    else:
        raise ValueError("Got a strange value --> %s" % str(x));
    return k,kk;

# Get columns before plunging forward
categorical_cols = pd.read_csv("./data/train_categorical_ohe.csv",nrows=5).columns.tolist()
numeric_cols = pd.read_csv("./data/train_numeric.csv",nrows=5).columns.tolist()
date_cols = pd.read_csv("./data/train_date.csv",nrows=5).columns.tolist()

i=0; n=10000; lf=[]; #n=100000;
k,kk = load_dicts("mean")
#for i in range(1):
while (i-1)*n < DATALENGTH:
    start_time = time.time()
    logging.debug("Doing the numbers between %d and %d" % (i*n, (i+1)*n))

    logging.debug("reading train_ohe.csv")
    train_ohe = pd.read_csv("./data/train_categorical_ohe.csv",skiprows=i*n,nrows=n,header=None)

    logging.debug("reading train_numeric.csv")
    train_numeric = pd.read_csv("./data/train_numeric.csv",skiprows=i*n,
                                nrows=n,header=None).fillna(k)

    logging.debug("reading train_date.csv");  # this still has 'NaN' values
    train_date = pd.read_csv("./data/train_date.csv",skiprows=i*n,
                             nrows=n,header=None).fillna(kk);

    logging.debug("Assigning Correct Columns")
    train_ohe.columns = categorical_cols
    train_numeric.columns = numeric_cols
    train_date.columns = date_cols
    
    logging.debug("appending and assembling everything together")
    lf.append(pd.merge(pd.merge(train_ohe,train_numeric,on="Id"),train_date,on="Id"));

    i += 1;
    logging.debug("- - - - - Took %f seconds - - - - -" % (time.time() - start_time));
    logging.debug("");

    # Clear out everything
    del train_ohe;
    del train_numeric;
    del train_date;
    

df = pd.concat(lf,axis=1);

logging.debug("writing to csv")
df.to_csv("./data/train_complete.csv")

# split data into 60/20/20
logging.debug("splitting data")
train, test_valid = train_test_split(df,train_size=0.6);
valid, test = train_test_split(test_valid,train_size=0.5);

# Then save everything
logging.debug("saving split data")
train.to_csv("./data/split_data/train.csv",index=False);
valid.to_csv("./data/split_data/valid.csv",index=False);
test.to_csv("./data/split_data/test.csv",index=False);
