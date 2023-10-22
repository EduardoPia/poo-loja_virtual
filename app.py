# Definicao da classe app, que sera utilizada para mediar a interacao do programa com o usuario
from tkinter import *
from tkinter import ttk # porque precisei disso????
from loja import Loja
from Classes_Base.produto import Produto
from Classes_Base.compra import Compra
from Classes_Base.pessoa import Pessoa
from Classes_Base.item_de_compra import Item_de_compra



class App:
    def __init__(self):
        self.loja = Loja()
        self.loja.carregar("loja.txt")
        
        self.root = Tk()
        
        self.main_frame = Frame(self.root)
        self.main_frame.pack(fill=BOTH, expand=1)

        self.my_canvas = Canvas(self.main_frame)
        self.my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        my_scrollbar = ttk.Scrollbar(self.main_frame, orient = VERTICAL, command=self.my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        self.my_canvas.configure(yscrollcommand=my_scrollbar.set)
        self.my_canvas.bind('<Configure>',lambda e: self.my_canvas.configure(scrollregion = self.my_canvas.bbox("all")))

        self.win = Frame(self.my_canvas)
        self.my_canvas.create_window((0,0), window=self.win, anchor="nw")
               
    def remover_labels_na_posicao(self,row, column):
        labels = self.win.grid_slaves(row=row, column=column)
        if labels != []:
            labels[0].grid_remove()
        
    def opcao_1(self):
        recebe = Tk()

        Nome =  Label(recebe, text = "Nome: ")
        Nome_e = Entry(recebe)
        Nome.grid(row=0, column=0)
        Nome_e.grid(row=0, column=1)
        
        Preco = Label(recebe, text = "Preco: ")
        Preco_e = Entry(recebe)
        Preco.grid(row=1, column=0)
        Preco_e.grid(row=1, column=1)
        
        Categoria = Label(recebe, text = "Categoria: ")
        Categoria_e = Entry(recebe)
        Categoria.grid(row=2, column=0)
        Categoria_e.grid(row=2, column=1)
        
        Codigo = Label(recebe, text = "Codigo: ")
        Codigo_e = Entry(recebe)
        Codigo.grid(row=3, column=0)
        Codigo_e.grid(row=3, column=1)
        
        def cria_prod():
            nome = Nome_e.get()
            preco = Preco_e.get()
            categoria = Categoria_e.get()
            codigo = Codigo_e.get()
            recebe.destroy()
            self.remover_labels_na_posicao(1,3)
            resultado = Label(self.win, text = "Falha ao cadastrar")
            resultado.grid(row = 1, column = 3)
            preco = float(preco)
            produtinho = Produto(nome,preco, categoria ,codigo)
            self.loja.produtos.append(produtinho)
            self.remover_labels_na_posicao(1,3)
            resultado = Label(self.win, text = f"Produto cadastrado com sucesso")
            resultado.grid(row = 1, column = 3)
        
        botao = Button(recebe, text = "Enviar informacoes", command=cria_prod)
        botao.grid(row=4,column=0)
        recebe.mainloop()
 
    def opcao_2(self):
        self.remover_labels_na_posicao(2,3)
        produtos = ""
        for n in self.loja.produtos:
            produtos += f"{self.loja.produtos.index(n)+1} - cod = {n.codigo}; nome = {n.nome}; preco = {n.preco()}; qnt = {n.quantidade_em_estoque()} \n"
        resultado = Label(self.win, text = f"Produtos: \n {produtos}")
        resultado.grid(row = 2, column = 3)
      
    def opcao_3(self):
        recebe = Tk()
    
        Codigo =  Label(recebe, text = "Codigo: ")
        Codigo_e = Entry(recebe)
        Codigo.grid(row=0, column=0)
        Codigo_e.grid(row=0, column=1)
        
        def get_info():
            codigo = Codigo_e.get()
            recebe.destroy()
            
            produto = self.loja.buscar_produto(codigo)
            self.remover_labels_na_posicao(3,3)
            if produto != None:
                info = f"Nome: {produto.nome} \n Quantidade: {produto.quantidade_em_estoque()} \n Preco: {produto.preco()} \n Categoria: {produto.categoria}"
                resultado = Label(self.win, text = f"Produto: \n {info}")
                resultado.grid(row = 3, column = 3)
            else:
                resultado = Label(self.win, text = f"Produto nao encotrado ")
                resultado.grid(row = 3, column = 3)

        botao = Button(recebe, text = "Enviar informacoes", command=get_info)
        botao.grid(row=1,column=0)
        recebe.mainloop()
    
    def opcao_4(self):
        recebe = Tk()
    
        Codigo =  Label(recebe, text = "Codigo: ")
        Codigo_e = Entry(recebe)
        Codigo.grid(row=0, column=0)
        Codigo_e.grid(row=0, column=1)
        
        Desconto =  Label(recebe, text = "Novo Desconto: ")
        Desconto_e = Entry(recebe)
        Desconto.grid(row=1, column=0)
        Desconto_e.grid(row=1, column=1)
        
        def adq_prod():
            codigo = Codigo_e.get()
            dsc = Desconto_e.get()
            recebe.destroy()
            #self.remover_labels_na_posicao(4,3)
            resultado = Label(self.win, text = f"Desconto inválido")
            resultado.grid(row = 4, column = 3)
            dsc = float(dsc)
            if (dsc >= 1.0) or (dsc < 0.0):
                return None
            produto = self.loja.buscar_produto(codigo)
            #self.remover_labels_na_posicao(4,3)
            if produto != None:
                produto.atualizar_desconto(dsc)
                resultado = Label(self.win, text = f"Desconto atualizada com sucesso")
                resultado.grid(row = 4, column = 3)
            else:
                resultado = Label(self.win, text = f"Produto nao encontrado")
                resultado.grid(row = 4, column = 3)
        
        botao = Button(recebe, text = "Enviar informacoes", command=adq_prod)
        botao.grid(row=2,column=0)
        recebe.mainloop()
            
    def opcao_5(self):
        recebe = Tk()
    
        Codigo =  Label(recebe, text = "Codigo: ")
        Codigo_e = Entry(recebe)
        Codigo.grid(row=0, column=0)
        Codigo_e.grid(row=0, column=1)
        
        Quantidade =  Label(recebe, text = "Quantidade adquirida: ")
        Quantidade_e = Entry(recebe)
        Quantidade.grid(row=1, column=0)
        Quantidade_e.grid(row=1, column=1)
        
        def adq_prod():
            codigo = Codigo_e.get()
            qnt = Quantidade_e.get()
            recebe.destroy()
            self.remover_labels_na_posicao(5,3)
            resultado = Label(self.win, text = f"Informação inválida")
            resultado.grid(row = 5, column = 3)
            qnt = int(qnt)
            if (qnt<0):
                return None
            produto = self.loja.buscar_produto(codigo)
            if produto != None:
                produto.registrar_aquisicao(qnt)
                resultado = Label(self.win, text = f"Quantidade atualizada com sucesso")
                resultado.grid(row = 5, column = 3)
            else:
                resultado = Label(self.win, text = f"Produto nao encontrado")
                resultado.grid(row = 5, column = 3)
        
        botao = Button(recebe, text = "Enviar informacoes", command=adq_prod)
        botao.grid(row=2,column=0)
        recebe.mainloop()
    
    def opcao_6(self):
        recebe = Tk()
    
        Codigo =  Label(recebe, text = "Codigo: ")
        Codigo_e = Entry(recebe)
        Codigo.grid(row=0, column=0)
        Codigo_e.grid(row=0, column=1)
        
        def adq_prod():
            codigo = Codigo_e.get()
            recebe.destroy()
            produto = self.loja.buscar_produto(codigo)
            self.remover_labels_na_posicao(6,3)
            if produto != None:
                self.loja.produtos.pop(self.loja.produtos.index(produto))
                resultado = Label(self.win, text = f"Produto removido com sucesso")
                resultado.grid(row = 6, column = 3)
            else:
                resultado = Label(self.win, text = f"Produto nao encontrado")
                resultado.grid(row = 6, column = 3)
        
        botao = Button(recebe, text = "Enviar informacoes", command=adq_prod)
        botao.grid(row=1,column=0)
        recebe.mainloop()
    
    def opcao_7(self):
        recebe = Tk()
    
        Nome =  Label(recebe, text = "Nome: ")
        Nome_e = Entry(recebe)
        Nome.grid(row=0, column=0)
        Nome_e.grid(row=0, column=1)
        
        Email =  Label(recebe, text = "Email: ")
        Email_e = Entry(recebe)
        Email.grid(row=1, column=0)
        Email_e.grid(row=1, column=1)
        
        Cpf =  Label(recebe, text = "Cpf: ")
        Cpf_e = Entry(recebe)
        Cpf.grid(row=2, column=0)
        Cpf_e.grid(row=2, column=1)
        
        def ini_compra():
            nome = Nome_e.get()
            email = Email_e.get()
            cpf = Cpf_e.get()
            recebe.destroy()
            
            client = Pessoa(nome,email,cpf)
            self.loja.iniciar_compra(client)
            self.remover_labels_na_posicao(7,3)
            resultado = Label(self.win, text = f"Compra iniciada com sucesso")
            resultado.grid(row = 7, column = 3)
        
        botao = Button(recebe, text = "Enviar informacoes", command=ini_compra)
        botao.grid(row=3,column=0)
        recebe.mainloop()
    
    def opcao_8(self):
        if self.loja.compra_aberta != None:
            self.loja.cancelar_compra()
        self.remover_labels_na_posicao(8,3)
        resultado = Label(self.win, text = f"Compra cancelada com sucesso")
        resultado.grid(row = 8, column = 3)
        
    def opcao_9(self):
        if self.loja.compra_aberta != None:
            self.loja.finalizar_compra()
        self.remover_labels_na_posicao(9,3)
        resultado = Label(self.win, text = f"Compra finalizada com sucesso    ")
        resultado.grid(row = 9, column = 3)
        
    def opcao_10(self):
        recebe = Tk()
    
        Codigo =  Label(recebe, text = "Codigo: ")
        Codigo_e = Entry(recebe)
        Codigo.grid(row=0, column=0)
        Codigo_e.grid(row=0, column=1)
        
        Quantidade =  Label(recebe, text = "Quantidade adquirida: ")
        Quantidade_e = Entry(recebe)
        Quantidade.grid(row=1, column=0)
        Quantidade_e.grid(row=1, column=1)
        
        def add_item():
            codigo = Codigo_e.get()
            qnt = Quantidade_e.get()
            recebe.destroy()
            self.remover_labels_na_posicao(10,3)
            resultado = Label(self.win, text = f"Quantidade invalida")
            resultado.grid(row = 10, column = 3)
            qnt = int(qnt)
            if qnt < 0:
                return None
            produto = self.loja.buscar_produto(codigo)
            if produto != None:
                    if self.loja.compra_aberta != None:
                        adicionar = 1
                        for item in self.loja.compra_aberta.itens:
                            if item.produto.nome == produto.nome:
                                resultado = Label(self.win, text = f"Produto ja esta na compra        ")
                                resultado.grid(row = 10, column = 3)
                                adicionar = 0
                                break
                        if adicionar == 1:
                            self.loja.compra_aberta.itens.append(Item_de_compra(produto, qnt))
                            resultado = Label(self.win, text = f"item adicionado com sucesso   ")
                            resultado.grid(row = 10, column = 3)
                    else:
                        resultado = Label(self.win, text = f"Nao ha compra aberta           ")
                        resultado.grid(row = 10, column = 3)
            else:
                resultado = Label(self.win, text = f"Produto nao encontrado         ")
                resultado.grid(row = 10, column = 3)
        
        botao = Button(recebe, text = "Enviar informacoes", command=add_item)
        botao.grid(row=2,column=0)
        recebe.mainloop()
        
    def opcao_11(self):
        info = ""
        if self.loja.compra_aberta == None:
            info += "Nao ha compra aberta"
        else:
            info += "--> Cliente "
            info += f"\n- Nome: {self.loja.compra_aberta.cliente.nome}"
            info += f"\n- Email: {self.loja.compra_aberta.cliente.email}"
            info += f"\n- Cpf: {self.loja.compra_aberta.cliente.cpf}"
            for item in self.loja.compra_aberta.itens:
                info += f"\n--> Item {self.loja.compra_aberta.itens.index(item)+1}: {item.produto.nome}"
                info += f"\n- Quantidade desejada: {item.quantidade}"
                info += f"\n- Preco unitario: {item.produto.preco()}"
                info += f"\n- Categoria: {item.produto.categoria}"
                info += f"\n- Codigo: {item.produto.codigo}"
            if len(self.loja.compra_aberta.itens) == 0:
                info += "\n-> Nao foram adicionados itens"
        self.remover_labels_na_posicao(11,3)
        resultado = Label(self.win, text = f"{info}")
        resultado.grid(row = 11, column = 3)
        
    def opcao_12(self):
        recebe = Tk()
    
        Indice =  Label(recebe, text = "Indice: ")
        Indice_e = Entry(recebe)
        Indice.grid(row=0, column=0)
        Indice_e.grid(row=0, column=1)
        
        def del_item():
            indice = Indice_e.get()
            recebe.destroy()
            self.remover_labels_na_posicao(12,3)
            resultado = Label(self.win, text = f"Indice incorreto")
            resultado.grid(row = 12, column = 3)
            indice = int(indice)
            
            if self.loja.compra_aberta != None:
                if indice not in range(1,len(self.loja.compra_aberta.itens)+1):
                    self.remover_labels_na_posicao(12,3)
                    resultado = Label(self.win, text = f"indice incorreto")
                    resultado.grid(row = 12, column = 3)
                else:
                    self.loja.compra_aberta.itens.pop(indice-1)
                    self.remover_labels_na_posicao(12,3)
                    resultado = Label(self.win, text = f"Item removido com sucesso")
                    resultado.grid(row = 12, column = 3)
            else:
                self.remover_labels_na_posicao(12,3)
                resultado = Label(self.win, text = f"Nao ha compra aberta")
                resultado.grid(row = 12, column = 3)
        
        botao = Button(recebe, text = "Enviar informacoes", command=del_item)
        botao.grid(row=1,column=0)
        recebe.mainloop()
        
    def opcao_13(self):
        recebe = Tk()
    
        Indice =  Label(recebe, text = "Indice: ")
        Indice_e = Entry(recebe)
        Indice.grid(row=0, column=0)
        Indice_e.grid(row=0, column=1)
        
        Quantidade =  Label(recebe, text = "Quantidade adquirida: ")
        Quantidade_e = Entry(recebe)
        Quantidade.grid(row=1, column=0)
        Quantidade_e.grid(row=1, column=1)
        
        def atu_qnt():
            indice = Indice_e.get()
            qnt = Quantidade_e.get()
            recebe.destroy()
            self.remover_labels_na_posicao(13,3)
            resultado = Label(self.win, text = f"Valores incorretos")
            resultado.grid(row = 13, column = 3)
            indice = int(indice)
            qnt = int(qnt)
            if qnt <0:
                return None
            
            if self.loja.compra_aberta != None:
                if indice not in range(1,len(self.loja.compra_aberta.itens)+1):
                    self.remover_labels_na_posicao(13,3)
                    resultado = Label(self.win, text = f"indice incorreto")
                    resultado.grid(row = 13, column = 3)
                else:
                    self.loja.compra_aberta.itens[indice-1].quantidade = qnt
                    self.remover_labels_na_posicao(13,3)
                    resultado = Label(self.win, text = f"Quantidade atualizada com sucesso")
                    resultado.grid(row = 13, column = 3)
            else:
                self.remover_labels_na_posicao(13,3)
                resultado = Label(self.win, text = f"Nao ha compra aberta")
                resultado.grid(row = 13, column = 3)
        
        botao = Button(recebe, text = "Enviar informacoes", command=atu_qnt)
        botao.grid(row=2,column=0)
        recebe.mainloop()
        
    def opcao_14(self):
        self.remover_labels_na_posicao(14,3)
        resultado = Label(self.win, text = f"Numero de produtos: {self.loja.r_numero_produtos()}")
        resultado.grid(row = 14, column = 3)

    def opcao_15(self):
        self.remover_labels_na_posicao(15,3)
        resultado = Label(self.win, text = f"Numero de vendas: {self.loja.r_numero_vendas()}")
        resultado.grid(row = 15, column = 3)

    def opcao_16(self):
        self.remover_labels_na_posicao(16,3)
        resultado = Label(self.win, text = f"Valor total vendido: {self.loja.r_valor_tot_vend()}")
        resultado.grid(row = 16, column = 3)
        
    def opcao_17(self):
        self.remover_labels_na_posicao(17,3)
        resultado = Label(self.win, text = f"Valor medio das compras: {self.loja.r_valor_med_compras()}")
        resultado.grid(row = 17, column = 3)
        
    def opcao_18(self):
        self.remover_labels_na_posicao(18,3)
        resultado = Label(self.win, text = f"Numero de usuarios: {self.loja.r_numero_usuarios()}")
        resultado.grid(row = 18, column = 3)
        
    def opcao_19(self):
        pessoa = self.loja.r_usuario_mais_compras()
        self.remover_labels_na_posicao(19,3)
        info = f"\nNome: {pessoa.nome} \nEmail: {pessoa.email} \nCpf: {pessoa.cpf}"
        resultado = Label(self.win, text = f"Usuario que mais fez compras: {info}")
        resultado.grid(row = 19, column = 3)
        
    def opcao_20(self):
        info = ""
        for produto in self.loja.r_5_mais_caros():
            info += f"\nNome: {produto.nome}"
            info += f"\nPreco unitario: {produto.preco()}"
            info += f"\nCategoria: {produto.categoria}"
            info += f"\nCodigo: {produto.codigo}"
        self.remover_labels_na_posicao(20,3)    
        resultado = Label(self.win, text = f"5 produtos mais caros: {info}")
        resultado.grid(row = 20, column = 3)
        
    def opcao_21(self):
        top = self.loja.r_5_mais_vendidos()
        info = ""
        for prod in top:
            info += f"\n-> Produto {top.index(prod)}:"
            info += f"\n- Nome: {prod[0]}"
            info += f"\n- Preco unitario: {prod[1]}"
            info += f"\n- Categoria: {prod[2]}"
        self.remover_labels_na_posicao(21,3)
        resultado = Label(self.win, text = f"5 produtos mais vendidos: {info}")
        resultado.grid(row = 21, column = 3)

    def opcao_22(self):
        lista_geral = self.loja.r_usuarios_compras()
        info = ""
        for i in range(len(lista_geral[0])):
            info += f"\n- Nome: {lista_geral[0][i]} \n- CPF: {lista_geral[1][i]} \n- Valor: {lista_geral[2][i]}"
        self.remover_labels_na_posicao(22,3)
        resultado = Label(self.win, text = f"--> Montante por usuario: {info}")
        resultado.grid(row = 22, column = 3)

    def opcao_23(self):
        recebe = Tk()
    
        nome_arq =  Label(recebe, text = "Nome do arquivo que sera salvo: ")
        nome_arq_e = Entry(recebe)
        nome_arq.grid(row=0, column=0)
        nome_arq_e.grid(row=0, column=1)
        self.remover_labels_na_posicao(23,3)
        resultado = Label(self.win, text = f"Nome invalido")
        resultado.grid(row = 23, column = 3)
        def salvar_loj():
            arquivo = nome_arq_e.get()
            recebe.destroy()
            self.loja.salvar(arquivo)
            self.win.destroy()
            self.root.destroy()
            self.main_frame.destroy()
        self.remover_labels_na_posicao(23,3)
        botao = Button(recebe, text = "Enviar informacoes", command=salvar_loj)
        botao.grid(row=1,column=0)
        recebe.mainloop()

    def menu(self):
        
        opc_1 = Button(self.win, text = "1. Cadastrar produto", command = self.opcao_1)
        opc_1.grid(row = 1, column = 0)
        opc_2 = Button(self.win, text = "2. Ver lista de produtos", command = self.opcao_2)
        opc_2.grid(row = 2, column = 0)
        opc_3 = Button(self.win, text = "3. Ver detalhes do produto", command = self.opcao_3)
        opc_3.grid(row = 3, column = 0)
        opc_4 = Button(self.win, text = "4. Atualizar desconto de produto", command = self.opcao_4)
        opc_4.grid(row = 4, column = 0)
        opc_5 = Button(self.win, text = "5. Registrar aquisicao de produto", command = self.opcao_5)
        opc_5.grid(row = 5, column = 0)
        opc_6 = Button(self.win, text = "6. Remover produto", command = self.opcao_6)
        opc_6.grid(row = 6, column = 0)
        opc_7 = Button(self.win, text = "7. Iniciar compra", command = self.opcao_7)
        opc_7.grid(row = 7, column = 0)
        opc_8 = Button(self.win, text = "8. Cancelar compra", command = self.opcao_8)
        opc_8.grid(row = 8, column = 0)
        opc_9 = Button(self.win, text = "9. Finalizar compra", command = self.opcao_9)
        opc_9.grid(row = 9, column = 0)
        opc_10 = Button(self.win, text = "10. Adicionar item na compra", command = self.opcao_10)
        opc_10.grid(row = 10, column = 0)
        opc_11 = Button(self.win, text = "11. Visualizar compra", command = self.opcao_11)
        opc_11.grid(row = 11, column = 0)
        opc_12 = Button(self.win, text = "12. Remover item da compra", command = self.opcao_12)
        opc_12.grid(row = 12, column = 0)
        opc_13 = Button(self.win, text = "13. Atualizar quantidade de item na compra", command = self.opcao_13)
        opc_13.grid(row = 13, column = 0)
        opc_14 = Button(self.win, text = "14. Relatório - Numero de produtos", command = self.opcao_14)
        opc_14.grid(row = 14, column = 0)
        opc_15 = Button(self.win, text = "15. Relatório - Número de vendas", command = self.opcao_15)
        opc_15.grid(row = 15, column = 0)
        opc_16 = Button(self.win, text = "16. Relatório - Valor total vendido", command = self.opcao_16)
        opc_16.grid(row = 16, column = 0)
        opc_17 = Button(self.win, text = "17. Relatório - Valor médio das compras", command = self.opcao_17)
        opc_17.grid(row = 17, column = 0)
        opc_18 = Button(self.win, text = "18. Relatório - Número de usuários", command = self.opcao_18)
        opc_18.grid(row = 18, column = 0)
        opc_19 = Button(self.win, text = "19. Relatório - Usuário que mais fez compras", command = self.opcao_19)
        opc_19.grid(row = 19, column = 0)
        opc_20 = Button(self.win, text = "20. Relatório - 5 produtos mais caros", command = self.opcao_20)
        opc_20.grid(row = 20, column = 0)
        opc_21 = Button(self.win, text = "21. Relatório - 5 produtos mais vendidos", command = self.opcao_21)
        opc_21.grid(row = 21, column = 0)
        opc_22 = Button(self.win, text = "22. Relatório - Montante por pessoa", command = self.opcao_22)
        opc_22.grid(row = 22, column = 0)
        opc_23 = Button(self.win, text = "23. Sair", command = self.opcao_23)
        opc_23.grid(row = 23, column = 0)


    def executar(self):
        titulo1 = Label(self.win, text = "Opcoes:")
        titulo1.grid(row = 0, column = 0)
        vazio = Label(self.win, text = "     ")
        vazio.grid(row = 0,column = 2)
        titulo2 = Label(self.win, text = "Resultados:")
        titulo2.grid(row = 0, column = 3)
        
        self.menu()
        
        self.win.mainloop()
 
aplicativo = App()
aplicativo.executar()