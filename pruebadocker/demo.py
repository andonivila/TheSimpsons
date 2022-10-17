import time 
import random 

while True :
    numero=random.randint(1,10)
    time.sleep(2)
    print (numero)
    if numero < 6 :
        print ("Entre el 1 y el 5")
    else :
        print ("Entre el 6 y el 10")

