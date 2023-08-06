class Animal_POO:
    def __init__(self,name, age, color_,sonido):
        self.nombre = name
        self.edad = age
        self.color = color_
        self.sonido = sonido
   
    def comunicar(self):
        print(self.nombre,"saluda asi:",self.sonido)
 
objeto1 = Animal_POO("Paco",4,"Negro","Miau")
print(objeto1.nombre, objeto1.edad, objeto1.color)
objeto1.comunicar()
 
objeto2 = Animal_POO("Juan",1,"Amarillo","Pio pio")
objeto2.comunicar()