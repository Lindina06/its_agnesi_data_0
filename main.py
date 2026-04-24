# main.py:
# Importa genera_profili da generatore.py
# Chiede all’utente quanti profili generare.
# Visualizza i profili in output, ben formattati.

import generatore as g

numeroProfili = int(input("Quanti profili vuoi generare?"))
listaProfili = g.genera_profili(numeroProfili)
print("Numero profili generati: ", len(listaProfili))
g.stampa_profili(listaProfili)



