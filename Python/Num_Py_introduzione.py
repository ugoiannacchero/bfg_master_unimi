#!/usr/bin/env python
# coding: utf-8

# ## Numpy (Numerical Python) intro:

# Numpy è una libreria di python creata per lavorare con gli array.
# 
# Gli array di base sono molto simili alle liste, ma ci danno delle potenzialità in più.
# 
# Numpy ci dà la possibilità di lavorare sempre con le liste, che qui sono chiamate array ma in maniera molto più veloce.
# 
# Numpy è la base per Pandas, Matplotlib, Scipy, ecc...

# In[1]:


import numpy as np


# In[2]:


array = np.array([1,2,3,4,5])


# In[3]:


print(array)


# In[4]:


lista = [1,2,3,4,5]


# In[5]:


print(lista)


# La differenza è che nelle liste, i valori sono separati dalla virgola. Mentre invece gli array no. E come detto precedentemente gli array sono molto più veloci nel calcolo.

# In[6]:


print(lista*5)


# In[7]:


print(array*5)


# Si può notare come le lista se moltiplicata per 5, duplica 5 volte i suoi valori.
# 
# Mentre invece gli array, permettono di moltiplicare i valori per 5.

# In[8]:


print(lista+5)


# In[ ]:


print(array*5)


# Questa è la vera differenza tra liste e array. Con le liste non possiamo effettuare le operazioni matematiche mentre con gli array si.

# Array ZERO DIMENSIONI: Contiene solo un valore

# In[ ]:


arr0D = np.array(1)


# In[ ]:


print(arr0D)


# Array UNA DIMENSIONE

# In[ ]:


arr1D = np.array([1,2,3,4,5,6])


# In[ ]:


print(arr1D)


# In[ ]:


arr1D.ndim #vedere la dimensione di un array


# Array DUE DIMENSIONI: è un [array che contiene [array]]

# In[ ]:


arr2D = np.array([[1,2,3],
                  [4,5,6]])


# In[ ]:


arr2D


# In[ ]:


arr2D.ndim #vedere la dimensione di un array


# Array TRE DIMENSIONI: è un [[[array che al suo interno contiene degli [array,che al suo interno contiene degli array]]]

# In[ ]:


arr3D = np.array([
                  [[1,2,3],[4,5,6]],
                  [[7,8,9],[10,11,12]]
                 ])


# In[ ]:


print(arr3D)


# In[ ]:


arr3D.ndim #vedere la dimensione di un array


# Creare in modo breve un array con n dimensioni:

# In[ ]:


arr5 = np.array([1,2,3], ndmin=5) # ndmin -> fai un array di 5 dimensioni


# In[ ]:


print(arr5)


# In[ ]:


arr5.ndim


# Creare velocemente un array con np.arange, in cui io gli dico da che numero partire, a che numero arrivare e quanti step fare.

# In[ ]:


arrArange = np.arange(5,50,5) #mi crei un array che parte da 5 arriva a 50 facendo salti di 5.


# In[ ]:


print(arrArange)


# In[ ]:


arrArange = np.arange(3,30) #mi crei un array che parte da 3 e arriva a 30. NO STEPS


# In[ ]:


print(arrArange)


# Creare un array di zeri

# In[ ]:


arrZeros = np.zeros(3) #crea un array con n zero.


# In[ ]:


print(arrZeros)


# In[ ]:


arrZeros = np.zeros((3,5,4)) # crea un array con un array con uno zero nella 1a dimensione (tre array (matrici)),
                             # cinque nella seconda dimensione, i 5 zero per colonna,
                             # quattro nella terza dimensione, i 4 zero per riga.


# In[ ]:


print(arrZeros)


# In[ ]:


arrOnes = np.ones((5,4,2)) # crea un array con 5 dimensioni (5 array),
                           # con 4 uno nella seconda dimensione, 4 uno per colonna
                           # 2 uno nella terza dimensione, 2 uno per riga.


# In[ ]:


print(arrOnes)


# ## Indicizzazione degli array:

# In[ ]:


arr1D = np.array([1,2,3,4,5])


# In[ ]:


arr1D[4]


# In[ ]:


