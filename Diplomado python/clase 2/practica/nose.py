import random

numero = random.randint(1, 20) 
adivinanza = int(input("Adivina el número del 1 al 20 tienes un intento: "))

try:
    adivinanza = numero
    print("ganaste")
except:
    print("perdistes")
