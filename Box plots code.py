# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#import csv
FAA_AA = pd.read_csv('R:/NEaar/People/Ellie Nelson/EQuate frameworks/Poland_Belarus/Poland_Belarus_FAA.csv')
THAA_AA = pd.read_csv('R:/NEaar/People/Ellie Nelson/EQuate frameworks/Poland_Belarus/Poland_Belarus_THAA.csv')

#extracting data from FAA csv and placing in dataframe
df_FAA = pd.DataFrame(FAA_AA)
df_FAA = df_FAA.rename(columns={col: col+'_FAA' 
                        for col in df_FAA.columns if col not in ['Replicate', 'Sample name',
                                                             'Genus', 'Species', 'materials',
                                                             'location', 'Quaternary sites',
                                                             'Level/ Sample', 'relative',
                                                             'Age if known', 'Age rank']})

for col in df_FAA.columns[11:22]:
    df_FAA[col] = pd.to_numeric(df_FAA[col], errors="coerce")

df_FAA = df_FAA.replace(np.nan, 0.0, regex=True) #all nan values removed and replace with 0s

# code if want to look at averages between horizons instead of replicates

#pulling THAA into dataframe
df_THAA = pd.DataFrame(THAA_AA)
df_THAA = df_THAA.rename(columns={col: col+'_THAA' 
                        for col in df_THAA.columns if col not in ['Replicate', 'Sample name',
                                                             'Genus', 'Species', 'materials',
                                                             'location', 'Quaternary sites',
                                                             'Level/ Sample', 'relative',
                                                             'Age if known', 'Age rank']})

for col in df_THAA.columns[11:22]:
    df_THAA[col] = pd.to_numeric(df_THAA[col], errors="coerce")

df_THAA = df_THAA.replace(np.nan, 0.0, regex=True) #all nan values removed and replace with 0s


def box_plot(site, aa, df_FAA, df_THAA, order):
    df_FAA = df_FAA.sort_values(["Level/ Sample"], ascending=True)
    df_THAA = df_THAA.sort_values(["Level/ Sample"], ascending=True)
    aa_FAA_col = aa + " D/L_FAA"
    aa_THAA_col = aa + " D/L_THAA"
    FAA = df_FAA.loc[df_FAA['Quaternary sites'] == site]
    aa_FAA = FAA[["Level/ Sample", aa_FAA_col]]
    THAA = df_THAA.loc[df_THAA['Quaternary sites'] == site]
    aa_THAA = THAA[["Level/ Sample", aa_THAA_col]]
    y_min = min(aa_THAA[aa_THAA_col] - 0.01)
    y_max = max(aa_FAA[aa_FAA_col] + 0.01)
    f = plt.Figure(figsize=(20,10))
    f, axes = plt.subplots(1, 2)
    sns.boxplot(x="Level/ Sample", y=aa_FAA_col, data=aa_FAA, ax=axes[0])
    sns.boxplot(x="Level/ Sample", y=aa_THAA_col, data=aa_THAA, ax=axes[1])
    axes[0].set_xlabel("Depth/ cm")
    axes[0].set_ylabel(aa_FAA_col)
    axes[0].set_ylim(y_min,y_max)
    axes[1].set_xlabel("Depth/ cm")
    axes[1].set_ylabel(aa_THAA_col)
    axes[1].set_ylim(y_min,y_max)
    
    f.suptitle(site + " " + aa, fontsize=12)
    f.tight_layout()
    plt.show()
    plt.close(f)

#Ortel Krowleski II box plots
ortel_asx = box_plot('Ortel Krolewski II', "Asx", df_FAA, df_THAA, [330.0, 210.0, 60.0])
ortel_ala = box_plot('Ortel Krolewski II', "Ala", df_FAA, df_THAA, [330.0, 210.0, 60.0])
ortel_glx = box_plot('Ortel Krolewski II', "Glx", df_FAA, df_THAA, [330.0, 210.0, 60.0])
ortel_val = box_plot('Ortel Krolewski II', "Val", df_FAA, df_THAA, [330.0, 210.0, 60.0])

#Ossowka box plots
ossowka_asx = box_plot('Ossowka', "Asx", df_FAA, df_THAA, [140.0, 110.0])
ossowka_ala = box_plot('Ossowka', "Ala", df_FAA, df_THAA, [140.0, 110.0])
ossowka_glx = box_plot('Ossowka', "Glx", df_FAA, df_THAA, [140.0, 110.0])
ossowka_val = box_plot('Ossowka', "Val", df_FAA, df_THAA, [140.0, 110.0])

#Hrud II box plots
Hrud_asx = box_plot('Hrud II', "Asx", df_FAA, df_THAA, [130.0, 80.0])
Hrud_ala = box_plot('Hrud II', "Ala", df_FAA, df_THAA, [130.0, 80.0])
Hrud_glx = box_plot('Hrud II', "Glx", df_FAA, df_THAA, [130.0, 80.0])
Hrud_val = box_plot('Hrud II', "Val", df_FAA, df_THAA, [130.0, 80.0])

def box_plot_FAA(aa, df_FAA):
    df_FAA = df_FAA.sort_values(["Age rank"], ascending=True)
    df_FAA["Level str"] = df_FAA['Level/ Sample'].astype(str)
    df_FAA["Level name"] = df_FAA["Quaternary sites"] + " " + df_FAA["Level str"]
    aa_FAA_col = aa + " D/L_FAA"
    FAA = df_FAA.loc[df_FAA['Age if known'] == "MIS 11"]
    aa_FAA = FAA[["Level name", aa_FAA_col]]
    f, ax = plt.subplots(figsize=(12, 8))
    sns.boxplot(x="Level name", y=aa_FAA_col, data=aa_FAA)
    ax.set_xlabel("Depth/ cm")
    ax.set_ylabel(aa_FAA_col)
    #ax[0].set_ylim(y_min,y_max)
    plt.xticks(rotation = 45)
    ax.set_title(aa + " MIS 11 FAA D/L values", fontsize=12)
    f.tight_layout()
    plt.show()
    plt.close(f)

FAA_asx = box_plot_FAA("Asx", df_FAA)
FAA_ala = box_plot_FAA("Ala", df_FAA)
FAA_glx = box_plot_FAA("Glx", df_FAA)
FAA_val = box_plot_FAA("Val", df_FAA)

def box_plot_THAA(aa, df_THAA):
    df_THAA = df_THAA.sort_values(["Age rank"], ascending=True)
    df_THAA["Level str"] = df_THAA['Level/ Sample'].astype(str)
    df_THAA["Level name"] = df_THAA["Quaternary sites"] + " " + df_THAA["Level str"]
    aa_THAA_col = aa + " D/L_THAA"
    THAA = df_THAA.loc[df_THAA['Age if known'] == "MIS 11"]
    aa_THAA = THAA[["Level name", aa_THAA_col]]
    sns.color_palette("tab10")
    f, ax = plt.subplots(figsize=(12, 8))
    sns.boxplot(x="Level name", y=aa_THAA_col, data=aa_THAA)
    ax.set_xlabel("Depth/ cm")
    ax.set_ylabel(aa_THAA_col)
    #ax[0].set_ylim(y_min,y_max)
    plt.xticks(rotation = 45)
    ax.set_title(aa + " MIS 11 THAA D/L values", fontsize=12)
    f.tight_layout()
    plt.show()
    plt.close(f)

THAA_asx = box_plot_THAA("Asx", df_THAA)
THAA_ala = box_plot_THAA("Ala", df_THAA)
THAA_glx = box_plot_THAA("Glx", df_THAA)
THAA_val = box_plot_THAA("Val", df_THAA)

