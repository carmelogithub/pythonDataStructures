lista=[1,2,"madrid",2.3,True,'juan',15] #soporta diferentes tipos de datos
print(lista)
print(lista[2]) #indice de la lista siempre comienza en el 0
print(lista[-1]) #muestra el item desde el final de la lista

lista.append("nuevo")
print(lista)
lista.insert(2,"otro")
print(lista)
lista.append("nuevo") #soporta duplicados
print(lista)
lista.sort() #lista soporte sorted, pero genera exception si hay datos heterogéneos
print(lista)
