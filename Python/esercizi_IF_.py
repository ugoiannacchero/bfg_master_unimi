#!/usr/bin/env python
# coding: utf-8

# 🍰 Esercizio 1
# Scrivere un programma che chiede all'utente di inserire un numero e stampa "Il numero è positivo" se il numero è maggiore di zero, altrimenti stampa il numero è negativo.

# In[5]:


x =  int(input('Inserisci un nuovo numero: '))

if x > 0:
    print('il numero è positivo')
else:
    print('il numero è negativo')


# 🍰 Esercizio 2
# Scrivere un programma che chiede all'utente di inserire due numeri e stampa "Il primo numero è maggiore" se il primo numero è maggiore del secondo, "Il secondo numero è maggiore" se il secondo numero è maggiore del primo, altrimenti stampa "I numeri sono uguali".

# In[6]:


x =  int(input('Inserisci un nuovo numero: '))
y =  int(input('Inserisci un nuovo numero: '))

if x > y:
    print('Il primo numero è maggiore')
elif y > x:
    print('Il secondo numero è maggiore')
else:
    print('I due numeri sono uguali')


# 🍰 Esercizio 3
# Scrivere un programma che chiede all'utente di inserire una stringa e stampa "La stringa è vuota" se la stringa è vuota, altrimenti stampa "La stringa non è vuota".

# In[1]:


stringa = str(input('Inserisci una stringa: '))

if stringa == None:
    print('La stringa è vuota')
else:
    print('La stringa non è vuota')


# 🍰 Esercizio 4
# Scrivere un programma che chiede all'utente di inserire un numero e stampa "Il numero è pari" se il numero è pari, altrimenti stampa "Il numero è dispari".

# In[3]:


numero = int(input('Inserisci un numero: '))

if numero % 2 == 0:
    print('Il numero è pari')
else:
    print('Il numero è dispari')


# 🍰 Esercizio 5
# Scrivere un programma che chiede all'utente di inserire una lettera e stampa "La lettera è una vocale" se la lettera è una vocale (a, e, i, o, u), altrimenti stampa "La lettera non è una vocale".

# In[5]:


lettera = str(input('Inserisci una lettera: '))

vocali = 'aeiou'

if lettera in 'aeiou':
    print ('La lettera è una vocale')
else:
    print('La lettera non è una vocale')


# 🍰 Esercizio 6
# Scrivere un programma che chiede all'utente di inserire un numero e stampa "Il numero è compreso tra 1 e 10" se il numero è compreso tra 1 e 10, altrimenti stampa "Il numero non è compreso tra 1 e 10".

# In[16]:


numero = int(input('Inserisci un numero intero: '))

if numero >=1 & numero <=10:
    print('Il numero è compreso tra 1 e 10')
else:
    print('Il numero non è compreso tra 1 e 10')



# 🍰 Esercizio 7
# Scrivere un programma che chieda all'utente di inserire un numero intero. Se il numero è maggiore di 10, stampare "Il numero è maggiore di 10". Se il numero è uguale a 10, stampare "Il numero è uguale a 10". Se il numero è minore di 10, stampare "Il numero è minore di 10".

# In[13]:


numero = int(input('Inserisci un numero intero: '))

if numero > 10:
    print('Il numero è maggiore di 10')
if numero == 10:
    print('Il numero è uguale a 10')
elif numero < 10:
    print('Il numero è minotre di 10')


# 🍰 Esercizio 8
# Scrivere un programma che chieda all'utente di inserire un carattere. Se il carattere è una vocale (a, e, i, o, u), stampare "Il carattere inserito è una vocale". Se il carattere è una consonante isAlpha(), stampare "Il carattere inserito è una consonante". Se il carattere non è una lettera, stampare "Il carattere inserito non è una lettera".

# In[17]:


carattere = input("Inserisci un carattere: ")

if carattere in "aeiou":
    print("Il carattere inserito è una vocale")
elif carattere.isalpha():
    print("Il carattere inserito è una consonante")
else:
    print("Il carattere inserito non è una lettera")


# 🍰 Esercizio 9 (difficile)
# Scrivere un programma che chieda all'utente di inserire tre numeri interi. Il programma deve verificare se i tre numeri formano un triangolo rettangolo. Se i tre numeri formano un triangolo rettangolo, stampare "I tre numeri formano un triangolo rettangolo". Altrimenti, stampare "I tre numeri non formano un triangolo rettangolo".

# In[19]:


a = int(input("Inserisci il primo lato: "))
b = int(input("Inserisci il secondo lato: "))
c = int(input("Inserisci il terzo lato: "))

if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("I tre numeri formano un triangolo rettangolo")
else:
    print("I tre numeri non formano un triangolo rettangolo")

