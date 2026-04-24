# Creare un’applicazione Python per simulare la generazione di profili utente
# utilizzando un modulo esterno (genuine-fake) e
# organizzare il progetto con file separati
# generatore.py:
# Importa GenuineFake dal modulo genuine-fake.
# Definisce una funzione genera_profili(n) che:
# Genera n profili fittizi contenenti:
# Nome completo, Email, Data di nascita, eta(calcolata)
# Indirizzo (città + stato), data creazione(datetime)
# Restituisce i dati come lista di dizionari.
# main.py:
# Importa genera_profili da generatore.py
# Chiede all’utente quanti profili generare.
# Visualizza i profili in output, ben formattati.


from genuine.fake import GenuineFake as gf 
import datetime as d

def genera_profili(n):
    
    profili_utente = []
    
    while len (profili_utente) < n:
        date_of_birth = gf.date_of_birth()
        utente = {
           'nomeCompleto' : gf.name(),
           'email' : gf.email(),
           'DataDiNascita' : date_of_birth,
           'eta' : calcola_eta(date_of_birth),
           'indirizzo' : gf.capital_city() + " " + gf.country(),
           'DataDiCreazione' : d.date.today()
        }
        
        profili_utente.append(utente)
        
        
    return profili_utente

def calcola_eta(DataDiNascita):
    today = d.date.today().strftime('%Y')
    data = DataDiNascita.split(' ')[2]
    return int(today) - int(data)

def stampa_profili(listaProfili):
    print('***** Lista di Profili Generati *****')
    print()
    for u in listaProfili:
        print('Nome Completo', u['nomeCompleto'])
        print('Email', u['email'])
        print('Data di Nascita', u['DataDiNascita'])
        print('Età', u['eta'])
        print('Indirizzo', u['indirizzo'])
        print('Data Creazione', u['DataDiCreazione'])
        print('---------------------------------------')
        print()
    

    

        
        
    