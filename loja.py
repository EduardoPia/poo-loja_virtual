# Definicao da classe loja, a classe central do programa, que ira gerir todas as acoes de manipulacao de inventario e 
# funcoes para que o usuario possa modificar a loja

from Classes_Base.pessoa import Pessoa
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

    def iniciar_compra(self, cliente: Pessoa):
        if self.compra_aberta != None:
            print("Erro: Ja existes uma compra aberta")
            return None
        self.compra_aberta = Compra(cliente)
    
    def buscar_produto(self,codigo:str) -> Produto:
        for produto in self.produtos:
            if produto.codigo == codigo:
                return produto
        return None
    
    def cancelar_compra(self):
        self.compra_aberta = None
        
    def finalizar_compra(self):
        vendidos_quantidade:list(int) = []
        vendidos_indice:list(int) = []
        for item in self.compra_aberta.itens:
            for i in range(len(self.produtos)):
                if self.produtos[i].codigo == item.produto.codigo:
                    print("oi")
                    print(self.produtos[i].quantidade_em_estoque())
                    print(item.produto.quantidade_em_estoque())
                    if self.produtos[i].quantidade_em_estoque() < item.produto.quantidade_em_estoque():
                        print(f"Erro: Quantidade insuficiente no estoque de {item.produto.codigo}")
                        return None
                    vendidos_quantidade.append(item.produto.quantidade_em_estoque())
                    vendidos_indice.append(i)
                    break
        for j in range(len(vendidos_indice)):
            self.produtos[vendidos_indice[j]].registrar_venda(vendidos_quantidade[j])
        self.compras.append(self.compra_aberta)
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
    
    def r_5_mais_caros(self) -> list:
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
                     
    def r_usuarios_compras(self):
        lista_usu:list(str) = [self.compras[0].cliente.nome]
        lista_cpf:list(int) = [] 
        total_compras:list(float) = []
        for usu in lista_usu:
            total_compras.append(0.0)
        
        for compra in self.compras:
            for nome_usuario in lista_usu:
                if nome_usuario == compra.cliente.nome:
                    break
            lista_usu.append(nome_usuario)
        lista_usu = sorted(lista_usu) 
        
        for compra in self.compras:
            total_compras[lista_usu.index(compra.cliente.nome)] += compra.custo()
            
        for usu in lista_usu:
            for compra in self.compras:
                if compra.cliente.nome == usu:
                    lista_cpf.append(compra.cliente.cpf)
                    break
        for i in range(lista_usu):
            print(f"i. {lista_usu[i]} cpf: {lista_cpf[i]} compras: {total_compras[i]}")
        
    def salvar(self, nome_arq):
        '''
        Modo de salvamento:
        linha 0 até n-1: salvamento dos n produtos, um em cada linha no seguinte formato: 
            produto,{nome},{preco},{quantidade},{desconto},{categoria},{codigo}
        linha n até n+m-1: salvamento das m compras realizadas, uma em cada linha no seguinte formato:
            compra,{cliente.nome},{cliente.email},{cliente.cpf},{itens[1].quantidade},{itens[1].produto.nome},...
            ...{itens[1].produto.preco},{itens[1].produto.quantidade},{itens[1].produto.desconto},{itens[1].produto.categoria},...
            ...{itens[1].produto.codigo} ... ... ,{itens[k].quantidade},{itens[k].produto.nome},...
            ...{itens[k].produto.preco},{itens[k].produto.quantidade},{itens[k].produto.desconto},{itens[k].produto.categoria},...
            ...{itens[k].produto.codigo}
        '''
        with open (nome_arq,"w") as arq:
            for produto in self.produtos:
                arq.write(f"produto,{produto.nome},{produto.get_preco()},{produto.quantidade_em_estoque()},")
                arq.write(f"{produto.get_desconto()},{produto.categoria},{produto.codigo}\n")
            for compra in self.compras:
                arq.write(f"compra,{compra.cliente.nome},{compra.cliente.email},{compra.cliente.cpf},")    
                for item in compra.itens:
                    arq.write(f"{item.quantidade},")
                    arq.write(f"{item.produto.nome},{item.produto.get_preco()},{item.produto.quantidade_em_estoque()},")
                    arq.write(f"{item.produto.get_desconto()},{item.produto.categoria},{item.produto.codigo}\n")
    
    def carregar(self, nome_arq):
        with open(nome_arq,"r") as arq:
            linhas = arq.readlines()
            for i in range(len(linhas)):
                linhas[i] = linhas[i].strip("\n")
                linhas[i] = linhas[i].split(",")
                if linhas[i][0] == "produto":
                    self.produtos.append(Produto(linhas[i][1],linhas[i][2],linhas[i][5],linhas[i][6]))
                    self.produtos[i].registrar_aquisicao(linhas[i][3])
                    self.produtos[i].atualizar_desconto(linhas[i][4])
                else:
                    cliente = Pessoa(linhas[i][1],linhas[i][2],linhas[i][3])
                    self.compras.append(Compra(cliente)) 
                    k = (4-len(linhas[i]))/7 #numero de itens
                    for j in range(k):
                        prod = Produto(linhas[i][j+5],linhas[i][j+6],linhas[i][j+9],linhas[i][j+10])
                        prod.registrar_aquisicao(linhas[i][j+7])
                        prod.atualizar_desconto(linhas[i][j+8]) 
                        self.compras.itens.append(Item_de_compra(prod,linhas[i][j+4]))                        
             


eu = Pessoa("eduardo","dudu@gm","198")
outro = Pessoa("outro","outro@gmai","197")
o_outro = Pessoa("o outro","o@hotmail","196")
produto_1 = Produto("leite",5.0,"comida","AB1")
produto_2 = Produto("molho",3.0,"comida","AB2")
produto_3 = Produto("geladeira",1000.1,"eletrodomestico","AB3")

loj = Loja()
loj.produtos.append(produto_1)
loj.produtos.append(produto_2)
loj.produtos.append(produto_3)
#print(loj.produtos)
loj.produtos[0].registrar_aquisicao(3)
loj.produtos[1].registrar_aquisicao(5)

#print(f"{loj.produtos[0].quantidade_estoque()}" )
#print(f"{loj.produtos[1].quantidade_estoque()}" )
#print(f"{loj.produtos[2].quantidade_estoque()}" )

loj.iniciar_compra(eu)
loj.compra_aberta.adicionar_produto(produto_1,2)
loj.finalizar_compra()

#loj.iniciar_compra(outro)
#loj.compra_aberta.adicionar_produto(produto_1,3)
#loj.finalizar_compra()

#loj.cancelar_compra()
#loj.iniciar_compra(outro)