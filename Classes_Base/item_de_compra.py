# Definicao da classe item de compra, que representa um item do carrinho de compra

from produto import Produto

class Item_de_compra():
    
    def __init__(self,produto:Produto, quantidade_comprada:int):
        if (type(produto) is not Produto) or (type(quantidade_comprada) is not int) or (quantidade_comprada<=0):
            print("Informacoes invalidas")
            return None
        self.produto = produto
        self.quantidade = quantidade_comprada
    
    def Custo(self):
        return(self.produto.preco()*self.quantidade)
    
    def Atualiza_Quantidade(self, qtd):
        sel.quantidade = qtd
