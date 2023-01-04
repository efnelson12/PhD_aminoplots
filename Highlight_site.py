# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 13:29:30 2022

@author: efn509
"""

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
FAA_AA = pd.read_csv('R:/NEaar/People/Ellie Nelson/EQuate frameworks/Germany/FAA_secure.csv')
THAA_AA = pd.read_csv('R:/NEaar/People/Ellie Nelson/EQuate frameworks/Germany/THAA_secure.csv')

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
df_base =  pd.concat([df_FAA, df_THAA[[('Asx D/L_THAA'),
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

#import csv
FAA_UK = pd.read_csv('R:/NEaar/People/Ellie Nelson/EQuate frameworks/Germany/Germany_FAA_withViernheim.csv')
THAA_UK = pd.read_csv('R:/NEaar/People/Ellie Nelson/EQuate frameworks/Germany/Germany_THAA_withViernheim.csv')

#extracting data from FAA csv and placing in dataframe
df_FAA_UK = pd.DataFrame(FAA_UK)
df_FAA_UK = df_FAA_UK.add_suffix("_FAA") #suffix data remains allocated to correct fraction

for col in df_FAA_UK.columns[10:22]:
    df_FAA_UK[col] = pd.to_numeric(df_FAA_UK[col], errors="coerce")


df_FAA_UK = df_FAA_UK.replace(np.nan, 0.0, regex=True)


# print(df_FAA.head(5))

#pulling THAA into dataframe
df_THAA_UK = pd.DataFrame(THAA_UK)
df_THAA_UK = df_THAA_UK.add_suffix("_THAA")

for col in df_THAA_UK.columns[11:22]:
    df_THAA_UK[col] = pd.to_numeric(df_THAA_UK[col], errors="coerce")


df_THAA_UK = df_THAA_UK.replace(np.nan, 0.0, regex=True)


#adding THAA D/L values to FAA dataframe
df_mean_UK =  pd.concat([df_FAA_UK, df_THAA_UK[[('Asx D/L_THAA'),
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


def sel_xy(df, site):
    df_site = df.loc[df['Quaternary sites_FAA'].isin(site)]
    return df_site

df_base = df_base.sort_values(["Age rank_FAA"], inplace=False, ascending=True)

#select the site you want to plot with your data
site_df = sel_xy(df_mean_UK, ['Bilzingsleben'])

site_df["Sites_Depth"] = site_df['Quaternary sites_FAA'] + " " + site_df["Level/ Sample_FAA"]
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
    #maximum values of x and y will dictate size of axis
    x_max = max(list(df1[FAA_mean]))
    y_max = max(list(df1[THAA_mean]))
    # specifying columns for site plot
    x= FAA_colnames[0]
    x_name = df2[x]
    y= THAA_colnames[0]
    y_name = df2[y]
    df_eem = df2.loc[df2['Age if known_FAA'] == "Eemian"]
    #creating dictionary to make individual markers for each horizon
    markers=['P', 'X', 's', '8', 'h']
    M_plt = []
    M_plt.append(markers[0:len(df2["Level/ Sample_FAA"].unique())])
    #plotting background age areas
    sns.set(style="ticks") 
    fig, ax = fig
    #Number of colours should much number of securely dated age definitions
    c_p = sns.crayon_palette(["Red", "Tumbleweed",
                              #Colours for Schoningen in next line
                              #"Granny Smith Apple", "Fern", "Asparagus", 
                              "Midnight Blue", "Orange", "Magenta",
                              "Green"])
    sns.scatterplot(ax=ax, x=df1[FAA_mean],
                         y=df1[THAA_mean], 
                         data=df1, hue=df1["Age if known_FAA"], 
                         style=df1["Age if known_FAA"], 
                         s=80, palette=c_p)
    df_eem = df2.loc[df2['Age if known_FAA'] == "Eemian"]
    #Add more colours to match number of sites you have included to highlight
    black = ["black"]
    # create a dictionary mapping the subscales to their color
    depth_to_site_dict = df2.set_index("Sites_Depth")['Quaternary sites_FAA'].to_dict()
    df2['Subscale'] = df2['Sites_Depth'].map(depth_to_site_dict)
    df2['Subscale'] = pd.Categorical(df2['Subscale'])  # creates a fixed order
    c_p = sns.xkcd_palette(black)
    sns.set_palette(sns.color_palette(c_p))
    sns.scatterplot(ax=ax, x=x_name, y=y_name, data=df2,
                    hue='Quaternary sites_FAA', style='Sites_Depth',
                    palette=c_p, s=80)
    #handles, labels = ax.get_legend_handles_labels()
    #index_depth_title = labels.index('Sites_Depth')
    #color_dict = {label: handle.get_facecolor()
     #             for handle, label in zip(handles[1:index_depth_title], labels[1:index_depth_title])}
    # loop through the items, assign color via the subscale of the item idem
    #for handle, label in zip(handles[index_depth_title + 1:], labels[index_depth_title + 1:]):
     #   handle.set_color(color_dict[depth_to_site_dict[label]])
    # create a legend only using the items
    #ax.legend(handles[index_depth_title + 1:], labels[index_depth_title + 1:], title='Site & Horizon')
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
Asx_plt = site_scatter(df_base, site_df, "Asx", asx, ["Germany"])
#glx = plt.subplots(figsize=(14, 8))
#Glx_plt = site_scatter(df_base, site_df,  "Glx", glx, ["Germany"])
ala = plt.subplots(figsize=(14, 8))
Ala_plt = site_scatter(df_base, site_df,  "Ala", ala, ["Germany"])
val = plt.subplots(figsize=(14, 8))
Val_plt = site_scatter(df_base, site_df, "Val", val, ["Germany"])

Ala = site_df.loc[site_df['Quaternary sites_FAA'] == ("Karsdorf")]
Ala["Ala D/L_THAA"]