# -*- coding: utf-8 -*-
"""
Created on Tue May 21 17:46:24 2019

@author: brank_000
"""
#correlation between the number of deaths associated with influenza and the average temperature
#Pearson's correlation

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import scipy
import scipy.stats

temp = pd.read_csv('avg_winter_temperature.csv')
pneum = pd.read_csv('flu_pneumonia.CSV')

merged = pd.merge(temp, pneum, on="state", how="inner")


#convert Celsius to Fahrenhait --> Return Celsius conversion of input
#math correlation between F and C --> F = C × 1.8 + 32 
def celsius_to_fahr(temp_celsius):
    temp_fahr = 9/5*temp_celsius + 32
    return temp_fahr
celsius_to_fahr(merged["avg_celsius"])

#new column "avg_fahreinheit"
merged["avg_fahrenheit"] = celsius_to_fahr(merged["avg_celsius"])


#create a function to interpret the results
death_rate = merged.iloc[:, 2].values       #independent variable vector
death_abs = merged.iloc[:, 3].values        #independent variable vector
avg_fahrenheit = merged.iloc[:, 4].values   #dependent variable vector

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
        print ('error')# if value is not between -1 and 1
        
#plot --> correlation between the number of deaths-absolute associated with influenza and the average temperature
personScoreFahrDeathAbs=scipy.stats.pearsonr(avg_fahrenheit, death_abs)      
interpret_corrcoef(personScoreFahrDeathAbs[0])
sns.regplot( data=merged, x='avg_fahrenheit', y='death_abs')

#plot --> correlation between the number of deaths-rate associated with influenza and the average temperature
personScoreFahrDeathRate=scipy.stats.pearsonr(avg_fahrenheit, death_rate)      
interpret_corrcoef(personScoreFahrDeathRate[0])
plt.figure() # create new window / blank chart
sns.regplot( data=merged, x='avg_fahrenheit', y='death_rate')

#math correlation between C and F --> C = (5/9) * (F - 32)

plt.show()