
# coding: utf-8
#EMPLOYEE COMPENSATION ANALYSIS
#1.Data contains fiscal and calendar year information. Same employee details exist twice in the dataset.  Filter data by calendar year and find average salary (you might have to find average for each of the  columns for every employee. Eg. Average of Total Benefits, Average of total compensation etc.) for  every employee.
#2.Now, find the people whose overtime salary is greater than 5% of salaries (salaries refers to ’Salaries'  column)
#3.For each ‘Job Family’ these people are associated with, calculate the percentage of total benefits with  respect to total compensation (so for each job family you have to calculate average total benefits and  average total compensation). Create a new column to hold the percentage value.
#4.Display the top 5 Job Families according to this percentage value using df.head().
#5.Write the output (jobs and percentage value) to a csv.


# In[1]:

#importing libraries
import os
import pandas as pd
import datetime as dt


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

emp_df=df[(df['Year Type']=='Calendar')]


# In[5]:

emp_df=pd.DataFrame(emp_df.groupby(['Employee Identifier','Job Family']).mean())


# In[6]:

emp_df


# In[7]:

emp_df.drop(['Year', 'Organization Group Code','Union Code'], axis=1, inplace=True)


# In[8]:

emp_df


# In[9]:

emp_df=emp_df[(emp_df['Overtime']>(0.05*emp_df['Salaries']))]


# In[10]:

emp_df


# In[11]:

emp_df['Percent_Total_Benefit']=(emp_df['Total Benefits']/emp_df['Total Compensation'])*100


# In[12]:

emp_df= emp_df[['Total Benefits','Total Compensation','Percent_Total_Benefit']]


# In[13]:

emp_df


# In[14]:

top_jobFamily=emp_df.sort_values(['Percent_Total_Benefit'], ascending=[False])


# In[15]:

top_jobFamily.reset_index(inplace=True)


# In[16]:

top_jobFamily.head(5)


# In[17]:

top_jobFamily=top_jobFamily.drop(['Employee Identifier'],axis=1)


# In[18]:

top_jobFamily.to_csv('Q2_Part_2.csv',index=False)
top_jobFamily.head(5)


# In[ ]:




# In[ ]:



