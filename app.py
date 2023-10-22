# Definicao da classe app, que sera utilizada para mediar a interacao do programa com o usuario
from loja import Loja
from Classes_Base.produto import Produto
from Classes_Base.compra import Compra
from Classes_Base.pessoa import Pessoa
from Classes_Base.item_de_compra import Item_de_compra


class App:
    def __init__(self):
        self.loja = Loja()
        self.loja.carregar("loja.txt")

    def menu(self):
        print("1. Cadastrar produto")
        print("2. Ver lista de produtos")
        print("3. Ver detalhes do produto")
        print("4. Atualizar desconto de produto")
        print("5. Registrar aquisicao de produto")
        print("6. Remover produto")
        print("7. Iniciar compra")
        print("8. Cancelar compra")
        print("9. Finalizar compra")
        print("10. Adicionar item na compra")
        print("11. Visualizar compra")
        print("12. Remover item da compra")
        print("13. Atualizar quantidade de item na compra")
        print("14. Relatório - Númmero de produtos")
        print("15. Relatório - Número de vendas")
        print("16. Relatório - Valor total vendido")
        print("17. Relatório - Valor médio das compras")
        print("18. Relatório - Número de usuários")
        print("19. Relatório - Usuário que mais fez compras")
        print("20. Relatório - 5 produtos mais caros")
        print("21. Relatório - 5 produtos mais vendidos")
        print("22. Relatório - Montante por pessoa")
        print("23. Sair\n")

        opcao = input("Escolha uma opcao:")
        try:
            opcao = int(opcao)
        except:
            print("Opcao invalida")
            opcao = self.menu()
        return opcao
    
    def executar(self):
        while True:
            opc = self.menu()
            if opc == 1: #cadastra um produto na loja
                try:
                    nome =  input("Digite o nome: ")
                    preco = float(input("Digite o preco: "))
                    categoria = input("Digite a categoria: ")
                    codigo = input("Digite o codigo: ")
                    produtinho = Produto(nome,preco, categoria ,codigo)
                    self.loja.produtos.append(produtinho)
                except:
                    print("informacoes invalidas, produto nao adicionado")

            elif opc == 2: # imprime lista de produtos na loja 
                # imprime indice, codigo, nome e valor com desconto
                for n in self.loja.produtos:
                    print(f"{self.loja.produtos.index(n)+1} - {n.codigo} {n.nome} {n.preco()} {n.quantidade_em_estoque()}") 
                print("\n")

            elif opc == 3: #imprime informacoes do produto buscado por codigo
                cod = input("Digite o codigo do produto: ")
                produto =self.loja.buscar_produto(cod)
                if produto != None:
                    print(f"NOME: {produto.nome}")
                    print(f"QUANTIDADE: {produto.quantidade_em_estoque()}")
                    print(f"PRECO COM DESCONTO: {produto.preco()}")
                    print(f"CATEGORIA: {produto.categoria}")
                    print(f"CODIGO: {produto.codigo}")
                else:
                    print("produto nao encontrado")
                
            elif opc == 4: #atualiza desconto por codigo
                cod = input("Digite o codigo do produto: ")
                produto = self.loja.buscar_produto(cod)
                try:
                    desc = float(input("Digite o novo desconto (0.0-1.0): "))
                except:
                    print("desconto invalido")
                
                if produto != None:
                    produto.atualizar_desconto(desc)
                else:
                    print("produto nao encontrado")

            elif opc == 5: #registra aquisicao por codigo
                cod = input("Digite o codigo do produto: ")
                produto = self.loja.buscar_produto(cod)
                try:
                    qtd = int(input("Digite a quantidade adquirida junto ao fornecedor: "))
                except:
                    print("quantidade invalida")
                if produto != None:
                    produto.registrar_aquisicao(qtd)
                else:
                    print("produto nao encontrado")
            
            elif opc == 6: #remove um produto da loja por codigo
                cod = input("Digite o codigo do produto: ")
                produto = self.loja.buscar_produto(cod)
                if produto != None:
                    self.loja.produtos.pop(self.loja.produtos.index(produto))
                else:
                    print("produto nao enocontrado")

            elif opc == 7: #pede nome, email, cpf, para utilizar metodo iniciar_compra, REVER
                nome = input("Digite o nome: ")
                email = input("Digite seu email: ")
                cpf = input("Digite seu cpf: ")
                self.loja.iniciar_compra(Pessoa(nome, email, cpf))

            elif opc == 8: #utiliza o metodo cancelar compra de loja
                if self.loja.compra_aberta != None:
                    self.loja.cancelar_compra()

            elif opc == 9: #utiliza o metodo finalizar compra de loja
                if self.loja.compra_aberta != None:
                    self.loja.finalizar_compra()

            elif opc == 10: #adiciona item na lista de compras
                cod = input("Digite o codigo do produto: ")
                try:
                    qtd = int(input("Digite a quantidade do produto: "))
                except:
                    print("quantidade invalida")   
                produto = self.loja.buscar_produto(cod)
                if produto != None:
                    if self.loja.compra_aberta != None:
                        if produto not in self.loja.compras:
                            self.loja.compra_aberta.itens.append(Item_de_compra(produto, qtd))
                        else:
                            print("Produto ja esta na lista de compras")
                else:
                    print("produto nao encontrado")

            elif opc == 11: #imprime a compra, duvidas aqui
                if self.loja.compra_aberta != None:
                    self.loja.printa_compra_aberta()

            elif opc == 12: #remove o produto por indice
                try:
                    indice = int(input("Digite o indice do produto: "))
                except:
                    print("indice invalido")
                
                if self.loja.compra_aberta != None:
                    if indice not in range(1,len(self.loja.compra_aberta.itens)+1):
                        print("indice incorreto")
                    self.loja.compra_aberta.itens.pop(indice-1)

            elif opc == 13: #atualiza a quantidade por indice
                try:
                    indice = int(input("Digite o indice do produto: "))
                    nova_qtd = int(input("Digite a nova quatidade do produto: "))
                except:
                    print("informacoes invalidas")
                if indice not in range(1,len(self.loja.compra_aberta.itens)+1):
                    print("indice incorreto")
                self.loja.compra_aberta.itens[indice-1].quantidade = nova_qtd

            elif opc == 14:
                print(f"Numero de produtos: {self.loja.r_numero_produtos()}")

            elif opc == 15:
                print(f"Numero de vendas: {self.loja.r_numero_vendas()}")

            elif opc == 16:
                print(f"Valor total vendido: {self.loja.r_valor_tot_vend()}")

            elif opc == 17:
                print(f"Valor medio das compras: {self.loja.r_valor_med_compras()}")

            elif opc == 18:
                print(f"Numero de usuarios: {self.loja.r_numero_usuarios()}")

            elif opc == 19:
                pessoa = self.loja.r_usuario_mais_compras()
                print(f"Usuario que mais fez compras:")
                print(f"NOME: {pessoa.nome}")
                print(f"EMAIL: {pessoa.email}")
                print(f"CPF: {pessoa.cpf}")
                
            elif opc == 20:
                print("5 produtos mais caros:")
                for produtos in self.loja.r_5_mais_caros():
                    print(f"NOME: {produtos.nome}")
                    print(f"Preco unitario: {produtos.preco()}")
                    print(f"Categoria: {produtos.categoria}")
                    print(f"Codigo: {produtos.codigo}")

            elif opc == 21:
                self.loja.r_5_mais_vendidos()

            elif opc == 22:
                self.loja.r_usuarios_compras()

            elif opc == 23:
                self.loja.salvar("loja2.txt")
                break

app = App()
app.executar()