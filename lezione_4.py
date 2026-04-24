# - Tuple: Collezioni di dati ORDINATE, IMMUTABILI e permettono duplicati.
# -> v = ('Roma', 'Milano', 'Napoli')
# tuple() | type() | len() | count(val)
# Accedere ad elementi di una tupla tramite un indice
# t[i] | t[i:i] | t[:i] | t[i:] | t[-i:-i]
# NON è possibile modificare elementi di una tupla tramite un indice
# Unire due o piu tuple con + (concatenazione)
# Copiare una tupla: nt = tuple(t)
# Possibile fare l'unpack di una tupla (estrarre dati da una tupla in variabili separate)
# Iterare Tupla con For | While
# for ele in list:
#    istruzioni


ta = ('Roma', 'Milano', 'Napoli') 
print(ta , type(ta))
ta = tuple(('Roma', 'Milano', 'Napoli', 'Roma'))
print(ta , type(ta), len(ta), ta.count('Roma'))

# Per modificare una tupla (NON SI FA) è necessario convertirla in una lista, modificarla e poi riconvertirla in tupla.
l = list(ta)
l.append('Torino')
t = tuple(l)
print(t, type(t), len(t), t.count('Roma'))

print(t[1]) # indexing
print(t[1:3]) # slicing

bigt = ta + t
print(ta)
print(t)
print(bigt)

# Copiare una tupla nt = tuple(t)
newt = tuple(bigt)
print(newt)

# Unpack di una tupla
t = ('Roma', 'Milano', 'Napoli')
t1 = t[0]
t1, t2 = t[0], t[1]
(c1, c2, c3) = t

print(c1)
print(c2)
print(c3)

# Iterare una tupla
i = 0
while i < len(t):
    print(t[i])
    i += 1

print("--------------------------")

for ele in t: 
    print(ele)
    
    
    
# Crea una tupla chiamata persona contenente le seguenti informazioni:
# nome, cognome, età, città
# Stampa l'intera tupla
# Stampa separatamente ciascun elemento della tupla(Uno per riga)
# inserendo una etichetta chiara (Nome: , Cognome: ...)
# verifica se l'età è maggiore o uguale a 18 e stampa un messaggio 
# adeguato (La persona nome cognome è maggiorenne oppure minorenne)

persona = ('Linda', 'Ferrara', 19, 'Roma')
print(persona)
print("Nome:", persona[0])
print("Cognome:", persona[1])
print("Età:", persona[2])
print("Città:", persona[3])

if persona[2] >= 18:
    print(f"La persona {persona[0]} {persona[1]} è maggiorenne.")
else:
    print(f"La persona {persona[0]} {persona[1]} è minorenne.")

    
    
    
    
    
    