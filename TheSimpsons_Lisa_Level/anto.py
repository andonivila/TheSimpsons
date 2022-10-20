import requests
from funcionpalabras import frecuencia_palabras

resp = requests.get('https://thesimpsonsquoteapi.glitch.me/quotes')

frase=resp.json()[0]['quote']

La_Frase = {'Frase': [f'{frase}']}

texto='You are providing a string representation of a dict to the DataFrame constructor, and not a dict itself. So this is the reason you get that error.'


frecuencia_palabras(texto)