# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 16:35:42 2022

@author: efn509
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



#This is the script for the geochronology of Poland and Belarus 
#To use this script data from FAA and THAA data need to be saved as separate csv files

#import csv
FAA_AA = pd.read_csv('R:/NEaar/People/Ellie Nelson/EQuate frameworks/Hungary/Hungary_FAA.csv')
THAA_AA = pd.read_csv('R:/NEaar/People/Ellie Nelson/EQuate frameworks/Hungary/Hungary_THAA.csv')

#extracting data from FAA csv and placing in dataframe
df_FAA = pd.DataFrame(FAA_AA)
df_FAA = df_FAA.add_suffix("_FAA") #suffix data remains allocated to correct fraction

#to prvent error in code all division errors are replaced with zeros

for col in df_FAA.columns[13:24]:
    df_FAA[col] = pd.to_numeric(df_FAA[col], errors="coerce")

df_FAA = df_FAA.replace(np.nan, 0.0, regex=True) #all nan values removed and replace with 0s

# code if want to look at averages between horizons instead of replicates

#pulling THAA into dataframe
df_THAA = pd.DataFrame(THAA_AA)
df_THAA = df_THAA.add_suffix("_THAA")

for col in df_THAA.columns[13:24]:
    df_THAA[col] = pd.to_numeric(df_THAA[col], errors="coerce")

df_THAA = df_THAA.replace(np.nan, 0.0, regex=True) #all nan values removed and replace with 0s



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

df_mean_all = df_mean_all.sort_values("Age Mid Point_FAA", inplace=False, ascending=True)
df_mean_all["Sites_Depth"] = df_mean_all["Quaternary sites_FAA"] + " " + df_mean_all["Level/ Sample_FAA"].astype("str")
df_mean_all["Sites_Depth"] = df_mean_all["Sites_Depth"] + ", " + df_mean_all["Age if known_FAA"]

#df_mean_all.to_csv("R:/NEaar/People/Ellie Nelson/EQuate frameworks/Germany/df_check.csv")

#UK DATA import to put behind Hungarian data

#all colours at https://xkcd.com/color/rgb/
colours = ["purple", "green", "blue", "pink",
           "brown", "red", "light blue", "teal",
           "orange", "light green", "magenta",
           "yellow", "grey", "lime green", "light purple",
           "dark green", "turquoise", "dark blue", "mauve",
           "seafoam", "maroon", "olive", "salmon",
           "periwinkle", "dark pink", "indigo", "mustard",
           "royal purple", "dark orange", "bright pink", "plum",
           "khaki", "sea blue", "leaf green", "eggplant",
           "greyish blue"]

markers = ['o', 'p', 'v', '*', '^', 'h', '<', '>', 'd', '8', 'P', 's', 'X',
           'o', 'p', 'v', '*', 'P', 'h', '<', '>', 'd', '8', 'P', 's', 'X',
           'o', 'p', 'v', '*', '^', 'h', '<', '>', 'd', '8', 'P']


#The following function creates scatter plots of FAA vs. THAA for all AAs
#If errors are signficant then axis will be thrown off
#This will require data to be reviewed before finalising.
#Plot will expand axis for any AA with D/L values over 1
def site_scatter(df1, AA, fig, country_ls, m, c):
    #creating lists of column containing the required AA
    FAA_colnames = [col for col in df1.columns if str(AA) + " D/L_FAA" in col]
    FAA_mean = FAA_colnames[0]
    THAA_colnames = [col for col in df1.columns if str(AA) + " D/L_THAA" in col]
    THAA_mean = THAA_colnames[0]
    #creating lists of column containing the required AA from UK]
    #maximum values of x and y will dictate size of axis
    x_max = max(list(df1[FAA_mean]))
    y_max = max(list(df1[THAA_mean]))
    #creating dictionary
    depth_to_site_dict = df1.set_index("Sites_Depth")["Age if known_FAA"].to_dict()
    df1['Subscale'] = df1['Sites_Depth'].map(depth_to_site_dict)
    df1['Subscale'] = pd.Categorical(df1['Subscale'])  # creates a fixed order
    print(df1['Subscale'])
    sns.set(style="ticks") 
    fig, ax = fig
    c_p = sns.xkcd_palette(colours)
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
              loc="center left", bbox_to_anchor=(1, 0.5), fontsize=9, ncol=2)
    plt.xlabel("FAA D/L")
    plt.ylabel("THAA D/L")
    Name = str(', '.join(country_ls))
    plt.title(str(Name) + " " + str(AA))
    ax.set_xlim(0, x_max + 0.1)
    ax.set_ylim(0, y_max + 0.1)
    plt.tight_layout()
    plt.show()
    
#Define which country you wish to plot from data by amending the selection in the list
#If only the one country keep this formatted as a list, so do not remove [] around the country selected

asx = plt.subplots(figsize=(14, 8))
Asx_plt = site_scatter(df_mean_all, "Asx", asx, ["Hungary"], 0.83649191, 0.007093790583386883)
glx = plt.subplots(figsize=(14, 8))
Glx_plt = site_scatter(df_mean_all, "Glx", glx, ["Hungary"], 0.8604198, -0.032206550310452)
#ser = plt.figure(figsize=(8, 6))
#Ser_plt = site_scatter(df_mean_all, "Ser", ser, ["Hungary"])
#arg = plt.figure(figsize=(8, 6))
#Arg_plt = site_scatter(df_mean_all, "Arg", arg, ["Hungary"])
ala = plt.subplots(figsize=(14, 8))
Ala_plt = site_scatter(df_mean_all, "Ala", ala, ["Hungary"], 0.94242474, -0.0562324275651056)
#tyr = plt.figure(figsize=(8, 6))
#Tyr_plt = site_scatter(df_mean_all, "Tyr", tyr, ["Hungary"])
val = plt.subplots(figsize=(14, 8))
Val_plt = site_scatter(df_mean_all, "Val", val, ["Hungary"], 0.92705853, -0.04813215476130053)
#phe = plt.figure(figsize=(8, 6))
#Phe_plt = site_scatter(df_mean_all, "Phe", phe, ["Hungary"])
#leu = plt.figure(figsize=(8, 6))
#Leu_plt = site_scatter(df_mean_all, "Leu", leu, ["Hungary"])
#ile = plt.figure(figsize=(8, 6))
#Ile_plt = site_scatter(df_mean_all, "Ile", ile, ["Hungary"])