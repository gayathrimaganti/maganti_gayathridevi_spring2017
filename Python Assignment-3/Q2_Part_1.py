
# coding: utf-8
#EMPLOYEE COMPENSATION ANALYSIS
#1.Find out the highest paid departments in each organization group by calculating mean of total compensation for every department.
#2.Output should contain the organization group and the departments in  each organization group with the total compensation from highest to  lowest value.
#3.Display a few rows of the output use df.head().
#4.Generate a csv output.

# In[1]:

#importing libraries
import os
import pandas as pd


# In[2]:

#creating relative path from current directory to access the input csv file

current_location=os.path.dirname('__file__')
input_data_location=os.path.join(current_location,'Data')
csv_file='employee_compensation.csv'

#accessing csv input data file through relative path
path=os.path.join(input_data_location,csv_file) 


# In[3]:

df=pd.read_csv(path,sep=',')
df


# In[4]:

#Grouping by Organization & Department and calculating their mean compensation
df2=pd.DataFrame(df.groupby(['Organization Group','Department']).mean()) 


# In[5]:

#creating a copy of the dataframe with 'total compensation' as the column
df2=df2[['Total Compensation']] 
df2.reset_index(inplace=True)

#Sorting the data according to highest to lowest compensation in each organization

df2=df2.sort_values(by=['Organization Group','Total Compensation'],ascending=[True,False]) 
df2.reset_index()

#Final columns in the dataframe
df2.columns=['Organization Group','Department','Total Compensation'] 

df2.head()



# In[6]:

#getting a .csv output of the dataframe
df2.to_csv('Q2_Part_1.csv', index = False)

#printing first 10 values of the dataframe
df2.head(10)


# In[ ]:




# In[ ]:



