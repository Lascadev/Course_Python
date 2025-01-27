#herencia es una forma de crear una nueva clase usando clases que ya han sido definidas
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print(f"Hola, mi nombre es {self.nombre}")

#se define la clase Empleado que hereda de la clase Persona
#super es una funcion que se refiere a la clase padre
#teoria de conjuntos es una coleccion de objetos
#herencia gerarquica es cuando una clase hereda de otra clase
class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

roberto = Empleado("Roberto", 30, "Venezolano", "Desarrollador", 1000)

print(roberto.hablar())

#pass es una palabra clave que se usa cuando no se quiere agregar ninguna otra propiedad o metodo a la clase