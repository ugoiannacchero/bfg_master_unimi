#!/usr/bin/env python
# coding: utf-8

# In[1]:


if 5 < 10:
    print('5 è minore di 10')


# In[2]:


x = 5

if x < 10:
    print('x è minore di 10')


# Questi sono gli operatorti di comparazione
# 
# - '==' condizione di uguaglianza
# - '!=' condizione di diversità
# - '<'  condizione di minore
# - '>' condizione di maggiore
# - '<=' condizione di minore uguale
# - '>=' condizione di maggiore uguale

# In[5]:


x = 200

if x <= 10:
    print('x è minore uguale di 10')
else:
    print('x è maggiore di 10')


# In[13]:


x = int(input('Inserire un numero intero: '))

if x < 10:
    print('x è minore di 10')
elif x == 10:
    print('x è uguale a 10')
else:
    print('x è maggiore di 10')


# Gli operatori logici sono 'AND' e 'OR':
# - and
# - or
# - not

# In[24]:


x = int(input('Inserisci un primo numero intero: '))
y = int(input('Inserisci un secondo numero intero: '))

if x<= 10 and y <=20:
    print('x è minore uguale di 10 e y è minore uguale di 20')
elif x<=10:
    print('x è minore uguale di 10')
elif y<=20:
    print('y è minore uguale di 20')
else:
    print('x non è minore di 10 e y non è minore di 20')


# if nested:

# In[29]:


x = int(input('Inserisci un numero intero: '))

if x % 2 == 0:
    print('Il numero è pari')
    if x <= 10:
        print('Il numero è pari ed è minore uguale di 10')
else:
    print('Il numero è dispari, e non mi interessa se è minore o uguale di 10')


# In[ ]:




