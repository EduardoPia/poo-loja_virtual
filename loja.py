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
                    if self.produtos[i].quantidade_em_estoque() < item.quantidade:
                        print(f"Erro: Quantidade insuficiente no estoque de {item.produto.codigo}")
                        return None
                    vendidos_quantidade.append(item.quantidade)
                    vendidos_indice.append(i)
                    break
        for j in range(len(vendidos_indice)):
            self.produtos[vendidos_indice[j]].registrar_venda(vendidos_quantidade[j])
        self.compras.append(self.compra_aberta)
        self.compra_aberta = None   

    def printa_compra_aberta (self):
        print("-> Cliente: ")
        print(f"- Nome: {self.compra_aberta.cliente.nome}")
        print(f"- Email: {self.compra_aberta.cliente.email}")
        print(f"- CPF: {self.compra_aberta.cliente.cpf}")
        for item in self.compra_aberta.itens:
            print(f"Item {self.compra_aberta.itens.index(item)}: {item.produto.nome}")
            print(f"Quantidade desejada: {item.quantidade}")
            print(f"Preco unitario: {item.produto.preco()}")
            print(f"Categoria: {item.produto.categoria}")
            print(f"Codigo: {item.produto.codigo}")
        if len(self.compra_aberta.itens) == 0:
            print("-> Nao foram adicionados itens")
  
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
                    num -= 1
                    break
            num += 1
            lista_usu.append(compra.cliente.nome)       
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
                quantias[len(quantias)-1] += 1
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
                    top.insert(top.index(prod),produto)
                    break
            top.append(produto)
        top_5:list(Produto) = []
        for i in range(min(len(top))):
            top_5.append(top[i])
        return top_5
    
    def r_5_mais_vendidos(self):
        prod_vends:list(str) = []
        qnt_vends:list(int) = []
        preco_vends:list(float) = []
        for compra in self.compras:
            for item in compra.itens:
                if item.produto.nome in prod_vends:
                    qnt_vends[prod_vends.index(item.produto.nome)] += item.quantidade
                    preco_vends[prod_vends.index(item.produto.nome)] += item.quantidade*item.produto.preco()

                else:
                    prod_vends.append(item.produto.nome)
                    qnt_vends.append(item.quantidade)
                    preco_vends.append(item.quantidade*item.produto.preco())
        for i in range(min(5,len(qnt_vends))):
            j = qnt_vends.index(max(qnt_vends))
            print(f"{i}. {prod_vends[j]} R${preco_vends[j]}")  
            prod_vends.pop(j)
            preco_vends.pop(j)
            qnt_vends.pop(j)
                     
    def r_usuarios_compras(self):
        lista_usu:list(str) = []
        for compra in self.compras:
            if compra.cliente.nome not in lista_usu:
                lista_usu.append(compra.cliente.nome)
        lista_usu = sorted(lista_usu)

        lista_cpf:list(str) = []
        for usu in lista_usu:
            for compra in self.compras:
                if usu == compra.cliente.nome:
                    lista_cpf.append(compra.cliente.cpf)
                    break

        lista_gasto:list(float) = []
        for i in range(len(lista_usu)):
            lista_gasto.append(0.0)
            for compra in self.compras:
                if compra.cliente.nome == lista_usu[i]:
                    lista_gasto[i] += compra.custo()

        for i in range(len(lista_usu)):
            print(f"Nome: {lista_usu[i]} CPF: {lista_cpf[i]} Valor: {lista_gasto[i]}")
   
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
                arq.write(f"compra,{compra.cliente.nome},{compra.cliente.email},{compra.cliente.cpf}")    
                for item in compra.itens:
                    arq.write(f",{item.quantidade}")
                    arq.write(f",{item.produto.nome},{item.produto.get_preco()},{item.produto.quantidade_em_estoque()}")
                    arq.write(f",{item.produto.get_desconto()},{item.produto.categoria},{item.produto.codigo}")
                arq.write("\n")
    
    def carregar(self, nome_arq):
        with open(nome_arq,"r") as arq:
            linhas = arq.readlines()
            for i in range(len(linhas)):
                linhas[i] = linhas[i].strip("\n")
                linhas[i] = linhas[i].split(",")
                #print(linhas[i])
                if linhas[i][0] == "produto":
                    self.produtos.append(Produto(linhas[i][1],float(linhas[i][2]),linhas[i][5],linhas[i][6]))
                    self.produtos[i].registrar_aquisicao(int(linhas[i][3]))
                    self.produtos[i].atualizar_desconto(float(linhas[i][4]))
                else:
                    cliente = Pessoa(linhas[i][1],linhas[i][2],linhas[i][3])
                    self.compras.append(Compra(cliente)) 
                    k = (len(linhas[i])-4)//7 #numero de itens
                    for j in range(k):
                        prod = Produto(linhas[i][7*j+5],float(linhas[i][7*j+6]),linhas[i][7*j+9],linhas[i][7*j+10])
                        prod.registrar_aquisicao(int(linhas[i][7*j+7]))
                        prod.atualizar_desconto(float(linhas[i][7*j+8]))
                        self.compras[len(self.compras)-1].itens.append(Item_de_compra(prod,int(linhas[i][7*j+4])))                        
             
#loj = Loja()
#loj.carregar("loja.txt")
#print(loj.r_numero_produtos())
#print(loj.r_numero_vendas())
#print(loj.r_valor_tot_vend())
#print(loj.r_valor_med_compras())
#print(loj.r_numero_usuarios())
#print(loj.r_usuario_mais_compras().nome)
#mais_caros = loj.r_5_mais_caros()
#print(mais_caros[1].nome)
#loj.r_5_mais_vendidos()
#loj.r_usuarios_compras()
##loj.iniciar_compra(Pessoa("eu","dudu@g","123"))
##loj.compra_aberta.adicionar_produto(loj.buscar_produto("AB2"),2)
##loj.printa_compra_aberta()



# eu = Pessoa("eduardo","dudu@gm","198")
# outro = Pessoa("outro","outro@gmai","197")
# o_outro = Pessoa("o outro","o@hotmail","196")
# produto_1 = Produto("leite",5.0,"comida","AB1")
# produto_2 = Produto("molho",3.0,"comida","AB2")
# produto_3 = Produto("geladeira",1000.1,"eletrodomestico","AB3")
# loj = Loja()
# loj.produtos.append(produto_1)
# loj.produtos.append(produto_2)
# loj.produtos.append(produto_3)
# loj.produtos[0].registrar_aquisicao(5)
# loj.produtos[1].registrar_aquisicao(5)
# loj.iniciar_compra(eu)
# loj.compra_aberta.adicionar_produto(produto_1,2)
# loj.finalizar_compra()
# loj.iniciar_compra(outro)
# loj.compra_aberta.adicionar_produto(produto_1,3)
# loj.compra_aberta.adicionar_produto(produto_2,3)
# loj.finalizar_compra()
# loj.iniciar_compra(outro)
# loj.compra_aberta.adicionar_produto(produto_2,1)
# loj.finalizar_compra()
# loj.iniciar_compra(outro)   
# loj.compra_aberta.adicionar_produto(produto_3,2)
# loj.salvar("loja.txt")

# def printaCompra (compra:Compra):
#     print(f"Nome: {compra.cliente.nome}")
#     print(f"email: {compra.cliente.email}")
#     print(f"cpf: {compra.cliente.cpf}")
#     for item in compra.itens:
#         print(f"quantidade: {item.quantidade}")
#         print(f"prod_nome: {item.produto.nome}")
#         print(f"prod_preco: {item.produto.get_preco()}")
#         print(f"prod_quantidade: {item.produto.quantidade_em_estoque()}")
#         print(f"prod_desconto: {item.produto.get_desconto()}")
#         print(f"prod_categoria: {item.produto.categoria}")
#         print(f"prod_preco: {item.produto.codigo}")

