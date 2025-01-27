class Phone:
    def __init__ (self, brand, model, camera, price): #constructor
        self.brand = brand
        self.model = model
        self.camera = camera
        self.price = price
    
    def call(self):
        print(f'Calling from: {self.model}')

    def close_call(self):
        print(f'Call ended from: {self.model}')

phone1 = Phone("Samsung", "Galaxy S21", "12MP", 1000)
phone2 = Phone("Apple", "Iphone 12", "12MP", 1200)

#def __init__ es un metodo constructor
#constructor es una funcion que se ejecuta al crear un objeto
#self es una referencia al objeto actual
#atributos es una variable que se le asigna a un objeto
#objetos es una instancia de una clase
#metodos es una funcion que se le asigna a un objeto

print(phone1.close_call())
