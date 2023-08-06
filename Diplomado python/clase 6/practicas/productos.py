import json

#descargar archivo jason por que no funciona la ruta
productos = open('c:/descargas/jsonProductos.json',)
# retorna objeto JSON como diccionario
data = json.load(productos)
print(data)
print("--------Iteracion de Json----------")
#Itera json para imprimir cada elemento
for elemento in data['Productos']:
    print (elemento)