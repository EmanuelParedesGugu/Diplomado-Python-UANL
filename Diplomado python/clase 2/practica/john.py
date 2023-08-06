import argparse

def calcular_promedio(args):
    try:
        # Obtener los valores de las calificaciones
        calificaciones = [args.m, args.e, args.g, args.b, args.i]

        # Convertir las calificaciones a números y calcular el promedio
        promedio = sum([float(calificacion) for calificacion in calificaciones]) / len(calificaciones)

        # Imprimir el resultado
        print("El promedio es:", promedio)
    except ValueError:
        print("Error: Se ha ingresado un valor no numérico.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", type=str, help="Calificación de matemáticas")
    parser.add_argument("-e", type=str, help="Calificación de español")
    parser.add_argument("-g", type=str, help="Calificación de geografía")
    parser.add_argument("-b", type=str, help="Calificación de biología")
    parser.add_argument("-i", type=str, help="Calificación de inglés")
    args = parser.parse_args()

    calcular_promedio(args)
