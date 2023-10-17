# Definicao da classe compra, que representa o carrinho de compras

from Classes_Base.pessoa import Pessoa
from Classes_Base.produto import Produto
from Classes_Base.item_de_compra import Item_de_compra

class Compra():
  
  def __init__(self, cliente:Pessoa):
    
    #if(type(cliente is not Pessoa)):
    #    print("Informacoes invalidas")
    #    return None
    self.cliente:Pessoa = cliente
    self.itens:list(Item_de_compra) = []

  def custo(self) -> float:
    custo = 0
    for item in self.itens:
      custo = custo + item.Custo()
    return custo
    
  def adicionar_produto(self, produto:Produto, quantidade_adiquirida:int):
    if (type(quantidade_adiquirida) is not int):
      print("Informacoes invalidas")
      return None
    novo_prod = Produto(produto.nome,produto.get_preco(),produto.categoria,produto.codigo)
    novo_prod.atualizar_desconto(produto.get_desconto())
    novo_prod.registrar_aquisicao(1)
    item_adicionado = Item_de_compra(novo_prod, quantidade_adiquirida)
    self.itens.append(item_adicionado)
    
  def remover_produto(self, indice_remover:int):
    if(indice_remover<0) or (indice_remover>(len(self.itens))) or (type(indice_remover) is not int):
      print("Item nao esta na lista ou input invalido")
      return None
    else:
      self.itens.pop(indice_remover-1)

  def atualizar_quantidade(self, indice_atualizar:int, nova_quantidade:int):
    if(type(nova_quantidade) is not int) or (nova_quantidade < 0) or (type(indice_atualizar) is not int):
      print("Informacoes invalidas")
      return None
    self.itens[indice_atualizar-1].quantidade = nova_quantidade
    
  def visuzalizar_compra(self):
    valor_total = 0.0
    for n in self.itens:
      valor_total = valor_total + n.Custo()
      #imprime o valor de cada item, o valor total dos itens e o indice do item para ser removido.
      print(f"{(self.itens.index(n)+1)} - Valor unitario: {n.produto.preco()} Valor Total do produto:{n.Custo()}")
    print(f"O valor total da compra eh {valor_total}")
