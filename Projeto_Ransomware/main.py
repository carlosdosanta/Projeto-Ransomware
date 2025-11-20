from utils import gerar_chave
from criptografar import executar_criptografia
from descriptografar import executar_descriptografia

def main():
    print("""
=== SISTEMA DE CRIPTOGRAFIA TESTE ACADÊMICO ===
1 - Gerar chave (apenas uma vez)
2 - Criptografar arquivos da pasta 'test_files'
3 - Descriptografar arquivos da pasta 'test_files'
0 - Sair
""")

    opcao = input("Escolha: ")

    if opcao == "1":
        gerar_chave()
    elif opcao == "2":
        executar_criptografia("test_files")
    elif opcao == "3":
        executar_descriptografia("test_files")
    elif opcao == "0":
        print("Saindo...")
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()