arr2D = np.array([[1,2,3],
                  [4,5,6]])


# Vogliamo prendere il numero 3:

# In[ ]:


arr2D[0,2] # obbiettivo printare il 3:
           # prendo la 1 dimensione che è 0
           # prendo il il 3 all'interno della 1a dimensione che ha indice 2.


# In[ ]:


#Obiettivo prendere il 6:

arr2D[1,2]


# In[ ]:


#Obiettivo prendere il 2,4,5.

arr2D[0,1] 


# In[ ]:


arr2D[1,0]


# In[ ]:


arr2D[1,1]


# In[ ]:


arr3D = np.array([ [[1,2,3],[4,5,6]],
                  [[7,8,9],[10,11,12]]])


# In pratica, la 1a dimensione ce la da il numero di array (matrici presenti) in questo caso sono due. Quindi:

# Nella prima dimensione l'indice 0 è per [[1,2,3],[4,5,6]]
# Mentre nella 1a dimensione l'indice 1 è per [[7,8,9],[10,11,12]]

# Per quanto riguarda la seconda dimensione, l'indice 0 sta per [1,2,3] o [7,8,9] a seconda della 1a dimensione scelta.

#Infine per selezionare il 10 all'interno di [10,11,12] usiamo l'indice 0.

#Recapitolando: scelgo la prima dimensione che mi interessa (in questo caso sono due array (matrici con 0 / 1) e io prendo la seconda quindi 1.
# Scelgo la seconda dimensione selezionando [10,11,12] piuttosto che [7,8,9]. prendendo indice 1.
# Scelgo la terza dimensione selezionando solo il 10 all'interno di [10,11,12] selezionando 0.

# arr3D[1,1,0]


# In[ ]:


arr3D.ndim


# In[ ]:


#obbiettivo prendere il 10:


# In[ ]:


arr3D[1,1,0]


# ## Slicing degli array:

# In[ ]:


arr = np.array([1,2,3,4,5])


# In[ ]:


# Prendere il 3:
print(arr[2])

print(arr[-3])


# Lo slicing serve per prendere da un indice all'altro. Da un index all'altro.

# In[ ]:


arr[0:2] # dall'indice 0 incluso, all'indice 2 (non incluso)


# In[ ]:


arr[:] # dall'inizio fino alla fine


# In[ ]:


arr[:3] # dall'inizio fino all'indice 3


# In[ ]:


arr[2:] # dall'indice 2 fino alla fine


# In[ ]:


arr[-2:] # dall'indice -2 fino alla fine


# In[ ]:


array[-4:-2] # dall'indice -4 all'indice -2


# In[ ]:


arr1 = np.arange(11)


# In[ ]:


arr1


# In[ ]:


arr1[0:7:2] # da indice 0
            # a indice 7
            # mi salti ogni 2


# In[ ]:


arr1[::2] # dall'inizio alla fine, step di due.


# Slicing array 3d

# In[ ]:


arr_3d = np.array([[
                  [1,2,3],[4,5,6]],
                  [[7,8,9],[10,11,12],
                  ]])


# In[ ]:


arr_3d.ndim


# In[ ]:


#obiettivo selezione gli index degli array della seconda prima dimensione [7,8,9],[10,11,12]


arr_3d[1,0:,0:3]


# In[ ]:


#prendere 5,6,10 e 11

arr_3d [0:,1,1:]


# In[ ]:


arr_pari = np.array([
                    [[0,1,2,3,4],[4,5,6,7,8]],
                    [[7,8,9,10,11],[11,12,13,14,15]]
])


# In[ ]:


arr_pari.ndim


# In[ ]:


#voglio printare solo l'indice dei numeri pari di questo array 3d:

arr_pari[0:,0:,::2]

# 0: prendimi tutti gli array della 1a dimensione
# 0: prendimi tutti gli array della 2nda dimensione
# ::2 prendimi tutti gli indici della terza dimensione, facendo step di 2.


# ## Tipi di dati:

