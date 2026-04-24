# Moduli 
# Un modulo è uno o più file esterni che contengono logica(Variabili, Funzioni, Classi, Oggetti etc...)
# Per poter utilizzare un modulo si deve importare nel progetto
# Possiamo utilizzare degli alias per importare un modulo
# import mio_modulo as alias
# Abbiamo tutta una serie di moduli build-in o moduli di terze parti
# dir(nomemodulo) restituisce una lista di funzioni del modulo 

import mio_modulo as m # importo gli elementi definiti nel mio modulo custom
import math # importa tutta la libreria math nel progetto
from math import sqrt, floor, ceil # importo solo le funzioni desiderate dal modulo match
import platform as p # importo un modulo per la lettura del device con cui sto collegando
import datetime as d # importo un modulo per la gestione delle date
import random as rand # importo un modulo per la gestione di valori casuali

print(m.miaVar)
print(m.miaFunc())

# Esempi del modulo math
num = 12.9
# print(math.floor(num))
# print(math.ceil(num))
print(sqrt(num))
print(floor(num))
print(ceil(num))

# print(dir(math))
if 'sqrt' in dir(math):
    print(math.sqrt(num))
    
# Esempio del modulo platform
print(p.architecture())
print(p.processor())
print(p.system())
print(p.python_version())
print(p.machine())

# Esempi del modulo datetime
print(d.datetime.now())
print(d.date.today())
print(d.datetime.now().strftime("%H:%M:%S"))
print(d.datetime.now().strftime("%d/%m/%Y"))
print(d.date.today().strftime('%d/%m'))


# Esempi del modulo random
numRand = rand.randint(1,13) # ritorna con un valore intero compreso tra 1 e 13 inclusi
floatRand = rand.random() # ritorna con un valore float compreso tra 0 e 1
cities = ['Roma', 'Milano', 'Torino', 'Palermo']
print(cities[rand.randint(0, len(cities)-1)])
print(rand.choice(cities))
print(numRand)
print(floatRand)


# PIP
# python -m ensurepip --default-pip se hai python e ti dice che non hai pip 
# pip --version -> Verifica la presenza di pip installata

from genuine.fake import GenuineFake as gf
print(gf.first_name())
print(gf.last_name())
print(gf.book())
print(gf.car_brand())
print(gf.drink())
print(gf.random_date())












