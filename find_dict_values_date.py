#!/.venv/bin/python
"""
This script imputes the missing data that is present to some degree  in train_numeric.
"""
import pandas as pd
import pickle
from multiprocessing import Pool

# Going to read in the data column by column
cols = pd.read_csv("./data/train_date.csv",nrows=5).columns.tolist()

#del cols[0];  # first is ID
k_mean = {}; k_median = {}; k_mode = {};


# Define the function to pool
def get_col(col):
    print "Now Completing %s" % str(col);
    
    # this is the bottleneck
    df = pd.read_csv("./data/train_date.csv",usecols=[col]);
    
    k_mean[col] = df.mean().tolist()[0];
    k_median[col] = df.median().tolist()[0];

p = Pool(7);
print p.map(get_col,cols[1:]);
    
print "now pickling... the average!"
output = open('train_date_mean_dictionary.pkl', 'wb');
pickle.dump(k_mean, output)
output.close();

print "now pickling... the median!"
output = open('train_date_median_dictionary.pkl','wb');
pickle.dump(k_median, output);
output.close();

print "All done!"
