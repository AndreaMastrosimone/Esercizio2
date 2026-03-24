import sys
'''print('ciao, ',sys.argv[1])##se non metto niente dopo argv, mi da errore, perchè non sa cosa stampare, se invece metto qualcosa, lo stampa. dice che l'indice è maggiore perchè non esiste se non metto nulla
print(sys.argv)'''

## la fregatura sta nel: se il programma è complicato devo ricordare l'ordine sennò si sballa.
## inoltre magari non ricordiamo perchè passiamo come parametro in input pippo, e non sappiamo cosa sia, e quindi non sappiamo cosa scrivere in input, e quindi ci da errore.
##quindi viene in aiuto argparse, che è una libreria che ci permette di gestire gli argomenti in input in modo più semplice e intuitivo, e ci permette di dare un nome agli argomenti, e di specificare se sono obbligatori o opzionali, e di specificare il tipo di dato, e di specificare un messaggio di aiuto, e di gestire gli errori in modo più semplice.
import argparse

# costruisce ed inizializza un oggetto ArgumentParser e lo assegna alla variabilie parser
parser = argparse.ArgumentParser()## gestisce tutti gli input del programma... bisogna registrarle con addargument
parser.add_argument('-n','--nome_esteso', help='Descrizione del parametro')
parser.add_argument('-b','--boolean_value', action='store_true', help="imposta il valore 'True' se trova il parametro")
parser.add_argument('-d','--con_default',  default='riferimento', help="Parametro che ha già un valore di default se non viene fornito l'argomento")

args = parser.parse_args() # fa il parsing degli argomenti da linea di comando e li memorizza in un oggetto args
## cercare di usare argparse per gestire gli argomenti in input, invece di sys.argv, perchè è più semplice e intuitivo, e ci permette di ricordare meglio cosa stiamo passando in input