from cryptography.fernet import Fernet

# Função para carregar a chave
def carregar_chave():
    with open("chave_secreta.key", "rb") as chave_arquivo:
        return chave_arquivo.read()

# Função para descriptografar o arquivo
def descriptografar_arquivo(nome_arquivo_criptografado, nome_arquivo_saida):
    chave = carregar_chave()  # Carrega a chave salva
    fernet = Fernet(chave)

    # Lê o arquivo criptografado
    with open(nome_arquivo_criptografado, "rb") as arquivo_criptografado:
        dados_criptografados = arquivo_criptografado.read()

    # Descriptografa os dados
    dados_originais = fernet.decrypt(dados_criptografados)

    # Salva o arquivo original
    with open(nome_arquivo_saida, "wb") as arquivo_descriptografado:
        arquivo_descriptografado.write(dados_originais)
    print(f"Arquivo '{nome_arquivo_saida}' descriptografado com sucesso!")

# ------------------------
# Passo para Descriptografar
# ------------------------

# Substitua pelo nome do seu arquivo criptografado e o nome desejado para o arquivo descriptografado
descriptografar_arquivo("emails_cadastrados.xlsx.enc", "emails_cadastrados_descriptografado.xlsx")
