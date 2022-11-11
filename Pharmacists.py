# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 20:09:23 2022

@author: Adithya O
"""
import pandas as pd
import matplotlib.pyplot as plt

"""
A code to visualise the number of pharmacists in public sector,private sector
and those who are not in active practice during the time span of 2006 to 2019.
"""

#A funtion to find the total count in each sector
def sumOfPharamasistsCount(df_Sector):
    """
    The dataframe df_sector is passed to find the sum of columns.
    The result is passed.
    Result example: year: 6567
                count: 4566
                sector: publicprivatenotinpractice
    """
    df_SectorSumResult = df_Sector.sum()
    return df_SectorSumResult


#A function to plot the line graph
def linegraph(): 
    """
    The linegraph function used to plot line grpah.
    3 line plots of public, private sector and not in active practice pharmacists are plotted.
    """
    plt.figure()
    plt.plot(df_public["year"],df_public["count"],'g-',label='Public')
    plt.plot(df_private["year"],df_private["count"],'b-',label='Private')
    plt.plot(df_notActive["year"],df_notActive["count"],'r-',label='Not in active Practice')
    plt.legend()
    plt.title('Pharmacist job analysis')
    plt.xlabel("Year")
    plt.ylabel("Count")
    plt.show()
    

#A function to plot the bar graph    
def barGraph():
    """
    The bargraph function used to plot bar grpah.
    Public and Not in active practice data are compared here.
    """
    plt.figure()
    plt.bar(df_public["year"],df_public["count"],label='Public')
    plt.bar(df_notActive["year"],df_notActive["count"],label='Not in active Practice')
    plt.xlabel("Year")
    plt.ylabel("Count")
    plt.title('Pharmacist job analysis')
    plt.legend()
    plt.show()


#A function to plot the pie chart
def piegraph():
    """
    The function to plot pie chart. 
    df_publiccount reads the sum of columns in public sector dataframe.
    df_privatecount reads the sum of columns in public sector dataframe.
    df_notactivecount reads the sum of columns in public sector dataframe.

    NewSectordata is used to create a new dataframe (df_TotalCountofSectors) for showing the total count in each sector.
    """
    df_publiccount = sumOfPharamasistsCount(df_public)
    df_privatecount = sumOfPharamasistsCount(df_private)
    df_notactivecount = sumOfPharamasistsCount(df_notActive)    
    NewSectordata = [['Public Sector',df_publiccount["count"]],['Private Sector',df_privatecount["count"]],['Not in Active Practice',df_notactivecount["count"]]]    
    df_TotalCountofSectors = pd.DataFrame(NewSectordata, columns=['sector','count'])
    plt.figure()
    plt.pie(df_TotalCountofSectors["count"], labels=df_TotalCountofSectors['sector'],autopct='%1.0f%%')
    plt.show()
    


#Read the data set
Data = pd.read_csv("pharmacists.csv")
df_Data = pd.DataFrame(Data)


#Filter the data as seperate sector. 
df_public = df_Data.loc[df_Data["sector"].isin(["Public Sector"])]
df_private = df_Data.loc[df_Data["sector"].isin(["Private Sector"])]
df_notActive = df_Data.loc[df_Data["sector"].isin(["Not in Active Practice"])]


#Calling functions to plot the grpahs
linegraph()
barGraph()
piegraph()







