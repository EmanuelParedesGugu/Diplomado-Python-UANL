class Vehiculo:
    def __init__(self, marca, color, placa, modelo):
        # Atributos
        self.marca = marca
        self.color = color
        self.placa = placa
        self.modelo = modelo
     
    def acelerar(self):
        print(f"Soy {self.marca}, estoy acelerando!!")

    def frenar(self):
        print(f"Soy {self.marca}, estoy frenando!!")

    def voltear(self, direccion):
        print(f"Soy {self.marca}, estoy volteando a la {direccion}")

class Auto (Vehiculo):
    numero_llantas = 4
    def tocar_claxon(self):
        print(f"Soy {self.marca}, y estoy tocando el claxon!!")

class JetSki(Vehiculo):
    flotadores = 2
    propulsor = 1
    def activar_propulsion(self):
        print(f"Soy {self.marca} y tengo la propulsión activada")

class Avion(Vehiculo):
    numeroLlantas = 24
    turbinas = 2
    def despegar(self):
        print(f"Soy {self.marca} y estoy despegando")

    def aterrizar(self):
        print(f"Soy {self.marca} y estoy aterrizando")

#------------PRUEBA-----------------------------------
# Creamos Objetos Carro
obj_mazda = Auto('Mazda 6', 'Rojo', 'RED126', '2020')
obj_renault = Auto('Renault Logan', 'Negro', 'FRE009', '2021')
obj_audi = Auto('Audi Q3', 'Blanco', 'DPK312', '2016')
obj_mazda.acelerar()
obj_mazda.voltear('izquierda')
obj_mazda.tocar_claxon()
print('--------------------------------------------------------')
# Creamos Objeto JetSki
obj_jet = JetSki('Sea-Doo Spark', 'Azul', 'G-DE0000', '2022')
obj_jet.acelerar()
obj_jet.voltear('izquierda')
obj_jet.activar_propulsion()
print('--------------------------------------------------------')
# Creamos Objeto Avion
obj_avion = Avion('Jet Privado', 'Blanco', 'G-DER4', '2014')
obj_avion.acelerar()
obj_avion.voltear('derecha')
obj_avion.despegar() 