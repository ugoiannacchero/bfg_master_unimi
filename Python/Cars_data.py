#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


cars_raw = pd.read_csv('/home/student/masterbfg/file.csv', sep = ',')


# ## Q. 1) Instruction ( For Data Cleaning ) - Find all Null Values in the dataset. If there is any null value in any column, then fill it with the mean of that column.

# In[3]:


cars_raw.isnull().sum()


# In[4]:


cars_raw.shape


# In[5]:


cars = cars_raw.dropna()c


# In[6]:


cars.shape


# ## Q. 2) Question ( Based on Value Counts )- Check what are the different types of Make are there in our dataset. And, what is the count (occurrence) of each Make in the data ?

# In[9]:


cars.Make.unique()


# In[7]:


cars['Make'].value_counts()


# ## Q. 3) Instruction ( Filtering ) - Show all the records where Origin is Asia or Europe.

# In[15]:


cars[(cars['Origin'] == 'Europe') | (cars['Origin'] == 'Asia')][['Make','Origin']].value_counts()


# ## Q. 4) Instruction ( Removing unwanted records ) - Remove all the records (rows) where Weight is above 4000.

# In[29]:


cars_light = cars[cars['Weight'] < 4000.0]


# In[30]:


cars_light.head()


# In[32]:


cars_light.shape


# In[38]:


cars_light[['Make', 'Weight']].count()


# ## Q. 5) Instruction ( Applying function on a column ) - Increase all the values of 'MPG_City' column by 3.

# In[39]:


cars_light.head()


# In[46]:


new_cars = cars_light.MPG_City+3


# In[47]:


new_cars.head(5)


# In[49]:


cars_light['MPG_City'] = cars_light['MPG_City'].apply(lambda  x:x+3)


# In[50]:


cars_light.head()


# In[54]:


cars_light.sort_values(by ='MPG_City', ascending = False)


# In[ ]:




