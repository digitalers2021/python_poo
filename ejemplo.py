

class Operaciones:

    def __init__(self):
        self.resultado = None

    def sumar(self, a, b):
        self.resultado = a + b

    def restar(self, a, b):
        self.resultado = a - b

    def hacer_todo(self, x, y):
        self.sumar(x, y)
        self.print_resultado()

    def print_resultado(self):
        print("El resultado es: ", self.resultado)


def sumar(a, b):
    resultado = a + b
    return resultado

def restar(a, b):
    resultado = a - b
    return resultado

def modifico_resultado(mi_objeto):
    mi_objeto.resultado = -10


op = Operaciones()

op.sumar(10, 10)
op.print_resultado()
modifico_resultado(op)
op.print_resultado()

