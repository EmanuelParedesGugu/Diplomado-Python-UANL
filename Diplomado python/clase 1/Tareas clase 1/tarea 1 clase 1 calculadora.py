num1= int(input("Ingresa un numero: "))
num2= int(input("Ingresa otro numero: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print("Tienes el numero " + str(num1) +  " y " + str(num2) + " seleccione la operacion que desea realizar con ellos: \n 1.Suma \n 2.Resta \n 3.Multiplicación \n 4.División")
operacion = input("selecciona la operación: ")

if operacion == "suma":
    print(suma)
elif operacion == "resta":
    print(resta)
elif operacion == "multiplicacion":
    print(multiplicacion)
elif operacion == "division":
    print(division)



