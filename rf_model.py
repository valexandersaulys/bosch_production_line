"""
Builds a simple random forest model
"""
from readin_data import read_data_all
from sklearn.ensemble import RandomForestClassifier
from utils import *

validation = []; testing = [];

# Read in the Data & train the model
rf_model = RandomForestClassifier(n_estimators=100);
for train,valid,test in read_data_all():
    rf_model.fit(train.drop('Response',axis=1),train['Response']);
    testing.append(test);
    y_true = valid['Response']
    y_preds = rf_model.predict(valid.drop('Response',axis=1));
    print "Score on Validation: %f" % MCC_score(y_true,y_preds);
    del train; del valid; del test;

# Concatenate the testing dataset
test_df = pd.concat(testing);
del testing;
y_preds = rf_model.predict(test_df.drop('Response',axis=1));
y_test = test_df['Response'];
print "Score on Test Set: %f" % MCC_score(y_test,y_preds);


