# Cada objeto encapsula dados e comportamentos relacionados
# objeto:instância de uma classe - criar objeto: instanciar um objeto
# a classe acompanha atributos e características

from modelos.avaliacao import Avaliacao

class Restaurante:
    # Representa um restaurante e suas características
    restaurantes = []

    # inicializando atribuições direcionadas para cada elemento novo criado com a definição do método init + referência self + valores a serem recebidos
    def __init__(self, nome, categoria):
        # Inicializa uma instância de Restaurante.

        self._nome = nome.title()
        self._categoria = categoria
        # atributo privado _
        self._ativo = False
        self._avaliacao = []
        # ao criar um objeto, fazer ele entrar na variável lista
        Restaurante.restaurantes.append(self)
    
    # retornar a informação sobre o objeto em formato de string, invés de em formato de endereço na memória
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    # criando meus próprios métodos - função para exibir informações dos restaurantes armazenados
    # método da classa @classmethod - não precisa instanciar o objeto
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} |{'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} |{restaurante.ativo}')

    # modificando como um atributo vai ser lido através do @property
    @property
    def ativo(self):
        return 'ativo' if self._ativo else 'inativo'

    def alternar_estado(self):
        self._ativo = not self._ativo

# método que recebe as avaliações
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

# método para exibir a média da avaliação
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media