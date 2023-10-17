# Definicao da classe app, que sera utilizada para mediar a interacao do programa com o usuario
# Definicao da classe app, que sera utilizada para mediar a interacao do programa com o usuario
from loja import Loja
from Classes_Base.produto import Produto


class App:
    def __init__(self):
        self.loja = Loja()

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

        opcao = int(input("Escolha uma opcao:"))
        return opcao
    
    def executar(self):
        while True:
            opc = self.menu()
            if opc == 1: #cadastra um produto na loja
                nome =  input("Digite o nome: ")
                preco = float(input("Digite o preco: "))
                categoria = input("Digite a categoria: ")
                codigo = input("Digite o codigo: ")
                
                produtinho = Produto(nome,preco, categoria ,codigo)
                
                self.loja.produtos.append(produtinho)

            elif opc == 2: # imprime lista de produtos na loja 
                # imprime indice, codigo, nome e valor com desconto
                for n in self.loja.produtos:
                    print(f"{self.loja.produtos.index(n)+1} - {self.loja.produtos.codigo} {self.loja.produtos.nome} {self.loja.produtos.preco()}") 

            elif opc == 3: #imprime informacoes do produto buscado por codigo
                cod = input("Digite o codigo do produto: ")
                produto =self.loja.buscar_produto(cod)

                print(f"NOME: {produto.nome}")
                print(f"QUANTIDADE: {produto.quantidade_em_estoque()}")
                print(f"DESCONTO: {produto.get_desconto}")
                print(f"PRECO COM DESCONTO: {produto.preco()}")
                print(f"CATEGIORIA: {produto.categoria}")
                print(f"CODIGO: {produto.codigo}")
                print(f"PRECO SEM DESCONTO: {produto.get_preco}")

            elif opc == 4: #atualiza desconto por codigo
                cod = input("Digite o codigo do produto: ")
                produto = self.loja.buscar_produto(cod)
                desc = float(input("Digite o novo desconto (0.0-1.0): "))
                produto.atualizar_desconto(desc)

            elif opc == 5: #registra aquisicao por codigo
                cod = input("Digite o codigo do produto: ")
                produto = self.loja.buscar_produto(cod)
                qtd = int(input("Digite a quantidade adquirida junto ao fornecedor: "))
                produto.registrar_aquisicao(qtd)
            
            elif opc == 6: #remove um produto da loja por codigo
                cod = input("Digite o codigo do produto: ")
                produto = self.loja.buscar_produto(cod)
                self.loja.produtos.pop(produto)

            elif opc == 7:
                pass

            elif opc == 8:
                pass

            elif opc == 9:
                pass

            elif opc == 10:
                pass

            elif opc == 11:
                pass

            elif opc == 12:
                pass

            elif opc == 13:
                pass

            elif opc == 14:
                pass

            elif opc == 15:
                pass

            elif opc == 16:
                pass

            elif opc == 17:
                pass

            elif opc == 18:
                pass

            elif opc == 19:
                pass

            elif opc == 20:
                pass

            elif opc == 21:
                pass

            elif opc == 22:
                pass

            elif opc == 23:
                break


