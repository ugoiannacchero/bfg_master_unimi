#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[5]:


rawdata = pd.read_csv('/home/student/masterbfg/netflix_titles.csv', sep = ',')
rawdata


# ## Task. 1) Is there any Duplicate Record in this dataset ? If yes, then remove the duplicate records.

# In[6]:


rawdata.shape


# In[7]:


rawdata.nunique()


# In[8]:


rawdata[rawdata.duplicated()] #per controllare se ci sono duplicati, in questo caso no.


# In[9]:


rawdata.drop_duplicates() #per rimuovere i duplicati


# In[10]:


rawdata.shape


# ## Task. 2) Is there any Null Value present in any column ? Show with Heat-map.

# In[11]:


rawdata.isnull().sum()


# In[12]:


df = rawdata.dropna()


# In[13]:


rawdata.shape


# In[14]:


df.shape


# In[15]:


import matplotlib.pyplot as plt


# In[16]:


import seaborn as sns


# In[17]:


sns.heatmap(rawdata.isnull())


# ## Q. 1) For 'Zodiac', what is the Show Id and Who is the Director of this show ?

# In[18]:


df[df['title'] == 'Zodiac'][['show_id','director']] 


# ## Q. 2) In which year the highest number of the TV Shows & Movies were released ? Show with Bar Graph.

# In[19]:


df['release_year'].value_counts()


# In[20]:


df.head()


# In[21]:


df['type'].count()


# In[22]:


df[(df['type'] == 'TV Show') | (df['type'] == 'Movie')][['release_year']].value_counts()


# In[23]:


df[df['type'] == 'Movie'][['release_year']].value_counts()


# In[24]:


df[df['type'] == 'TV Show'][['release_year']].value_counts()


# In[25]:


plt.hist(df[df['type'] == 'Movie'][['release_year']])
plt.hist(df[df['type'] == 'TV Show'][['release_year']])
plt.ylabel('n° movies / TV shows')
plt.xlabel('Year')
plt.show()


# ## Q. 3) How many Movies & TV Shows are in the dataset ? Show with Bar Graph.

# In[51]:


df[(df['type'] == 'Movie') | (df['type'] == 'TV Show')][['type']].value_counts()


# ## Q. 4) Show all the Movies that were released in year 2000.

# In[77]:


df[(df['type'] == 'Movie') & (df['release_year'] == 2000)][['title', 'release_year']]


# In[75]:


#AND & funziona con il loc.

df.loc[(df['type'] == 'Movie') & (df['release_year'] == 2000), ('title','release_year')].value_counts()


# ## Q. 5) Show only the Titles of all TV Shows that were released in India only.

# In[82]:


df.loc[(df['country'] == 'India') & (df['type'] == 'TV Show'), ('country', 'type', 'title')]


# ## Q. 6) Show Top 10 Directors, who gave the highest number of TV Shows & Movies to Netflix ?

# In[86]:


import numpy as np


# In[104]:


df['director'].value_counts().head(10)


# ## Q. 7) Show all the Records, where "Type is Movie and Listed_in is Comedies" or "Country is United Kingdom".

# In[117]:


df_movies = df[df['type'] == 'Movie']
df_movies.head(10)


# In[120]:


df_shows = df[df['type'] == 'TV Show']
df_shows.head(10)


# In[118]:


df_movies[(df_movies['listed_in'] == 'Comedies') | (df_movies['country'] == 'United Kingdom')][['type', 'title', 'listed_in']]


# ## Q. 8) In how many movies/shows, Jack Black was cast ?

# In[132]:


#str.contains mi cerca un valore all'interno

df_movies[df_movies['cast'].str.contains('Jack Black')]


# In[133]:


# count().sum()

df_movies[df_movies['cast'].str.contains('Jack Black')].count().sum()


# ## Q. 9) What are the different Ratings defined by Netflix ?

# In[138]:


df['rating'].unique()


# ## Q. 9.1) How many Movies got the 'TV-14' rating, in Canada ?

# In[153]:


df_movies[(df_movies['rating'].str.contains('TV-14')) & (df_movies['country'] == 'Canada')].count()


# ## Q. 9.2) How many TV Shows got the 'TV-MA' rating, after year 2018 ?

# In[165]:


df_shows[(df_shows['rating'].str.contains('TV-MA')) & (df_shows['release_year'] > 2018)].count()


# ## Q. 10) What is the maximum duration of a Movie/Show on Netflix ?

# In[185]:


df_movies.sort_values(by = 'duration', ascending = True).head(2)


# In[198]:


# COME AGGIUNGERE DUE NUOVE COLONNE "MINUTES" E "UNIT" SPLITTANDO LA COLONNA "DURATION".

df_movies[['Minutes', 'Unit']] = df_movies["duration"].str.split(' ', expand = True)


# In[206]:


#nel dataframe filtrato con i film, nella colonna Minutes, che però è una stringa quindi trasformo in integer (numero), e poi vedo il max(). 

df_movies.Minutes.astype(int).max()


# In[190]:


df_shows.sort_values(by = 'duration', ascending = False).head(2)


# In[208]:


df_shows[['Number', 'Season']] = df_shows['duration'].str.split(' ', expand=True)


# In[209]:


df_shows.head(2)


# In[211]:


#nel dataframe filtrato con gli shows, nella colonna Numero di stagioni, che però è una stringa quindi trasformo in integer (numero), e poi vedo il max(). 

df_shows.Number.astype(int).max()


# ## Q. 11) Which individual country has the Highest No. of TV Shows ?

# In[214]:


#value counts mi conta le righe della colonna (UNA SOLA NON DUE) che mi interessa.

df_shows['country'].value_counts()


# ## Q. 12) How can we sort the dataset by Year ?

# In[218]:


df.sort_values(by = 'release_year', ascending = True)


# ## Q. 13) Find all the instances where: type is 'Movie' and listed_in is 'Dramas' or type is 'TV Show' & listed_id is 'Kids' TV'.

# In[232]:


df[((df['type'] == 'Movie')) & ((df['listed_in'] == 'Dramas')) | ((df['type'] == 'TV show')) & ((df['listed_in'] == "Kids' TV"))]


# In[233]:


df[((df['type'].str.contains('Movie'))) & ((df['listed_in'].str.contains('Dramas'))) | ((df['type'].str.contains('TV show'))) & ((df['listed_in'].str.contains("Kids' TV")))]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




