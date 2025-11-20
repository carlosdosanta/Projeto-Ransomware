from cryptography.fernet import Fernet
import os

# Gera a chave (usar uma vez)
def gerar_chave():
    if not os.path.exists("chave.key"):
        chave = Fernet.generate_key()
        with open("chave.key", "wb") as arq:
            arq.write(chave)
        print("Chave gerada.")
    else:
        print("A chave já existe.")

# Carrega a chave existente
def carregar_chave():
    return open("chave.key", "rb").read()

# Lista arquivos dentro de uma pasta
def listar_arquivos(pasta):
    arquivos = []
    for raiz, _, nomes in os.walk(pasta):
        for nome in nomes:
            caminho = os.path.join(raiz, nome)
            if not nome.endswith(".key"):
                arquivos.append(caminho)
    return arquivos
