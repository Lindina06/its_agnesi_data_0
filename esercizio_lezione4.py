# Un piccolo negozio di libri desidera gestire il proprio catalogo 
# in maniera semplice. 
# Ogni libro è rappresentato da una tupla contenente le seguenti 
# informazioni: 
# (titolo: str, autore: str, anno_pubblicazione: int, prezzo: float)
# Scrivi uno script Python che soddisfi i seguenti requisiti:
# - Crea una lista di almeno 5 libri, ciascuno rappresentato 
#   come una tupla nel formato sopra indicato.
# - Stampa tutti i libri presenti nel catalogo, uno per riga, 
#   formattando le informazioni in modo leggibile 
#   (es. “Titolo: ..., Autore: ..., Anno: ..., Prezzo: ...”).
# - Chiedi all’utente un anno, quindi stampa tutti i libri 
#   pubblicati dopo quell’anno.
# - Chiedi all’utente il nome di un autore e mostra 
#   tutti i libri scritti da quell’autore.
# - Calcola e stampa il prezzo medio dei libri presenti nel catalogo.
# - Trova e stampa il libro più costoso nel catalogo.
# - Poiché le tuple sono immutabili, spiega in un commento come 
#   potresti aggiornare il prezzo di un libro

catalogo = [
    ("Il Signore degli Anelli", "J.R.R. Tolkien", 1954, 29.99),
    ("1984", "George Orwell", 1949, 19.99),
    ("Il Grande Gatsby", "F. Scott Fitzgerald", 1925, 14.99),
    ("Harry Potter e la Pietra Filosofale", "J.K. Rowling", 1997, 24.99),
    ("Il Codice Da Vinci", "Dan Brown", 2003, 22.99)
]

catalogo = tuple(catalogo)
for libro in catalogo:
    titolo, autore, anno, prezzo = libro # unpacking della tupla
    print(f"Titolo: {titolo}, Autore: {autore}, Anno: {anno}, Prezzo: {prezzo}")

anno_input = int(input("Inserisci un anno per vedere i libri pubblicati dopo quell'anno: "))
libri_trovati = False
print(f"Libri pubblicati dopo {anno_input}:")
for libro in catalogo:
    titolo, autore, anno, prezzo = libro
    if anno > anno_input:
        print(f" Titolo: {titolo}, Autore: {autore}, Anno: {anno}, Prezzo: {prezzo}")
        libri_trovati = True

if not libri_trovati:
    print(f"Nessun libro trovato pubblicato dopo l'anno {anno_input}.")

autore_input = input("Inserisci il nome di un autore per vedere i suoi libri: ").strip().lower()
libri_trovati = False
print(f"Libri scritti da {autore_input}:")
for libro in catalogo:
    titolo, autore, anno, prezzo = libro
    if autore.lower() == autore_input.lower():
        print(f"Titolo: {titolo}, Autore: {autore}, Anno: {anno}, Prezzo: {prezzo}")
        libri_trovati = True

if not libri_trovati:
    print(f"Nessun libro trovato per l'autore {autore_input}.")
  
print("--------------------------")
   
prezzo_totale = 0
for libro in catalogo:
    prezzo_totale += libro[3]

prezzo_medio = float(prezzo_totale) / len(catalogo)
print(f"Prezzo medio dei libri: {prezzo_medio:.2f}")

print("--------------------------")


libro_piu_costoso = catalogo[0]
for libro in catalogo:
    if libro[3] > libro_piu_costoso[3]:
        libro_piu_costoso = libro
print(f"Il libro più costoso è: Titolo: {libro_piu_costoso[0]}, Autore: {libro_piu_costoso[1]}, Anno: {libro_piu_costoso[2]}, Prezzo: {libro_piu_costoso[3]}")

# Poiché le tuple sono immutabili, per aggiornare il prezzo di un libro,
# potremmo creare una nuova tupla con le stesse informazioni del libro originale,
# ma con il prezzo aggiornato, e poi sostituire la tupla originale nella lista del catalogo con quella nuova.
# Ad esempio, se volessimo aggiornare il prezzo del primo libro, potremmo fare qualcosa del genere:
# nuovo_prezzo = 34.99
# libro_aggiornato = (catalogo[0][0], catalogo[0
#   ][1], catalogo[0][2], nuovo_prezzo)
# catalogo[0] = libro_aggiornato
#   In questo modo, abbiamo creato una nuova tupla con il prezzo aggiornato e l'abbiamo sostituita nella lista del catalogo.
# Tuttavia, poiché le tuple sono immutabili, non possiamo modificare direttamente il prezzo all'interno della tupla originale.


# Soluzione 1
vecchio_libro = catalogo[0]
nuovo_libro = list(vecchio_libro)
nuovo_libro[3] = 9.99
vecchio_libro = tuple(nuovo_libro)
print(vecchio_libro)

# Soluzione 2
vecchio_libro = (vecchio_libro[0], vecchio_libro[1], vecchio_libro[2], 9.99)
print(vecchio_libro)







