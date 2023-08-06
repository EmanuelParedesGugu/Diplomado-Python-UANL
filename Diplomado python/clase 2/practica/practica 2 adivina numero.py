import random

numero = random.randint(1, 20) 
#adivinanza = int(input("Adivina el número del 1 al 20 tienes tres intentos: "))
intentos = 0

while intentos < 3:
    intentos += 1
    adivinanza = int(input("Adivina el número del 1 al 20: "))

try:
    if adivinanza == numero:
        print("Ganaste un premio")
    else:
        print("Intenta de nuevo:", numero)

    if intentos == 3:
        print("Se acabaron los intentos el número era: ", numero)
    
except:
    print("Hubo un error.")




#try:
  #  r = requests.get(pagina)

   # if r.status_code == 200:
    #    print('Página encontrada')
     #   print(r.content)
    #else:
      #  print('ERROR')
#except requests as error:
 #   print('Error al acceder a la página:', error)

