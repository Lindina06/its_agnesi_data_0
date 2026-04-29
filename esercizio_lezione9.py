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
    
        












