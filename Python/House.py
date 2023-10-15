#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


import matplotlib as plt


# ## Q. 1) Convert the Datatype of 'Date' column to Date-Time format.

# In[32]:


df = pd.read_csv('/home/ugo/masterbfg/Kaggle/House Prices/house.csv', sep = ',')


# In[33]:


df


# In[34]:


df['date'].dtype


# In[35]:


df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')


# In[36]:


df['date'].dtype


# In[37]:


df_crimes = df.dropna()


# In[38]:


df.shape


# In[39]:


df_crimes.shape


# ## Q. 2) Add a new column ''year'' in the dataframe, which contains years only.
# 
# ## (2.B) Add a new column ''month'' as 2nd column in the dataframe, which contains month only.

# In[40]:


df['date'] = df['date'].astype(str)


# In[41]:


df.head()


# In[42]:


df[['year', 'month', 'day']] = df['date'].str.split('-', expand = True)


# In[43]:


df.head()


# ## Q. 3) Remove the columns 'year' and 'month' from the dataframe.

# In[17]:


df = df.drop(df.columns[-2], axis = True)


# In[18]:


df.head()


# In[19]:


df = df.drop(df.columns[-2], axis = True)


# In[31]:


df.head()


# ## Q. 4) Show all the records where 'No. of Crimes' is 0. And, how many such records are there ?

# In[44]:


len(df[df.no_of_crimes == 0])


# ## Q. 5) What is the maximum & minimum 'average_price' per year in england ?

# In[46]:


df.year.unique()


# In[62]:


df.groupby(df.year).average_price.agg([np.max,np.min])


# ## Q. 6) What is the Maximum & Minimum No. of Crimes recorded per area ?

# In[50]:


df.head()


# In[61]:


df.groupby(df.area).no_of_crimes.agg([np.max,np.min])


# ## Q. 7) Show the total count of records of each area, where average price is less than 100000.

# In[60]:


df.area[df.average_price < 100000].value_counts()

