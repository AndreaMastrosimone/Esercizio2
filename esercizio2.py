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

'''Contate le righe non vuote che compongono l’estratto'''
diviso=testo.split('\n') ##contiene alcuni elementi che sono 'il nulla' che si trovava fra i due spazi. ##si poteva usare .splitlines()
count=0
for i in diviso: ## signfica per ogni i che è un valore in diviso
  if i!= "": 
    count=count+1
print('Le righe non vuote sono',count)

'''Contate le parole che compongono l’estratto'''
parole=testo.split()
print('Il totale delle parole è',len(parole))

'''Contate i caratteri alfanumerici che compongono l’estratto'''
alfanumerici="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
caratteri=0
for i in testo:
  for valido in alfanumerici:
    if i==valido:
      caratteri=caratteri+1
print('Il numero di caratteri è: ',caratteri)

'''Chiedere all’utente una lettera e contate quante volte compare nel testo'''
print('Scegli una lettera')


