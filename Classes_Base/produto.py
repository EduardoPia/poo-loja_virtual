# Definicao da classe produto
class Produto:
    def __init__(self, nome:str, preco:float, categoria:str):
      self.nome = nome
      self.__preco = 0
      self.categoria = categoria
      self.__qtd_estoque = 0
      self.__desconto = 0.0
  
    #retorna preco com desconto  
    def preco(self): 
      return self.__preco*(1-self._desconto)
        
    #incrementa a quantidade em estoque  
    def registrar_aquisicao(self,qtd_comprados):
      self.__qtd_estoque = self.__qtd_estoque + qtd_comprados
        
    #decrementa a quantidade em estoque  
    def registrar_venda(self,qtd_comprados):
      self.__qtd_estoque = self.__qtd_estoque - qtd_comprados
        
    #retorna a quantidade em estoque  
    def quantidade_estoque(self):
      return self.__qtd_estoque

    #atualiza o desconto, valindando a entrada
    def atualizar_desconto(self, novo_desconto):
      if(type(novo_desconto) is not float or novo_desconto<0 and novo_desconto>=1):
          print("Valores invalidos")
      self.__desconto = self.novo_desconto

    #atualiza preco, validando a entrada
    def atualizar_preco(self, novo_preco):
      if(type(novo_preco) is not float or novo_preco<=0):
          print("Valores invalidos")
      self.__preco = novo_preco
