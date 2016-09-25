"""
This will contain scripts to read in the data and assemble a stitched
together set. Then it splits them into a train/valid/test sets. 

Saving data is taking the longest to compute
"""
import pandas as pd
import time, pickle
from sklearn.cross_validation import train_test_split

DATALENGTH = 1183748;
TRAIN_NUMERIC = "./data/train_numeric.csv"
TRAIN_CAT = "./data/train_categorical.csv"
TRAIN_DATE = "./data/train_date.csv"

# helper function to process imputing dictionaries
def load_dicts(x):
    if x=="mean":
        k = pickle.load( open("train_numeric_mean_dictionary.pkl","rb") )
    elif x=="median":
        k = pickle.load( open("train_numeric_median_dictionary.pkl","rb") )
    else:
        raise ValueError("Got a strange value for k --> %s" % str(x));
    return k;

i=0; n=10000; lf=[]; #n=100000;
k = load_dicts("mean")
#while i*n < DATALENGTH:
for i in range(1):
    start_time = time.time()
    print "Doing the numbers between %d and %d" % (i*n, (i+1)*n)

    print "reading train_ohe.csv"
    train_ohe = pd.read_csv("./data/train_categorical_ohe.csv",skiprows=i*n,nrows=n)

    print "reading train_numeric.csv"
    train_numeric = pd.read_csv("./data/train_numeric.csv",skiprows=i*n,nrows=n).fillna(k)

    print "reading train_date.csv"  # this still has 'NaN' values
    train_date = pd.read_csv("./data/train_date.csv",skiprows=i*n,nrows=n)

    print "appending and assembling everything together"
    lf.append(pd.merge(pd.merge(train_ohe,train_numeric,on="Id"),train_date,on="Id"));

    print "";
df = pd.concat(lf,axis=1);

print "writing to csv"
df.to_csv("./data/train_complete.csv")

# split data into 60/20/20
print "splitting data"
train, test_valid = train_test_split(df,train_size=0.6);
valid,test = train_test_split(test_valid,train_size=0.5);

# Then save everything
print "saving split data"
train.to_csv("./data/split_data/train.csv",index=False);
valid.to_csv("./data/split_data/valid.csv",index=False);
test.to_csv("./data/split_data/test.csv",index=False);
