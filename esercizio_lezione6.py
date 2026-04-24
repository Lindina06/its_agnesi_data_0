# Riscrivere l'esercizio del giorno precedente
# Utilizzando le funzioni 

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

def registrazione_partecipante(dati):
    dati_partecipante = dati.split(',')
    eta = int(dati_partecipante[3])
    # Controllare età degli iscritti e se superiore a 20 salvarli 
    if len(dati_partecipante) == 4 and eta > 20:
        partecipante_dict = {
            'nome': dati_partecipante[0],
            'cognome': dati_partecipante[1],
            'citta': dati_partecipante[2],
            'eta': eta
            
        }
        return partecipante_dict
    else : 
        print("Formato dei valori inseiriti non corretto oppure eta minore di 20")
        return 
def assegna_evento(partecipante):
        while True:
            print("A quale evento vuoi registrarti?")
            dati_evento = input('1 - Python Day | 2 - Data Science Lab | 3 - Python Day + Data Science Lab ->')
            if dati_evento not in ['1', '2', '3']:
                    print('Evento non corretto!!!')
            else:
                if dati_evento == '1':
                    print("Registrazione effettuata a Python Day")
                    python_day.add(tuple(partecipante.values()))
                elif dati_evento == '2':
                    print("Registrazione effettuata a Data Science Lab")
                    data_science_lab.add(tuple(partecipante.values()))
                elif dati_evento == '3':
                    print("Registrazione effettuata a Python Day e Data Science Lab")
                    python_day.add(tuple(partecipante.values()))
                    data_science_lab.add(tuple(partecipante.values()))    
                break   
def stampa_partecipanti(partecipanti, titolo):
    print(f"----- {titolo}-----")
    print("Numero partecipanti: ", len(partecipanti))
    for partecipante in partecipanti:
        partecipante_dict = {
        'nome': partecipante[0],
        'cognome': partecipante[1],
        'citta': partecipante[2],
        'eta': partecipante[3]
        }         
        print(f" - Nome: {partecipante_dict['nome']}, Cognome: {partecipante_dict['cognome']}, Città: {partecipante_dict['citta']}, Età: {partecipante_dict['eta']}")


while True:
    dati = input("Inserisci dati partecipante (es. Alice,Neri,Roma,30) o fine per terminare: ").strip()
    if dati.lower() == 'fine':
        print('----- Fine registrazione partecipanti -----')
        break
        
    partecipante = registrazione_partecipante(dati)   
    
    if partecipante :
        assegna_evento(partecipante)
        
stampa_partecipanti(python_day, 'Python Day')
stampa_partecipanti(data_science_lab, 'Data Science Lab')
partecipanti_unici = python_day | data_science_lab
stampa_partecipanti(partecipanti_unici, 'Partecipanti Unici')
partecipanti_python_day = python_day - data_science_lab
stampa_partecipanti(partecipanti_python_day, 'Partecipanti Esclusivi Python Day')
partecipanti_data_science_lab = data_science_lab - python_day
stampa_partecipanti(partecipanti_data_science_lab, 'Partecipanti Esclusivi Data Science Lab')
        
    
            
    
    





