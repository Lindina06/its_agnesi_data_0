from decimal import Decimal # importo un modulo che mi trasforma il numero intero in valore decimale

class Libro:
    # Attributo di classe: comune a tutti i libri, serve come contatore globale
    __contatore = 0

    def __init__(self, titolo, autore, pagine, supporto, prezzo):
        # Proprietà private: l'uso del doppio underscore __ impedisce l'accesso diretto dall'esterno
        self.__titolo = titolo
        self.__autore = autore
        self.__pagine = pagine
        self.__supporto = self.valida_supporto(supporto) # Può essere "Digitale" o "Cartaceo"
        self.__prezzo = prezzo # richiamo il setter di prezzo
        Libro.__contatore += 1
        
    # PROPERTY (Getter): permettono di leggere le proprietà private come se fossero variabili pubbliche
    @property
    def titolo(self):
        return self.__titolo    # per estrarre un titolo visto che lo abbiamo messo con __titolo quindi solo lettura nel terminale 
                                # ma non modificarlo sennò si utilizza setter

    @property
    def autore(self):
        return self.__autore
    
    @property
    def pagine(self):
        return self.__pagine
    
    @property
    def prezzo(self):
        return self.__prezzo
    
    @property
    def supporto(self):
        return self.__supporto
    
    @supporto.setter #per modificare il supporto per poi validarlo 
    def supporto(self, supporto):
        self.__supporto = self.valida_supporto(supporto) 
    
    @prezzo.setter
    def prezzo(self, prezzo):
        if prezzo < 0:
            self.__prezzo = Decimal(0)
        self.__prezzo = Decimal(prezzo)
            
            
            
    def valida_supporto(self, supporto):
        if supporto.capitalize() == "Digitale":
            return 'Digitale'
        elif supporto.capitalize() == "Cartaceo":
            return 'Cartaceo'
        else:
            print('Hai inserito un supporto non valido, di default sarà carteo')

     

    # Metodo di istanza: restituisce una stringa con i dettagli del libro
    def info(self):
        return f"Libro: {self.__titolo} | Supporto: {self.__supporto} | Prezzo: {self.__prezzo}€"

# Creiamo una lista che contiene 5 oggetti di tipo Libro
lista_libri = [
    Libro("Il Gattopardo", "G. Tomasi di Lampedusa", 300, "Cartaceo", 15.00),
    Libro("1984", "G. Orwell", 328, "Digitale", 8.50),
    Libro("Il fu Mattia Pascal", "L. Pirandello", 250, "Cartaceo", 12.00),
    Libro("Dune", "F. Herbert", 600, "Digitale", 9.99),
    Libro("L'ombra del vento", "C.R. Zafón", 450, "Cartaceo", 19.00)
]

# Inizializziamo una lista per raccogliere solo i prezzi e fare i calcoli matematici


# Ciclo for: analizziamo ogni libro dentro la nostra lista
for libro in lista_libri:
    print(libro.titolo)    
    prezzi = [libro.prezzo for libro in lista_libri]
    # CALCOLI 
    # sum(prezzi) somma tutti i numeri, len(prezzi) ci dice quanti sono
    prezzo_medio = sum(prezzi) / len(prezzi)
    prezzo_alto = max(prezzi)  # max() trova il valore più alto nella lista
    prezzo_basso = min(prezzi) # min() trova il valore più basso nella lista
       
# --- OUTPUT FINALE ---
print("-" * 40)
print(f"ANALISI PREZZI:")
print(f"Il prezzo medio è: {prezzo_medio:.2f}€") # :.2f serve a mostrare solo 2 decimali
print(f"Il prezzo più alto è: {prezzo_alto}€")
print(f"Il prezzo più basso è: {prezzo_basso}€")

digitali = [libro for libro in lista_libri if libro.supporto == 'Digitale']
cartaceo = [libro for libro in lista_libri if libro.supporto == 'Cartaceo']
for libro in digitali : print(libro.titolo)
for libro in cartaceo : print(libro.titolo)