from cryptography.fernet import Fernet
import os

# # Função para gerar a chave
# def gerar_chave():
#     chave = Fernet.generate_key()
#     with open("chave_secreta.key", "wb") as chave_arquivo:
#         chave_arquivo.write(chave)
#     print("Chave gerada e salva no arquivo 'chave_secreta.key'.")

# Função para carregar a chave
def carregar_chave():
    with open("chave_secreta.key", "rb") as chave_arquivo:
        return chave_arquivo.read()

# Função para criptografar o arquivo
def criptografar_arquivo(nome_arquivo):
    # Verifica se o arquivo existe
    if not os.path.exists(nome_arquivo):
        print(f"Erro: o arquivo '{nome_arquivo}' não foi encontrado.")
        return

    chave = carregar_chave()  # Carrega a chave salva
    fernet = Fernet(chave)

    # Lê os dados do arquivo Excel
    with open(nome_arquivo, "rb") as arquivo:
        dados = arquivo.read()

    # Criptografa os dados
    dados_criptografados = fernet.encrypt(dados)

    # Cria o arquivo criptografado
    with open(nome_arquivo + ".enc", "wb") as arquivo_criptografado:
        arquivo_criptografado.write(dados_criptografados)
    print(f"Arquivo '{nome_arquivo}' criptografado com sucesso!")

# ------------------------
# Passos para garantir
# ------------------------

# Passo 1: Gerar a chave (executar apenas uma vez)
#gerar_chave()  # Execute apenas uma vez para gerar a chave

# Passo 2: Criptografar o arquivo Excel
criptografar_arquivo("emails_cadastrados.xlsx")  # Substitua pelo nome do seu arquivo