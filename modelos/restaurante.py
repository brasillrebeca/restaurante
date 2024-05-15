# Cada objeto encapsula dados e comportamentos relacionados
# objeto:instância de uma classe - criar objeto: instanciar um objeto
# a classe acompanha atributos e características
'''
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False
'''
class Restaurante:
    #variável lsita
    restaurantes = []

    # inicializando atribuições direcionadas para cada elemento novo criado com a definição do método init + referência self + valores a serem recebidos
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        # atributo privado _
        self._ativo = False
        # ao criar um objeto, fazer ele entrar na variável lista
        Restaurante.restaurantes.append(self)
    
    # retornar a informação sobre o objeto em formato de string, invés de em formato de endereço na memória
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    # criando meus próprios métodos - função para exibir informações dos restaurantes armazenados
    def listar_restaurantes():
        print(f'{'Nome do restaurante'} | {'Categoria'} | {'Status'}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

# modificando como um atributo vai ser lido através do @property
@property
def ativo(self):
    return 'verddeiro' if self._ativo else 'falso'

restaurante_praca = Restaurante('Praça', 'Gourmet')
# usar . para acessar atributos do objeto
'''restaurante_praca.nome = 'Praça'''''
restaurante_pizza = Restaurante('Pizza express', 'Italiano')

# o dir é utilizado para exibir todos os métodos do objeto
# o vars é utilizado para exibir apenas os métodos especificados através do código
'''
print(dir(restaurante_praca))
print(vars(restaurante_pizza))
'''

# método próprio de classes: listar_restaurantes()
Restaurante.listar_restaurantes()