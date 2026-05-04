# Contare le occorrenze di un elemento
# Scrivere una funzione ricorsiva che conti quante volte un valore appare in una lista.
# Scrivi una funzione -> def conta_elemento(lista, valore) che:
# ✔ restituisce il numero di volte in cui valore compare nella lista
# ✔ utilizza la ricorsione
# ❌ non usare .count()

# Caso base: lista vuota → ritorna 0
# Caso ricorsivo: se il primo elemento è uguale a valore → +1 poi continua con il resto della lista

# Debug richiesto -> Aggiungi logging per capire il flusso della funzione ricorsiva



import logging as log

log.basicConfig(level=log.DEBUG)


def conta_elemento(lista, valore):
    log.debug(f'Lista corrente {lista}')
    if len(lista) == 0:
        log.debug(f'Caso base: lista vuota -> ritorna 0')
        
        return 0
    
    if lista[0] == valore:
        log.debug(f'Valore : {lista[0]} = {valore} conta +1')
        return 1 + conta_elemento(lista[1:], valore)
    else:
        log.debug(f'Non fare nulla e procedi con la ricorsione')
        return conta_elemento(lista[1:], valore)
    

# print('Numero occorenze del valore cercato: ', conta_elemento([1,2,2,3,2],2))

# Hai una lista di studenti rappresentati come dizionari:
# studenti = [ {"nome": "Luca", "voto": 28}, {"nome": "Anna", "voto": 17}, {"nome": "Marco", "voto": 30}, {"nome": "Giulia", "voto": 22}, {"nome": "Paolo", "voto": 18}, {"nome": "Sara", "voto": 15}, {"nome": "Mario", "voto": 22} ]

# List Comprehension
# 1 Crea una lista contenente solo i nomi degli studenti sufficienti (voto ≥ 18)
# 2 Crea una lista con i voti aumentati di 1 punto, ma solo per chi ha voto ≥ 18
# 3 Crea una lista di stringhe nel formato: "Nome - Promosso/Bocciato"
# Set Comprehension
# 4 Crea un set con tutti i voti unici
# 5 Crea un set contenente solo i voti insufficienti
# Dictionary Comprehension
# 6 Crea un dizionario: {nome: voto}
# 7 Crea un dizionario contenente solo gli studenti promossi
# 8 Crea un dizionario: {nome: "Eccellente" | "Buono" | "Sufficiente" | "Insufficiente"}
# usando le seguenti regole:
# ≥ 27 → Eccellente
# ≥ 21 → Buono
# ≥ 18 → Sufficiente
# < 18 → Insufficiente
studenti = [
    {"nome": "Luca", "voto": 28}, 
    {"nome": "Anna", "voto": 17}, 
    {"nome": "Marco", "voto": 30}, 
    {"nome": "Giulia", "voto": 22},
    {"nome": "Paolo", "voto": 18},
    {"nome": "Sara", "voto": 15},
    {"nome": "Mario", "voto": 22}
]

# 1 Crea una lista contenente solo i nomi degli studenti sufficienti (voto ≥ 18)
studenti_sufficienti =  [s['nome'] for s in studenti if s['voto'] >= 18]
print(studenti_sufficienti)

# 2 Crea una lista con i voti aumentati di 1 punto, ma solo per chi ha voto ≥ 18
voti_aumentati = [s['voto'] + 1 for s in studenti if s['voto'] >= 18]
print(voti_aumentati)

# 3 Crea una lista di stringhe nel formato: "Nome - Promosso/Bocciato"
# risultati = [(s['nome'] + ' - ' + 'Promosso') if s['voto'] >= 18 else (s['nome'] + ' - ' + 'Bocciato')  for s in studenti]
risultati = [f"{s['nome']} - Promosso" if s['voto'] >= 18 else f"{s['nome']} - Bocciato" for s in studenti]
print(risultati)

# 4 Crea un set con tutti i voti unici
voti_unici = {s['voto'] for s in studenti}
print(voti_unici)

# 5 Crea un set contenente solo i voti insufficienti
voti_insufficienti = {s['voto'] for s in studenti if s['voto'] < 18}
print(voti_insufficienti)

# 6 Crea un dizionario: {nome: voto}
dizionario_voti = {s['nome']: s['voto'] for s in studenti}
print(dizionario_voti)

# 7 Crea un dizionario contenente solo gli studenti promossi
studenti_promossi = {s['nome']: s['voto'] for s in studenti if s['voto'] >= 18}
print(studenti_promossi)

# 8 Crea un dizionario: {nome: "Eccellente" | "Buono" | "Sufficiente" | "Insufficiente"}
#   usando le seguenti regole: ≥ 27 → Eccellente ≥ 21 → Buono ≥ 18 → Sufficiente < 18 → Insufficiente
valutazione = {
    s['nome']: (
        'Eccellente' if s['voto'] >= 27 else
        'Buono' if s['voto'] >= 21 else
        'Sufficiente' if s['voto'] >= 18 else
        'Insufficiente'
    ) for s in studenti }
print(valutazione)
    
    
        












