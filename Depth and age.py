# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 10:05:19 2022

@author: efn509
"""

#script to compare age with D/L values
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#import csv
FAA_AA = pd.read_csv('R:/NEaar/People/Ellie Nelson/EQuate frameworks/Hungary/Hungary_FAA.csv')
THAA_AA = pd.read_csv('R:/NEaar/People/Ellie Nelson/EQuate frameworks/Hungary/Hungary_THAA.csv')


#extracting data from FAA csv and placing in dataframe
df_FAA = pd.DataFrame(FAA_AA)


# code if want to look at averages between horizons instead of replicates

#pulling THAA into dataframe
df_THAA = pd.DataFrame(THAA_AA)



def age_scatter(df1, AA, fig1, fraction):
    #creating lists of column containing the required AA
    FAA_colnames = [col for col in df1.columns if str(AA) in col]
    #THAA_colnames = [col for col in df2.columns if str(AA) + " D/L_THAA" in col]
    #FAA plot
    sns.set(style="ticks") 
    ax = sns.scatterplot(x=df1["Age Mid Point"],
                         y=df1[FAA_colnames[0]], 
                         data=df1, hue=df1["Quaternary sites"], 
                         palette="dark", markers=True, s=60)
    ax.set_xlabel("Age/ ka")
    ax.set_ylabel(str(AA) + " " + str(fraction))
    plt.legend(loc="lower right")
    plt.show


asx_FAA = plt.figure(figsize=(10, 6))
Asx_FAA_plt = age_scatter(df_FAA, "Asx", asx_FAA, "FAA D/L")

asx_THAA = plt.figure(figsize=(10, 6))
Asx_THAA_plt = age_scatter(df_THAA, "Asx", asx_THAA, "THAA D/L")


ala_FAA = plt.figure(figsize=(10, 6))
Ala_FAA_plt = age_scatter(df_FAA, "Ala", ala_FAA, "FAA D/L")

ala_THAA = plt.figure(figsize=(10, 6))
Ala_THAA_plt = age_scatter(df_THAA, "Ala", ala_THAA, "THAA D/L")


glx_FAA = plt.figure(figsize=(10, 6))
Glx_FAA_plt = age_scatter(df_FAA, "Glx", glx_FAA, "FAA D/L")

glx_THAA = plt.figure(figsize=(10, 6))
Glx_THAA_plt = age_scatter(df_THAA, "Glx", glx_THAA, "THAA D/L")


val_FAA = plt.figure(figsize=(10, 6))
Val_FAA_plt = age_scatter(df_FAA, "Val", val_FAA, "FAA D/L")

val_THAA = plt.figure(figsize=(10, 6))
Val_THAA_plt = age_scatter(df_THAA, "Val", val_THAA, "THAA D/L")

#depth
def depth_scatter(df1, AA, fig1, fraction):
    #creating lists of column containing the required AA
    FAA_colnames = [col for col in df1.columns if str(AA) in col]
    #THAA_colnames = [col for col in df2.columns if str(AA) + " D/L_THAA" in col]
    sns.set(style="ticks") 
    ax = sns.scatterplot(x=df1["Level/ Sample"],
                         y=df1[FAA_colnames[0]], 
                         data=df1, hue=df1["Quaternary sites"], 
                         palette="dark", markers=True, s=60)
    ax.set_xlabel("Depth/ m")
    ax.set_ylabel(str(AA) + " " + str(fraction))
    plt.legend(loc="lower right")
    plt.show()

asx_FAA_depth = plt.figure(figsize=(8, 6))
Asx_FAA_depth = depth_scatter(df_FAA, "Asx", asx_FAA_depth, "FAA D/L")

asx_THAA_depth = plt.figure(figsize=(8, 6))
Asx_THAA_depth = depth_scatter(df_THAA, "Asx", asx_THAA_depth, "THAA D/L")


ala_FAA_depth = plt.figure(figsize=(8, 6))
Ala_FAA_depth = depth_scatter(df_FAA, "Ala", ala_FAA_depth, "FAA D/L")

ala_THAA_depth = plt.figure(figsize=(8, 6))
Ala_THAA_depth = depth_scatter(df_THAA, "Ala", ala_THAA_depth, "THAA D/L")


glx_FAA_depth = plt.figure(figsize=(8, 6))
Glx_FAA_depth = depth_scatter(df_FAA, "Glx", glx_FAA_depth, "FAA D/L")

glx_THAA_depth = plt.figure(figsize=(8, 6))
Glx_THAA_depth = depth_scatter(df_THAA, "Glx", glx_THAA_depth, "THAA D/L")


val_FAA_depth = plt.figure(figsize=(8, 6))
Val_FAA_depth = depth_scatter(df_FAA, "Val", val_FAA_depth, "FAA D/L")

val_THAA_depth = plt.figure(figsize=(8, 6))
Val_THAA_depth = depth_scatter(df_THAA, "Val", val_THAA_depth, "THAA D/L")


#MIS correlation
def MIS_cat(df1, AA, fig1, fraction):
    #creating lists of column containing the required AA
    FAA_colnames = [col for col in df1.columns if str(AA) in col]
    #THAA_colnames = [col for col in df2.columns if str(AA) + " D/L_THAA" in col]
    plt.figure(figsize=(10, 6))
    sns.set_palette("dark")
    ax = sns.scatterplot(data=df1, x="MIS", y=FAA_colnames[0], hue="Quaternary sites", 
                s=50)
    ax.set_ylabel(AA + " " + fraction)
    plt.legend(loc="lower right")
    plt.show()
 

asx_FAA_MIS = plt.figure(figsize=(8, 6))
Asx_FAA_MIS = MIS_cat(df_FAA, "Asx", asx_FAA_MIS, "FAA D/L")

asx_THAA_MIS = plt.figure(figsize=(8, 6))
Asx_THAA_MIS = MIS_cat(df_THAA, "Asx", asx_THAA_MIS, "THAA D/L")


ala_FAA_MIS = plt.figure(figsize=(8, 6))
Ala_FAA_MIS = MIS_cat(df_FAA, "Ala", ala_FAA_MIS, "FAA D/L")

ala_THAA_MIS = plt.figure(figsize=(8, 6))
Ala_THAA_MIS = MIS_cat(df_THAA, "Ala", ala_THAA_MIS, "THAA D/L")


glx_FAA_MIS = plt.figure(figsize=(8, 6))
Glx_FAA_MIS = MIS_cat(df_FAA, "Glx", glx_FAA_MIS, "FAA D/L")

glx_THAA_MIS = plt.figure(figsize=(8, 6))
Glx_THAA_MIS = MIS_cat(df_THAA, "Glx", glx_THAA_MIS, "THAA D/L")


val_FAA_MIS = plt.figure(figsize=(8, 6))
Val_FAA_MIS = MIS_cat(df_FAA, "Val", val_FAA_MIS, "FAA D/L")

val_THAA_MIS = plt.figure(figsize=(8, 6))
Val_THAA_MIS = MIS_cat(df_THAA, "Val", val_THAA_MIS, "THAA D/L")