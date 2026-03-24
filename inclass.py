testo = '''
Day after day, day after day,
We stuck, nor breath nor motion;
As idle as a painted ship
Upon a painted ocean.

Water, water, every where,
And all the boards did shrink;
Water, water, every where,
Nor any drop to drink.

The very deep did rot: O Christ!
That ever this should be!
Yea, slimy things did crawl with legs
Upon the slimy sea.

About, about, in reel and rout
The death-fires danced at night;
The water, like a witch's oils,
Burnt green, and blue and white.
'''





##punto 1 esercizio 2
diviso =testo.split('\n')
contatore =0
for riga in diviso:
    if len(riga)>0:
        contatore=contatore+1
print('Il numero di righe è:',contatore)

##punto 2 ##utile splitines
parole=testo.split()
print('Il totale delle parole è',len(parole))

##punto 3 ##passare da stringa a lista
'''Contate i caratteri alfanumerici che compongono l’estratto'''
alfanumerici="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
caratteri=0
for i in testo:##gli elementi di testo sono i caratteri, quindi i è un carattere: testo è una stringa!!!!(gli elementi di una stringa sono i caratteri)
  for valido in alfanumerici: ##alterantiva: usare direttamente for i in alfanumerici
    if i==valido:
      caratteri=caratteri+1
print('Il numero di caratteri è: ',caratteri)

##punto 4
'''Chiedere all’utente una lettera e contate quante volte compare nel testo'''
alfabeto="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
letter=input('Scegli una lettera:  ')
while letter not in alfabeto:
  letter=input('Carattere non valido. Selezionare una lettera: ')
print('conteggio: ',testo.count(letter))

#punto 5
'''Sostituite tutte le parole day, water e about con la parola PYTHON in tutti i versi'''
new_testo=[]
for i in parole:
  if i.lower() not in ["day","water","about"]:
    new_testo.append(i)
  else :
    new_testo.append("PYTHON")
print(new_testo)
#renderlo un testo come prima
new_testo_stringa=""
for i in new_testo:
  new_testo_stringa=new_testo_stringa+i+" "
print(new_testo_stringa)

#punto 6
'''Riscrivete il testo in modo che tutte le parole in posizione dispari siano scritte in maiuscolo'''
testo_upper=[]
j=0
for i in parole:
  j=j+1
  if j%2!=0:
    testo_upper.append(i.upper())
  else:
    testo_upper.append(i)

#punto 7
'''Riscrivere il testo invertendo l’ordine delle frasi dal basso all’alto.'''
testo_contrario=[]
for i in range(len(diviso)-1,-1,-1): ##primo -1 perchè vogliamo includere lo 0, secondo -1 per decrementare
  testo_contrario.append(diviso[i])

#punto 8

'''Riscrivete il testo in modo che il secondo verso di ogni strofa sia scritto a specchio (cioè al contrario carattere per carattere: Ad esempio, questa frase’ –> ‘esarf atseuq ,oipmese dA’)'''
testo_modificato=[]
for i in range( len(diviso)):
  if i%4==1:
    testo_modificato.append(diviso[i][::-1]) ##slicing negativo
  else:
    testo_modificato.append(diviso[i])
  
#punto 9
'''Trovate eventuali parole che compaiono in tutte le strofe'''
'''strofe=testo.split("\n\n")
parole_strofe=strofe.split()
set_parole_strofe={parole_strofe
                }'''