# Helper function to read in the data
import pandas as pd
from random import randint

DATALENGTH = 1183748;
TRAIN_NUMERIC = "./data/train_numeric.csv"
TRAIN_CAT = "./data/train_categorical.csv"
TRAIN_DATE = "./data/train_date.csv"

def read_data_numeric(n,i=0):           
    i = i * n;
    cols = pd.read_csv(TRAIN_NUMERIC,nrows=5).columns.tolist();
    while i < DATALENGTH:
          df = pd.read_csv(TRAIN_NUMERIC,skiprows=i,nrows=n)
          df.columns = cols;
          yield df;
          i += n;

def read_data_categorical(n,i=0):           
    i = i * n;
    cols = pd.read_csv(TRAIN_CAT,nrows=5).columns.tolist();
    while i < DATALENGTH:
          df = pd.read_csv(TRAIN_CAT,skiprows=i,nrows=n)
          df.columns = cols;
          yield df;
          i += n;

def read_data_date(n,i=0):           
    i = i * n;
    cols = pd.read_csv(TRAIN_DATE,nrows=5).columns.tolist();
    while i < DATALENGTH:
          df = pd.read_csv(TRAIN_DATE,skiprows=i,nrows=n)
          df.columns = cols;
          yield df;
          i += n;




        
