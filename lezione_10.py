# La programmazione orientata agli oggetti (OOP) si basa su: 
# classi -> modelli
# oggetti -> istanze

# Permette di:
# organizzare il codice 
# modellare il mondo reale 
# migliorare la riusabilità

# Definizione di classe
# class MiaClasse:
# Creazione di un oggetto:
# obj = MiaClasse()

# Metodi nelle classi
# Un metodo è una funzione definita all'interno di una classe e serve a:
# operare sui dati di un oggetto
# incapsulare la logica

# Differenza fondamentale
# Funzione -> indipedente
# Metodo -> legato ad una classe

# Metodo di istanza -> il tipo più comune
# lavora sui dati dell'oggetto tramite 'self'

# il parametro 'self' rappresenta:
# l'istanza corrente 
# il collegamento tra il metodo e l'oggetto

# Metodo di classe -> condiviso tra tutti gli oggetti della classe 
# Un metodo di classe lavora sulla classe e non sull'oggetto/istanza della classe
# si definisce utilizzando @classmethod 

# un linguaggio ad oggetti si basa su 4 principi fondamentali:
# Incapsulamento
# Ereditarietà
# Polimorfismo
# Astrazione

# In python non esistono veri modificatori di accesso come in java, c++ etc
# Si usano per convenzione

# Incapusulamento è uno dei principi fondamentali della OOP (programmazione ad oggetti)
# Consiste nel nascondere i dati interni (Ma non sono protetti)
# Permettere l'accesso ai dati solo tramite dei metodi controllati 
# Obiettivo: proteggere lo stato interno di un oggetto
# Evitare modifiche non valide (Conenzione)
# Rendere così il codice più sicuro e manutenibile

# Convenzioni e sintassi per rappresentare un attributo public, protected, private:
# self.prop   -> public
# self._prop  -> protected
# self.__prop -> private 

# Vantaggi dell’incapsulamento
# Protegge i dati
# Riduce bug
# Migliora la manutenzione
# Permette validazione automatica
# Facilita il refactoring

# Errori comuni
# Usare variabili pubbliche sempre
# Usare get_ e set_ come in Java -> In Python è meglio: @property


class Automobile:
    
    totale = 0
    
    # costruttore
    def __init__(self, marca, modello, colore):
        self.__marca = marca
        self.__modello = modello
        self.__colore = colore
        self.__targa = None
        self.incrementa()
        
    # Metodo di istanza
    def info(self):
        print(f"Automobile: {self.marca} {self.modello} Colore:{self.colore} Targa: {self.targa}")
    
    # Metodo di classe
    @classmethod
    def incrementa(cls):
        cls.totale += 1 
    
    # Getter e Setter per modificare proprietà private  
    def getTarga(self):
        return self.targa
    
    def setTarga(self, targa):
        self.targa = targa
        
# auto = Automobile()
# auto.marca = 'Ford'
# auto.modello = 'Fiesta'
# auto.targa = 'CD456FG'
# print(auto)   
    
auto1 = Automobile('Fiat', 'Panda', 'Nero')
# print(auto1.totale)
auto2 = Automobile('Ford', 'Fiesta', 'Verde')
# print(auto2.totale)
auto3 = Automobile('Renault', 'Clio', 'Bianco')

auto1.targa = 'AB123CD'

# auto1.info()
# auto2.info()

print(Automobile.totale)

# print(auto1.targa)
print(auto1.getTarga())


#####################################################################

class ContoCorrente:
    
    def __init__(self, nome, cognome):
        self.__nome = nome
        self.__cognome = cognome
        self.__saldo = 0
    
    # Metodo di istanza
    def info(self):
        print(f"Conto corrente di {self.__nome} {self.__cognome} Saldo: {self.__saldo}")
        
    # Metodo migliore 
    #Le 'property' sono il modo più Pythoniano per fare l'incapsulamento
    # Property
    @property 
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, importo):
        if importo <= 0:
            print('Non puoi aggiungere importi negativi')
            return
        self.__saldo = importo        
    
c = ContoCorrente("Mario", "Rossi")
c.saldo = 200 # Sto utilizzando il metodo Setter
print(c.saldo) # Sto utilizzando il metodo Getter
c.info()

print('###########################################################################')

# Esempio pratico 
# fare la classe
class Studente:
    
    # Attributo di classe privato
    __contatore_matricola = 0
    # fare il costruttore
    def __init__(self, nome):
        self.__matricola = self.__genera_matricola()        
        self.__nome = nome # lo definisco privato per non modificarlo
        self.__voti = [] # creare una lista vuota per aggiungere per ogni studente più voti
    
    
    # Espone l'attributo privato __nome in sola lettura. Permette di accedere al nome con 'oggetto.nome' invece di 'oggetto.get_nome()'.
        
    @property
    def nome(self):
        return self.__nome
    
    # Restituisce la lista dei voti. Usando @property, proteggiamo l'attributo da sovrascritture accidentali dall'esterno della classe.
    @property 
    def voti(self):
        return self.__voti
    
    
    
    # Metodo di instanza
    def info(self):
        return f'Studente: {self.__nome} matricola: {self.__matricola} voti: {self.__voti}'
    
    def aggiungi_voto(self, voto):
        if voto > 0 and voto <= 30:
            self.__voti.append(voto)
        else:
            print('Hai aggiunto un valore errato')
    
    
    
    # Metodo di classe perchè riguarda tutti gli oggetti
    @classmethod    
    def __genera_matricola(cls): #Metodo che non posso richiamare dall'esterno 
            cls.__contatore_matricola += 1
            matricola = cls.__contatore_matricola 
            if matricola < 10:
                matricola = f"US000{matricola}"
            elif matricola < 100:
                matricola = f"US00{matricola}"
            elif matricola < 1000:
                matricola = f"US0{matricola}"
            else:
                matricola = f"US{matricola}"
            return matricola
        

s1 = Studente('Mario Rossi')
s2 = Studente('Giuseppe verdi')
s3 = Studente('Francesca Neri')
# Errore richiamare questo metodo al di fuori della classe Studente
# s.genera_matricola()

s1.aggiungi_voto(30)
s1.aggiungi_voto(25)
s1.aggiungi_voto(18)

print(s1.info())
print(s2.info())
print(s3.info())








