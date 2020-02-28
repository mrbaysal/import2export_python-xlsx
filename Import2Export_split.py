"""
import numpy as np
import pandas as pd

from dfply import *
path_toget='path'
path_togo='path'
df=pd.read_excel(path_toget+'.xlsx')

for i in range(len(df['X'])):
    a=df>>filter_by(df.Sirketler==df['X'][i])
    a.reset_index(drop=True)
    a.index=a.index+1
    a.to_excel(path_togo+'{}.xlsx'.format(df['X'][i]))

"""