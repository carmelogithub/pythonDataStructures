import pandas as pd
data=[
{'nombre':'marta','ciudad':'madrid','unidades':100},
{'nombre':'luis','ciudad':'sevilla','unidades':70},
{'nombre':'sofia','ciudad':'valencia','unidades':120},
{'nombre':'laura','ciudad':'madrid','unidades':130}
]
#print(data)
print(data[2]['nombre'])
data[2]['nombre']='victoria' #update
print(data[2]['nombre'])
#data.sort() #genera un error, no porque la list no soporta sort, sino porque la list contiene dict
#print(data)
nuevo={'nombre':'marta','ciudad':'madrid','unidades':100}
dictOrdenado=sorted(nuevo.items(), key=lambda x:x[0])
print(dictOrdenado)

df=pd.DataFrame(data)
print(df)
df_sorted=df.sort_values(by=['ciudad'])
print(df_sorted)