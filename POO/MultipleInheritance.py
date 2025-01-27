#herencia es una forma de crear una nueva clase usando clases que ya han sido definidas
#self es una referencia al objeto actual
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print(f"Hola, mi nombre es {self.nombre}")

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        print(f"Mi habilidad es {self.habilidad}")

class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa

    #con super puedo acceder a el metodo de la clase padre en este caso Artista

    def presentarse(self):
        return (f"{super().mostrar_habilidad()}")

roberto = EmpleadoArtista("Roberto", 30, "Venezolano", "Desarrollador", 1000, "Google")
print(roberto.presentarse())

pedro = Artista("Cantar")
#issubclass nos permite saber si una clase es hija de otra clase
herencia = issubclass(EmpleadoArtista, Persona)

#imprime True si EmpleadoArtista es hija de Persona

#isinstance nos permite saber si un objeto es una instancia de una clase
#en este caso roberto es una instancia de la clase Artista
instancia = isinstance(roberto, Artista)
instancia2 = isinstance(pedro, Persona)
#instancia2 es False porque pedro no es una instancia de la clase Persona
print(instancia2)
print(instancia)
print(herencia)

#pass es una palabra clave que se usa cuando no se quiere agregar ninguna otra propiedad o metodo a la clase
