##############################Programma svolto da################################
######################Vendrame Alessandro, Collarini Marco#######################
###Dopo una ricerca abbiamo deciso di utilizzare l'algoritmo di Trial Division###
#################################################################################
import time

def fattorizzazione(n: int):        # Funzione che fattorizza di 'v'
    array = []                      # Creazione dell'array dentro al quale verranno salvati i fattori di 'n'
    while n % 2 == 0:               
        array.append(2)             # Finchè il resto di n/2 sarà 0 inserisce '2' in 'array' 
        n /= 2
    f = 3                           # Creazione di 'f = 3' dove 'f' è il prossimo numero primo che va a dividere 'n'
    while f * f <= n:               
        if n % f == 0:  
            array.append(f)         # Finchè 'f' moltiplicato per se stesso (per velocizzare la 'ricerca') è <= di 'n' e se il resto di 'n'/'f' è 0, allora aggiungi 'f' ad 'array' 
            n /= f                  # Si divide 'n' per 'f'
        else:
            f += 2                  # Altrimenti finchè 'f' moltiplicato per se stesso è <= di 'n' aggiungi 2 ad 'f' (rimane dispari)
                                    # Solo i numeri dispari sono primi :D
    if n != 1: array.append(n)      # Se 'n' è 1 non viene aggiunto in 'array'
    return array                    # Ritorna 'array'

def calcola_ripetizioni(v : []):            # Funzione che calcola le ripetizioni dei numeri all'interno di 'v'
    ripetizioni = []                        # Creazione di array ausiliario 'ripetizioni' 

    for x in v:                             # Per ogni numero in 'v'
        trovato = False                     # Variabile ausiliaria che permette di capire se il numero è stato trovato o meno
        for couple in ripetizioni:          # Scorre il vettore 'ripetizioni'
            if couple[0] == x:              # Se in ripetizioni è già presente il numero
                couple[1] += 1              # Viene incrementata il valore delle volte in cui appare
                trovato = True              

        if not trovato:
            ripetizioni.append([x,1])       # Nel caso in cui non fosse stato trovato, viene aggiunta la coppia [x,1]
    return ripetizioni                      # Ritorna 'ripetizioni'

def stampa(v:[]):                                                           # Funzione che formatta e stampa il risultato ottenuto 
    res = ""                                                                # Creazione di stringa ausiliaria 'res' 
    for x in v:                                               # Cicla fino alla fine di 'v'
        if(x[1] > 1):                    
            if v.index(x) != len(v)-1:                                   
                res += str(x[0]) + "^" + str(x[1]) + " * "      # Se il numero nel quale 'n' si ripete è > 1 e se il valore letto non è l'ultimo allora aggiunge in 'res' la stringa 
        else: 
            if v.index(x) != len(v)-1:
                res += str(x[0]) + " * "                        # Se il numero nel quale 'n' si ripete è == 0 e se il valore letto non è l'ultimo allora aggiunge in 'res' la stringa 
            else:
                res += str(x[0])                                # Altrimenti se è l'ultimo numero aggiunge in 'res' la stringa 
    return res                                                  # Ritorna res

n = int(input("Inserisci un numero: "))                         # Richiede in input il valore di 'n'

start_time = time.time()                                        # Start cronomentro 

v = calcola_ripetizioni(fattorizzazione(n))                     # Richiama la funzione calcola_ripetizioni() passando come paramentro il risultato ritornato da fattorizzazione(n)

tempo_impiegato = round(time.time() - start_time, 5)            # Stop cronometro 

print(stampa(v))                                                # Stampa risultato
print("Tempo di esecuzione: " + str(tempo_impiegato))           # Stampa il tempo di esecuzione