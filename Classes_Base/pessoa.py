# Definicao da classe compra, que armazena os dados de uma pessoa

class Pessoa():
    
    def __init__(self,nome:str,email:str,cpf:str):
        if (type(nome) is not str) or (type(email) is not str) or (type(cpf) is not int and type(cpf) is not str):
            print("Informacoes invalidas")
            return None
        cpf = str(cpf)
        self.nome:str = nome
        self.email:str = email
        self.cpf:str = cpf
        
    
    
        
    