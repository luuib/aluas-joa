class Animal():
    patas = 4
    tem_rabo = False
    pelo = True
    especie = ""
    sexo = 'macho'

class Cachorro(Animal):
    tem_rabo = True
    especie = 'Canis lupus familiares'
    raca = 'shitzu'
    nome = 'Sergio'
    porte = 'pequeno'

    def latir ():
        return 'AUAUAUAUAUAUAUAUAUAUAUAAUAUAUAUAUA'
    def comer():
        return 'nhaminhami'
    def dormir ():
        return 'ZzzzzZZZzzZZzzzZZzzZzzzZzzZzzzzZZzZZzZZzzZZzzZzzZzzZZzzZzZzzZzzZZzZzzZZzZZzzZZzZZzzZZZzzZZzzZZzZZzZZZzZZzZZzZZZZzzZZzZz'

print(Cachorro.patas)
print(Cachorro.pelo)
print(Cachorro.latir)
print(Cachorro.comer)
print(Cachorro.dormir)
print(Cachorro.porte)
print(Cachorro.raca)
print(Cachorro.especie)
print(Cachorro.nome)
print(Cachorro.sexo)
