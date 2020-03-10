# -*- coding: utf-8 -*-

#correlation between the number of deaths associated with influenza and the average temperature
#Pearson's correlation

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import scipy
import scipy.stats

#convert Celsius to Fahrenhait --> Return Celsius conversion of input
#math correlation between F and C --> F = C × 1.8 + 32 
def celsius_to_fahr(temp_celsius):
    temp_fahr = 9/5*temp_celsius + 32
    return temp_fahr

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

#begin program
#avg_winter_temperature.csv - the average temperature during the winter season from 2015/2016 by State; 
temp = pd.read_csv('avg_winter_temperature.csv')
#flu_pneumonia.CSV - the number of deaths and the death rate associated with the Influenza virus by State in 2015; 
pneum = pd.read_csv('flu_pneumonia.csv')
# merged two tables on state(common column)
merged = pd.merge(temp, pneum, on="state", how="inner")

celsius_to_fahr(merged["avg_celsius"])

# add new column "avg_fahreinheit" as a task from homework
merged["avg_fahrenheit"] = celsius_to_fahr(merged["avg_celsius"])


#create a function to interpret the results
death_rate = merged.iloc[:, 2].values       #independent variable vector
death_abs = merged.iloc[:, 3].values        #independent variable vector
avg_fahrenheit = merged.iloc[:, 4].values   #dependent variable vector


        
#plot --> correlation between the number of deaths-absolute associated with influenza and the average temperature
# --> returns - rfloat(Pearson’s correlation coefficient) in [0] column and
# p-valuefloat(two-tailed p-value) in [1] column
personScoreFahrDeathAbs=scipy.stats.pearsonr(avg_fahrenheit, death_abs) 
#we take [0] column - rfloat(Pearson’s correlation coefficient)     
interpret_corrcoef(personScoreFahrDeathAbs[0])
plt.title('Correlation between the number of deaths-absolute associated with influenza and the average temperature')
sns.regplot( data=merged, x='avg_fahrenheit', y='death_abs')

#plot --> correlation between the number of deaths-rate associated with influenza and the average temperature
personScoreFahrDeathRate=scipy.stats.pearsonr(avg_fahrenheit, death_rate)      
interpret_corrcoef(personScoreFahrDeathRate[0])
plt.figure() # create new window / blank chart
plt.title('Correlation between the number of deaths-rate associated with influenza and the average temperature')
sns.regplot( data=merged, x='avg_fahrenheit', y='death_rate')

plt.show()