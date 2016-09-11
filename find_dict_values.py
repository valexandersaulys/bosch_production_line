#!/.venv/bin/python
"""
This script imputes the missing data that is present to some degree  in train_numeric.
"""
import pandas as pd
import pickle

# Going to read in the data column by column
cols = pd.read_csv("./data/train_numeric.csv",nrows=5).columns.tolist()

# Create a blank dataframe
pd.DataFrame(columns=cols[:5]).to_csv("./data/train_numeric_imputed.csv",index=False);
"""pd.DataFrame(cols[0],columns=['id']).to_csv(open("./data/train_numeric_imputed.csv",'a'),
                                            index=False);"""
#del cols[0];  # first is ID
k_mean = {}; k_median = {}; k_mode = {};

i = 1;
for col in cols:
    print "Now completing %s, Col %d of %d" % (str(col),i,len(cols)+1);

    # this is the bottleneck
    df = pd.read_csv("./data/train_numeric.csv",usecols=[col]);

    k_mean[col] = df.mean().tolist()[0];
    k_median[col] = df.median().tolist()[0];
    k_mode[col] = df.mode().tolist()[0];

    i += 1;

print "now pickling... the average!"
output = open('train_numeric_mean_dictionary.pkl', 'wb');
pickle.dump(k_mean, output)
output.close();

print "now pickling... the median!"
output = open('train_numeric_median_dictionary.pkl','wb');
pickle.dump(k_median, output);
output.close();

print "now pickling... the mode!"
output = open('train_numeric_mode_dictionary.pkl','wb');
pickle.dump(k_mode, output);
output.close();

print "All done!"
