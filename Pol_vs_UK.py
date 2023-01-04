# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 15:58:53 2022

@author: efn509
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#import csv
MIS_5e = pd.read_csv('R:/NEaar/People/Ellie Nelson/EQuate frameworks/Poland_Belarus/Poland MIS 5e vs. UK.csv')

#extracting data from FAA csv and placing in dataframe
MIS_5e_df = pd.DataFrame(MIS_5e)

def sel_xy(df, site):
    df_site = df.loc[df['Country'].isin(site)]
    return df_site

no_poland = sel_xy(MIS_5e_df, ["MIS 5e"])
#MIS5e_min = min(no_poland["Hyd Ala D/L"])
#MIS5e_max = max(no_poland["Hyd Ala D/L"])

#plotting box plot

f = plt.Figure(figsize=(14, 10))
#f.add_axes([0.5, 0.5, 1, 1])
sns.set_palette(sns.color_palette("colorblind"))
ax = sns.boxplot(x="Country", y="Hyd Ala D/L", data=MIS_5e_df)
#ax.set_xlabel("Depth/ cm")
ax.set_ylabel("Total alanine D/L")
ax.tick_params(axis='x', rotation=20)
#ax.set_ylim(y_min,y_max)
#f.suptitle(site + " " + aa, fontsize=12)
#plt.title("Comparison of Polish Holsteinian with UK MIS 9 and MIS 11")
plt.gcf().subplots_adjust(bottom=0.20)


#f.tight_layout()
plt.rcParams['figure.dpi'] = 500
plt.rcParams['savefig.dpi'] = 500
plt.show()
plt.close(f)