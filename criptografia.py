""" import os
import customtkinter as ctk
from tkinter import filedialog
from tkinter import messagebox
import time
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from hashlib import sha256  # Para garantir que a chave tenha 32 bytes
from cryptography.hazmat.primitives import padding

# Variável global para armazenar a chave
chave = None

# Função para garantir que a chave tenha o tamanho correto
def garantir_tamanho_chave(chave):
    # Garante que a chave tenha 32 bytes (para AES-256)
    if len(chave) < 32:
        chave = chave.ljust(32, b'\0')  # Preenche com 0 se a chave for menor
    elif len(chave) > 32:
        chave = chave[:32]  # Trunca se a chave for maior
    return chave

# Função de Criptografia
def criptografar_arquivo(chave, caminho_arquivo):
    try:
        # Garantir que a chave tenha 32 bytes
        chave = garantir_tamanho_chave(chave)

        with open(caminho_arquivo, "rb") as f:
            arquivo_conteudo = f.read()

        # Criar o objeto de cifra com a chave
        cipher = Cipher(algorithms.AES(chave), modes.CBC(chave[:16]), backend=default_backend())
        encryptor = cipher.encryptor()

        # Adicionar padding aos dados
        padder = padding.PKCS7(128).padder()
        dados_padded = padder.update(arquivo_conteudo) + padder.finalize()

        # Criptografar o conteúdo
        arquivo_criptografado = encryptor.update(dados_padded) + encryptor.finalize()

        # Salvar o arquivo criptografado
        caminho_arquivo_criptografado = caminho_arquivo + ".enc"
        with open(caminho_arquivo_criptografado, "wb") as f:
            f.write(arquivo_criptografado)

        os.remove(caminho_arquivo)
        print(f"Arquivo criptografado com sucesso: {caminho_arquivo_criptografado}")
    except Exception as e:
        print(f"Erro ao criptografar o arquivo: {e}")

# Função de Descriptografia
def descriptografar_arquivo(chave, caminho_arquivo):
    try:
        # Garantir que a chave tenha 32 bytes
        chave = garantir_tamanho_chave(chave)

        with open(caminho_arquivo, "rb") as f:
            arquivo_conteudo = f.read()

        # Criar o objeto de cifra com a chave
        cipher = Cipher(algorithms.AES(chave), modes.CBC(chave[:16]), backend=default_backend())
        decryptor = cipher.decryptor()

        # Descriptografar o conteúdo
        arquivo_descriptografado = decryptor.update(arquivo_conteudo) + decryptor.finalize()

        # Remover o padding
        unpadder = padding.PKCS7(128).unpadder()
        dados_sem_padding = unpadder.update(arquivo_descriptografado) + unpadder.finalize()

        # Salvar o arquivo descriptografado
        caminho_arquivo_descriptografado = caminho_arquivo.replace(".enc")
        with open(caminho_arquivo_descriptografado, "wb") as f:
            f.write(dados_sem_padding)

        print(f"Arquivo descriptografado com sucesso: {caminho_arquivo_descriptografado}")
    except Exception as e:
        print(f"Erro ao descriptografar o arquivo: {e}")

# Função para resetar o caminho da chave
def resetar_caminho_chave():
    chave_label.configure(text="")  # Reseta o label da chave

# Função para exibir mensagem temporária
def mostrar_mensagem_temporaria(mensagem):
    mensagem_label.configure(text=mensagem)
    app.update()  # Atualiza a janela imediatamente
    time.sleep(5)  # Espera por 5 segundos
    mensagem_label.configure(text="")  # Limpa a mensagem após 5 segundos

# Função chamada quando a criptografia for realizada
def criptografar_arquivo_como_usuario():
    caminho_chave = chave_label.cget("text")
    caminho_arquivo = filedialog.askopenfilename(title="Escolher arquivo para criptografar")
    if not caminho_arquivo:
        messagebox.showerror("Erro", "Selecione um arquivo para criptografar!")
        return

    if not chave:
        messagebox.showerror("Erro", "Selecione o arquivo da chave!")
        return

    criptografar_arquivo(chave, caminho_arquivo)
    
    resetar_caminho_chave()  # Reseta o caminho da chave
    mostrar_mensagem_temporaria("Arquivo criptografado com sucesso!")  # Exibe a mensagem

# Função chamada quando a descriptografia for realizada
def descriptografar_arquivo_como_usuario():
    caminho_chave = chave_label.cget("text")
    caminho_arquivo = filedialog.askopenfilename(title="Escolher arquivo para descriptografar")
    if not caminho_arquivo:
        messagebox.showerror("Erro", "Selecione um arquivo para descriptografar!")
        return

    if not chave:
        messagebox.showerror("Erro", "Selecione o arquivo da chave!")
        return

    descriptografar_arquivo(chave, caminho_arquivo)
    
    resetar_caminho_chave()  # Reseta o caminho da chave
    mostrar_mensagem_temporaria("Arquivo descriptografado com sucesso!")  # Exibe a mensagem

# Função chamada para buscar a chave
def buscar_chave():
    global chave  # Torna a variável 'chave' global
    caminho_chave = filedialog.askopenfilename(title="Escolher arquivo da chave", filetypes=[("Arquivos de chave", "*.key")])
    chave_label.configure(text=caminho_chave)  # Atualiza o label com o caminho escolhido
    if caminho_chave:
        with open(caminho_chave, "rb") as f:
            chave = f.read()  # Lê a chave do arquivo e armazena na variável global
            chave = garantir_tamanho_chave(chave)  # Garante que a chave tenha 32 bytes

# Configuração da janela principal
app = ctk.CTk()
app.title('Sistema de Criptografia e Descriptografificação')
app.geometry("600x400")

# Label para mostrar o caminho da chave
chave_label = ctk.CTkLabel(app, text="Caminho da chave não selecionado", width=400, height=30)
chave_label.pack(pady=20)

# Botão para escolher o arquivo da chave
buscar_button = ctk.CTkButton(app, text="Escolher chave", command=buscar_chave)
buscar_button.pack(pady=10)

# Botão para criptografar o arquivo
criptografar_button = ctk.CTkButton(app, text="Criptografar", command=criptografar_arquivo_como_usuario)
criptografar_button.pack(pady=10)

# Botão para descriptografar o arquivo
descriptografar_button = ctk.CTkButton(app, text="Descriptografar", command=descriptografar_arquivo_como_usuario)
descriptografar_button.pack(pady=10)

# Label para mostrar mensagens temporárias
mensagem_label = ctk.CTkLabel(app, text="", width=400, height=30, text_color="green")
mensagem_label.pack(pady=20)

# Iniciar a interface
app.mainloop()
"""


