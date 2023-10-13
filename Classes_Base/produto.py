# Definicao da classe produto
class Produto:
    def __init__(self, nome:str, preco:float, categoria:str, codigo:str):
      if (type(nome) is not str) or (type(preco) is not float and type(preco) is not int) or (type(categoria) is not str) or (type(codigo) is not str):
          print("Informacoes invalidas")
          return None
      preco = float(preco)
      self.nome:str = nome
      self.__preco:float = preco
      self.categoria:str = categoria
      self.__qtd_estoque:int = 0
      self.__desconto:float = 0.0
      self.codigo:str = codigo
  
    #retorna preco com desconto  
    def preco(self) -> float: 
      return self.__preco*(1-self._desconto)
        
    #incrementa a quantidade em estoque  
    def registrar_aquisicao(self, qtd_comprados:int):
      if (type(qtd_comprados) is not int) or (qtd_comprados<0):
        print("Informacoes invalidas")
        return None
      self.__qtd_estoque = self.__qtd_estoque + qtd_comprados
        
    #decrementa a quantidade em estoque  
    def registrar_venda(self,qtd_vendidos:int):
      if (type(qtd_vendidos) is not int) or (qtd_vendidos<0):
        print("Informacoes invalidas")
        return None
      self.__qtd_estoque = self.__qtd_estoque - qtd_vendidos
        
    #retorna a quantidade em estoque  
    def quantidade_estoque(self) -> int:
      return self.__qtd_estoque

    #atualiza o desconto, valindando a entrada
    def atualizar_desconto(self, novo_desconto:float):
      if(type(novo_desconto) is not float) or (novo_desconto<0) or (novo_desconto>=1):
          print("Valores invalidos")
      self.__desconto = self.novo_desconto

    #atualiza preco, validando a entrada
    def atualizar_preco(self, novo_preco:float):
      if(type(novo_preco) is not float or novo_preco<=0):
          print("Valores invalidos")
      self.__preco = novo_preco
