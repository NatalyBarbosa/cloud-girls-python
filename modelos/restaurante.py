from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria): #__init__ é um construtor

        self._nome = nome.title() #self é uma 
        self._categoria = categoria.upper() #upper() coloca em caixa alta
        self._ativo = False #_ : privado
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self): #__str__ (por convenção) mostra as infromações em formato de texto
        return f'{self._nome} | {self._categoria}'
    

    @classmethod #referencia a classe como argumento coloca o (cls)
    def listar_restaurantes(cls):
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} |{"Status"}')

        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} |{restaurante.ativo}') #menu
         

    @property #modifica como o atributo vai ser lido
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    def alternar_estado(self): #método para os objetos
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property #cpaz de ler as informações
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        
        soma = sum(avaliacao._nota for avaliacao in self._avaliacao)

        quantidade = len(self._avaliacao)
        media = round(soma/quantidade, 1)

        return media
    

    #def adicionar_bebida(self, bebida):
    #    self._cardapio.append(bebida)

    #def adicionar_prato(self, prato):
    #    self._cardapio.append(prato)

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio): #a função retorna True se item for uma instância de ItemCardapio e False caso contrário.
            self._cardapio.append(item)

    @property      
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self._nome}\n')
        for i,item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{i}. Nome:{item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}'
                print(mensagem_prato)

            else:
                mensagem_bebida = f'{i}. Nome:{item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)