import os
import customtkinter as ctk
from tkinter import filedialog
from cryptography.fernet import Fernet


# Função chamada para buscar o caminho da chave
# Função para carregar a chave
def carregar_chave(caminho_chave):
    with open(caminho_chave, "rb") as chave_arquivo:
        return chave_arquivo.read()

# Função para criptografar o arquivo
def criptografar_arquivo(nome_arquivo, caminho_chave):
    chave = carregar_chave(caminho_chave)
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
    
    # Excluir o arquivo original
    os.remove(nome_arquivo)
    print(f"Arquivo '{nome_arquivo}' original excluído.")

# Função para descriptografar o arquivo
def descriptografar_arquivo(nome_arquivo_criptografado, caminho_chave):
    chave = carregar_chave(caminho_chave)
    fernet = Fernet(chave)

    # Lê o arquivo criptografado
    with open(nome_arquivo_criptografado, "rb") as arquivo_criptografado:
        dados_criptografados = arquivo_criptografado.read()

    # Descriptografa os dados
    dados_originais = fernet.decrypt(dados_criptografados)

    # Salva o arquivo original
    nome_arquivo_saida = nome_arquivo_criptografado.replace(".enc", "")
    with open(nome_arquivo_saida, "wb") as arquivo_descriptografado:
        arquivo_descriptografado.write(dados_originais)
    print(f"Arquivo '{nome_arquivo_saida}' descriptografado com sucesso!")

    # Excluir o arquivo criptografado
    os.remove(nome_arquivo_criptografado)
    print(f"Arquivo '{nome_arquivo_criptografado}' criptografado excluído.")


def buscar_chave():
    caminho_chave = filedialog.askopenfilename(title="Escolher arquivo da chave", filetypes=[("Arquivos de chave", "*.key")])
    chave_label.configure(text=caminho_chave)  # Atualiza a label com o caminho escolhido
    return caminho_chave

# Função chamada para buscar o arquivo a ser criptografado/descriptografado
def buscar_arquivo():
    caminho_arquivo = filedialog.askopenfilename(title="Escolher arquivo", filetypes=[("Todos os arquivos", "*.*")])
    arquivo_label.configure(text=caminho_arquivo)  # Atualiza a label com o caminho do arquivo
    return caminho_arquivo

# Função para iniciar a criptografia
def iniciar_criptografia():
    caminho_chave = chave_label.cget("text")
    caminho_arquivo = arquivo_label.cget("text")
    
    if caminho_chave and caminho_arquivo:
        criptografar_arquivo(caminho_arquivo, caminho_chave)
        # Atualizar a interface
        arquivo_label.configure(text="")  # Limpa o caminho do arquivo após criptografar

# Função para iniciar a descriptografia
def iniciar_descriptografia():
    caminho_chave = chave_label.cget("text")
    caminho_arquivo = arquivo_label.cget("text")
    
    if caminho_chave and caminho_arquivo:
        descriptografar_arquivo(caminho_arquivo, caminho_chave)
        # Atualizar a interface
        arquivo_label.configure(text="")  # Limpa o caminho do arquivo após descriptografar

# Interface gráfica com customtkinter
app = ctk.CTk()

# Título da janela
app.title("Sistema de Criptografia e Descriptografia")
app.geometry("600x400")

# Label e Botão para carregar a chave
chave_label = ctk.CTkLabel(app, text="Caminho da chave: Nenhuma chave selecionada.", width=400, height=25)
chave_label.pack(pady=20)

botao_buscar_chave = ctk.CTkButton(app, text="Escolher Chave", command=buscar_chave)
botao_buscar_chave.pack(pady=5)

# Label e Botão para escolher o arquivo
arquivo_label = ctk.CTkLabel(app, text="Nenhum arquivo selecionado.", width=400, height=25)
arquivo_label.pack(pady=20)

botao_buscar_arquivo = ctk.CTkButton(app, text="Escolher Arquivo", command=buscar_arquivo)
botao_buscar_arquivo.pack(pady=5)

# Botões para criptografar e descriptografar
botao_criptografar = ctk.CTkButton(app, text="Criptografar Arquivo", command=iniciar_criptografia)
botao_criptografar.pack(pady=10)

botao_descriptografar = ctk.CTkButton(app, text="Descriptografar Arquivo", command=iniciar_descriptografia)
botao_descriptografar.pack(pady=10)

# Rodar o aplicativo
app.mainloop()