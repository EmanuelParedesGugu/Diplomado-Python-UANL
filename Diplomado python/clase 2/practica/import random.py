import requests

pagina = input('Inserte página: ')

try:
    r = requests.get(pagina)

    if r.status_code == 200:
        print('Página encontrada')
        print(r.content)
    else:
        print('Página no encontrada')
except requests.exceptions.RequestException as e:
    print('Error al acceder a la página:', e)