# Le variabili possono conservare dati di diverso tipo, e dati di diverso tipo possono fare cose diverse.
# 
# Python ha i seguenti tipi di dati, che di default vengono classificati in:
# 
# - Text Type:	    str
#   
# - Numeric Types:	int, float, complex
# 
# - Sequence Types:	list, tuple, range
# 
# - Mapping Type:	    dict
# 
# - Set Types:	    set, frozenset
# 
# - Boolean Type:   	bool
# 
# - Binary Types: 	bytes, bytearray, memoryview
# 
# - None Type:    	NoneType

# Tipo di array-protocol per le stringhe (vedi Il protocollo dell'interfaccia dell'array)
# Il primo carattere specifica il tipo di dati e i caratteri restanti specificano il numero di byte per elemento, ad eccezione di Unicode, dove viene interpretato come il numero di caratteri. La dimensione dell'elemento deve corrispondere a un tipo di dati esistente, o verrà generato un errore. I tipi supportati sono:
# 
# - boolean '?'
# 
# - (signed) byte 'b'
# 
# - unsigned byte 'B'
# 
# - (signed) integer 'i'
# 
# - unsigned integer 'u'
# 
# - floating-point 'f'
# 
# - complex-floating point 'c'
# 
# - timedelta 'm'
# 
# - datetime 'M'
# 
# - (Python) objects 'O'
# 
# - zero-terminated bytes (not recommended) 'S', 'a'
# 
# - Unicode string 'U'
# 
# - raw data (void) 'V'
# 
# 

# In[ ]:


array1 = np.array([1,2,3,4,5])


# In[ ]:


array1.dtype


# In[ ]:


array2 = np.array([ 'a', 'b', 'c'])


# In[ ]:


array2.dtype


# In[ ]:


array3 = np.array([1.1,2.2,3.3])


# In[ ]:


array3.dtype


# In[ ]:


array4 = np.array([True, False, True])


# In[ ]:


array4.dtype


# In[ ]:


array = np.array([1,2,3,4,5], dtype = 'S')


# In[ ]:


array.dtype


# In[ ]:


array


# In[ ]:


array = array.astype('i')


# In[ ]:


print(array+5)


# ## wiew e copy

# A livello teorico wiew e copy servono per fare la stessa cosa, ovvero copiare il contenuto di un array in un altro array.

# La differenza sostanziale è che mentre copy fa una copia effettiva dell'array.
# 
# View è un pò una copia fittizia, quando modifico la copia io modifico la mia copia e modifico anche l'originale.

# In[ ]:


array = np.array([1,2,3])


# In[ ]:


array_copy = array.copy()


# In[ ]:


array


# In[ ]:


array_copy


# Esempio copy:
# 
# Se io modifico il mio array originale sostituendo l'1 all'indice 0 con 10, vedrò che sul mio array originale avrò 10, mentre sull'array copia no.

# In[ ]:


array[0] = 10


# In[ ]:


array


# In[ ]:


array_copy


# Esempio view:
# 
# Dopo aver fatto view, se modifico l'array anche l'array view verrà modificato.

# In[ ]:


array_view = array.view()


# In[ ]:


array


# In[ ]:


array_view


# In[ ]:


array[0] = 222


# In[ ]:


array


# In[ ]:


array_view


# Controllare la base degli array, il proprietario.
# 
# Quando con base controllo se l'array è uguale a None.
# 
# Devo ricordarmi che se esce True noi sappiamo che l'array è proprietario dei dati, diversamente no.

# In[ ]:


array.base == None


# In[ ]:


array_view == None


# ## Shape e Reshape:

# Con shape vediamo la forma dell'array, quanti array ci sono nella prima dimensione e nella seconda dimensione per esempio.
# 
# Con reshape cambiamo la forma dell'array, ad esempio possiamo trasformare un array 2d in 1d o viceversa.
# E' importante usare delle combinazioni che possono essere uguali alla lunghezza dell'array corrispettiva.
# Se l'array ha 12 elementi, potrò fare 4x3 o 3x4 o 2x6 o 6x2.

# In[ ]:


array = np.array([1,2,3,4,5,6])


# In[ ]:


array.shape


# In[ ]:


array = np.array([[1,2,3],
                  [4,5,6]])


# In[ ]:


array.shape


# In[ ]:


array.reshape(-1) #fa tornare l'array da due dimensioni a una dimensione.


