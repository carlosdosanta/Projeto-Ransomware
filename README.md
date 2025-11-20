# Desafio de Projeto Que Simula Um Ransomware no VScode Criptografando Arquivos do Usuário em Ambiente Controlado (BootCamp Santander - Cibersegurança 2025)

Este documento descreve o passo a passo completo para rodar o projeto de
criptografia em Python, incluindo estrutura do projeto, execução e
funcionamento dos scripts.

------------------------------------------------------------------------

## 📁 1. Estrutura do Projeto

Crie uma pasta chamada **projeto_cripto** e coloque dentro dela os
seguintes arquivos:

    projeto_cripto/
    │ main.py
    │ utils.py
    │ criptografar.py
    │ descriptografar.py
    └── test_files/
           seus_arquivos_para_teste.txt

------------------------------------------------------------------------

## 🧩 2. Função de Cada Arquivo

### **utils.py**

Contém funções utilitárias, como a geração e leitura da chave de
criptografia.

### **criptografar.py**

Responsável por criptografar arquivos dentro da pasta `test_files`.

### **descriptografar.py**

Responsável por descriptografar arquivos também dentro da pasta
`test_files`.

### **main.py**

Menu principal que chama todas as funções acima.

<img width="555" height="138" alt="image" src="https://github.com/user-attachments/assets/636f0dcc-75e3-4e6e-a274-830e3ba7bb0a" />




------------------------------------------------------------------------

## ▶️ 3. Como Executar no VS Code

1.  Abra a pasta `projeto_cripto` no VS Code.
2.  Abra o terminal integrado:\
    **Ctrl + \`**
3.  Execute o script principal:

```{=html}
<!-- -->
```
    python main.py

------------------------------------------------------------------------

## 📌 4. Opções do Menu

Ao executar, você verá:

    1 - Gerar chave de criptografia
    2 - Criptografar arquivos
    3 - Descriptografar arquivos
    0 - Sair

------------------------------------------------------------------------

## 🔐 5. Processo de Criptografia

1.  Gere a chave **(opção 1)** --- será criado o arquivo `key.key`.
2.  Coloque arquivos de teste na pasta `test_files`.
3.  Execute **opção 2** para criptografá-los.

------------------------------------------------------------------------

## 🔓 6. Processo de Descriptografia

Se quiser reverter:

    3 - Descriptografar arquivos

------------------------------------------------------------------------

