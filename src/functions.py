import scipy.stats as scs
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import re
import json


def is_bad_import(x):
    '''
    Checks if row is of numeric type.  If row is numeric, returns True, else returns false
    --------
    PARAMETERS
    x: str, bool, int, list, set, etc...
        -   Input to check
    --------
    RETURNS
    __: bool
        -   True if x is not numeric, False if x is numeric
    '''
    try:
        float(x)
        return True
    except:
        return False


def get_date(dt):
    '''
    convert datetime string to python datetime.date output
    --------
    PARAMETERS
    dt: str - Date or datetime input (can also be in datetime.datetime format)
    --------
    RETURNS
    dateout: datetime.date - truncated datetime as date
    '''
    dlst = str(dt).strip().split()[0].split('-')
    return date(int(dlst[0]), int(dlst[1]), int(dlst[2]))

def get_count(cell):
    '''
    converts nltk parts of speech tuples into counts of parts of speech
    '''
    cnt_dict = Counter()
    for i in cell:
        cnt_dict[i[:2]] += 1
    return cnt_dict