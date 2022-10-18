import pandas as pd
import time 

while True:
    time.sleep(2)
    print('Hola')
    datos_main={"Hola":["Adios"]}
    df=pd.DataFrame(datos_main)
    df.to_csv("C:\\Users\\Usuario\\Documents\\GitHub\\TheSimpsons\\2ºDiaPruebas\\main\\p.csv", mode='a')

