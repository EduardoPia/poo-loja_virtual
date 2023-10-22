# Arquivo que sera executado para gerar nossa loja, e utilizara os outros arquivos

from app import App


if __name__ == '__main__':
    aplicativo = App()
    aplicativo.executar()