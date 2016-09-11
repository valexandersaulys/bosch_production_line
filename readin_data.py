# Helper function to read in the data
import pandas as pd
from random import randint

DATALENGTH = 1183748;
TRAIN_NUMERIC = "./data/train_numeric.csv"
TRAIN_CAT = "./data/train_categorical.csv"
TRAIN_DATE = "./data/train_date.csv"

def read_data_numeric(n,i=0,imputing="mean"): 
    i = 0;
    cols = pd.read_csv(TRAIN_NUMERIC,nrows=5).columns.tolist();
    k = load_dicts(imputing);
    while i < DATALENGTH:
          df = pd.read_csv(TRAIN_NUMERIC,skiprows=(i*n),nrows=n)
          df.columns = cols;
          yield df.fillna(k);
          i += 1;

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
    elif x=="median":
        k = pickle.load( open("train_numeric_median_dictionary.pkl","rb") )
    else:
        raise ValueError("Got a strange value for k --> %s" % str(x));
    return k;


        
