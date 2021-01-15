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

Abbiamo inizialmente ipotizzato che l'afabeto utilizzato nella frase cifrata fosse a 28 lettere, di conseguenza bisognava trovare un numero x tale che ***posizioneLettera * x % 29***
desse come risultato la posizione della lettera nell'alfabeto "latino". Il modulo di 29, che è un numero primo, è dovuto dal fatto che nell'alfabeto sono presenti
28 lettere e facendo il modulo di 29 abbiamo la possibilità di impostare un *range*, garantendo l'associazione di tutti i caratteri.


