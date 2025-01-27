#crear una clase llamada "Estudiante" con los siguientes atributos: Nombre. Edad, Grado ademas crear un metodo que muestre "el estudiante (nombre) esta estudiando" y 
# usar el metodo estuar()
#se debe interactuar con el usuario y este debe brindar los atributos del estudiante y al escribir estudiar utilizar el metodo creado "no case sensitive"

class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print(f"El estudiante {self.nombre} esta estudiando")

nombre = input("Nombre del estudiante: ")
edad = int(input("Edad del estudiante: "))
grado = int(input("Grado del estudiante: "))

estudiante = Estudiante(nombre, edad, grado)

print(f"""
        Datos del estudiante: \n\n
        Nombre: {estudiante.nombre} \n
        Edad: {estudiante.edad} \n
        Grado: {estudiante.grado} \n
        """)


while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        estudiante.estudiar()