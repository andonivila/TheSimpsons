import pandas as pd
import time


while True:
    time.sleep(2)
    data={"CACA":["puta"]} 
    print('Hola') 
    df=pd.DataFrame(data)  
    df.to_csv("C:\\Users\\Usuario\\Documents\\GitHub\\TheSimpsons\\1º Parte\\ASCO\\main\\Lisa\\asco.csv", mode='a')

