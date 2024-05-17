class forma:
    def area (self):
        pass

class Quadrdado(forma):
    def __init__(self, lado):
        self.lado = lado

    def area (self):
        return self.lado ** 2
    
quadrdo = Quadrdado(12)

print(quadrdo.area())

class circulo(forma):
    def __init__(self, raio):
        self.raio = raio

    def area (self):
        return 3.14 * self.raio
    
circulo = circulo(12)
print(circulo.area())
