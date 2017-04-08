
# coding: utf-8
#CRICKET MATCHES ANALYSIS
#1.Calculate the average score for each team which host the game and win the game.
#2.Remember that if a team hosts a game and wins the game, their score can be innings_1  runs or innings_2 runs. You have to check if the host team won the game, check which  innings they played in (innings_1 or innings_2), and take the runs scored in that innings.  The final answer is the average score of each team satisfying the above condition.
#3.Display a few rows of the output use df.head()
#4.Generate a csv output
# In[1]:

#importing libraries
import os
import pandas as pd
import numpy


# In[2]:

#creating relative path from current directory to access the input csv file

current_location=os.path.dirname('__file__')
input_data_location=os.path.join(current_location,'Data')
csv_file='cricket_matches.csv'

#accessing csv input data file through relative path
path=os.path.join(input_data_location,csv_file) 


# In[3]:

df=pd.read_csv(path,sep=',')
df


# In[4]:

#Checking where the home team is also the winner of the match
df=df[(df['home']==df['winner'])]


# In[5]:

# Selecting the necessary columns for analysis
df1=df[['home','winner','innings1','innings1_runs','innings2','innings2_runs']] 


# In[6]:

df1


# In[7]:

df1['Score'] = df1['innings1_runs'].where(df1['home'] == df1['innings1'], df1['innings2_runs'])


# In[8]:

df1


# In[9]:

df1=df1[['home','Score']]


# In[10]:

df1


# In[11]:

df1=pd.DataFrame(df1.groupby(['home']).mean()) #Taking the avg score of each team.


# In[12]:

df1.reset_index()


# In[13]:

df1.to_csv('Q3_Part_1_Output.csv')


# In[ ]:



