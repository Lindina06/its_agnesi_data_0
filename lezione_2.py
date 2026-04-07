<<<<<<< HEAD
#https://github.com/emanueleumberto/its_agnesi_data4
# Operatori
# - Operatori di assegnamento [=]
# - Operatori aritmetici [+ - * / %(il modulo: da il resto) **(elevamento a potenza) //(divisione tra interi che da numero intero)]
# - Operatori aritmetici [+= (aggiungi e assegna) -= *= /= %=]
# - Operatori di comparazione [>, <, ==, !=(not: cioè diverso da), >=, <=, is, is not, in, not in] -> booleani: True or False
# - Operatori logici [and or not (nrgo una condizione) xor(condiziona vera se entrambe sono false)]

# AND
# TRUE and TRUE -> TRUE
# TRUE and FALSE -> FALSE
# FALSE and TRUE -> FALSE
# FALSE and FALSE -> FALSE

# OR
# TRUE or TRUE -> TRUE
# TRUE or FALSE -> TRUE
# FALSE or TRUE -> TRUE
# FALSE or FALSE -> FALSE

# XOR
# TRUE or TRUE -> FALSE
# TRUE or FALSE -> FALSE
# FALSE or TRUE -> FALSE
# FALSE or FALSE -> TRUE

# NOT
# NOT TRUE -> FALSE
# NOT FALSE -> TRUE

a = 10
b = 3
c = 3

print(int(a/b))
print(a//b)
print(a%b)
print(3**3)

#a = a + 5
a += 5
print(a>b)
print(a == b)
print(a != b)
print('i' in 'Ciao')
print('x' not in 'Ciao')

a = 10
b = 10
c = 3
print( a > b and b > c)
print( a > b or b > c)
print(not(a < b))

# Strutture di controllo
# - IF ELIF(else if) ELSE
#   if condizione: 
#       blocco di istruzioni
#   elif condizione:
#       blocco di istruzioni
#   else:
#       blocco di istruzioni 
#
# - if condizione: istruzioni else: istruzioni

if a > b:
    print("A è maggiore di B")
elif a == b:
   print("A è uguale a B")
else:
    print("A è minore di B")


# Strutture iterative 
# - WHILE
#   while condizione:
#       blocco di istruzioni
num = 0
while num < 5:
    print("blocco d'istruzioni")
    num += 1
    
while True: # finchè vero è vero cicla per fare un ciclo infinito 
    scelta = input("Inserisci il tuo nome oppure fine per terminare: ") 
    if scelta == "fine": 
        break # per fare terminare il ciclo infinito tramite l'inserimento fine
    
    print(f"Ciao {scelta}")
    
print("FINE")

# - FOR
#   for ele in iterable:
#        blocco di istruzioni 
    
    
    
=======
#https://github.com/emanueleumberto/its_agnesi_data4
# Operatori
# - Operatori di assegnamento [=]
# - Operatori aritmetici [+ - * / %(il modulo: da il resto) **(elevamento a potenza) //(divisione tra interi che da numero intero)]
# - Operatori aritmetici [+= (aggiungi e assegna) -= *= /= %=]
# - Operatori di comparazione [>, <, ==, !=(not: cioè diverso da), >=, <=, is, is not, in, not in] -> booleani: True or False
# - Operatori logici [and or not (nrgo una condizione) xor(condiziona vera se entrambe sono false)]

# AND
# TRUE and TRUE -> TRUE
# TRUE and FALSE -> FALSE
# FALSE and TRUE -> FALSE
# FALSE and FALSE -> FALSE

# OR
# TRUE or TRUE -> TRUE
# TRUE or FALSE -> TRUE
# FALSE or TRUE -> TRUE
# FALSE or FALSE -> FALSE

# XOR
# TRUE or TRUE -> FALSE
# TRUE or FALSE -> FALSE
# FALSE or TRUE -> FALSE
# FALSE or FALSE -> TRUE

# NOT
# NOT TRUE -> FALSE
# NOT FALSE -> TRUE

a = 10
b = 3
c = 3

print(int(a/b))
print(a//b)
print(a%b)
print(3**3)

#a = a + 5
a += 5
print(a>b)
print(a == b)
print(a != b)
print('i' in 'Ciao')
print('x' not in 'Ciao')

a = 10
b = 10
c = 3
print( a > b and b > c)
print( a > b or b > c)
print(not(a < b))

# Strutture di controllo
# - IF ELIF(else if) ELSE
#   if condizione: 
#       blocco di istruzioni
#   elif condizione:
#       blocco di istruzioni
#   else:
#       blocco di istruzioni 
#
# - if condizione: istruzioni else: istruzioni

if a > b:
    print("A è maggiore di B")
elif a == b:
   print("A è uguale a B")
else:
    print("A è minore di B")


# Strutture iterative 
# - WHILE
#   while condizione:
#       blocco di istruzioni
num = 0
while num < 5:
    print("blocco d'istruzioni")
    num += 1
    
while True: #finchè vero è vero cicla
    scelta = input("Inserisci il tuo nome oppure fine per terminare: ") 
    if scelta == "fine": 
        break #per fare terminare il ciclo tramite l'inserimento fine
    
    print(f"Ciao {scelta}")
    
print("FINE")

# - FOR
#   for ele in iterable:
#        blocco di istruzioni 
    
    
    
>>>>>>> 4444ac70e90da96401149c95785d2e556ebbb051
    