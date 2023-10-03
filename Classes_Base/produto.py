# Definicao da classe produto
class Produto:
    def __init__(self, nome:str, preco:float, categoria:str):
      sel.nome = nome
      self._preco = 0
      self.categoria = categoria
      self._qtd_estoque = 0
      self._desconto = 0.0
  
    #retorna preco com desconto  
    def preco(self): 
      return self._preco*self._desconto
      
    def registrar_aquisicao(self,qtd_comprados):
      self._qtd_estoque = self._qtd_estoque + self.qtd_comprados
      
    def registrar_venda(self,qtd_comprados):
      self._qtd_estoque = self._qtd_estoque - self.qtd_comprados
      
    def quantidade_estoque(self):
      return self._qtd_estoque
  
    def atualizar_desconto(self, novo_desconto):
      if(...):

    def atualizar_preco(self, novo_preco):
      if(...):
