import requests
dic={}
while True : 
    resp = requests.get('https://thesimpsonsquoteapi.glitch.me/quotes')
    frase=resp.json()[0]['quote']
    quitar = ",;:.\n!"
    for caracter in quitar:
        frase = frase.replace(caracter,"")
    
    frase2=frase.split()
    frase=frase2
    

    for cambiante in frase:
        if cambiante in dic:
            dic[cambiante]+=1
        else:
            dic[cambiante]=1
    
    for cambiante in dic:
        frecuencia = dic[cambiante]
        print(f"La palabra '{cambiante}' tiene una frecuencia de {frecuencia}")




'''
    texto='ademas de esta casa en zamora tambien tengo una casa en Canet de berenguer y hay viven mis padres'
    texto2=texto.split()
    texto=texto2

    for cambiante in texto:
        if cambiante in dic:
            dic[cambiante]+=1
        else:
            dic[cambiante]=1

    for cambiante in dic:
        frecuencia = dic[cambiante]
        print(f"La palabra '{cambiante}' tiene una frecuencia de {frecuencia}")

'''