#!/usr/bin/env python
# coding: utf-8

# In[109]:


import pandas as pd
import numpy as np


# In[110]:


df_raw = pd.read_csv('Kaggle/project7.csv', sep = ',')


# In[111]:


df_raw.head()


# Q. 1) What are all different subjects for which Udemy is offering courses ?courses ?

# In[112]:


df_raw.subject.value_counts()


# In[ ]:





# Q. 2) Which subject has the maximum number of courses.

# In[113]:


df_raw.subject.max()


# In[114]:


df_raw.subject.min()


# Q. 3) Show all the courses which are Free of Cost.

# In[115]:


df_raw[df_raw.price == 'Free'][['course_title', 'price']].value_counts()


# In[ ]:





# Q. 4) Show all the courses which are Paid.

# In[116]:


df_raw[df_raw.price != 'Free'][['course_title','price']].value_counts()


# In[ ]:





# Q. 5) Which are Top Selling Courses ?

# In[117]:


df_raw.sort_values('num_subscribers', ascending = False).head(10)


# In[ ]:





# Q. 6) Which are Least Selling Courses ?

# In[118]:


df_raw.sort_values('num_subscribers', ascending = True).head(19)


# In[119]:


df_raw.price.value_counts()


# In[120]:


df_raw[df_raw.price == 'Free'][['course_title','price']]


# In[121]:


df_raw.price.head()


# In[ ]:





# Q. 7) Show all courses of Graphic Design where the price is below 100 ?

# In[129]:


df_raw.value_counts()


# In[131]:


df_raw.price.value_counts()


# In[132]:


df_price = df_raw[df_raw.price != 'Free']


# In[135]:


df_price.price = df_price.price.astype(int)


# In[136]:


df_price.head()


# In[138]:


df_price_below_100 = df_price[(df_price.subject == 'Graphic Design') & (df_price.price < 100)].head()


# In[140]:


df_price_below_100.sort_values('price')


# Q. 8) List out all the courses that are related to 'Python'.

# In[146]:


df_raw[df_raw.course_title.str.contains('Python')][['course_title','subject']]


# Q. 9) What are courses that were published in the year 2015 ?

# In[147]:


df_raw.head()


# In[150]:


df_raw['published_timestamp'] = pd.to_datetime(df_raw.published_timestamp)


# In[154]:


df_raw.published_timestamp.dtype


# In[155]:


df_raw.published_timestamp.head()


# In[159]:


df_raw['Year'] = df_raw['published_timestamp'].dt.year


# In[160]:


df_raw.head()


# In[162]:


df_raw[df_raw.Year == 2015][['subject', 'course_title', 'Year']]


# Q. 10) What is the Max. Number of Subscribers for Each Level of courses ?

# In[171]:


df_raw.groupby('level')['num_subscribers'].max()

