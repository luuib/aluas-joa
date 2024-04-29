class Celular:
    def __init__(self, marca, modelo, bateria):
        self.marca = marca
        self.modelo = modelo
        self.bateria = bateria
        self.ligado = False

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print("O celular está ligado.")
        else:
            print("O celular já está ligado.")

    def despertar(self):
        if self.ligado:
            print("O celular está despertando.")
        else:
            print("Por favor, ligue o celular primeiro.")

    def carregar(self):
        if self.ligado:
            print("O celular está carregando.")
            self.bateria = 100
        else:
            print("Por favor, ligue o celular primeiro.")

# Exemplo de uso:
meu_celular = Celular("Iphone ", "s15", 50)
meu_celular.ligar()
meu_celular.despertar()
meu_celular.carregar()
