import json

productos = open('c:/Python/Frutas.json',)
# retorna objeto JSON como diccionario
data = json.load(productos)
print(data)
print("--------Iteracion de Json----------")
#Itera json para imprimir cada elemento
for elemento in data['Frutas']:
    print(elemento)