
# coding: utf-8

#NYC VEHICLE COLLISION ANALYSIS
#1.For each month in 2016, find out the percentage of collisions in Manhattan out of that year's total accidents in New York City.
#2.Display a few rows of the output use df.head().
#3.Generate a csv output with four columns (‘Month’, ‘Manhattan’, ‘NYC’,‘Percentage’)

# In[3]:

#importing libraries
import os
import pandas as pd
import datetime as dt


# In[4]:

#creating relative path from current directory to access the input csv file

current_location=os.path.dirname('__file__')
input_data_location=os.path.join(current_location,'Data')
csv_file='vehicle_collisions.csv'

#accessing csv input data file through relative path
path=os.path.join(input_data_location,csv_file) 


# In[5]:

df=pd.read_csv(path,sep=',')
df


# In[55]:

#converting data-type of date(object-string) into datetime data-type
df['DATE']=pd.to_datetime(df['DATE']) 


# In[56]:

df1=df[(df['BOROUGH']=='MANHATTAN') & (pd.DatetimeIndex(df['DATE']).year==2016)]


# In[57]:

df1=df1.ix[:,('DATE','BOROUGH')]


# In[58]:

df1['MONTH']=df1['DATE'].dt.month


# In[63]:

df1['MONTH'] = df1['DATE'].apply(lambda x: x.strftime('%B'))


# In[64]:

df1


# In[65]:

final_df= pd.DataFrame()


# In[68]:

final_df['MANHATTAN'] = df1[df1['BOROUGH']=='MANHATTAN'].groupby(['MONTH'],sort = False).count()


# In[ ]:

final_df['NYC'] = df.groupby(['MONTH']).count()


# In[ ]:

final_df['PERCENTAGE']= final_df['MANHATTAN']/final_df['NYC']


# In[ ]:

final_df.reset_index()


# In[ ]:

final_df.head()


# In[ ]:

final_df.to_csv('Q1_Part_1.csv',index=False)

