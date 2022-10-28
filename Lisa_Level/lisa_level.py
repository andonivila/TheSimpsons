'''
En este caso:
Time nos permite hacer pausas durante el codigo
OS nos permite crear carpetas 
Urllilb.requests nos permite descargar una imagen de una URL concreta 
Requests nos permite hacer una peticion GET a una API 
Shutil nos permite mover un archivo a una carpeta, en este caso una foto a su carpeta

'''
import time
import os
import urllib.request
import requests
import shutil

'''
Creamos un diccionario vacio para guardar un contador de las palabras 

'''
dic={}
i=0
w=0
while True:
   
    time.sleep(2)
    '''
    Requests.Get crea una peticion GET (https://www.ionos.es/digitalguide/hosting/cuestiones-tecnicas/http-request/)
    '''
    resp = requests.get('https://thesimpsonsquoteapi.glitch.me/quotes')
    '''
    Llamamos al contenido de la respuesta de la API con () 
    de todo el contenido, nos interesa el primer diccionario [0]
    y de todo el diccionario queremos el valor de la llave ['quote']
    '''
    personaje=resp.json()[0]['character']
    frase=resp.json()[0]['quote']
    '''
    URL guarda la URL donde se encuentra la imagen que quremos descargar
    '''
    url=resp.json()[0]['image']
    '''
    Con la variable file podemos darle un nombre a la imagen que vamos a descargar
    igual que el personaje, y ademas le damos la extension .png que nos permite 
    abrirla 
    '''
    file= (f"Esta es la foto de {personaje}.png")

    '''
    No podemos tener 2 directorios con el mismo nombre, 
    por eso if not nos permite comprobar si existe ya una carpeta 
    que se llame como el personaje 

    Si no existe descargaremos la imagen de la URL de la API
    Crearemos una carpeta con el nombre del personaje 
    Y cogeremos la imagen que se llamara  como el personaje gracias a la variable file
    y lo meteremos en su carpeta correspondiente

    '''
    if not (os.path.exists(personaje)):
        r=urllib.request.urlopen(url)
        f=open(file,'wb')
        f.write(r.read())
        f.close()
        os.mkdir(personaje)
        time.sleep(0.5)
        shutil.move(file,personaje)
        time.sleep(0.5)
    
    '''
    De aqui en adelante vamos a descargar las frases
    y contar el orden en el que van entrando
    '''
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
