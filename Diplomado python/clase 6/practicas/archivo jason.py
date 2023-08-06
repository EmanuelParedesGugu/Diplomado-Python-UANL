import json

# Abre archivo JSON

f = open('data_file.json',)

# retorna objeto JSON como diccionario

data = json.load(f)

#Imprime contenido completo

print(data)

# Cierra archivo

f.close()