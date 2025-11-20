from utils import carregar_chave, listar_arquivos
from cryptography.fernet import Fernet

def criptografar_arquivo(caminho, chave):
    f = Fernet(chave)
    with open(caminho, "rb") as file:
        dados = file.read()

    # Proteção: evitar dupla criptografia
    try:
        f.decrypt(dados)
        print(f"[IGNORADO] {caminho} já parece criptografado.")
        return
    except:
        pass

    dados_cripto = f.encrypt(dados)

    with open(caminho, "wb") as file:
        file.write(dados_cripto)

    print(f"[OK] Criptografado: {caminho}")


def executar_criptografia(pasta):
    chave = carregar_chave()
    arquivos = listar_arquivos(pasta)

    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)

    print("\nCriptografia concluída.")
