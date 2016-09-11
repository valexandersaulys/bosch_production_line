import pandas as pd
import pickle

l = ['./old_dicts/train_numeric_median_dictionary.pkl','./old_dicts/train_numeric_mode_dictionary.pkl']

for x in l:
    new_k = {}
    k = pickle.load( open( x, "rb" ) )
    for entry in k:
        new_k[entry] = k[entry].tolist()[0]
    pickle.dump( new_k, open(x[12:],"wb") )
