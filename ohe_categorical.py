#!.venv/bin/activate
"""
"""
import pandas as pd
import multiprocessing,time
from readin_data import read_data_categorical

SAVENAME = "./data/train_categorical_ohe.csv"
columns = pd.read_csv("./data/train_categorical.csv",nrows=5).columns.tolist()
"""
# Get every column, turn them into OHE, write them to separate CSV files with the 'Id' column too
# Running this parallelized (I have an 8 core machine)
def f(column):
    df = pd.read_csv("./data/train_categorical.csv",usecols=['Id',column])
    pd.get_dummies(df,dummy_na=True).to_csv("./data/ohe_separate/"+column+".csv",index=False);

pool = multiprocessing.Pool(processes=8)
pool.map(f,columns[1:])
"""
# Read each separate CSV for a limited # of nrows, build a master CSV from that
i = 0; DATALENGTH = 1183748; n=100000;
while i*n < DATALENGTH:
    start_time = time.time()
    print "Doing the numbers between %d and %d" % (i*n,(i+1)*n)
    lf=[]; j=0;
    # Is there a way to parallize this via map/reduce?
    for column in columns[1:]:
        #print "Completing Column %d of %d" % (j+1,len(columns[1:])+1);  # This takes no time
        cf = pd.read_csv("./data/ohe_separate/"+column+".csv",skiprows=i*n,nrows=n)
        lf.append(cf);
        j += 1;
    print "Now Concatenating..."
    df = pd.concat(lf,axis=1);

    if i==0:
        with open("./data/train_categorical_ohe.csv","a") as f:
            df.to_csv(f,index=False)
    else:
        with open("./data/train_categorical_ohe.csv","a") as f:
            df.to_csv(f,headers=False,index=False)
    i += 1;
    print "- - - - time elapsed %f - - - -" % float(time.time() - start_time);
