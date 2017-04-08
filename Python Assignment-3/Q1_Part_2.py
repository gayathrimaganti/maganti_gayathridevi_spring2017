
# coding: utf-8
# NYC Vehicle Collision Analysis
#1.For each borough, find out distribution of each collision scale. (One car  involved? Two? Three? or more?) (From 2015 to present)
#2.Display a few rows of the output use df.head().
#3.Generate a csv output with five columns ('borough', 'one-vehicle', 'two-vehicles', 'three-vehicles', 'more-vehicles')


# In[1]:

#importing libraries
import os
import pandas as pd


# In[2]:

#creating relative path from current directory to access the input csv file

current_location=os.path.dirname('__file__')
input_data_location=os.path.join(current_location,'Data')
csv_file='vehicle_collisions.csv'

#accessing csv input data file through relative path
path=os.path.join(input_data_location,csv_file) 


# In[3]:

df=pd.read_csv(path,sep=',')
df


# In[4]:

select_col_df=df.ix[:,('BOROUGH','VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE', 'VEHICLE 5 TYPE')]


# In[5]:

select_col_df['VEHICLES']=select_col_df.loc[:,('VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE',
                                    'VEHICLE 5 TYPE')].count(axis=1)


# In[6]:

select_col_df


# In[7]:

num_of_vehi=select_col_df.groupby(['BOROUGH','VEHICLES']).VEHICLES.count() 


# In[8]:

num_of_vehi


# In[9]:

df1=pd.DataFrame({'Sum':num_of_vehi})


# In[10]:

df1.reset_index(inplace=True)


# In[11]:

df1


# In[12]:

df2=df1.pivot(index='BOROUGH', columns='VEHICLES', values='Sum') 


# In[13]:

df2.columns=['ZERO_VEHICLE_INVOLVED','ONE_VEHICLE_INVOLVED','TWO_VEHICLES_INVOLVED','THREE_VEHICLES_INVOLVED','FOUR_VEHICLES_INVOLVED','FIVE_VEHICLES_INVOLVED']


# In[14]:

df2['MORE_VEHICLES_INVOLVED'] = df2['FOUR_VEHICLES_INVOLVED'] + df2['FIVE_VEHICLES_INVOLVED'] 
df2= df2.loc[:,('ONE_VEHICLE_INVOLVED','TWO_VEHICLES_INVOLVED','THREE_VEHICLES_INVOLVED','MORE_VEHICLES_INVOLVED')]
df2.reset_index(inplace=True)


# In[15]:

df2.head()


# In[16]:

df2.to_csv('Q1_Part_2.csv',index=False) 


# In[ ]:



