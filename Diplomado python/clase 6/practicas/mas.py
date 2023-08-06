import requests

monto = input("Ingresa el monto a convertir:")
divisaOrigen = input("Ingresa la divisa origen (MXN/USD/EUR):")
divisaDestino = input("Ingresa la divisa destino (MXN/USD/EUR):")

header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
#r = requests.get('https://api.frankfurter.app/latest?amount='+monto+'&from='+divisaOrigen+'&to='+divisaDestino
#, data={'key': 'value'}, headers=header)
#print(r.content)

datos = {'amount': monto, 'from': divisaOrigen, 'to':divisaDestino}
r = requests.get("https://api.frankfurter.app/latest", params=datos, headers=header)
print(r.content)
print("-------------------------------------------")
print(r.json())