# In[ ]:


array = np.arange(1,13)


# In[ ]:


array


# In[ ]:


array.reshape(4,3) #mi crea un array bidimensionale. In cui la 1 dimensione è 4 mentre la seconda è 3.


# In[ ]:


array = np.arange (1,19)


# In[ ]:


array


# In[ ]:


array.reshape(2,3,3) # I 18 elementi li ridispongo in questo modo:
                     # 2 array nella 1a dimensione
                     # 3 array nella 2nda dimensione
                     # 3 elementi per ciascuna ultima dimensione

# 2 x 3 x 3 = 18


# In[ ]:


array.reshape(3,1,6)

# 3 x 1 x 6 = 18


# In[ ]:


array.reshape(1,18,1)

#1 x 18 x 1


# In[ ]:


array.reshape(9,1,2)

#9 x 1 x 2 = 18


# Se avessimo una dimensione sconosciuta, non sappiamo cosa mettere in una dimensione. Possiamo usare il -1 per dire a numpy di calcolare in automatico quella dimensione.

# In[ ]:


array = np.arange(1,25)


# In[ ]:


array


# In[ ]:


array.reshape(6,-1,4) # qui numpy ha calcolato la seconda dimensione ponendo 4

# 6 x -1 x 4 = 24

# -1 = 4


# Per spianare un array abbiamo due alternative:
# 
# - usare flatten
# 
# - reshape(-1)

# In[ ]:


array.flatten()


# In[ ]:


array.reshape(-1)


# ## Iterare gli array:

# In[ ]:


array = np.arange(1,7)


# In[ ]:


for x in array:  #per ogni elemento di array mi mandi a schermo ogni singolo elemento
    print(x)


# Fin qui tutto semplice ma le grane iniziano quando noi vogliamo utilizzare un ciclo for con array di più dimensioni.

# In[ ]:


array = array.reshape(2,3,1)
array


# In[ ]:


for x in array: # 1a dimensione
    for y in x: # 2a dimensione
        for z in y: # 3a dimensione
            print(z)


# Ottengo tutto quello che printavo con una dimensione.

# Se volessimo fare tutto in una volta sola, possiammo usare nditer:

# In[ ]:


for x in np.nditer(array):
    print (x)


# Questo metodo di dà tante possibilità, come cambiare il tipo di dato in corsa.

# In[ ]:


for x in np.nditer(array,
                   flags=['buffered'], # serve per utilizzare op_dtypes, va imparato così com'è
                   op_dtypes ='S'):  # fa diventare il tipo di dato da int a 'S' (stringa)
                                     # op_dtypes ci dice che il tipo di output non è più un intero ma una stringa 
    print (x)


# Proviamo a prendere i numeri dispari del primo array monodimensionale in un array bidimensionale:

# In[ ]:


array = np.arange(1,11)


# In[ ]:


array = array.reshape(2,5)


# In[ ]:


array


# In[ ]:


for x in np.nditer(array[0,::2]):
    print(x)


# Utilizzando np.ndenumerate possiamo vedere gli index, con il corrispettivo elemento

# In[ ]:


for idx, x in np.ndenumerate(array):
    print(idx,x)


# ## Unire gli array:
# 
# - concatenate array 1D e 2D
# 
# - stack

# In[ ]:


arr1 = np.arange(1,5)
arr2 = np.arange(5,10)


# In[ ]:


arr1


# In[ ]:


arr2


# Con np.concatenate prende gli elementi dell'array 1 e dell'array 2 e le concatena:

# In[ ]:


arr3 = np.concatenate((arr1,arr2))


# In[ ]:


arr3


# Ciò può essere fatto anche con gli array 2d:

# In[ ]:


array2d1 = np.array([
                    [1,2,3],
                    [4,5,6]
                    ])


# In[ ]:


array2d2 = np.array([
                    [7,8,9],
                    [10,11,12]
                    ])


# In[ ]:


array2d1


# In[ ]:


array2d2


# In[ ]:


array2d3 = np.concatenate((array2d2,array2d1))


# In[ ]:


array2d3


# Possiamo anche specificare gli assi:

# In[ ]:


