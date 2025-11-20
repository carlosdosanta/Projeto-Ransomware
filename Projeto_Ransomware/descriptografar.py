from utils import carregar_chave, listar_arquivos
from cryptography.fernet import Fernet

def descriptografar_arquivo(caminho, chave):
    f = Fernet(chave)
    with open(caminho, "rb") as file:
        dados = file.read()

    try:
        dados_original = f.decrypt(dados)
    except:
        print(f"[IGNORADO] {caminho} não está criptografado ou já foi restaurado.")
        return

    with open(caminho, "wb") as file:
        file.write(dados_original)

    print(f"[OK] Descriptografado: {caminho}")


def executar_descriptografia(pasta):
    chave = carregar_chave()
    arquivos = listar_arquivos(pasta)

    for arquivo in arquivos:
        descriptografar_arquivo(arquivo, chave)

    print("\nDescriptografia concluída.")
