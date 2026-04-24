# - Set: Collezioni di dati NON ORDINATE e per questo non indicizzabili, 
#        non modificabili e non permettono duplicati indicati da {}
# -> v = {'Roma', 'Milano', 'Napoli'}
# set() | type() | len()
# Non è possibile accedere e/o modificare elementi di un set tramite un indice
# è possibile aggiungere elementi ad un set tramite add('val') | update(newSet)
# è possibile rimuovere elementi da un set 
# tramite remove(val) | discard(val) | pop() | clear()
# posso copiare un set ns = s.copy() | ns = set(s)
# Unire due o piu set con union() | update()
# Creare un nuovo set con tutti gli elementi di un set uniti ma senza duplicati con union()
# possibile unire due o più set con intersection()
# Creare un nuovo setcin tutti i dati comuni presenti nei set (inner join)
# è possibile unire due o più set con difference()
# Creare un nuovo set con tutti i dati presenti nel set principale (left join) ma non presenti negli altri set
# è possibile unire due o più set con symmetric_difference()
# Creare un nuovo set con tutti i dati presenti nei set ma non comuni a tutti i set (outer join)
# Iterare Set con For | While


s1 = {'Roma', 'Milano', 'Torino', 'Roma'}
s2 = set(('Napoli', 'Milano', 'Firenze', 'Roma')) 
print(s1, type(s1))
print(s2, type(s2))
print(len(s1))

# s1.add('Firenze')
# s1.remove('Milano')
# s1.pop()

s_union = s1.union(s2) 
print("Set union: ", s_union) # {'Roma', 'Milano', 'Torino', 'Napoli', 'Firenze'}
s_intersection = s1.intersection(s2)
print("Set intersection: ", s_intersection) # {'Roma', 'Milano'}
s_difference = s1.difference(s2)
print("Set difference: ", s_difference) # {'Torino'}
s_symmetric_difference = s1.symmetric_difference(s2)
print("Set symmetric difference: ", s_symmetric_difference) # {'Torino', 'Napoli', 'Firenze'}

print("--------------------------")

# - Dictonary: Collezioni di dati ORDINATE e modificabili ma non permettono duplicati (insieme di chiave : valore)
# I Dizionari sono insiemi di coppie chiave/valore, sono l'equivalente degli oggetti in altri linguaggi di programmazione, e sono indicati da {}
# -> v = {"nome": "Mario", "cognome": "Rossi", "citta": "Roma"}
# dict() | type() | len()
# Accedere ad elementi di un dizionario tramite la chiave
# è possibile modificare elementi di un dizionario tramite la chiave
# d[key] = 'nuovo valore' | d.update({key: 'nuovo valore'})
# è possibile rimuovere degli elementi da un dizionario tramite la chiave
# d.pop(key) | del d[key] | d.clear()
# è possibile aggiungere nuovi elementi ad un dizionario tramite una nuova chiave
# d[new_key] = 'valore' | d.update({new_key: 'valore'})
# è possibile copiare un dizionario nd = d.copy() | nd = dict(d)
# è possibile iterare con il ciclo for e ciclo while un dizionario, iterando sulle chiavi, sui valori o su entrambe le cose




d1 = {"nome": "Mario", "cognome": "Rossi", "citta": "Roma", "anni": 25}
print(d1, type(d1), len(d1))
d2 = dict({"nome": "Luigi", "cognome": "Bianchi", "citta": "Milano", "anni": 30})
print(d2, type(d2), len(d2))

d1["email"] = "mario.rossi@example.com"
print(d1["nome"])
d1["cognome"] = "Rossini"
d1.update({"citta": "Torino", "anni": 99})
print(d1)

d1.pop("citta")
del d1["anni"]
print(d1)

dc = d2.copy()
dc = dict(d2)

for k in d2.keys():
    print(k, d2[k]) # stampa le chiavi e i valori del dizionario

for v in d2.values():
    print(v) # stampa i valori del dizionario

for i in d2.items(): # itero una tupla che contiene coppie chiave/valore del dizionario
    print(i) # stampa le coppie chiave/valore del dizionario

for k in d2: # iterando direttamente sulle chiavi del dizionario
    print(k, d2[k]) # stampa le chiavi e i valori del dizionario





























