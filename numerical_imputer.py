#!/.venv/bin/python
"""
This script imputes the missing data that is present to some degree  in train_numeric.
"""
import pandas as pd

# Going to read in the data column by column
cols = pd.read_csv("./data/train_numeric.csv",nrows=5).columns.tolist()

# Create a blank dataframe
pd.DataFrame(columns=cols[:5]).to_csv("./data/train_numeric_imputed.csv",index=False);
"""pd.DataFrame(cols[0],columns=['id']).to_csv(open("./data/train_numeric_imputed.csv",'a'),
                                            index=False);"""
#del cols[0];  # first is ID

for col in cols[:5]:
    print "Now completing %s" % str(col);
    
    df = pd.read_csv("./data/train_numeric.csv",usecols=[col])

    df = df.fillna(df.mean())  # maybe median?
    
    with open("./data/train_numeric_imputed.csv",'a') as f:
        df.to_csv(f,headers=False,index=False);
