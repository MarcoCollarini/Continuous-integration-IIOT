FRASE = "IL TUO MESSAGGIO E STATO DECRIPTATO."
ALFABETO_LATINO =   ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","\\"," ","."] 
ALFABETO_CRIPTATO = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","[","\\", "@"]
WORDS = []

def findCryptoKey():
    AUX_ALPHABET = []
    for letter in ALFABETO_LATINO:
        #print(letter)
        letterPosition = ALFABETO_LATINO.index(letter)+1
        cryptLetterPosition = ((letterPosition * 19) % 29)-1
        AUX_ALPHABET.append(ALFABETO_CRIPTATO[cryptLetterPosition])
        #print(letterPosition)
        #print(cryptLetterPosition)
        #print(ALFABETO_CRIPTATO[cryptLetterPosition])
    return AUX_ALPHABET

def decryptSentence(decryptKey : []):
    decryptedSentence = ""
    for letter in FRASE:
        decryptedSentence += decryptKey[ALFABETO_LATINO.index(letter)]
    return decryptedSentence

ALFABETO_DECRIPTATO = findCryptoKey()
print(FRASE)
print(decryptSentence(ALFABETO_DECRIPTATO))
#print(longestWord())
print(ALFABETO_LATINO)
print(ALFABETO_CRIPTATO)
print(ALFABETO_DECRIPTATO)




