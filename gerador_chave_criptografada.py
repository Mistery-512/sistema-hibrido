from cryptography.fernet import Fernet
import customtkinter as ctk
from tkinter import messagebox

def gerar_chave():
    # Gera uma chave única
    chave = Fernet.generate_key()
    # Salva a chave em um arquivo
    with open("chave_secreta.key", "wb") as chave_arquivo:
        chave_arquivo.write(chave)
    messagebox.showinfo('Sistema', 'Chave Gerada e salva no arquivo "Chave_secreta.key".')

# Interface gráfica com customtkinter
app = ctk.CTk()

# Título da janela
app.title("Gerador de Chave de Acesso")
app.geometry("600x400")

lbl = ctk.CTkLabel(app, text='Aviso: Clique apenas 1(uma) vez\npara Criar a Chave de Acesso caso ainda não tenha.')
lbl.pack(pady=20)

lbl2 = ctk.CTkLabel(app,text='Observação: Caso tenha criado a chave de acesso, não utilize este programa novamente.')
lbl2.pack(pady=20)

lbl3 = ctk.CTkLabel(app,text='Últimas observações:\nSistema de uso único.\nCaso você perca a chave de acesso ou a apague por engano,\nuse esse sistema novamente.\n\nAVISO: TOME MUITO CUIDADO COM A SUA CHAVE DE ACESSO.',font=('arial',15,'bold'))
lbl3.pack(pady=20)

btn = ctk.CTkButton(app, text='Clique aqui para Gerar Chave de Acesso.',command=gerar_chave)
btn.pack(pady=20)

app.mainloop()