import time
import pandas as pd

while True:
    time.sleep(2)
    print('Hola')
    datos={'Esto':['Funciona']}
    df=pd.DataFrame(datos)
    df.to_csv("C:\\Users\\Usuario\\Documents\\GitHub\\TheSimpsons\\2ºDiaPruebas 2.0\\a.csv",mode='a')