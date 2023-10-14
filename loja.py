# Definicao da classe loja, a classe central do programa, que ira gerir todas as acoes de manipulacao de inventario e 
# funcoes para que o usuario possa modificar a loja

from Classes_Base.pessoa import Pessoa
from Classes_Base.produto import Produto 
#from Classes_Base.item_de_compra import Item_de_compra
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

    def iniciar_compra(self, cliente: Pessoa):
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

    def r_valor_med_compras(self) -> float:
        return(self.r_valor_tot_vend()/self.r_numero_vendas())
    
    def r_numero_usuarios(self) -> int:
        num = 0
        lista_usu:list(str) = []
        for compra in self.compras:
            for usuario in lista_usu:
                if usuario == compra.cliente.nome:
                    break
            num += 1
            lista_usu.append(compra.client.nome)       
        return num     

    def r_usuario_mais_compras(self) -> Pessoa:
        lista_usu:list(str) = []
        for compra in self.compras:
            lista_usu.append(compra.cliente.nome)
        lista_usu = sorted(lista_usu)
        lista_nov:list(str) = [lista_usu[0]]
        quantias:list(int) = [1]
        for i in range(1,len(lista_usu)):
            if lista_usu[i] == lista_usu[i-1]:
                quantias[len(quantias)] += 1
            else:
                lista_nov.append(lista_usu[i])
                quantias.append(1)
        nome_maior = lista_nov[quantias.index(max(quantias))]
        for compra in self.compras:
            if compra.cliente.nome == nome_maior:
                return compra.cliente
    
    def r_5_mais_caros(self) -> list(Produto):
        top:list(Produto) = []
        for produto in self.produtos:
            for prod in top:
                if produto.preco() > prod.preco():
                    top.insert(produto)
                    break
                top.append(produto)
        top_5:list(Produto) = []
        for i in range(len(top)):
            top_5.append(top[i])
        return top_5
    
    def r_5_mais_vendidos(self):
        prod_vendidos:list(str) = []
        quantidade_vendidos:list(int) = []
        for compra in self.compras:
            for item in compra.itens:
                for prod in prod_vendidos:
                    if item.produto.nome == prod:
                        quantidade_vendidos[prod_vendidos.index(prod)] += item.quantidade
                        break
                    if prod == prod_vendidos[len(prod_vendidos)]:
                        prod_vendidos.append(item.produto.nome)
                        quantidade_vendidos.append(item.quantidade)
        for i in range(5):
            print(f"{i}. {prod_vendidos[quantidade_vendidos.index(max(quantidade_vendidos))]} R${quantidade_vendidos[quantidade_vendidos.index(max(quantidade_vendidos))]}")  
            prod_vendidos.pop(quantidade_vendidos.index(max(quantidade_vendidos)))
            quantidade_vendidos.pop(quantidade_vendidos.index(max(quantidade_vendidos)))
                     
                    
                
            
        
                  
            



# loj = Loja()
# client = Pessoa("jose","dudu@gmail","198775")
# loj.iniciar_compra(client)

  