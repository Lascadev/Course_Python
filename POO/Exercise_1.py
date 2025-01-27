#crear una clase llamada "Estudiante" con los siguientes atributos: Nombre. Edad, Grado ademas crear un metodo que muestre "el estudiante (nombre) esta estudiando" y 
# usar el metodo estuar()
#se debe interactuar con el usuario y este debe brindar los atributos del estudiante y al escribir estudiar utilizar el metodo creado "no case sensitive"

class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
pedro = Estudiante("Pedro", 15, 10)

print(pedro.edad)