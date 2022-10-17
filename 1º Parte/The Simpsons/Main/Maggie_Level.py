import requests
import time
import pandas as pd

while True:
    time.sleep(1)
    resp = requests.get('https://thesimpsonsquoteapi.glitch.me/quotes')
    frase=resp.json()[0]['quote']
    personaje=resp.json()[0]['character']
    Lisa='Lisa Simpson'
    Homer='Homer Simpson'
    print (frase)
    print (personaje)
    if personaje==Lisa:
        Lisa_Frase = {'Frase': [f'{frase}'], 'Personaje':[f'{personaje}']}
        df=pd.DataFrame(Lisa_Frase)
        df.to_csv('C:\\Users\\Usuario\\Documents\\GitHub\\TheSimpsons\\1º Parte\\The Simpsons\\Lisa\\lisa.csv', mode='a' , header=True, index=False)
    elif personaje==Homer:
        Homer_Frase = {'Frase': [f'{frase}'], 'Personaje' : [f'{personaje}']}
        df=pd.DataFrame(Homer_Frase)
        df.to_csv('C:\\Users\\Usuario\\Documents\\GitHub\\TheSimpsons\\1º Parte\\The Simpsons\\Homer\\homer.csv', mode='a' , header=True, index=False)
    else: 
        Resto_Frase = {'Frase': [f'{frase}'], 'Personaje' : [f'{personaje}']}
        df=pd.DataFrame(Resto_Frase)
        df.to_csv('C:\\Users\\Usuario\\Documents\\GitHub\\TheSimpsons\\1º Parte\\The Simpsons\\General\\general.csv', mode='a' , header=True, index=False)
