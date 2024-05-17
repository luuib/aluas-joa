class Animal:

    def emitir_som(self):
        return'qual qeur som'
class Cachorro(Animal):
    def emitir_som(self):
        return 'auauauauauaauua'
    
cachorro = Cachorro()
print(cachorro.emitir_som())

class gato (Animal):
    def emitir_som(self):
        return 'miau'
    