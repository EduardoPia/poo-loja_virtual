# Definicao da classe compra, que representa o carrinho de compras

from pessoa import Pessoa
from produto import Produto
from item_compra import Item_de_compra

class Compra():
  
  def __init__(self, cliente:Pessoa, itens:Produto):
    
    if(type(cliente is not Pessoa) or type(itens) is not Produto):
        print("Informacoes invalidas")
        return None
    self.cliente = cliente
    self.itens = itens[]

  def custo(self):
    custo = 0
    for produtos in itens:
      custo = custo + Custo(produto, quantidade_comprada):
    return custo
    #duvidas_aqui
  def adicionar_produto(self, produto:Produto, quantidade_adiquirida:int):

  def remover_produto(self):

  def atualizar_quantidade(self):

  def visuzalizar_compra(self):
