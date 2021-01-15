# Continuous-integration-IIOT

<p align="center">
  <img src="/ref/logo.png?raw=true" />
</p>

## Esercizio 1

### Consegna

Sia dato il messaggio seguente in codice:

 `V C Z J	C	Z	I	Z	J	M	Z	J	L	X	Y	H	M	J	Y	H	E	M	C	W	S	J	M	\	W	Z	N	C	X	W	J	S	Y	Q	X	W	Z	C	O	X	J	H	M	C	J	D	V	S	O	J	\	H	Y	H	W	W	Z	O	H	@`

Si scriva un programma che proponga una possibile decriptazione dello stesso sapendo che il messaggio originale è in LATINO e che è stato utilizzato un carattere anche per la spaziatura (il carattere J). Se decriptato fornisce un consiglio per l'esercizio successivo. Il voto viene dato dalla valutazione del modo utilizzato per la decriptazione. Informazioni aggiuntive:
- E' un codice che usa una formula y = f(x) mod p con p un primo
- E' importante sapere di cosa si parla
- Il messaggio da un'informazione per il progetto 2

### Ragionamento

Stando a quanto dice la consegna, per tradurre la frase criptata abbiamo bisogno di trovare la formula *f(x)*, tale che *y = f(x) mod p* con *p* primo dia come risultato la posizione
della lettera corrispondente a quella letta dalla frase codificata.

Per ottenere questo risultato abbiamo inanzitutto analizzato l'alfabeto utilizzato nella parola codificata, già sapendo che il carattere *J* equivale ad uno spazio e
ipotizzando che il carattere *@* fosse un punto.

> ***Fase di ricerca della chiave di criptazione***

Abbiamo inizialmente ipotizzato che l'afabeto utilizzato nella frase cifrata fosse a 28 lettere, di conseguenza bisogna trovare un numero x tale che ***posizioneLettera * x % 29*** dia come risultato la posizione della lettera nell'alfabeto "latino". Il modulo di 29, che è un numero primo, è dovuto dal fatto che nell'alfabeto sono presenti
28 lettere e facendo il modulo di 29 abbiamo la possibilità di impostare un *range*, garantendo l'associazione di tutti i caratteri.

Abbiamo tradotto parte della frase manualmente per avere dei dati su cui basarci. I risultati ottenuti sono i seguenti:

```
S (19) -> M (13)
T (20) -> C (3)
U (21) -> V (22)
V (22) -> L (12)
```
Assumendo che `p = 29` possiamo notare che l'incremento tra le lettere successive di destra (mod 29) è 19. 

Quindi `f(x) = 19*x`.

### Sviluppo

> ***Creazione variabili***
```
FRASE = "OZJ[SJOXYCXYNZS\HWHJXWSJISE\SJMXYXJVEJNWXQWSOOSJ[SCCXJIHEH@"
ALFABETO_LATINO =   ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","\\"," ","."] 
ALFABETO_CRIPTATO = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","[","\\", "@"]
```
- FRASE → Codice da decriptare, paramentro dato in input
- ALFABETO_LATINO → Vettore contenente le lettere dell'alfabeto, aggiungendo alcuni caratteri speciali
- ALFABETO_CRIPTATO → Vettore contenete le lettere dell'ipotetico alfabeto cifrato

> ***Creazione funzioni***
- `findCryptoKey()` → 
- `decryptSentence(decryptKey : [])` → 


