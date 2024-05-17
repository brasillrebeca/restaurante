from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
'''
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 8)
restaurante_praca.receber_avaliacao('Emy', 2)
'''
bebida_suco = Bebida('Suco de Melancia', 5.0,'grande')
prato_paozinho = Prato('Paozinho',2.00,'O melhor pão da cidade')

def main():
    print(bebida_suco)
    print(prato_paozinho)

if __name__ == '__main__':
    main()
