import requests
import json
import time
import pandas as pd

resp = requests.get('https://thesimpsonsquoteapi.glitch.me/quotes')

frase=resp.json()[0]['quote']
personaje=resp.json()[0]['character']

Lisa='Lisa Simpson'
Homer='Homer Simpson'

print (frase)
print (personaje)


temporizador=1
while temporizador==1:
    time.sleep(2)
    resp = requests.get('https://thesimpsonsquoteapi.glitch.me/quotes')
    frase=resp.json()[0]['quote']
    personaje=resp.json()[0]['character']
    Lisa='Lisa Simpson'
    Homer='Homer Simpson'

my_dict = {"test":1, "testing":2}

