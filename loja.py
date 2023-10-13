# Definicao da classe loja, a classe central do programa, que ira gerir todas as acoes de manipulacao de inventario e 
# funcoes para que o usuario possa modificar a loja

from Classes_Base.pessoa import Pessoa as Pessoa
from Classes_Base.produto import Produto 
from Classes_Base.item_de_compra import Item_de_compra
from Classes_Base.compra import Compra
# import Classes_Base
# Pessoa = Classes_Base.Pessoa
# Produto = Classes_Base.Produto
# Item_de_compra = Classes_Base.Item_de_compra
# Compra = Classes_Base.Compra

class Loja():
    
    def __init__(self):
        self.produtos: list(Produto) = []
        self.compras: list(Compra) = []
        self.compra_aberta: Compra = None

    def iniciar_compra(self, cliente):
        if self.compra_aberta != None:
            print("Erro: Ja existes uma compra aberta")
            return None
        self.compra_aberta = Compra(cliente)
    
    def buscar_compra(self,codigo:str) -> Produto:
        for produto in self.produtos:
            if produto.codigo == codigo:
                return produto
        return None
    
    def cancelar_compra(self):
        self.compra_aberta = None
        
    def finalizar_compra(self):
        self.compras.append(self.Compra_aberta)
        for item in self.compra_aberta.itens:
            for i in range(len(self.produtos)):
                if self.produtos[i].codigo == item.produto.codigo:
                    self.produtos[i].registrar_venda(item.produto.quantidade_estoque)
        self.compra_aberta = None   
  
    def r_numero_produtos(self) -> int:
        produtos_v = 0
        for compra in self.compras:
            for item in compra.itens:
                produtos_v += item.quantidade
        return produtos_v
    
    def r_numero_vendas(self) -> int:
        return len(self.compras)
    
    def r_valor_tot_vend(self) -> float:
        valor_tot = 0.0
        for compra in self.compras:
            for item in compra.itens:
                valor_tot += item.Custo()
        return valor_tot






# loj = Loja()
# client = Pessoa("jose","dudu@gmail","198775")
# loj.iniciar_compra(client)

  