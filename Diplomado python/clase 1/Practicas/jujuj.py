def calculator(operation, num1, num2):
    if operation == "suma":
        result = num1 + num2
        print(f"El resultado de la {operation} es {result}")
    elif operation == "resta":
        result = num1 - num2
        print(f"El resultado de la {operation} es {result}")
    elif operation == "multiplicacion":
        result = num1 * num2
        print(f"El resultado de la {operation} es {result}")
    elif operation == "division":
        result = num1 / num2
        print(f"El resultado de la {operation} es {result}")
    else:
        print("Operación no válida")

operation = input("Ingrese el tipo de operación a realizar (suma, resta, multiplicacion, division): ")
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

calculator(operation, num1, num2)
