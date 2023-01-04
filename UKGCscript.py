# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 13:14:17 2021

@author: efn509
"""

#United Kingdom framework in order to compare the others
#Netherlands geochronological framework
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

#This is the script for the geochronology of Poland and Belarus 
#To use this script data from FAA and THAA data need to be saved as separate csv files

#import csv
FAA_AA = pd.read_csv('R:/NEaar/People/Ellie Nelson/EQuate frameworks/United Kingdom/UK FAA.csv')
THAA_AA = pd.read_csv('R:/NEaar/People/Ellie Nelson/EQuate frameworks/United Kingdom/UK THAA.csv')

#extracting data from FAA csv and placing in dataframe
df_FAA = pd.DataFrame(FAA_AA)
df_FAA = df_FAA.add_suffix("_FAA") #suffix data remains allocated to correct fraction

for col in df_FAA.columns[7:18]:
    df_FAA[col] = pd.to_numeric(df_FAA[col], errors="coerce")


df_FAA = df_FAA.replace(np.nan, 0.0, regex=True)


# print(df_FAA.head(5))

#pulling THAA into dataframe
df_THAA = pd.DataFrame(THAA_AA)
df_THAA = df_THAA.add_suffix("_THAA")

for col in df_THAA.columns[7:18]:
    df_THAA[col] = pd.to_numeric(df_THAA[col], errors="coerce")


df_THAA = df_THAA.replace(np.nan, 0.0, regex=True)


#adding THAA D/L values to FAA dataframe
df_mean_all =  pd.concat([df_FAA, df_THAA[[('Asx D/L mean_THAA'), ('Asx D/L sd_THAA'),
                                           ('Glx D/L mean_THAA'), ('Glx D/L sd_THAA'),
                                           ('Ser D/L mean_THAA'), ('Ser D/L sd_THAA'),
                                           ('Ala D/L mean_THAA'), ('Ala D/L sd_THAA'),
                                           ('Val D/L mean_THAA'), ('Val D/L sd_THAA'),
                                           ('[S]/[A] mean_THAA'), ('[S]/[A] sd_THAA')]]], axis=1)

#FAA_colnames = [col for col in df_mean_all.columns if "Asx" + " D/L mean_FAA" in col]
#FAA_mean = FAA_colnames[0]

#The following function creates scatter plots of FAA vs. THAA for all AAs
#If errors are signficant then axis will be thrown off
#This will require data to be reviewed before finalising.
#Plot will expand axis for any AA with D/L values over 1
def site_scatter(df, AA, fig, country_ls):
    #creating lists of column containing the required AA
    FAA_colnames = [col for col in df.columns if str(AA) + " D/L mean_FAA" in col]
    FAA_mean = FAA_colnames[0]
    #FAA_std = FAA_colnames[1]
    THAA_colnames = [col for col in df.columns if str(AA) + " D/L mean_THAA" in col]
    THAA_mean = THAA_colnames[0]
    #THAA_std = THAA_colnames[1]
    #maximum values of x and y will dictate size of axis
    x_max = max(list(df[FAA_mean]))
    y_max = max(list(df[THAA_mean]))
    #creating dictionary
    depth_to_site_dict = df.set_index("Name_FAA")["Suspected age_FAA"].to_dict()
    df['Subscale'] = df['Name_FAA'].map(depth_to_site_dict)
    df['Subscale'] = pd.Categorical(df['Subscale'])  # creates a fixed order
    sns.set(style="ticks")  
    ax = sns.scatterplot(x=df[FAA_mean],
                         y=df[THAA_mean], 
                         data=df, hue=df["Subscale"], 
                         style=df["Name_FAA"], 
                         palette="colorblind", markers=True, s=60
                         )
    # create a dictionary mapping the subscales to their color
    handles, labels = ax.get_legend_handles_labels()
    index_depth_title = labels.index('Name_FAA')
    color_dict = {label: handle.get_facecolor()
                  for handle, label in zip(handles[1:index_depth_title], labels[1:index_depth_title])}
    # loop through the items, assign color via the subscale of the item idem
    for handle, label in zip(handles[index_depth_title + 1:], labels[index_depth_title + 1:]):
        handle.set_color(color_dict[depth_to_site_dict[label]])
    # create a legend only using the items
    ax.legend(handles[index_depth_title + 1:], labels[index_depth_title + 1:], title='Site', 
              loc="center left", bbox_to_anchor=(1, 0.5), fontsize=7, ncol=3)
    x = np.array(list(df[FAA_mean])).reshape((-1,1))
    y = np.array(list(df[THAA_mean]))
    model = LinearRegression().fit(x, y)
    r_sq = model.score(x, y)
    #plt.errorbar(df[FAA_mean], df[THAA_mean], 
     #            df[FAA_std], 
      #           df[THAA_std], ls="none", fmt='',
       #          ecolor='black', elinewidth=0.3)
    plt.xlabel("FAA")
    plt.ylabel("THAA")
    Name = str(', '.join(country_ls))
    plt.title(str(Name) + " " + str(AA) + " THAA vs. FAA plot")
    ax.set_xlim(0, x_max + 0.1)
    ax.set_ylim(0, y_max + 0.1)
    plt.tight_layout()
    plt.show()
    print('coefficient of determination:', r_sq)
    print('intercept:', model.intercept_)
    print('slope:', model.coef_)


#Define which country you wish to plot from data by amending the selection in the list
#If only the one country keep this formatted as a list, so do not remove [] around the country selected

asx = plt.figure(figsize=(16, 8))
Asx_plt = site_scatter(df_mean_all, "Asx", asx, ["United Kingdom"])
glx = plt.figure(figsize=(16, 8))
Glx_plt = site_scatter(df_mean_all, "Glx", glx, ["United Kingdom"])
ala = plt.figure(figsize=(16, 8))
Ala_plt = site_scatter(df_mean_all, "Ala", ala, ["United Kingdom"])
val = plt.figure(figsize=(16, 8))
Val_plt = site_scatter(df_mean_all, "Val", val, ["United Kingdom"])

