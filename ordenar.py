#carga el archivo Productos.json
#muestra los productos ordenados descendente por nombre
import pandas as pd
import json

df=pd.read_json('Productos.json')
print(df)
df_sorted=df.sort_values(by=['nombre'])
print(df_sorted)