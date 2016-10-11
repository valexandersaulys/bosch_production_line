"""
This file is just for testing pandas
"""
from readin_data import read_data_all

def r():
    for train,valid,test in read_data_all():
        break;
    return train,valid,test;
