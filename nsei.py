class Carro:
    def __init__(self, modelo ,cor ,bateria):
        self.modelo = modelo
        self.cor = cor
        self.bateria = bateria

    def acelerar(self):
        return 'acelerando'
    def modelo (self):
        if self.modelo == 'iphone':
            return 'rico'
        elif self.modelo == 'nokia':
            return 'pobre'
    def bateria(self):
        if self.bateria == '2024':
            return 'rico'
    def cor(self):
        if self.cor == 'preto':
            return ''

carro1 = Carro('iphone', 2024,'preto')

print('o seu celular e :' carro1)