array2d3 = np.concatenate((array2d2,array2d1), axis = 1)


# In[ ]:


array2d3


# La funzione stack:
# 
# - stack
# 
# - hstack
# 
# - vstack
# 
# - dstack

# In[ ]:


arrayA = np.array([1,2,3])


# In[ ]:


arrayB = np.array([4,5,6])


# In[ ]:


arrayC = np.array([7,8,9])


# In[ ]:


np.concatenate((arrayA,arrayB,arrayC), axis = 0)


# Con stack creiamo a stackare un array, creando una dimensione aggiuntiva.

# In[ ]:


np.stack((arrayA,arrayB,arrayC), axis = 0) #stackato gli elementi in base all'asse 0, ovvero l'index del primo array 1D.


# In[ ]:


np.stack((arrayA,arrayB,arrayC), axis =1) #stackato gli elementi in base all'asse 1, ovvero l'index 0 di ogni array 1D.


# In[ ]:


np.hstack((arrayA,arrayB,arrayC)) #lo fa horizontal


# In[ ]:


np.vstack((arrayA,arrayB,arrayC)) #lo fa vertical


# In[ ]:


np.dstack((arrayA,arrayB,arrayC)) #stacka gli eementi in base all'index 0 di ogni array 1D.


# ## Dividere un array

# Per gli assi 1D e 2D:
# 
# - array_split
# - split

# In[ ]:


arr = np.arange (1,7)


# In[ ]:


arr


# In[ ]:


np.split(arr,2)


# In[ ]:


np.split(arr,3)


# Con split non possiamo dividere gli array in qualcosa che non è una divisione eguale.
# 
# Con split gli array saranno sempre divisi in maniera uguale.

# In[ ]:


np.split(arr,4)


# Questo problema può essere risolto con array_split(), perchè nel momento in cui la divisione non è uguale lui riesce a dividere anche in array ineguali.

# In[ ]:


arr = np.array_split(arr,4)

arr


# Se volessimoa accederea gli array interni:

# In[ ]:


arr[2]


# In[ ]:


arr[0]


# In[ ]:


Per quanto riguarda gli array 2D:


# In[ ]:


arr2D = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]
                 ])


# In[ ]:


arr2D


# In[ ]:


np.array_split(arr2D,2, axis = 0) # con axis = 0 gli array iniziano a partire dal valore corrispondentea all'index 0


# In[ ]:


np.array_split(arr2D,2, axis = 1) #con axis = 1 gli arrai iniziano con gli indici a partire dagli indici del primo array 1D


# In[ ]:


arr = np.array([[[1,2,3],[4,5,6,]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]])


# In[ ]:


arr.ndim


# In[ ]:


print(arr)


# In[ ]:


np.vsplit(arr,3) #splitto sull'asse verticale


# In[ ]:


np.hsplit(arr,2) #splitto sull'asse orizzontale


# In[ ]:


np.dsplit(arr,3) 


# ## Come cercare, ordinare e filtrare in un array: 
# 
# - np.where
# - sort
# - filter

# In[ ]:


arr = np.array([1,2,2,3,3,3,4,5,6,6,7,3,4,5,9])


# In[ ]:


arr


# - np.where()

# In[ ]:


np.where(arr == 3)


# In[ ]:


np.where(arr%2 == 0)


# - np.sort()

# In[ ]:


np.sort(arr)


# In[ ]:


arr2 = np.array([
                [3,2,1,4],
                [5,3,5,3],
                [1,0,4,9]
                ])


# In[ ]:


arr2


# In[ ]:


np.sort(arr2)


# - np.filter()

# Creo un filtro per conoscere se i gli elementi all'interno dell'array sono numeri pari:

# In[ ]:


filtro = []


# In[ ]:


for x in arr:
    if x % 2 ==0:
        filtro.append(True)
    else:
        filtro.append(False)


# In[ ]:


filtro


# Verifico che è vero:

# In[ ]:


arrayfiltrato = arr[filtro]

arrayfiltrato


# In maniera più semplice avrei potuto fare:

# In[ ]:


filtro = arr % 2 == 0


# In[ ]:


arr[filtro]


# ## La classe random

# Come generare array con numeri casuali:

