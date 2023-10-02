# Definicao da classe compra, que representa o carrinho de compras

from pessoa import Pessoa
from produto import Produto
from item_compra import Item_de_compra

class Compra():
  
  def __init__(self, cliente:Pessoa):
    
    if(type(cliente is not Pessoa)):
        print("Informacoes invalidas")
        return None
    self.cliente = cliente
    self.itens = []

  def custo(self):
    custo = 0
    for produtos in itens:
      custo = custo + Item_de_compra.Custo(produto, quantidade_comprada):
    return custo #duvidas_aqui
    
  def adicionar_produto(self, produto:Produto, quantidade_adiquirida:int):
    item_adicionado = Item_de_compra(produto,quantidade_adquirida)
    itens.append(item_adicionado) #precisa de return?
    
  def remover_produto(self, indice_remover:int):
    if(indice_remover<0 or indice_remover>(len(itens)-1) or type(indice_remover) is not int):
      print("Item nao esta na lista ou input invalido")
      return None
    else:
      itens.pop(indice_remover-1) #precisa de return?

  def atualizar_quantidade(self):

  def visuzalizar_compra(self):
