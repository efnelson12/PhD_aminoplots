# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 15:34:00 2022

@author: efn509
"""

#Script to check if there are any issues with the data 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from mycolorpy import colorlist as mcp

#This is the script for the geochronology of Poland and Belarus 
#To use this script data from FAA and THAA data need to be saved as separate csv files

#make sure you replace any #VALUE and #DIV in csv with a '0'

#import csv
FAA_AA = pd.read_csv('R:/NEaar/People/Ellie Nelson/Data_check_AAR.csv')


#plotting concentration
df_concentration = pd.DataFrame(FAA_AA[["Sample name", "relative", "Quaternary sites", "location", "[Asx]", "[Glx]", "[Ser]", "[L-Thr]", "[L-His]",
                                        "[Gly]", "[L-Arg]", "[Ala]", "[Tyr]",
                                        "[Val]", "[Phe]", "[Leu]", "[Ile]"]])
for col in df_concentration.columns[4:16]:
    df_concentration[col] = pd.to_numeric(df_concentration[col], errors="coerce")


df_concentration = df_concentration.replace(np.nan, 0.0, regex=True)


df_conc_hun = df_concentration.loc[df_concentration["relative"] == "Hungary"]


df_conc_average = df_conc_hun.groupby(["location", "Quaternary sites", 
                                            'relative']).agg([np.mean]).reset_index()
            
df_conc_melt = pd.melt(df_conc_average, id_vars=["location", "Quaternary sites", 
                                            'relative'], var_name="Amino Acid",
                       value_name="Concentration")


color1=mcp.gen_color(cmap="tab20", n=13)

def pie_chart(df, depth, site):
    AA_df = df.loc[df["location"] == depth]
    aminos = list(AA_df["Amino Acid"])
    #fig = fig
    y = list(AA_df["Concentration"])
    plt.figure(figsize=(10,10))
    plt.pie(y, labels = aminos, colors=color1, rotatelabels=(True), labeldistance=(1.05))
    plt.title(str(site) + " " + str(depth), pad=5.0, fontsize=16)
    plt.show()



#plotting composition

AA_conc = ["[Asx]", "[Glx]", "[Ser]", "[L-Thr]", "[L-His]",
                                        "[Gly]", "[L-Arg]", "[Ala]", "[Tyr]",
                                        "[Val]", "[Phe]", "[Leu]", "[Ile]"]

df_concentration["Total_conc"] = df_concentration.sum(axis=1)

for AA in AA_conc:
    df_concentration[str(AA) + " %"] = df_concentration[AA]/df_concentration["Total_conc"]
 
comp_list = []    
for AA in AA_conc:
    comp_list.append(str(AA) + " %") 
    

df_composition = df_concentration[["Sample name", "relative", "Quaternary sites",
                                                  "location"]].copy()
df_composition[comp_list] = df_concentration[comp_list].copy()

df_comp_melt = pd.melt(df_composition, id_vars=["Sample name", "relative", "Quaternary sites",
                                                  "location"], var_name="Amino Acid",
                       value_name="Composition")

dev_df = df_comp_melt.loc[df_comp_melt["Quaternary sites"] == "Devavanya"]
dev_depths = list(dev_df ["location"].unique())

ves_df = df_comp_melt.loc[df_comp_melt["Quaternary sites"] == "Veszto"]
ves_depths = list(ves_df ["location"].unique())

#for depth in dev_depths:
 #   pie_chart(df_comp_melt, depth, "Devavanya")
    
#for depth in ves_depths:
 #   pie_chart(df_comp_melt, depth, "Veszto")
    
#plotting bar chart for Devavanya data
def double_std(array):
 return np.std(array) * 2
 
sorterIndex_dev = dict(zip(dev_depths, range(len(dev_depths))))

def aa_mean(df, AA, sorterIndex):
    aa_df = df.loc[lambda df: df["Amino Acid"] == AA]
    aa_df_mean = aa_df.groupby(["location", "Quaternary sites", 
                            "Amino Acid"]).agg([np.mean, double_std]).reset_index()
    aa_df_mean["Depth rank"] = aa_df_mean["location"].map(sorterIndex)
    aa_df_mean.sort_values(['Depth rank'],
        ascending = [True], inplace = True)
    aa_df_mean.drop('Depth rank', 1, inplace = True)
    aa_df_mean.reset_index()
    mean_list = list(aa_df_mean["Composition", "mean"])
    std_list = list(aa_df_mean['Composition', 'double_std'])
    location_list = list(aa_df_mean["location"])
    return mean_list, std_list, location_list
    

Asx_mean, Asx_std, Asx_loc = aa_mean(dev_df, "[Asx] %", sorterIndex_dev)
Glx_mean, Glx_std, Glx_loc = aa_mean(dev_df, "[Glx] %", sorterIndex_dev)
Ser_mean, Ser_std, Ser_loc = aa_mean(dev_df, "[Ser] %", sorterIndex_dev)
Ala_mean, Ala_std, Ala_loc = aa_mean(dev_df, "[Ala] %", sorterIndex_dev)
Val_mean, Val_std, Val_loc = aa_mean(dev_df, "[Val] %", sorterIndex_dev)
Phe_mean, Phe_std, Phe_loc = aa_mean(dev_df, "[Phe] %", sorterIndex_dev)

N_dev = len(dev_depths)
ind = np.arange(N_dev)
width = 0.1

fig1, ax1 = plt.subplots(figsize=(12,6))

Asx_plot = ax1.bar(ind, Asx_mean, width, color='r') #yerr=Asx_std)
Glx_plot = ax1.bar(ind + width, Glx_mean, width, color='g') #yerr=Glx_std)
Ser_plot = ax1.bar(ind + width * 2, Ser_mean, width, color='b') #yerr=Ser_std)
Ala_plot = ax1.bar(ind + width * 3, Ala_mean, width, color='c') #yerr=Ala_std)
Val_plot = ax1.bar(ind + width * 4, Val_mean, width, color='m') #yerr=Val_std)
Phe_plot = ax1.bar(ind + width * 5, Phe_mean, width, color='y') #yerr=Phe_std)

# add some text for labels, title and axes ticks
ax1.set_ylabel('Composition')
ax1.set_title('Amino acid composition versus depth for Devavanya Core')
ax1.set_xticks(ind + width * 2.5)
ax1.set_xticklabels((dev_depths))
ax1.legend((Asx_plot[0], Glx_plot[0], Ser_plot[0],
            Ala_plot[0], Val_plot[0], Phe_plot[0]), 
           ('Asx', 'Glx', 'Ser', 'Ala', 'Val', 'Phe'))

#plot for veszto
sorterIndex_ves = dict(zip(ves_depths, range(len(ves_depths))))

Asx_mean_v, Asx_std_v, Asx_loc_v = aa_mean(ves_df, "[Asx] %", sorterIndex_ves)
Glx_mean_v, Glx_std_v, Glx_loc_v = aa_mean(ves_df, "[Glx] %", sorterIndex_ves)
Ser_mean_v, Ser_std_v, Ser_loc_v = aa_mean(ves_df, "[Ser] %", sorterIndex_ves)
Ala_mean_v, Ala_std_v, Ala_loc_v = aa_mean(ves_df, "[Ala] %", sorterIndex_ves)
Val_mean_v, Val_std_v, Val_loc_v = aa_mean(ves_df, "[Val] %", sorterIndex_ves)
Phe_mean_v, Phe_std_v, Phe_loc_v = aa_mean(ves_df, "[Phe] %", sorterIndex_ves)

N_ves = len(ves_depths)
ind_v = np.arange(N_ves)
width = 0.1

fig2, ax2 = plt.subplots(figsize=(12,6))

Asx_plot_v = ax2.bar(ind_v, Asx_mean_v, width, color='r') #yerr=Asx_std_v)
Glx_plot_v = ax2.bar(ind_v + width, Glx_mean_v, width, color='g') #yerr=Glx_std)
Ser_plot_v = ax2.bar(ind_v + width * 2, Ser_mean_v, width, color='b') #yerr=Ser_std)
Ala_plot_v = ax2.bar(ind_v + width * 3, Ala_mean_v, width, color='c') #yerr=Ala_std)
Val_plot_v = ax2.bar(ind_v + width * 4, Val_mean_v, width, color='m') #yerr=Val_std)
Phe_plot_v = ax2.bar(ind_v + width * 5, Phe_mean_v, width, color='y') #yerr=Phe_std)

# add some text for labels, title and axes ticks
ax2.set_ylabel('Composition')
ax2.set_title('Amino acid composition versus depth for Veszto Core')
ax2.set_xticks(ind_v + width * 2.5)
ax2.set_xticklabels((ves_depths))
ax2.legend((Asx_plot_v[0], Glx_plot_v[0], Ser_plot_v[0],
            Ala_plot_v[0], Val_plot_v[0], Phe_plot_v[0]), 
           ('Asx', 'Glx', 'Ser', 'Ala', 'Val', 'Phe'))
