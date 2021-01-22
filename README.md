# Continuous-integration-IIOT

<p align="center">
  <img src="/ref/logo.png?raw=true" />
</p>

## Esercizio 1

### Consegna

Sia dato il seguente messaggio in codice:

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

### Formula utilizzata

Seguendo la consegna la formula che otteniamo sarà `y = 19 * x % 29` 

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
- `findCryptoKey()` → l'algoritmo si compone di quanto segue:
  - creazione di an array ausiliario `AUX_ALPHABET = []` 
  - scansione di ogni lettera `letter` presente nell'array `ALFABETO_LATINO` 
    - salvataggio della posizione di `letter` presente in `ALFABETO_LATINO`
    - utilizzando la formula citata in [precedenza](https://github.com/MarcoCollarini/Continuous-integration-IIOT/blob/main/README.md#formula-utilizzata) otteniamo la posizione       di `letter` all'interno di `ALFABETO_CRIPTATO`
    - salvataggio della lettera criptata all'interno di `AUX_ALPHABET`
  - `return` di `AUX_ALPHABET`
> *NB: Questo array ci permette di accoppiare le lettere dell'alfabeto latino con quelle dell'alfabeto criptato*
    
- `decryptSentence(decryptKey : [])` → questo algoritmo prende come parametro di input il vettore delle lettere criptate `ALFABETO_DECRIPTATO` ed esegue le seguenti operazioni:
  > ALFABETO_DECRIPTATO = *findCryptoKey()*
  
  > *decryptSentence*(ALFABETO_DECRIPTATO)
  - creazione di una variabile ausiliaria `decryptedSentence = ""`
  - scansione di ogni lettera `letter` presente nella stringa `FRASE`
    - concatenazione della lettera presente in `ALFABETO_LATINO` nella posizione di `letter` all'interno dell'array `decryptKey` 
      > *decryptedSentence += ALFABETO_LATINO[decryptKey.index(letter)]*`
  - `return` di `decryptedSentence`
  
### Conclusioni

Eseguendo il codice la stringa `FRASE = VCZJCZIZJMZJLXYHMJYHEMCWSJM\WZNCXWJSYQXWZCOXJHMCJDVSOJ\HYHWWZOH@ ` viene decriptata in `UTI TIBI SI VOLES LENSTRA SCRIPTOR ALGORITMO EST QUAM CELERRIME.`.

In seguito abbiamo pensato di sviluppare un algoritmo che fosse in grado di criptare un messaggio scritto in chiaro utilizzando la [formula](https://github.com/MarcoCollarini/Continuous-integration-IIOT/blob/main/README.md#formula-utilizzata). 

Messaggio criptato: 

`ZYJCVXJOHMMSQQZXJHJMCSCXJRH\WZNCSCX@JSYYSJNWXMMZOS@`

## Esercizio 2

### Consegna

Sia dato un numero intero `0 < n < 10.000.000.000`, proporre un programma che lo fattorizzi nei suoi fattori primi. Deve essere implementato il tempo di esecuzione del programma mediante la libreria `time`. Il voto del programma verrà dato in base al tempo di esecuzione del programma in particolare su tre numeri assegnati al momento della verifica seguendo il seguente criterio: 
- Vengono calcolati i tempi di esecuzione di ciascun programma a meno di 6 cifre decimali.
- Viene valutato il corretto output del programma
- Viene stilata una classifica delle tempistiche tra i programmi con il corretto output e stabilito il voto. Migliore sarà il tempo, migliore sarà il voto. Il tempo più basso avrà voto 100/100. Il tempo peggiore, se rispetterà l'output, avrà voto 60/100.
- Verranno assegnati voti negativi se l'output richiesto non verrà raggiunto.

## Algoritmo utilizzato 

Nonostante "l'indizio" rivelato dall'[esercizio precedente](https://github.com/MarcoCollarini/Continuous-integration-IIOT/blob/main/README.md#conclusioni), abbiamo deciso di utilizzare l'algoritmo di `Trial Division`, perchè dopo alcune ricerche online ci sembrava il più efficiente. 





# Il team

- [**Marco Collarini**](https://github.com/MarcoCollarini)
- [**Alessandro Vendrame**](https://github.com/alessandrovendrame)



      


