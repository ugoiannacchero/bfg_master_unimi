#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


# In[5]:


dailyweather = pd.read_parquet('/home/ugo/masterbfg/Kaggle/Weather/daily_weather.parquet', engine = 'fastparquet')


# In[6]:


dailyweather


# In[7]:


dailyweather.head()


# In[8]:


dailyweather.tail()


# In[11]:


dailyweather.shape


# In[14]:


dw_na = dailyweather.dropna()


# In[15]:


dw_na.shape


# ## Q. 1)  Find all the unique 'Wind Speed' values in the data.

# In[20]:


dw_na['avg_wind_speed_kmh'].unique()


# In[21]:


dw_na.nunique() # nunique() serve per controllare il numero di valori unici in ogni colonna del dataframe


# ## Q. 2) Find the number of times when the 'Season is exactly Summer'.

# In[31]:


dw_na.loc[dw_na['season'] == 'Summer'].sum


# In[60]:


dw_na[dw_na['season'] == 'Summer'][['season']].copy()


# ## Q. 3) Find the number of times when the 'Wind Speed was exactly 4 km/h'.

# In[58]:


dw_na[dw_na['avg_wind_speed_kmh'] == 4.0][['avg_wind_speed_kmh']].copy()


# ## Q. 4) Find out all the Null Values in the data.

# In[56]:


dailyweather.isnull().sum().sum() #due volte sum mi calcola il numero totale di null values di tutto il dataframe.


# In[62]:


dailyweather.isnull().sum() #calcola il numero di null values per ogni colonna


# In[52]:


dailyweather.notnull().sum()


# ## Q. 5) Rename the column name 'Weather' of the dataframe to 'Weather Condition'.

# In[63]:


dw_na.rename(columns = {'city_name':'city'}) #ricordarsi di aprire un dizionario {'nome colonna':'nomenuovo'}


# ## Q. 6) What is the mean 'precipitation_mm' ?

# In[67]:


dw_na['precipitation_mm'].mean()


# ## Q. 7) What is the Standard Deviation of 'Pressure'  in this data?

# In[73]:


import numpy as np


# In[74]:


dw_na['avg_sea_level_pres_hpa'].std()


# In[138]:


dw_na.groupby(['city_name'])[numeric_columns].mean()
dw_na.groupby(['city_name'])[numeric_columns].agg([np.std, np.mean])


# ## Q. 8) What is the Variance of 'snow_depth_mm' in this data ?

# In[91]:


dw_na['snow_depth_mm'].var()


# ## Q. 9) Find all instances when 'Budapest' was recorded.

# In[104]:


dw_na.loc[dw_na['city_name'] == 'Pago Pago'].copy()


# ## Q. 10) Find all instances when 'Wind Speed is above 24' and 'Average Temperature is 25'.

# In[120]:


dw_na.loc[(dw_na['avg_temp_c'] == 25) & (dw_na['avg_wind_speed_kmh'] > 24), 'city_name'].count()


# ## Q. 11) What is the Mean value of each column against each 'Season' ?

# In[130]:


numeric_columns = dw_na.select_dtypes(include=[np.number]).columns
dw_na.groupby(['season'])[numeric_columns].mean()


# In[136]:


dw_na.groupby(['season'])[numeric_columns].agg([np.mean,np.std, np.var])


# ## Q. 12) What is the Minimum & Maximum value of each column against each 'Season' ?

# In[150]:


numeric_columns = dw_na.select_dtypes(include=[np.number]).columns
dw_na.groupby(['season'])[numeric_columns].agg([np.min,np.max])


# ## Q. 13) Show all the Records where Season is Autumn.

# In[161]:


dw_na[dw_na['season'] == 'Autumn']


# ## Q. 14) Find all instances when 'season is summer' or 'wind spees above 40'.

# In[172]:


dw_na[(dw_na['season'] == 'Summer') | (dw_na['avg_wind_speed_kmh'] > 40)].copy()


# ## Q. 15) Find all instances when :
# ### A. 'Season is Winter' and 'precipitation is greater than 4.0'
# ### or
# ### B. 'wind speed is above 40'

# In[178]:


dw_na[((dw_na['season'] == 'Winter') & (dw_na['precipitation_mm'] == 4.0)) | (dw_na['avg_wind_speed_kmh'] > 40)]


# In[ ]:




