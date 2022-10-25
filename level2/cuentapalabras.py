import requests

dic={}
i=0
w=0

while True: 
    resp = requests.get('https://thesimpsonsquoteapi.glitch.me/quotes')
    frase=resp.json()[0]['quote']
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
    
  