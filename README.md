# Desafio de Projeto - Simula um Ransomware no VScode Criptografando Arquivos do Usuário em Ambiente Controlado (BootCamp Santander - Cibersegurança 2025)

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
<img width="266" height="261" alt="image" src="https://github.com/user-attachments/assets/dd918871-11b8-48ae-bea9-877db65719d0" />


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





------------------------------------------------------------------------

## ▶️ 3. Como Executar no VS Code

1.  Abra a pasta `projeto_cripto` no VS Code.
2.  Abra o terminal integrado:\
    **Ctrl + \`**
3.  Execute o script principal:

4. comando: python main.py

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

<img width="753" height="120" alt="image" src="https://github.com/user-attachments/assets/13f908be-2a32-45ae-9898-e72257070b3c" />


2.  Coloque arquivos de teste na pasta `test_files`.

<img width="771" height="167" alt="image" src="https://github.com/user-attachments/assets/27bf28c1-5ff5-486a-9f79-980e8baffa4a" />

3.  Execute **opção 2** para criptografá-los.

   <img width="566" height="106" alt="image" src="https://github.com/user-attachments/assets/fc409229-bf7b-47dc-8e5f-28012dbdd322" />


------------------------------------------------------------------------

## 🔓 6. Processo de Descriptografia

Se quiser reverter:

    3 - Descriptografar arquivos

   


------------------------------------------------------------------------
 <img width="625" height="98" alt="image" src="https://github.com/user-attachments/assets/f420bc93-87bf-4657-b671-6435fa6b2d2e" />

------------------------------------------------------------------------
##🛡️ 7. Medidas de Mitigação (Prevenção) de Ransomware

As principais estratégias para prevenir um ataque de ransomware são:

1. Backups Regulares e Seguros

2. Atualização de Sistemas e Software
Mantenha o sistema operacional, aplicativos e firmware sempre atualizados (com patching em dia). As atualizações frequentemente corrigem vulnerabilidades de segurança que o ransomware pode explorar.

3. Conscientização e Treinamento do Usuário

4. Segurança de Acesso e Redes

5. Ferramentas de Proteção
Utilize soluções robustas de antivírus e anti-malware em todos os dispositivos, e certifique-se de que estão ativas e atualizadas.

Configure firewalls de rede e baseados em host para bloquear conexões de entrada não autorizadas.

Use ferramentas de filtragem de e-mail para colocar em quarentena anexos e URLs suspeitas.

------------------------------------------------------------------------
##🚨 8. O Que Fazer Depois da Infecção
Se você ou sua organização sofrer um ataque de ransomware, as etapas de resposta devem ser seguidas imediatamente e com calma para conter a propagação e iniciar a recuperação:

1. Isolamento e Contenção
Desconecte o dispositivo infectado imediatamente da rede (Wi-Fi, Ethernet, Bluetooth). Isso é crucial para evitar que o malware se espalhe para outros sistemas, unidades de rede e backups.

Não desligue o equipamento abruptamente, pois alguns ransomwares podem agravar os danos após uma reinicialização forçada.

2. Identificação e Notificação
Identifique a variante de ransomware, se possível. Isso pode ajudar a descobrir se há uma ferramenta de descriptografia gratuita disponível (sites como o No More Ransom podem ajudar).

Notifique as autoridades competentes (polícia ou órgãos especializados em crimes cibernéticos) e, em um ambiente corporativo, a equipe de TI/Segurança.

Em caso de violação de dados, comunique os afetados e autoridades conforme a LGPD.

3. Não Pague o Resgate
Especialistas em segurança e autoridades geralmente não recomendam pagar o resgate. Pagar não garante a recuperação dos dados e financia a indústria do crime cibernético, incentivando novos ataques.

4. Recuperação
Se os backups estiverem seguros e isolados, restaure os sistemas a partir deles.

Atenção: Certifique-se de que os backups não foram comprometidos ou que o ransomware não esteja dormente neles.

Use ferramentas de descriptografia (gratuitas ou comerciais) se uma estiver disponível para a variante de ransomware.

5. Análise e Reforço da Segurança
Realize uma análise forense para entender como o ransomware entrou (o vetor de ataque) e quais vulnerabilidades foram exploradas.

Corrija as vulnerabilidades identificadas (aplique patches, reconfigure sistemas).

Altere todas as senhas e reforce a segurança (revisite as medidas de mitigação).

Treine novamente a equipe sobre as lições aprendidas com o incidente.
 
 [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/carlos-henrique-80365897/)
