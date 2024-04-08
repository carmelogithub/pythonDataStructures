import json
import pandas as pd

lista=[15,20,'sevilla',36,20,'valencia',14]
#print(lista)
conjunto=set(lista)
#print(conjunto)

datos=pd.read_json('datos.json')
#print(datos)
df=pd.DataFrame(datos)
#print(df)
#eliminar duplicados de un DataFrame
#df.duplicated(df.columns[~df.columns.isin(['precio'])])
print(df.duplicated(df.columns[~df.columns.isin(['nombre'])]))
#sólo elimina duplicados si tienes todo el dict igual


df_sinduplicado=df.drop_duplicates(df.columns[~df.columns.isin(['nombre'])],keep='first')
print(df_sinduplicado)