#!/usr/bin/env python
# coding: utf-8

# ## ESERCIZI METODI STRINGHE:

# 🍰 Esercizio 1
# Assegnare una stringa "ciao mondo" ad una variabile "stringa" e utilizzare il metodo upper() per convertirla in maiuscolo in una nuova variabile.

# In[12]:


stringa = 'ciao mondo'


# In[14]:


stringa.upper()


# 🍰 Esercizio 2
# Assegnare una stringa "Benvenuti a Roma" ad una variabile "stringa" e utilizzare il metodo lower() per convertirla in minuscolo in una nuova variabile.

# In[15]:


Stringa = 'Benvenuti a Roma'


# In[16]:


Stringa.lower()


# 🍰 Esercizio 3
# Assegnare una stringa "Il meglio deve ancora venire" ad una variabile "stringa" e utilizzare il metodo split() per dividere la stringa in una lista di parole.

# In[17]:


Stringa = 'Il meglio deve ancora venire'


# In[19]:


Stringa.split(' ')


# 🍰 Esercizio 4
# Assegnare una stringa "Hello World" ad una variabile "stringa" e utilizzare il metodo replace() per sostituire "World" con "Python".

# In[20]:


stringa = 'Hello World'


# In[22]:


stringa.replace('World', 'Python')


# 🍰 Esercizio 5
# Assegnare una stringa " Ciao " ad una variabile "stringa" e utilizzare il metodo strip() per rimuovere gli spazi vuoti all'inizio e alla fine della stringa.

# In[23]:


stringa = ' Ciao '


# In[24]:


stringa.strip(' ')


# 🍰 Esercizio 6
# Assegnare una stringa "abcdefg" ad una variabile "stringa" ed estrarre i primi tre caratteri.

# In[25]:


stringa = 'abcdefg'


# In[29]:


stringa[0:3]


# 🍰 Esercizio 7
# Assegnare una stringa "Python" ad una variabile "stringa" e utilizzare il metodo startswith() per verificare se la stringa inizia con "Py".

# In[30]:


stringa = 'Python'


# In[31]:


stringa.startswith('Py')


# 🍰 Esercizio 8
# Assegnare una stringa "Ciao mondo" ad una variabile "stringa" e utilizzare il metodo count() per contare il numero di volte in cui la lettera "o" appare nella stringa.

# In[32]:


stringa = 'Ciao Mondo'


# In[33]:


stringa.count('o')


# 🍰 Esercizio 9
# Assegnare una stringa "Ciao mondo" ad una variabile "stringa". Mandare quindi a schermo gli ultimi 5 caratteri della stringa in maiuscolo, sostituendo il carattere "o" con "k".

# In[34]:


stringa = 'Ciao mondo'


# In[35]:


stringa.upper()


# In[42]:


stringa.upper().replace('O', 'K')[-5:]


# ## ESERCIZI FORMATTAZIONE STRINGHE

# 🍰 Esercizio 1
# Creare due variabili "nome" e "cognome" e concatenarle a schermo.

# In[47]:


nome = 'ugo'


# In[48]:


cognome = 'iannacchero'


# In[52]:


nome + ' ' + cognome


# 🍰 Esercizio 2
# Utilizzare la formattazione delle stringhe per ottenere "Il numero è: 42".

# In[53]:


numero = 42


# In[55]:


print('Il mio numero è {}'.format(numero))


# 🍰 Esercizio 3
# Utilizzare la formattazione delle stringhe per ottenere "Il numero binario di 42 è 0b101010". Per il binario utilizzare bin(numero)

# In[57]:


print('Il il numero binario di {} è {}'.format(numero, bin(numero)))


# 🍰 Esercizio 4
# Partendo dalla variabile "numero" uguale a 5, utilizzare le f-strings (interpolazione) per ottenere "Il quadrato di 5 è 25".

# In[58]:


numero = 5


# In[59]:


stringa = f"Il quadrato di {numero} è {numero ** 2}"


# In[60]:


stringa


# 🍰 Esercizio 5
# Partendo da "nome" e "cognome" utilizzare la formattazione strighe per ottenere "Il mio nome è {nome} ed il cognome è {cognome}". Come da esempio dovete fare riferimento al nome delle variabili e non alla posizione usata dentro format.

# In[63]:


stringa = f'Il mio nome è {nome} ed il mio cognome è {cognome}'.format(nome, cognome)


# In[64]:


stringa


# 🍰 Esercizio 6
# Facendo riferimento all'esercizio precedente ottenere il seguente risultato modificando i valori nel format(): "Il mio nome è LUCA ed il cognome è RoKKi"

# In[67]:


nome = "Luca"
cognome = "Rossi"


# In[68]:


stringa = "Il mio nome è {nome} ed il cognome è {cognome}".format(nome=nome.upper(), cognome=cognome.replace("s", "K"))


# In[69]:


stringa


# In[ ]:




