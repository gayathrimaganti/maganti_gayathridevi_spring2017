
# coding: utf-8

#MOVIE AWARDS ANALYSIS
#1.You are supposed to extract data from the awards column in this dataset and split it into several  columns. An example is given below.
#2.The awards has details of wins, nominations in general and also wins and nominations in certain  categories(e.g. Oscar, BAFTA etc.)
#3.You are supposed to create a win and nominated column (these 2 columns contain total number of wins  and nominations) and other columns that extract the number of wins and nominations for each category  of award.
#4.If a movie has 2 Oscar nominations and 4 Oscar won, the columns Oscar_Awards_Won should have  value 4 and Oscar_Awards_Nominated should have value 2. You should also have a total won and  nominated column which aggregates all the awards (won or nominated).
#5.Create two separate columns for each award category (won and nominated).
#6.Write your output to a csv file.
# In[1]:

#importing libraries
import os
import pandas as pd
import datetime as dt
import numpy as np


# In[2]:

#creating relative path from current directory to access the input csv file

current_location=os.path.dirname('__file__')
input_data_location=os.path.join(current_location,'Data')
csv_file='movies_awards.csv'

#accessing csv input data file through relative path
path=os.path.join(input_data_location,csv_file) 


# In[3]:

df=pd.read_csv(path,sep=',')
df


# In[6]:

df1=df[['Awards']]


# In[7]:

df1


# In[11]:

df1['Awards_won'] = df1['Awards'].str.extract("(\d+) win")
df1['Awards_nominated'] =  df1['Awards'].str.extract("(\d+) nomination")
df1['Prime_Awards_won'] = df1['Awards'].str.extract("Won (\d+) Primetime Emmy")
df1['Prime_Awards_nominated'] = df1['Awards'].str.extract("Nominated for (\d+) Primetime Emmy")
df1['Oscar_Awards_nominated'] = df1['Awards'].str.extract("Nominated for (\d+) Oscar")
df1['Oscar_Awards_won'] = df1['Awards'].str.extract("Won (\d+) Oscar")
df1['Golden_Globe_Awards_nominated'] = df1['Awards'].str.extract("Nominated for (\d+) Golden Globe")
df1['Golden_Globe_Awards_won'] =df1['Awards'].str.extract("Won (\d+) Golden Globe")
df1['BAFTA_Awards_nominated'] = df1['Awards'].str.extract("Nominated for (\d+) BAFTA")
df1['BAFTA_Awards_won'] = df1['Awards'].str.extract("Won (\d+) BAFTA")


# In[12]:

df2= df1.fillna(0)


df2['Awards_won'] = df2['Awards_won'].astype(str).astype(int)
df2['Prime_Awards_won'] = df2['Prime_Awards_won'].astype(str).astype(int)
df2['Oscar_Awards_won'] = df2['Oscar_Awards_won'].astype(str).astype(int)
df2['Golden_Globe_Awards_won'] = df2['Golden_Globe_Awards_won'].astype(str).astype(int)
df2['BAFTA_Awards_won'] =df2['BAFTA_Awards_won'].astype(str).astype(int)
df2['Awards_nominated'] =df2['Awards_nominated'].astype(str).astype(int)
df2['Prime_Awards_nominated'] = df2['Prime_Awards_nominated'].astype(str).astype(int)
df2['Oscar_Awards_nominated'] = df2['Oscar_Awards_nominated'].astype(str).astype(int)
df2['Golden_Globe_Awards_nominated'] = df2['Golden_Globe_Awards_nominated'].astype(str).astype(int)
df2['BAFTA_Awards_nominated'] = df2['BAFTA_Awards_nominated'].astype(str).astype(int)


df2['Total_Awards_Won'] = df2['Awards_won'] + df2['Prime_Awards_won'] + df2['Oscar_Awards_won'] + df2['Golden_Globe_Awards_won']+df2['BAFTA_Awards_won']



df2['Total_Awards_Nominated'] = df2['Awards_nominated'] + df2['Prime_Awards_nominated']+ df2['Oscar_Awards_nominated'] + df2['Golden_Globe_Awards_nominated'] + df2['BAFTA_Awards_nominated'] 


df2


# In[14]:

df2.to_csv("Q4_Part_1.csv",index=False)


# In[ ]:




# In[ ]:



