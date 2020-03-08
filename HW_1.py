# -*- coding: utf-8 -*-
"""
Created on Tue May 21 17:46:24 2019

@author: brank_000
"""
#Correlation between 
#the number of deaths associated with influenza and the average temperature

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import scipy
import scipy.stats

temp = pd.read_csv('avg_winter_temperature.csv')
pneum = pd.read_csv('flu_pneumonia.CSV')

merged = pd.merge(temp, pneum, on="state", how="inner")


#Convert Celsius to Fahrenhait --> Return Celsius conversion of input
def celsius_to_fahr(temp_celsius):
    temp_fahr = 9/5*temp_celsius + 32
    return temp_fahr
celsius_to_fahr(merged["avg_celsius"])

#new column "avg_fahreinheit"
merged["avg_fahrenheit"] = celsius_to_fahr(merged["avg_celsius"])

death_rate = merged.iloc[:, 2].values #independent variable vector
death_abs = merged.iloc[:, 3].values #independent variable vector
avg_fahrenheit = merged.iloc[:, 4].values   #dependent variable vector

# create a function to interpret the results
def interpret_corrcoef(value):
    if (value == -1):
        print ('perfect negative')
    elif (value > -1 and value <=-0.7):
        print ('strong negative')
    elif (value > -0.7 and value <=-0.5):
        print ('moderate negative')
    elif (value > -0.5 and value <=-0.3):
        print ('weak negative')
    elif (value > -0.3 and value <=0.3):
        print ('no relationship')
    elif (value > 0.3 and value <=0.5):
        print ('weak positive')
    elif (value > 0.5 and value <=0.7):
        print ('moderate positive')
    elif (value > 0.7 and value <1):
        print ('strong positive')
    elif (value == 1):
        print ('perfect positive')
    else:
        print ('error')
        
# correlation
personRResult=scipy.stats.pearsonr(avg_fahrenheit, death_abs)      
interpret_corrcoef(personRResult[0])
sns.regplot( data=merged, x='avg_fahrenheit', y='death_abs')

# correlation
personRResult1=scipy.stats.pearsonr(avg_fahrenheit, death_rate)      
interpret_corrcoef(personRResult1[0])
plt.figure(); # create new window / blank chart
sns.regplot( data=merged, x='avg_fahrenheit', y='death_rate')

