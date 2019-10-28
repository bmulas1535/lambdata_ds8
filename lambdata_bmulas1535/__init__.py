"""
lambdata - a collection of data science helper functions
"""
import pandas as pd 
import numpy as np 

# More code here #
ONES = pd.DataFrame(np.ones(10))
ZEROS = pd.DataFrame(np.zeros(50))

def test_func():
    print('This is a test function.')
    return
def increment(x):
    return(x + 1)