import random

numero = random.randint(1, 20)

adivinanza = int(input("Adivina el número del 1 al 20, tienes tres intentos: "))

try:
    if adivinanza == numero:
        print("¡Ganaste un premio!")
    else:
        print("Lo siento, el número era", numero)




#try:
  #  r = requests.get(pagina)

   # if r.status_code == 200:
    #    print('Página encontrada')
     #   print(r.content)
    #else:
      #  print('ERROR')
#except requests as error:
 #   print('Error al acceder a la página:', error)

