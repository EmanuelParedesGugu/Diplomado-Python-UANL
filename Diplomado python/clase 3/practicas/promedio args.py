def promedio(*args):
    suma = 0
    for calificacion in args:
        suma = suma + calificacion
    prom = suma/len(args)
    return(prom)
 
print(promedio(10,9,8,8))