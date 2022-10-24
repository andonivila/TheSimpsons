import os
import urllib.request
import requests
import shutil

resp = requests.get('https://thesimpsonsquoteapi.glitch.me/quotes')
personaje=resp.json()[0]['character']
url=resp.json()[0]['image']
file= (f"Esta es la foto de {personaje}.png")

r=urllib.request.urlopen(url)
f=open(file,'wb')
f.write(r.read())
f.close()


os.mkdir(personaje)

shutil.move(file,personaje,copy_function=shutil.copy)
shutil.move(personaje,'Lisa_Level',copy_function=shutil.copy)



