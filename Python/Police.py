#!/usr/bin/env python
# coding: utf-8

# In[51]:


import pandas as pd
import numpy as np


# ## Q. 1) Instruction ( For Data Cleaning ) - Remove the column that only contains missing values.

# In[21]:


df = pd.read_csv('Police.csv', sep = ',')


# In[22]:


df.head()


# In[25]:


df.drop(columns = ['country_name'])


# In[31]:


df.head()


# ## Q. 2) Question ( Based on Filtering + Value Counts ) - For Speeding , were Men or Women stopped more often ?

# In[38]:


df[((df.violation == 'Speeding') & (df.violation_raw == 'Speeding')) & ((df.driver_gender == 'M') | (df.driver_gender == 'F'))].value_counts()


# In[47]:


df[((df.violation == 'Speeding') & (df.violation_raw == 'Speeding')) & (df.driver_gender == 'M')][['driver_gender']].value_counts()


# In[48]:


df[((df.violation == 'Speeding') & (df.violation_raw == 'Speeding')) & (df.driver_gender == 'F')][['driver_gender']].value_counts()


# ## Q. 3) Question ( Groupby ) - Does gender affect who gets searched during a stop ?
# Question ( mapping + data-type casting )

# In[64]:


#in search_conducted i TRUE e FALSE sono dei bool e quindi vengono considerati come 1 e 0.

#chiedendo la somma dei valori nella colonna search_conducted fai solamente la somma dei TRUE.

df.groupby('driver_gender').search_conducted.sum()


# In[65]:


df.search_conducted.value_counts()


# In[66]:


df.search_conducted.dtype


# ## Q. 4) Question ( mapping + data-type casting ) - What is the mean stop_duration ?

# In[74]:


df[['time','minutes']] = df.stop_duration.str.split(' ', expand = True)


# In[78]:


df.time.dtype


# In[81]:


df['stop_duration_mean'] = df['stop_duration'].map({ '0-15 Min' : 7.5, '16-30 Min' : 24, '30+ Min' :45})


# In[82]:


df.head()


# In[88]:


for i in df.time :
    print(df.time.replace(int(i))
        


# In[ ]:





# ## Q. 5) Question ( Groupby , Describe ) - Compare the age distributions for each violation.

# In[92]:


#applico describe() a driver_age per capire la media dell'eta, la standard deviation il min...

df.groupby('violation').driver_age.describe()


# In[95]:


#describe lo puoi applicare a violation ma non ha senso, perchè violation ha le stringhe.

df.groupby('driver_age').violation.describe()


# In[ ]:




