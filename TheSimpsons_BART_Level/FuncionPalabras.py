import requests
import matplotlib.pyplot as plt
dic={}
i=0
while i<2 : 
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
    i+=1

keys=[]
valores=[]

for a in dic:
 keys.append(a)
for b in dic.values():
    valores.append(b)

plt.bar(keys, height=valores)
plt.show()

