
import time
import os
import urllib.request
import requests
import shutil

dic={}
i=0
w=0
while True:
    time.sleep(2)
    resp = requests.get('https://thesimpsonsquoteapi.glitch.me/quotes')
    personaje=resp.json()[0]['character']
    frase=resp.json()[0]['quote']
    url=resp.json()[0]['image']
    file= (f"Esta es la foto de {personaje}.png")

    if not (os.path.exists(personaje)):
        r=urllib.request.urlopen(url)
        f=open(file,'wb')
        f.write(r.read())
        f.close()
        os.mkdir(personaje)
        time.sleep(0.5)
        shutil.move(file,personaje)
        time.sleep(0.5)
    
    quitar = ",;:.\n!"
    for caracter in quitar:
        frase = frase.replace(caracter,"")
    
    frase2=frase.split()
    frase=frase2
    

    for cambiante in frase:
        if cambiante in dic:
            dic[cambiante]=w
        else:
            dic[cambiante]=w
        w+=1
    print (dic)
