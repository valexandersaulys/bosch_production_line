"""
This containers helper functions to assist in doing work
"""
from sklearn.metrics import confusion_matrix
from math import sqrt

def MCC_score(y_true,y_pred):
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    numerator = float( (tp*tn) - fp*fn  )
    denominator = sqrt( (tp+fp)*(tp+fn)*(tn+fp)*(tn+fn) );
    return float( numerator / denominator );
