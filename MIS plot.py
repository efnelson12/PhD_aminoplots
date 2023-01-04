# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 17:11:50 2022

@author: efn509
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

    
### Loop the data lines
with open("//userfs/efn509/w2k/MIS delta 18 values/lisiecki_recration.txt", 'r') as temp_f:
    # get No of columns in each line
    col_count = [ len(l.split("\t")) for l in temp_f.readlines() ]

### Generate column names  (names will be 0, 1, 2, ..., maximum columns - 1)
column_names = [i for i in range(0, max(col_count))]

### Read csv
df = pd.read_csv("//userfs/efn509/w2k/MIS delta 18 values/lisiecki_recration.txt", header=None, delimiter="\t", 
names=column_names)
col_names = list(df.iloc[0])
df = pd.read_csv("//userfs/efn509/w2k/MIS delta 18 values/lisiecki_recration.txt", header=None, delimiter="\t", names=col_names)
df.drop(0, inplace=True); df.reset_index(drop=True, inplace=True)

df

plot = sns.lineplot(data=df, x="Time(ka)", y="Benthic_d18O_(per mil)")
