#!/usr/bin/env python
# coding: utf-8

# In[1]:


### Le funzioni


# Fatti la pasta
# 
# prendi la pentola
# 
# metti la pasta
# 
# metti il sugo
# 
# impiatta

# In[2]:


def fai_la_pasta():
    print('metti acqua')
    print('fai bollire')
    print('metti la pasta')


# In[3]:


fai_la_pasta() #in questo modo il codice diventa più corto e intuibile


# In[4]:


#Se abbiamo a cena un ospite che vuole i fusilli piuttosto che gli spaghetti, è necessario definire dei parametri.


# In[60]:


tipo_pasta = 'fusilli'


# In[61]:


def fai_la_pasta(tipo_pasta, metti_sugo):
    print('metti acqua')
    print('fai bollire')
    print('metti ' + tipo_pasta + ' come pasta')
    if metti_sugo:
        print('metti sugo')


# In[62]:


fai_la_pasta(tipo_pasta, True)


# Il parametro è la variabile generica che usiamo nella definizione della variabile, ad esempio il tipo di pasta.
# 
# Mentre l'argomento è il valore effettivo che andiamo a mettere.

# I parametri possono essere:
# 
# - arbitrary arguments
# - keyboard arguments
# - arbitrary keyword arguments

# I parametri di default:

# In[67]:


def fai_la_pasta(tipo_pasta = 'spaghetti'):
    print('metti acqua')
    print('fai bollire')
    print('metti ' + tipo_pasta + 'come pasta')


# In[68]:


fai_la_pasta()


# ESERCIZI

# Esercizio 1 Scrivere una funzione che accetti una lista di interi e restituisca una lista di tuple, dove ogni tupla contenga l'elemento e il suo indice nella lista originale. Ad esempio se la funzione viene chiamata con la lista [4,5,6,7] , dovrebbe restituire [(4,0),(5,1),(6,2),7,3)]

# In[92]:


def indice_elemento(lista):
    risultato=[]
    for i in range(len(lista)):
        risultato.append((lista[i],i))
    return risultato


# In[93]:


indice_elemento([4,5,6,7])


# Esercizio 2 Creare una funzione che accetti una lista di stringhe e restituisca un dizionario dove le chiavi sono le stringhe e i valori sono il numero di volte in cui ogni stringa appare nella lista. Ad esempio s ela funzione viene chiamata con la lista ['ciao', 'mondo', 'ciao', 'mondo', 'mondo'], la lista dovrebbe restituire ['ciao':2,'mondo':3]

# In[98]:


def conta_parole(parole):
    risultato ={}
    for parola in parole:
        if parola in risultato:
            risultato[parola]+=1
        else:
            risultato[parola]=1
    return risultato
            
print(conta_parole(['anna', 'edo', 'cristina', 'mario', 'anna', 'mario', 'cristina', 'mario']))


# Esercizio 3 Scegliere una funzione che restituisca una lista di interi e restituisca il numero di elementi poi presenti nella lista. Ad esempio, se la funzione viene chiamata con la lista [1,2,3,4,5] , dovrebbe restituire [2]

# In[103]:


def conta_pari(lista):
    contatore =0
    for numero in lista:
        if numero %2==0:
            contatore +=1
    return contatore

conta_pari([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22])


# Esercizio 4 Scrivere una funzione che accetti una stringa e un carattere di ricerca e restituisca il numero di volte in cui il carattere appare nella stringa. Ad esempio se la funzione viene chiamata con la stringa 'ciao' e il carattere 'o' dovrebbe restituire 1.

# In[106]:


def conta_carattere(stringa, carattere_da_cercare):
    contatore = 0
    for carattere in stringa:
        if carattere == carattere_da_cercare:
            contatore +=1
    return contatore

conta_carattere('meraviglioso','i')


# Esercizio 5 Scrivere una funziona che accetti una lista di interi e restituisca una lista di interi contenente solo i numeri divisibili per 3. Ad esempio, se la funzione viene chiamata con la lista [1,2,3,4,5,6,7,8,9,10] la lista dovrebbe restituire 3,6,9.

# In[109]:


def divisibili_per_3(lista):
    risultato = []
    for numero in lista:
        if numero % 3 == 0:
            risultato.append(numero)
    return risultato

divisibili_per_3([22,45,33,66,69,98,99,102,43,62])    