# In[ ]:


from numpy import random


# Creare un numero intero compreso tra 0 e 100:
# - random.randint()

# In[ ]:


x = random.randint(100)

x


# Creare un numero compreso tra 0 e 1:
# - random.rand() -> è automaticamente tra 0 e 1, specificando un numero dici quanti numeri compresi tra 0 e 1 mettere nell'array

# In[ ]:


y = random.rand()

y


# In[ ]:


random.rand(4)


# In[ ]:


random.rand(8)


# In[ ]:


random.rand(1,3,9)


# Usiamo queste funzionalità per creare array di n dimensioni con numeri random:

# Per scegliere quante dimensioni in size basta inserire il numero:
# - per 1D solo un numero size = (5)
# - per 2D due numeri size = (3,2)
# - per 3D tre numeri size = (3,2,2)

# In[ ]:


arr = random.randint(1000,      #elementi compresi tra 0 e 100
                     size=(5)) #array di 15 valori


# In[ ]:


arr


# In[ ]:


arr2D = random.randint(100,
                       size = (2,3))


# In[ ]:


arr2D


# In[ ]:


arr3D = random.randint(290,
                       size = (2,2,3))


# In[ ]:


arr3D


# In[ ]:


arr = np.array([1,2,3,4,5,6])


# In[ ]:


random.choice(arr) # sceglie un numero a caso compreso nell'array


# In[ ]:


random.choice(arr) # ogni volta sarà diverso


# In[ ]:


arrchoice = random.choice(arr, size = (5,3,3)) #crea un array tridimensionali, con una size ben definita.


# In[ ]:


arrchoice


# Data distribution

# In[ ]:


values = np.array([10,20,30,40,50])


# In[ ]:


values


# In[ ]:


probability = np.array([0.1,0.2,0.2,0.3,0.2])


# In[ ]:


arrchoice = random.choice(values, p = probability, size = (20))


# In[ ]:


arrchoice


# Shuffle agisce sull'array, invertendo i valori senza bisogno di assegnarlo ad un array.

# In[ ]:


random.shuffle(values)


# In[ ]:


values


# Permutation invece non agisce sull'array, in quanto deve essere assegnato ad un nuovo array

# In[ ]:


values_permutation = random.permutation(values)


# In[ ]:


values_permutation


# In conclusione di base, permutation() e shuffle() fanno la stessa cosa, ma in modo diverso.

# ## ufunc() - Funzioni universali:
# 
# Le funzioni universali ci permettono di effettuare funzioni aritmetiche sugli np.array

# Per esempio controlliamo il type di una ufunc come add:

# In[ ]:


type(np.add)


# Controlliamo il type di concatenate che non è una ufunc:

# In[ ]:


type(np.concatenate)


# Provo a creare una mia ufunc()

# In[ ]:


def addcinque(x):
    return x +5


# In[ ]:


addcinque = np.frompyfunc(addcinque,1,1) #registro la funzione


# In[ ]:


arr = np.array([1,2,6,7,3,2,3,0])


# In[ ]:


addcinque(arr)


# Queste sono alcuen ufunc() che abbiamo a disposizione in numpy:

# In[ ]:


arr1 = np.array([1,2,3,4,5,6])
arr2 = np.array([7,8,9,10,11,12])


# Addizionare con np.add()

# In[ ]:


arr = np.add(arr1,arr2)


# Sottrarre con np.subtract()

# In[ ]:


np.subtract(arr1,arr2)


# Moltiplicare con np.multiply()

# In[ ]:


np.multiply(arr1,arr2)


# Dividere con np.divide()

# In[ ]:


np.divide(arr1,arr2)


# Elevare alla potenza con np.power()

# In[ ]:


np.power(arr1,arr2)


# Resto della divisione con np.remainder()

# In[ ]:


np.remainder(arr1,arr2)


# Troncare il decimale con np.trunc()

# In[ ]:


np.trunc([2.2323, 4.9329])


# Togliere le virgole con np.fix()

# In[ ]:


np.fix([4.231,7.32])


# Arrotondare con np.around()

# In[ ]:


np.around([5.213,8.131])


# FINE

# In[ ]:




