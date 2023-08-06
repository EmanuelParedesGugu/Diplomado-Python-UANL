class Circulo:
    pi = 3.14159
    
    def __init__(self, radio):
        self.radio = radio
    
    def obtener_area(self):
        area = self.pi * (self.radio ** 2)
        return area
    
    def obtener_perimetro(self):
        perimetro = 2 * self.pi * self.radio
        return perimetro

radio = float(input("Ingrese el valor del radio: "))
mi_circulo = Circulo(radio)

print("Area:", mi_circulo.obtener_area())
print("Perimetro:", mi_circulo.obtener_perimetro())