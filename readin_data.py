# Helper function to read in the data
import pandas as pd
from random import randint
import pickle
from sklearn.cross_validation import train_test_split

DATALENGTH = 1183748;
TRAIN_NUMERIC = "./data/train_numeric.csv"
TRAIN_CAT = "./data/train_categorical_ohe.csv"
TRAIN_DATE = "./data/train_date.csv"

def read_data_all(n=10000,i=0,imputing="mean",split_size=0.3): 
    i = 0;
    cols_numeric = pd.read_csv(TRAIN_NUMERIC,nrows=5).columns.tolist();
    cols_ohe = pd.read_csv(TRAIN_CAT,nrows=5).columns.tolist();
    cols_date = pd.read_csv(TRAIN_DATE,nrows=5).columns.tolist();
    k,kk = load_dicts(imputing);
    A = True; B = True;
    while A:
        # Numeric Data
        df_numeric = pd.read_csv(TRAIN_NUMERIC,skiprows=i*n,nrows=n,header=None,low_memory=False)
        df_numeric.columns = cols_numeric;
        df_numeric = df_numeric.fillna(k);

        # OHE Categorical Data
        df_ohe = pd.read_csv(TRAIN_CAT,skiprows=i*n,nrows=n,header=None,low_memory=False)
        df_ohe.columns = cols_ohe;
        df_ohe = df_ohe.fillna(kk);

        # Date Data
        df_date = pd.read_csv(TRAIN_DATE,skiprows=i*n,nrows=n,header=None,low_memory=False)
        df_date.columns = cols_date;
        df_date = df_date.fillna(0);  # damn time values screwing things up

        # Then assmeble together
        df = pd.merge(pd.merge(df_ohe,df_numeric,on="Id"),df_date,on="Id")
        del df_numeric, df_ohe, df_date; # To clear out memory, hopefully
        
        train, kooky = train_test_split(df,test_size=split_size);
        valid, test = train_test_split(kooky,test_size=0.5);
        yield train,valid,test;
        i += 1;
        # Want to go just one over the data length
        if ((i*n) < DATALENGTH) and (B==False):
            A = True;
        elif (i*n) < DATALENGTH:
            B = False;
        else:
            A = False;

def read_data_categorical(n,i=0):           
    i = 0;
    cols = pd.read_csv(TRAIN_CAT,nrows=5).columns.tolist();
    while i < DATALENGTH:
        df = pd.read_csv(TRAIN_CAT,skiprows=(i*n),nrows=n)
        df.columns = cols;
        yield df;
        i += 1;
        
def read_data_date(n,i=0):           
    i = 0;
    cols = pd.read_csv(TRAIN_DATE,nrows=5).columns.tolist();
    while i < DATALENGTH:
        df = pd.read_csv(TRAIN_DATE,skiprows=(i*n),nrows=n)
        df.columns = cols;
        yield df;
        i += 1;

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


        
