# Sei incaricato di gestire le iscrizioni a due eventi:
# Python Day e Data Science Lab.
# Ogni partecipante fornisce il proprio nome, cognome, città e età.
# Alcuni partecipanti possono iscriversi a entrambi gli eventi.
# Il tuo compito è analizzare i dati raccolti utilizzando set e dizionari.
# - Tramite un ciclo effettuare la registrazione di partecipanti e
# prevedere un fine registrazione.
# - Richiedere all'utente tramite input di inserire N partecipanti al Python Day,
# fornendo per ciascun iscritto il nome, il cognome, la città ed età
# (es. Alice,Neri,Roma,30).
# - Richiedere all'utente di inserire i partecipanti al Data Science Lab,
# con le stesse modalità.
# - Memorizzare i dati in dizionari, dove le chiavi sono nome,cognome,citta ed eta
# - Controllare le età degli iscritti e se superiore a 20 salvarli
# in un set di nome PythonDay o DataScienceLab altrimenti stampare un errore.
# - Utilizzare i set per determinare:
# L'insieme completo dei partecipanti unici.
# I partecipanti iscritti a entrambi gli eventi.
# I partecipanti esclusivi di ciascun evento.
# - Stampare:
# il numero totale e i partecipanti a ciascun evento
# il numero totale e i partecipanti unici
# il numero totale e i partecipanti esclusivi di ciascun evento.

python_day = set((
    ('Alice','Neri','Roma',30), 
    ('Mario','Rossi','Milano',22), 
    ('Francesca','Verdi','Torino',41)
    ))
data_science_lab = set((
    ('Giuseppe','Gialli','Napoli',34), 
    ('Alice','Neri','Roma',30), 
    ('Antonio','Bianchi','Roma',33)
    ))

print("----- Registrazione Partecipanti -----")

# Tramite un ciclo effettuare la registrazione di partecipanti e prevedere un fine registrazione
# Alice,Neri,Roma,30


while True:
    dati = input("Inserisci dati partecipante (es. Alice,Neri,Roma,30) o fine per terminare: ").strip()
    if dati.lower() == 'fine':
        print('----- Fine registrazione partecipanti -----')
        break
    
    dati_partecipante = dati.split(',')
    eta = int(dati_partecipante[3])
    if len(dati_partecipante) == 4 and eta > 20:
        partecipante_dict = {
            'nome': dati_partecipante[0],
            'cognome': dati_partecipante[1],
            'citta': dati_partecipante[2],
            'eta': eta
        }
    else : 
        print("Formato dei valori inseiriti non corretto oppure eta minore di 20")
        continue
    
    while True:
        print("A quale evento vuoi registrarti?")
        dati_evento = input('1 - Python Day | 2 - Data Science Lab | 3 - Python Day + Data Science Lab ->')
        if dati_evento not in ['1', '2', '3']:
            print('Evento non corretto!!!')
            continue
        else:
            if dati_evento == '1':
                print("Registrazione effettuata a Python Day")
                python_day.add(tuple(partecipante_dict.values()))
            elif dati_evento == '2':
                print("Registrazione effettuata a Data Science Lab")
                data_science_lab.add(tuple(partecipante_dict.values()))
            elif dati_evento == '3':
                print("Registrazione effettuata a Python Day e Data Science Lab")
                python_day.add(tuple(partecipante_dict.values()))
                data_science_lab.add(tuple(partecipante_dict.values()))
            break
    
# print("Python Day: ", python_day)
# print("Data Science Lab: ", data_science_lab)

# Metodi per calcolare l'unione, l'intersezione e la differenza tra set
# L'insieme completo dei partecipanti unici.
# partecipanti_unici = python_day.union(data_science_lab)
partecipanti_unici = python_day | data_science_lab
# print(partecipanti_unici)

# I partecipanti iscritti a entrambi gli eventi.
# partecipanti_comuni = python_day.intersection(data_science_lab)
# partecipanti_comuni = python_day & data_science_lab
# print(partecipanti_comuni) 

# I partecipanti esclusivi di ciascun evento.
# partecipanti_python_day = python_day.difference(data_science_lab)
partecipanti_python_day = python_day - data_science_lab
# print(partecipanti_python_day)
# partecipanti_data_science_lab = data_science_lab.difference(python_day)
partecipanti_data_science_lab = data_science_lab - python_day
# print(partecipanti_data_science_lab)


# - Stampare:
#       il numero totale e i partecipanti a ciascun evento
#       il numero totale e i partecipanti unici    
#       il numero totale e i partecipanti esclusivi di ciascun evento. 

print("----- Python Day -----")
print("Numero partecipanti: ", len(python_day))
for partecipante in python_day:
    partecipante_dict = {
        'nome': partecipante[0],
        'cognome': partecipante[1],
        'citta': partecipante[2],
        'eta': partecipante[3]
    }
    
    print(f" - Nome: {partecipante_dict['nome']}, Cognome: {partecipante_dict['cognome']}, Città: {partecipante_dict['citta']}, Età: {partecipante_dict['eta']}")

print("----- Data Science Lab -----")
print("Numero partecipanti: ", len(data_science_lab))
for partecipante in data_science_lab:
    partecipante_dict = {
        'nome': partecipante[0],
        'cognome': partecipante[1],
        'citta': partecipante[2],
        'eta': partecipante[3]
    }
    
    print(f" - Nome: {partecipante_dict['nome']}, Cognome: {partecipante_dict['cognome']}, Città: {partecipante_dict['citta']}, Età: {partecipante_dict['eta']}")

print("----- Paretcipanti Unici -----")
print("Numero partecipanti partecipanti unici: ", len(partecipanti_unici))
for partecipante in partecipanti_unici:
    partecipante_dict = {
        'nome': partecipante[0],
        'cognome': partecipante[1],
        'citta': partecipante[2],
        'eta': partecipante[3]
    }
    
    print(f" - Nome: {partecipante_dict['nome']}, Cognome: {partecipante_dict['cognome']}, Città: {partecipante_dict['citta']}, Età: {partecipante_dict['eta']}")

print("----- Paretcipanti Esclusivi Python Day -----")
print("Numero partecipanti partecipanti esclusivi: ", len(partecipanti_python_day))
for partecipante in partecipanti_python_day:
    partecipante_dict = {
        'nome': partecipante[0],
        'cognome': partecipante[1],
        'citta': partecipante[2],
        'eta': partecipante[3]
    }
    
    print(f" - Nome: {partecipante_dict['nome']}, Cognome: {partecipante_dict['cognome']}, Città: {partecipante_dict['citta']}, Età: {partecipante_dict['eta']}")

print("----- Paretcipanti Esclusivi Data Science Lab -----")
print("Numero partecipanti partecipanti esclusivi: ", len(partecipanti_data_science_lab))
for partecipante in partecipanti_data_science_lab:
    partecipante_dict = {
        'nome': partecipante[0],
        'cognome': partecipante[1],
        'citta': partecipante[2],
        'eta': partecipante[3]
    }
    
    print(f" - Nome: {partecipante_dict['nome']}, Cognome: {partecipante_dict['cognome']}, Città: {partecipante_dict['citta']}, Età: {partecipante_dict['eta']}")












