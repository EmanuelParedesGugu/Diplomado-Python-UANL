import requests

pagina = input('Inserte página: ')

try:
    r = requests.get(pagina)

    if r.status_code == 200:
        print('Página encontrada')
        print(r.content)
    else:
        print('ERROR')
except requests.exceptions.RequestException as error:
    print('Error al acceder a la página:', error)
