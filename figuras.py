import math
class Figura():
    def dame_perimetro(self):
        print("Esta figura no tiene perímetro")
    def dame_area(self):
        print("Esta figura no tiene área")

class Cuadrado(Figura):
    def __init__(self,lado):
        self.lado = lado
    def calculo_area(self):
        return self.lado * self.lado
    def calculo_perimetro(self,lado):
        return 4 * self.lado
       
c = Cuadrado(2)
print(c.calculo_area())

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    def calculo_area(self):
        return math.pi * (self.radio ** 2)
    def calculo_perimetro(self):
        return math.pi * 2 * (self.radio)
       
r = Circulo(2)
print(r.calculo_area())

