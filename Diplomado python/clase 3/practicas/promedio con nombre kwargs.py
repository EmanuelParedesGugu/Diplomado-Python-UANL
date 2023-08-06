def promedio_con_Nombre(**kwargs):
    suma = 0
    for key,value in kwargs.items():
       # print("{0} = {1}".format(key, value))
        print("materia",key,"=",value)
        suma = suma + value
    prom = suma/len(kwargs)
    return(prom)
 
resultado = promedio_con_Nombre(matematicas = 9, ingles = 10, fisica = 8, biologia = 8, historia = 9)
print(resultado)