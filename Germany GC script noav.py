# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 10:18:10 2022

@author: efn509
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 09:37:15 2022

@author: efn509
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



#This is the script for the geochronology of Poland and Belarus 
#To use this script data from FAA and THAA data need to be saved as separate csv files

#import csv
FAA_AA = pd.read_csv('R:/NEaar/People/Ellie Nelson/EQuate frameworks/Germany/Germany_FAA_withCR.csv')
THAA_AA = pd.read_csv('R:/NEaar/People/Ellie Nelson/EQuate frameworks/Germany/Germany_THAA_withCR.csv')

#extracting data from FAA csv and placing in dataframe
df_FAA = pd.DataFrame(FAA_AA)
df_FAA = df_FAA.add_suffix("_FAA") #suffix data remains allocated to correct fraction

for col in df_FAA.columns[12:23]:
    df_FAA[col] = pd.to_numeric(df_FAA[col], errors="coerce")

df_FAA = df_FAA.replace(np.nan, 0.0, regex=True) #all nan values removed and replace with 0s
# code if want to look at averages between horizons instead of replicates

#pulling THAA into dataframe
df_THAA = pd.DataFrame(THAA_AA)
df_THAA = df_THAA.add_suffix("_THAA")

for col in df_THAA.columns[12:23]:
    df_THAA[col] = pd.to_numeric(df_THAA[col], errors="coerce")

df_THAA = df_THAA.replace(np.nan, 0.0, regex=True)

#adding THAA D/L values to FAA dataframe
df_mean_all =  pd.concat([df_FAA, df_THAA[[('Asx D/L_THAA'),
                                           ('Glx D/L_THAA'),
                                           ('Ser D/L_THAA'),
                                           ('Arg D/L_THAA'),
                                           ('Ala D/L_THAA'),
                                           ('Tyr D/L_THAA'),
                                           ('Val D/L_THAA'),
                                           ('Phe D/L_THAA'),
                                           ('Leu D/L_THAA'),
                                           ('Ile D/L_THAA'),
                                           ('[Ser]/[Ala]_THAA')]]], axis=1)

#df_mean_all = df_mean_all.sort_values(by=["Quaternary sites_FAA"], axis=0)

df_mean_all["Sites_Depth"] = df_mean_all["Quaternary sites_FAA"] + " " + df_mean_all["Level/ Sample_FAA"].astype("str")
df_mean_all = df_mean_all.sort_values("Age rank_FAA", inplace=False, ascending=True)
#df_mean_all.to_csv("R:/NEaar/People/Ellie Nelson/EQuate frameworks/Germany/df_check.csv")



#import csv
FAA_UK = pd.read_csv('R:/NEaar/People/Ellie Nelson/EQuate frameworks/United Kingdom/UK FAA.csv')
THAA_UK = pd.read_csv('R:/NEaar/People/Ellie Nelson/EQuate frameworks/United Kingdom/UK THAA.csv')

#extracting data from FAA csv and placing in dataframe
df_FAA_UK = pd.DataFrame(FAA_UK)
df_FAA_UK = df_FAA_UK.add_suffix("_FAA") #suffix data remains allocated to correct fraction

for col in df_FAA_UK.columns[12:23]:
    df_FAA_UK[col] = pd.to_numeric(df_FAA_UK[col], errors="coerce")


df_FAA_UK = df_FAA_UK.replace(np.nan, 0.0, regex=True)


# print(df_FAA.head(5))

#pulling THAA into dataframe
df_THAA_UK = pd.DataFrame(THAA_UK)
df_THAA_UK = df_THAA_UK.add_suffix("_THAA")

for col in df_THAA_UK.columns[12:23]:
    df_THAA_UK[col] = pd.to_numeric(df_THAA_UK[col], errors="coerce")


df_THAA_UK = df_THAA_UK.replace(np.nan, 0.0, regex=True)


#adding THAA D/L values to FAA dataframe
df_mean_UK =  pd.concat([df_FAA_UK, df_THAA_UK[[('Asx D/L mean_THAA'), ('Asx D/L sd_THAA'),
                                                ('Glx D/L mean_THAA'), ('Glx D/L sd_THAA'),
                                                ('Ser D/L mean_THAA'), ('Ser D/L sd_THAA'),
                                                ('Ala D/L mean_THAA'), ('Ala D/L sd_THAA'),
                                                ('Val D/L mean_THAA'), ('Val D/L sd_THAA'),
                                                ('[S]/[A] mean_THAA'), ('[S]/[A] sd_THAA')]]], axis=1)

#number of markers needs to match the number produced with the following code:
print(len(df_mean_all["Sites_Depth"].unique()))
markers = ['o', 'p', 'o', 'p', 'v', '*', '^', 'h', '<', '>', 'd', '8', 
           'P', 's', 'X', 'o', 'p', 'v', '*', 'P', 'h', '<', '>', 'd', 
           '8', 'P', 'o', 'p', 'v', '*', '^', 'h', '<', '>', 'd', '8', 
           'P', 's', 'X', 'o', 'p', 'v', '*', 'P', 'h', '<', '>', 'd', 
           '8', 'P', 'o', 'p', 'v', '*', '^', 'h', '<', '>', 'd', 'X', 
           'P', 's', 'X', 'o', 'p', 'v', '*', 'P', 'h', '<', '>', 'd',
           '8', 'P', 'o', 'p', 'v', '*', '^', 'h', '<', '>', 'd', '8',
           'P', 'o', 'p', 'v', '*', '^', 'h', '<', '>']



