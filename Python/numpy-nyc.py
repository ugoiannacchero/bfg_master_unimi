#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np


# In[18]:


#genero da un file di testo (csv) un array, skippando l'header che nel caso di un array sarebbero valori nulli:

taxi = np.genfromtxt('nyc_taxis.csv', delimiter = ',', skip_header= True)


# In[19]:


taxi


# ## What is the mean speed of the car rides?

# In[40]:


# velocità = spazio / tempo -> (trip_dist / trip_length)

# Poi faccio la media, facendo .mean()

(taxi[:, 7] / (taxi[:, 8]/3600)).mean()


# In[22]:


import pandas as pd


# In[36]:


speed_df = pd.DataFrame(speed)


# In[37]:


speed_df.rename(columns={0:'speed'})


# ## Number of rides taken in febraury

# In[41]:


# Devo vedere quante volte nella colonna del mese (pickup_month) c'è febbraio (1):


# In[56]:


bbas = taxi[taxi[:,1] == 2,1]


# In[76]:


len(bbas) #numero di giri fatti in febbrario.


# In[79]:


bbas.shape # stesso metodo di prima


# ## Number of rides where tip was more than 50$

# In[85]:


hightip = taxi[taxi[:,12] > 50.00,12]


# In[90]:


len(hightip)


# ## Number of rides where drop was JFK

# In[ ]:


#in the column dropoff_location JFK is 2


# In[91]:


bbas2 = taxi[taxi[:, -9] == 2, -9]


# In[92]:


len(bbas2)


# In[ ]:




