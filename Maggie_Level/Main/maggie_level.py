'''
En este caso:
Requests permite pedirle informacion a la API 
Time nos permite hacer pausas durante el codigo
Pandas nos permite introducir los datos que queramos en un CSV
''' 
import requests
import time
import pandas as pd

#While -> True crea un bucle infinito
while True:
    time.sleep(30)
    #Requests.Get crea una peticion GET (https://www.ionos.es/digitalguide/hosting/cuestiones-tecnicas/http-request/)
    resp = requests.get('https://thesimpsonsquoteapi.glitch.me/quotes')
    #La API nos entrega un "paquete" (lista de diccionarios) con distintos datos, de los cuales solo nos interesan 2
    '''
    Llamamos al contenido de la respuesta de la API con () 
    de todo el contenido, nos interesa el primer diccionario [0]
    y de todo el diccionario queremos el valor de la llave ['quote']
    ''' 
    frase=resp.json()[0]['quote']
    personaje=resp.json()[0]['character']
    '''
    Como vamos a clasificar las quote dependiendo del personaje que lo diga
    creamos 2 variables para comparar
    '''
    Lisa='Lisa Simpson'
    Homer='Homer Simpson'
    '''
    El 1º criterio es que la frase la diga Lisa, si personaje es = Lisa Simpson
    crearemos un diccionario con 2 llaves y 2 valores, las llaves seran Frase y Personaje
    y sus valores descargados de la API 
    '''
    '''
    Creamos un DataFrame con el diccionario y lo introducimos en el CSV, 
    mode = 'a' nos permite introducir datos en el CSV sin sobrescribir los datos 
    Con Header True podremos ver las llaves de nuestro diccionario, es decir Frase y Personaje
    Y con Index False eliminamos un contador  
    '''
    if personaje==Lisa:
        Lisa_Frase = {'Frase': [f'{frase}'], 'Personaje':[f'{personaje}']}
        df=pd.DataFrame(Lisa_Frase)
        df.to_csv('C:\\Users\\Usuario\\Documents\\GitHub\\TheSimpsons\\Maggie_Level\\Main\\lisa.csv', mode='a' , header=True, index=False)
    elif personaje==Homer:
        Homer_Frase = {'Frase': [f'{frase}'], 'Personaje' : [f'{personaje}']}
        df=pd.DataFrame(Homer_Frase)
        df.to_csv('C:\\Users\\Usuario\\Documents\\GitHub\\TheSimpsons\\Maggie_Level\\Main\\homer.csv', mode='a' , header=True, index=False)
    else: 
        Resto_Frase = {'Frase': [f'{frase}'], 'Personaje' : [f'{personaje}']}
        df=pd.DataFrame(Resto_Frase)
        df.to_csv('C:\\Users\\Usuario\\Documents\\GitHub\\TheSimpsons\\Maggie_Level\\Main\\general.csv', mode='a' , header=True, index=False)
