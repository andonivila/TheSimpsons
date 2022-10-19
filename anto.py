import requests

resp = requests.get('https://thesimpsonsquoteapi.glitch.me/quotes')

print(resp)
frase=resp.json()

print(frase)