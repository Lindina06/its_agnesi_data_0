# Logging

# Il logging in Python è il meccanismo standard per registrare eventi
# che avvengono durante l'esecuzione di un programma.
# Serve per il debug, monitoraggio, audit, analisi di errori in ambienti di produzione
# è preferibile a print() perchè: è configurabile, supporta livelli di gravità,
# può scrivere su più destinazioni (console, file, rete). 

# modulo logging è già incluso nella standard library
# logging ha un'archittettura basata su: Logger, Handler, Formatter e Level

# livelli logging - Ordine di severità
# - DEBUG -> Informazioni per il debug 
# - INFO -> Eventi normali funzionamento
# - WARNING -> Situazione anomale ma non critiche
# - ERROR -> Errori che impediscono il corretto funzionamento
# - CRITICAL -> Errori che bloccano completamente l'applicazione

# Handler: destinazione dei log
# - StreamHandler -> console
# - FindHandler -> file
# - RotatingHandler -> dimensioni di file

import logging as log

log.basicConfig(level=log.ERROR)

log.debug('Messaggio di debug')
log.info("Messaggio di info")
log.warning("messaggio di warning")
log.error("Messaggio di error")
log.critical("Messaggio di critical")