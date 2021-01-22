FRASE = "OZJ[SJOXYCXYNZS\HWHJXWSJISE\SJMXYXJVEJNWXQWSOOSJ[SCCXJIHEH@"                                                                           # STRINGA DI INPUT
ALFABETO_LATINO =   ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","\\"," ","."]      # Array contenente l'alfabeto "normale"
ALFABETO_CRIPTATO = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","[","\\", "@"]     # Array contenente l'alfabeto in codice
WORDS = []                                                                                                                                      # Array che conterrà le parole    

def findCryptoKey():                                                                # Funzione che permette di costruire una mappa di decriptazione
    AUX_ALPHABET = []                                                               # Creazione di un array ausiliario
    for letter in ALFABETO_LATINO:                                                  # Per ogni lettera presente nell'alfabeto
        #print(letter)
        letterPosition = ALFABETO_LATINO.index(letter)+1                            # Salva la posizione della lettera nell'alfabeto
        cryptLetterPosition = ((letterPosition * 19) % 29)-1                        # Esegue il calcolo spiegato nella documentazione e salva il risultato
        AUX_ALPHABET.append(ALFABETO_CRIPTATO[cryptLetterPosition])                 # Aggiunge all'alfabeto "mappa" la lettera che si trova in posizione 'cryptLetterPosizion' 
        #print(letterPosition)
        #print(cryptLetterPosition)
        #print(ALFABETO_CRIPTATO[cryptLetterPosition])
    return AUX_ALPHABET                                                             # Ritorna la mappa

def decryptSentence(decryptKey : []):                                               # Funzione che decripta la stringa in codice
    decryptedSentence = ""                                                          # Stringa ausiliaria
    for letter in FRASE:                                                            # Per ogni lettera nella stringa in codice
        decryptedSentence += ALFABETO_LATINO[decryptKey.index(letter)]              # Aggiunge alla stringa ausiliaria la lettera corrispondente
        print(letter)
        print(decryptKey.index(letter))
        print(ALFABETO_LATINO[decryptKey.index(letter)])
        
    return decryptedSentence                                                        # Ritorna la stringa decriptata



ALFABETO_DECRIPTATO = findCryptoKey()                                               # Creazione dell'alfabeto "mappa"
print(FRASE)
print(decryptSentence(ALFABETO_DECRIPTATO))                                         # Stampa la frase decriptata

print(ALFABETO_LATINO)
print(ALFABETO_CRIPTATO)
print(ALFABETO_DECRIPTATO)




