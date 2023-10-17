# Definicao da classe compra, que representa um produto da loja
from typing import Union

class Produto():
    
    def __init__(self, nome:str, preco:float, categoria:str, codigo:str):
        if (type(nome) is not str) or (type(preco) is not float and type(preco) is not int) or (type(categoria) is not str):
            print("Informacoes invalidas")
            return None
        preco = float(preco)
        self.nome = nome
        self.__preco = preco
        self.__quantidade = 0
        self.__desconto = 0.0
        self.categoria = categoria
        self.codigo = codigo
        
    def preco(self):
        return (self.__preco*(1-self.__desconto))
    
    def get_preco(self):
        return self.__preco
    
    def get_desconto(self):
        return self.__desconto
    
    def registrar_aquisicao(self, quantidade_extra:int):
        if (type(quantidade_extra) is not int) or (quantidade_extra<0):
            print("Informacoes invalidas")
            return None
        self.__quantidade += quantidade_extra
    
    def registrar_venda(self, quantidade_vendida:int):
        if (type(quantidade_vendida) is not int) or (quantidade_vendida>self.__quantidade) or (quantidade_vendida<0):
            print("Informacoes invalidas")
            return None
        self.__quantidade -= quantidade_vendida
        
    def quantidade_em_estoque(self):
        return self.__quantidade
    
    def atualizar_desconto(self, novo_desconto:Union[int,float]):
        if (type(novo_desconto) is not float) and (novo_desconto != 0):
            print("Informacoes invalidas")
            return None
        if (novo_desconto<0 or novo_desconto>=1):
            print("Informacoes invalidas")
            return None
        self.__desconto = novo_desconto
        
    def atualizar_preco(self, novo_preco: Union[float,int]):
        if (type(novo_preco) is not float and type(novo_preco) is not int) or (novo_preco<=0):
            print("Informacoes invalidas")
            return None
        novo_preco = float(novo_preco)
        self.__preco = novo_preco
   
