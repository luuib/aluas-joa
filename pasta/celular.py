class Celular():
    bateria = 'Ifinita'
    tela = '4x3'
    tem_camera = True
    tem_botao = True
    tem_antena = True
    cor = 'preto'
    modelo = 'Tijolão'

    def ligaao ():
        print('Ligando...')

    def mensagem():
        print('Enviando Mensagem...')

    def jg_cobra():
        return'O MELHOR jogo'

print(Celular.bateria)
print(Celular.jg_cobra())