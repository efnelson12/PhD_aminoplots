# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 12:23:21 2022

@author: efn509
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 16:42:03 2022

@author: efn509
"""

#script to compare age with D/L values
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.patches as mpatches

#import csv
THAA_AA = pd.read_csv('R:/NEaar/People/Ellie Nelson/EQuate frameworks/Hungary/Age errorcsv.csv')


# code if want to look at averages between horizons instead of replicates

#pulling THAA into dataframe
df_THAA = pd.DataFrame(THAA_AA)

mean_dl = df_THAA.groupby(['Age Mid Point',"Min","Max", "Quaternary sites"]).agg({'Val D/L': ['mean', 'min', 'max']}).reset_index()
y = list(mean_dl['Val D/L', 'mean'])
min_age = list(mean_dl['Min', ''])
max_age = list(mean_dl['Max', ''])
mean_dl['Val D/L', 'min'] = mean_dl['Val D/L', 'min'] - 0.02
mean_dl['Val D/L', 'max'] = mean_dl['Val D/L', 'max'] + 0.02

min_dl = list(mean_dl['Val D/L', 'min'])
max_dl = list(mean_dl['Val D/L', 'max'])


sns.set(style="ticks")
plt.Figure(figsize=(14,8))
#plt.hlines(y= y[0], xmin=min_dl[0], xmax=max_dl[0],
 #         color='b')
#plt.hlines(y= y[1], xmin=min_dl[1], xmax=max_dl[1],
 #         color='b')
#plt.hlines(y= y[2], xmin=min_dl[2], xmax=max_dl[2],
 #         color='b')
#plt.hlines(y= y[3], xmin=min_dl[3], xmax=max_dl[3],
 #         color='b')
#plt.hlines(y= y[4], xmin=min_dl[4], xmax=max_dl[4],
 #         color='b')
#plt.hlines(y= y[5], xmin=min_dl[5], xmax=max_dl[5],
 #         color='b')
#plt.hlines(y= y[6], xmin=min_dl[6], xmax=max_dl[6],
 #         color='b')
#plt.hlines(y= y[7], xmin=min_dl[7], xmax=max_dl[7],
 #         color='b')
#plt.hlines(y= y[8], xmin=min_dl[8], xmax=max_dl[8],
 #         color='b')
#plt.hlines(y= y[9], xmin=min_dl[9], xmax=max_dl[9],
 #         color='b')
#plt.(min_dl[0], max_dl[0], facecolor='w', alpha=0.2)
#plt.axvspan(min_dl[1], max_dl[1], facecolor='g', alpha=0.2)
#plt.axvspan(min_dl[2], max_dl[2], facecolor='r', alpha=0.2)
#plt.axvspan(min_dl[3], max_dl[3], facecolor='blue', alpha=0.2)
#plt.axvspan(min_dl[4], max_dl[4], facecolor='orange', alpha=0.2)
#plt.axvspan(min_dl[5], max_dl[5], facecolor='pink', alpha=0.2)
#plt.axvspan(min_dl[6], max_dl[6], facecolor='yellow', alpha=0.2)
#plt.axvspan(min_dl[7], max_dl[7], facecolor='purple', alpha=0.2)
#plt.axvspan(min_dl[8], max_dl[8], facecolor='magenta', alpha=0.2)
#plt.axvspan(min_dl[9], max_dl[9], facecolor='cyan', alpha=0.2)
plt.fill([min_age[0], min_age[0], max_age[0], max_age[0]], 
         [min_dl[0], max_dl[0], max_dl[0], min_dl[0]], 
         color = 'purple', alpha = 0.2)
plt.fill([min_age[1], min_age[1], max_age[1], max_age[1]], 
         [min_dl[1], max_dl[1], max_dl[1], min_dl[1]], 
         color = 'green', alpha = 0.2)
plt.fill([min_age[2], min_age[2], max_age[2], max_age[2]], 
         [min_dl[2], max_dl[2], max_dl[2], min_dl[2]], 
         color = 'blue', alpha = 0.2)
plt.fill([min_age[3], min_age[3], max_age[3], max_age[3]], 
         [min_dl[3], max_dl[3], max_dl[3], min_dl[3]], 
         color = 'green', alpha = 0.2)
plt.fill([min_age[4], min_age[4], max_age[4], max_age[4]], 
         [min_dl[4], max_dl[4], max_dl[4], min_dl[4]], 
         color = 'orange', alpha = 0.2)
plt.fill([min_age[5], min_age[5], max_age[5], max_age[5]], 
         [min_dl[5], max_dl[5], max_dl[5], min_dl[5]], 
         color = 'red', alpha = 0.2)
plt.fill([min_age[6], min_age[6], max_age[6], max_age[6]], 
         [min_dl[6], max_dl[6], max_dl[6], min_dl[6]], 
         color = 'blue', alpha = 0.2)
plt.fill([min_age[7], min_age[7], max_age[7], max_age[7]], 
         [min_dl[7], max_dl[7], max_dl[7], min_dl[7]], 
         color = 'blue', alpha = 0.2)
plt.fill([min_age[8], min_age[8], max_age[8], max_age[8]], 
         [min_dl[8], max_dl[8], max_dl[8], min_dl[8]], 
         color = 'green', alpha = 0.2)
plt.fill([min_age[9], min_age[9], max_age[9], max_age[9]], 
         [min_dl[9], max_dl[9], max_dl[9], min_dl[9]], 
         color = 'blue', alpha = 0.2)
plt.fill([min_age[10], min_age[10], max_age[10], max_age[10]], 
         [min_dl[10], max_dl[10], max_dl[10], min_dl[10]], 
         color = 'green', alpha = 0.2)
plt.fill([min_age[11], min_age[11], max_age[11], max_age[11]], 
         [min_dl[11], max_dl[11], max_dl[11], min_dl[11]], 
         color = 'red', alpha = 0.2)
plt.fill([min_age[12], min_age[12], max_age[12], max_age[12]], 
         [min_dl[12], max_dl[12], max_dl[12], min_dl[12]], 
         color = 'orange', alpha = 0.2)
plt.fill([min_age[13], min_age[13], max_age[13], max_age[13]], 
         [min_dl[13], max_dl[13], max_dl[13], min_dl[13]], 
         color = 'orange', alpha = 0.2)
plt.fill([min_age[14], min_age[14], max_age[14], max_age[14]], 
         [min_dl[14], max_dl[14], max_dl[14], min_dl[14]], 
         color = 'green', alpha = 0.2)
plt.fill([min_age[15], min_age[15], max_age[15], max_age[15]], 
         [min_dl[15], max_dl[15], max_dl[15], min_dl[15]], 
         color = 'red', alpha = 0.2)
plt.fill([min_age[16], min_age[16], max_age[16], max_age[16]], 
         [min_dl[16], max_dl[16], max_dl[16], min_dl[16]], 
         color = 'blue', alpha = 0.2)
plt.fill([min_age[17], min_age[17], max_age[17], max_age[17]], 
         [min_dl[17], max_dl[17], max_dl[17], min_dl[17]], 
         color = 'orange', alpha = 0.2)
plt.fill([min_age[18], min_age[18], max_age[18], max_age[18]], 
         [min_dl[18], max_dl[18], max_dl[18], min_dl[18]], 
         color = 'green', alpha = 0.2)
plt.fill([min_age[19], min_age[19], max_age[19], max_age[19]], 
         [min_dl[19], max_dl[19], max_dl[19], min_dl[19]], 
         color = 'green', alpha = 0.2)
plt.fill([min_age[20], min_age[20], max_age[20], max_age[20]], 
         [min_dl[20], max_dl[20], max_dl[20], min_dl[20]], 
         color = 'red', alpha = 0.2)
plt.fill([min_age[21], min_age[21], max_age[21], max_age[21]], 
         [min_dl[21], max_dl[21], max_dl[21], min_dl[21]], 
         color = 'blue', alpha = 0.2)
plt.fill([min_age[22], min_age[22], max_age[22], max_age[22]], 
         [min_dl[22], max_dl[22], max_dl[22], min_dl[22]], 
         color = 'red', alpha = 0.2)
plt.fill([min_age[23], min_age[23], max_age[23], max_age[23]], 
         [min_dl[23], max_dl[23], max_dl[23], min_dl[23]], 
         color = 'orange', alpha = 0.2)
plt.fill([min_age[24], min_age[24], max_age[24], max_age[24]], 
         [min_dl[24], max_dl[24], max_dl[24], min_dl[24]], 
         color = 'red', alpha = 0.2)
plt.fill([min_age[25], min_age[25], max_age[25], max_age[25]], 
         [min_dl[25], max_dl[25], max_dl[25], min_dl[25]], 
         color = 'green', alpha = 0.2)
plt.fill([min_age[26], min_age[26], max_age[26], max_age[26]], 
         [min_dl[26], max_dl[26], max_dl[26], min_dl[26]], 
         color = 'green', alpha = 0.2)
plt.fill([min_age[27], min_age[27], max_age[27], max_age[27]], 
         [min_dl[27], max_dl[27], max_dl[27], min_dl[27]], 
         color = 'red', alpha = 0.2)
plt.fill([min_age[28], min_age[28], max_age[28], max_age[28]], 
         [min_dl[28], max_dl[28], max_dl[28], min_dl[28]], 
         color = 'green', alpha = 0.2)
plt.fill([min_age[29], min_age[29], max_age[29], max_age[29]], 
         [min_dl[29], max_dl[29], max_dl[29], min_dl[29]], 
         color = 'orange', alpha = 0.2)
plt.fill([min_age[30], min_age[30], max_age[30], max_age[30]], 
         [min_dl[30], max_dl[30], max_dl[30], min_dl[30]], 
         color = 'green', alpha = 0.2)
plt.fill([min_age[31], min_age[31], max_age[31], max_age[31]], 
         [min_dl[31], max_dl[31], max_dl[31], min_dl[31]], 
         color = 'green', alpha = 0.2)
sns.scatterplot(x=df_THAA["Age Mid Point"],
                     y=df_THAA["Val D/L"], 
                     data=df_THAA, hue=df_THAA["Quaternary sites"], 
                     palette="dark", markers=True, s=60)
plt.xlabel("Age/ ka")
plt.ylabel("Total Valine D/L")



plt.legend(loc="lower right")
plt.show
plt.savefig("Val vs. age.png")