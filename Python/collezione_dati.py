#!/usr/bin/env python
# coding: utf-8

# ## Collezione di dati:
# 
# - list  x = []
# - tuple x = ()
# - set 
# - dictionary x = {}
# 
# Tutto ciò che è nelle parentesi sono più valori racchiusi in una variabile.
# 
# Per ogni collezione diversa, cambiano delle proprietà. Le liste hanno proprietà diverse dalle Tuple e così dai Dictionary.
# 
# Una collezione è ordinata quando ha un ordine predefinito, e l'aggiunta di qualcosa non va a variare l'ordine.

# In[3]:


lista_città = ['Milano', 'Napoli', 'Bologna', 'Roma']


# In[4]:


lista_città[0]


# Gli indici sono dei elementi ordinati, ordinato e indicizzato vanno di pari passo.

# Modificabile e Immutabile vanno anche di pari passo anche se hanno significato contrario.
# 
# Una lista è modificabile perchè posso aggiungere un elemento alla lista, così come possiamo rimuoverlo.
# 
# Al contratio una collezione di dati immutabile è una collezione in cui non possiamo modificare, aggiungere, rimuovere elementi.
# 
# Poi potremmo anche duplicare gli elementi.

# - Le *Liste* sono collezioni di dati ordinati, modificabili e permettono duplicati.
# 
# - Le *Tuple* sono collezioni di dati ordinati ma immutabili, tuttavia permettono duplicati.
# 
# 
# 
# - I *Set* sono collezioni non ordinate, e perciò non sono indicizzate. Non permettono i duplicati.
# 
# - I *Dizionari* sono collezioni di dati ordinate e modificabili, ma non permettono duplicati.

# ### LISTE

# In[5]:


città = ['milano', 'roma', 'napoli']


# In[6]:


y = ['milano', True, 100]


# ### Come utilizzare:
# 
# - len()
# - type()
# - list()

# In[7]:


type(città)


# In[8]:


type(y)


# In[9]:


len(città)


# In[10]:


len(y)


# In[11]:


list(città)


# In[12]:


list(y)


# In[13]:


città[1]


# In[14]:


y[2]


# In[15]:


città[1:2]


# In[16]:


città[:2]


# In[17]:


città[2:3]


# Rinominare un elemento dall'indice:

# In[18]:


città[2] = 'Brescia'


# In[19]:


città


# Aggiungere un elemento alla lista:
# 
# - append() per inserire alla fine della lista
# - insert() per inserire in una posizione della lista senza rimuovere quella presente

# In[20]:


città.append('Lamezia Terme')


# In[21]:


città


# In[22]:


città.insert(1, 'Genova')


# In[23]:


città


# Estendere la lista, tramire un'altra lista:
# 
# - extend()

# In[24]:


città.extend(y)


# In[34]:


città


# In[26]:


y


# In[31]:


for i in range(len(città)):
    print(città[i])


# In[32]:


i=0

while i < len(città):
    print(città[i])
    i +=1


# Modificare l'ordine di una lista:
# 
# - asc
# - desc
# - reverse

# In[36]:


città


# In[37]:


città[-2] = 'Modena'


# In[38]:


città


# In[40]:


città[-1] = 'Reggio Calabria'


# Ordinare la lista con:
# 
# - sort()

# In[41]:


città.sort()


# In[42]:


città


# In[44]:


città.sort(reverse=True)


# In[45]:


città


# Copiare la lista con:
# 
# - copy()

# In[49]:


città2 = città.copy()


# In[50]:


città2


# In[51]:


città


# ### Esercizi 'Collezioni Dati':

# Esercizio 1 Creare una lista di numeri interi e stampare solo gli elementi che sono divisibili per 3.

# In[59]:


lista = [1,2,3,4,5,6,7,8,9,10]


# In[60]:


for numero in lista:
    if numero % 3 == 0:
        print(numero)


# Esercizio 2 Creare una tupla di stringhe e stampare solo le stringhe di lunghezza pari.

# In[64]:


stringhe = ('marco', 'giovanni', 'silvestro', 'davide', 'anna')


# In[65]:


for parola in stringhe:
    if len(parola) %2 ==0:
        print(parola)


# Esercizio 3 Creare un set e una lista di numeri interi. Stampare solo i numeri che sono presenti sia nel set che nella lista.

# In[66]:


set = {1,2,3,4,5,6,10,20,30}
lista = [10,20,30,40,50,60,1,2,3]


# In[67]:


for numero in lista:
    if numero in set:
        print(numero)


# Esercizio 4 Creare un dizionario in cui le chiavi sono stringhe e i valori sono numeri interi. Stampare solo le coppie chiave-valore il cui valore è maggiore di 5.

# In[70]:


dict = {'sport' : 4,
        'maschi' : 8,
        'femmine': 4,
        'alunni' :9}

for chiave,valore in dict.items(): # .items() ci restituisce staccati chiave e valore
    if valore > 5:
        print(chiave,valore)


# Esercizio 5 Creare una lista di tuple, in cui ogni tupla contiene due stringhe. Stampare le tuple in cui la prima stringa inizia con la lettera 'a'.

# In[71]:


lista = [('barba','baffi'), ('mullet','melone'), ('astice', 'gambero')]


# In[76]:


for tupla in lista:
    if tupla[0][0] == 'a':
        print(tupla)


# Esercizio 6 Creare un set_di_tuple in cui ogni tupla contiene due numeri interi. Stampare le tuple in cui la somma dei due numeri è un numero pari.

# In[77]:


set = {(1,2),(6,8),(3,4),(5,6)}


# In[78]:


for tupla in set:
    if (tupla[0] + tupla[1]) % 2 == 0:
        print(tupla)

