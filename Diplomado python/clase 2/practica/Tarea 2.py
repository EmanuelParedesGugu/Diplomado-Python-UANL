import sys

try:
  
    if len(sys.argv) != 12:
        raise ValueError("Debes proporcionar los parámetros correctamente.")

    
    mate = float(sys.argv[sys.argv.index("-m") + 1])
    español = float(sys.argv[sys.argv.index("-e") + 1])
    geografia = float(sys.argv[sys.argv.index("-g") + 1])
    biologia = float(sys.argv[sys.argv.index("-b") + 1])
    ingles = float(sys.argv[sys.argv.index("-i") + 1])

    Promedio = (mate+ español + geografia + biologia + ingles) / 5

    print("El promedio es:", Promedio)

except ValueError as e:
    print("Error:", e)