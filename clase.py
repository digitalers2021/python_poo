

class Persona:

    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni

    def decir_hola(self):
        print(f"Hola me llamo {self.nombre}")

    def cambiar_dni(self, nuevo_dni):
        self.dni = nuevo_dni
    
    def print_dni(self):
        print(self.dni)


if __name__ == "__main__":
    print("Mi programa")
    #juan = Persona(nombre="Juan", dni="123.345")
    juan = Persona("Juan", "123.345")
    juan.decir_hola()
    juan.cambiar_dni("abc")
    juan.print_dni()

    rosa = Persona("Rosa", "3.4.5")
    rosa.cambiar_dni("444")
    rosa.decir_hola()
