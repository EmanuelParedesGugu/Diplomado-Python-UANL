import json

dictFrutas = {"Fruta" : "Papaya" , "Precio" : 30, "Unidades" : 100}
info = open('c:/Python/Frutas.json',)
frutas = json.load(info)
frutas["Frutas"].append(dictFrutas)

print(frutas["Frutas"])