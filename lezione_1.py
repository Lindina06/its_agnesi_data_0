# Questo è un commento
# ctrl + ù -> attiva/disattiva commento
# Python non è un linguaggio fortemente tipizzato
# String miaVar -> Java -> fortemente tipizzato 
# print vuol dire stampa e lo fa con la variabile che sta sopra 
# per farlo per più variabili devi ripetere sotto ad ogni assegnazione della variabile il comando print
# type insieme a print ti indica il tipo di dato (nel terminale) 

miaVar = 5
#print(miaVar, type(miaVar))
miaVar = "testo"
#print(miaVar, type(miaVar))
miaVar = True 
#print(miaVar, type(miaVar))

abc = None
#print(abc)

# Nomenclatura di un elemento python
nomeDatoVariabile = 0   # CamelCase -> ad ogni parola l'inizio è con la lettera maiuscola
NomeDatoVariabile = 0   #PascalCase -> anche la prima lettera maiuscola
nome_dato_variabile = 0 #SnakeCase -> con l'underscore e non con il trattino 
NOME_DATO_VARIABILE = 0 # con tutto maiuscolo di solito definiscono le costanti -> variabili con contenuto fisso (non costante)

# Assegnazioni singole
x = 1
y = 2
z = 3

# Assegnazioni multiple
x,y,z = 1,2,3
x = y = z = 1 #Assegnare lo stesso valore alle variabili

# Tipi di dato
# - int     -> numerico intero   -> d = 5
# - float   -> numerico decimale -> d = 5,5 
# - string  -> testo             -> d = "testo"
# - boolean -> True/False        -> d = True
# - none    -> None              -> d= None

# Funzioni predefinite in Python 
# print(args)    -> Funzione predefinita che stampa nel terminale il valore di args
# type(var)      -> Funzione predefinita che restituisce il tipo di dato di una variabile 
# input()        -> Funzione predefinita che permette l'inserimento di valori da terminale
# len(str)       -> Funzione predefinita che restituisce la lunghezza di una stringa
# help(func)     -> Restuisce la documentazione di una funzione passata come un parametro 

# Funzioni predefinite di Casting
# int(param)       -> Restituisce il valore inserito in formato int
# float(param)     -> Restituisce il valore inserito in formato float
# str(param)       -> Restituisce il valore inserito in formato str
# bool(param)      -> Restituisce il valore inserito in formato bool
# bool(0)          ->striga/contenitore/valore/lista vuota è False se c'è qualcosa dentro è True

miaVar = "sono una Stringa"
print(miaVar)
print(type(miaVar))
print(len(miaVar))
nome = 'Mario Rossi' #input("Inserisci un nome: ")
print("il nome che hai inserito è: ",nome)
age = '25' #input("Inserisci età: ") # -> stringa
eta = int(age) # trasformo la stringa in un valore intero
#eta = float(age) # trasformo la stringa in un valore decimale
#eta = bool(age) # trasformo la stringa in un valore booleano
print(type(eta))

print("FINE")

# String in python
# Per creare una stringa in python si utilizzano '' o ""
# Per creare una stringa multiriga si utilizzano ''' ''' oppure """ """
# Possiamo accedere ai singoli caratteri di una stringa tramite l'indice [i]
#Possiamo selezionare porzioni di stringhe[n:m]
# indexing sfruttare un indice per ricavare un valore
# slicing taglia la stringa e prende sottoinsieme
# Metodi predefiniti per manipolare una stringa

multiStr = """ Sono
           una
            stringa"""
    #  0123456789......
str = " Sono una Stringa " # stringa a singola riga
print(str[0]) 
print(str[5:8]) # non include m in [n:m] 
print(str[:8]) # restituirà dall'inizio della stringa
print(str[5:]) # restituirà dalla fine della stringa
print(str[-5:-1]) # inizierà a contare dalla fine quindi dalla r fino a g
print(str[-7:]) # partirà da s e poi prenderà in considerazione la fine da s in poi 

print(str.lower()) # Restituisce una copia di una stringa in minuscolo
print(str.upper()) # Restituisce una copia di una stringa in maiuscolo
print(str.strip()) # Restituisce una copia di una stringa senza gli spazi all'inizio e alla fine
print(str.replace('n','x', 1)) # Restituisce una copia di una stringa tipo 'n'(Ielemento),(con)'x', 1 ->(solo del primo elemento che incotri nella stringa)
print(str.split(' ')) # Restituisce una contenitore con porzioni di stringa tagliate in base ad un separatore
print(str)

nome= "Mario"
cognome= "Rossi"
eta = 25
# saluta = "Ciao " + nome + " " + cognome + "anni " + "sono una stringa!"
saluta = "Ciao {} {} anni {} sono una stringa!" # {} sono segnaposti che specifici dentro cosa va con format(nomeV1,nomeV2 etc)
print(saluta.format(nome, cognome, eta))
saluta =  "Ciao {1} {0} anni {2} sono una stringa!"
print(saluta.format(cognome, nome, eta))
#                       0     1    2
saluta =  "Ciao {name} {lastname} anni {age} sono una stringa!"
print(saluta.format(name = nome, lastname = cognome, age = eta))

print(f"Ciao {nome} {cognome} anni {eta} sono una stringa!")

# if-else, if condizione: istruzioni else: istruzione
age =15
if age >= 18:
    print("Maggiore di 18")
else:
    print("Minore o uguale di 18")
    

    