df_mean_all["Sites_Depth"] = df_mean_all["Quaternary sites_FAA"] + " " + df_mean_all["Level/ Sample_FAA"].astype("str")
df_mean_all = df_mean_all.sort_values(["Age rank_FAA", "Sites_Depth"], inplace=False, ascending=True)


#The following function creates scatter plots of FAA vs. THAA for all AAs
#If errors are signficant then axis will be thrown off
#This will require data to be reviewed before finalising.
#Plot will expand axis for any AA with D/L values over 1
def site_scatter(df1, df2, AA, fig, country_ls):
    #creating lists of column containing the required AA
    FAA_colnames = [col for col in df1.columns if str(AA) + " D/L_FAA" in col]
    FAA_mean = FAA_colnames[0]
    THAA_colnames = [col for col in df1.columns if str(AA) + " D/L_THAA" in col]
    THAA_mean = THAA_colnames[0]
    #creating lists of column containing the required AA from UK
    FAA_col_UK = [col for col in df2.columns if str(AA) + " D/L mean_FAA" in col]
    FAA_UK = FAA_col_UK[0]
    THAA_col_UK = [col for col in df2.columns if str(AA) + " D/L mean_THAA" in col]
    THAA_UK = THAA_col_UK[0]
    #maximum values of x and y will dictate size of axis
    x_max = max(list(df1[FAA_mean]))
    y_max = max(list(df1[THAA_mean]))
    #creating dictionary
    depth_to_site_dict = df1.set_index("Sites_Depth")["Age if known_FAA"].to_dict()
    df1['Subscale'] = df1['Sites_Depth'].map(depth_to_site_dict)
    df1['Subscale'] = pd.Categorical(df1['Subscale'])  # creates a fixed order
    sns.set(style="ticks") 
    fig, ax = fig
    #sns.scatterplot(ax=ax, x=df2[FAA_UK], y=df2[THAA_UK], 
     #           data=df2, alpha=0.25,
      #          palette="Greys", s=80,
       #         style=df2["Suspected age_FAA"])
    c_p = sns.crayon_palette(["Red", "Tumbleweed", "Granny Smith Apple",
                               "Pacific Blue", 
                              "Midnight Blue", "Chestnut", "Inchworm",
                              "Vivid Violet", "Orange", "Gray",
                               "Brown", 
                              "Olive Green", "Wisteria", "Pine Green",
                              "Gold", "Blue", "Brick Red",
                              "Jungle Green", "Peach", "Eggplant",
                              "Shadow", "Mango Tango", "Timberwolf", 
                              "Yellow", "Mahogany"])
    sns.set_palette(sns.color_palette(c_p))
    sns.scatterplot(ax=ax, x=df1[FAA_mean],
                         y=df1[THAA_mean], 
                         data=df1, hue=df1["Subscale"], 
                         style=df1["Sites_Depth"], 
                         markers=markers, s=80)
    # create a dictionary mapping the subscales to their color
    handles, labels = ax.get_legend_handles_labels()
    index_depth_title = labels.index('Sites_Depth')
    color_dict = {label: handle.get_facecolor()
                  for handle, label in zip(handles[1:index_depth_title], labels[1:index_depth_title])}
    # loop through the items, assign color via the subscale of the item idem
    for handle, label in zip(handles[index_depth_title + 1:], labels[index_depth_title + 1:]):
        handle.set_color(color_dict[depth_to_site_dict[label]])
    # create a legend only using the items
    ax.legend(handles[index_depth_title + 1:], labels[index_depth_title + 1:], title='Site & Horizon', 
              loc="center left", bbox_to_anchor=(1, 0.5), fontsize=7, ncol=2)
    plt.xlabel("FAA D/L")
    plt.ylabel("THAA D/L")
    Name = str(', '.join(country_ls))
    plt.title(str(Name) + " " + str(AA))
    plt.tight_layout()
    ax.set_xlim(0, x_max + 0.1)
    ax.set_ylim(0, y_max + 0.1)
    plt.show()
#Define which country you wish to plot from data by amending the selection in the list
#If only the one country keep this formatted as a list, so do not remove [] around the country selected

asx = plt.subplots(figsize=(14, 8))
Asx_plt = site_scatter(df_mean_all, df_mean_UK, "Asx", asx, ["Germany"])
glx = plt.subplots(figsize=(14, 8))
Glx_plt = site_scatter(df_mean_all, df_mean_UK,  "Glx", glx, ["Germany"])
#ser = plt.figure(figsize=(8, 6))
#Ser_plt = site_scatter(df_mean_all, df_mean_UK,  "Ser", ser, ["Germany"])
#arg = plt.figure(figsize=(8, 6))
#Arg_plt = site_scatter(df_mean_all, "Arg", arg, ["Germany"])
ala = plt.subplots(figsize=(14, 8))
Ala_plt = site_scatter(df_mean_all, df_mean_UK,  "Ala", ala, ["Germany"])
#tyr = plt.figure(figsize=(8, 6))
#Tyr_plt = site_scatter(df_mean_all, "Tyr", tyr, ["Germany"])
val = plt.subplots(figsize=(14, 8))
Val_plt = site_scatter(df_mean_all, df_mean_UK, "Val", val, ["Germany"])
#phe = plt.figure(figsize=(8, 6))
#Phe_plt = site_scatter(df_mean_all, "Phe", phe, ["Germany"])
#leu = plt.figure(figsize=(8, 6))
#Leu_plt = site_scatter(df_mean_all, "Leu", leu, ["Germany"])
#ile = plt.figure(figsize=(8, 6))
#Ile_plt = site_scatter(df_mean_all, "Ile", ile, ["Germany"])