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

libro1 = ("Il Signore degli Anelli", "J.R.R. Tolkien", 1954, 29.99)
libro2 = ("1984", "George Orwell", 1949, 19.99)
libro3 = ("Il Grande Gatsby", "F. Scott Fitzgerald", 1925, 14.99)
libro4 = ("Harry Potter e la Pietra Filosofale", "J.K. Rowling", 1997, 24.99)
libro5 = ("Il Codice da Vinci", "Dan Brown", 2003, 22.99)   
catalogo = [libro1, libro2, libro3, libro4, libro5]
for libro in catalogo:
    print(f"Titolo: {libro[0]}, Autore: {libro[1]}, Anno: {libro[2]}, Prezzo: {libro[3]}") 
anno = int(input("Inserisci un anno: "))
print(f"Libri pubblicati dopo il {anno}:")
for libro in catalogo:
    if libro[2] > anno:
        print(f"Titolo: {libro[0]}, Autore: {libro[1]}, Anno: {libro[2]}, Prezzo: {libro[3]}")
    else:
        print(f"Nessun libro trovato pubblicato dopo il {anno}.")
        
autore = input("Inserisci il nome di un autore: ")
print(f"Libri scritti da {autore}:")
for libro in catalogo:
    if libro[1].lower() == autore.lower():
        print(f"Titolo: {libro[0]}, Autore: {libro[1]}, Anno: {libro[2]}, Prezzo: {libro[3]}")  
    else: 
        print(f"Nessun libro trovato per l'autore {autore}.")
prezzi = [libro[3] for libro in catalogo]
prezzo_medio = sum(prezzi) / len(prezzi)     
print(f"Prezzo medio dei libri:{prezzo_medio} $", )
prezzo_più_alto = max(prezzi)
for libro in catalogo:
    if libro[3] == prezzo_più_alto:
        print(f"Il libro più costoso è: Titolo: {libro[0]}, Autore: {libro[1]}, Anno: {libro[2]}, Prezzo: {libro[3]}")
        


# Per aggiornare il prezzo di un libro, poiché le tuple sono immutabili,
# potresti convertire la tupla in una lista, modificare il prezzo e poi riconvertirla in tupla.
