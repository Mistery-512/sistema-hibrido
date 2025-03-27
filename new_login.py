import customtkinter as ctk
from customtkinter import CTkImage
from PIL import Image

# Configurando o CustomTkinter
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# Criando a janela principal
app = ctk.CTk()
state='zoomed'

# Carregando a imagem de fundo inicialmente
original_bg_image = Image.open("imagens/image_background_login.png")
bg_image = CTkImage(light_image=original_bg_image, size=(800, 600))

# Adicionando a imagem de fundo diretamente na janela
bg_label = ctk.CTkLabel(app, image=bg_image, text="")
bg_label.place(relx=0.5, rely=0.5, anchor="center")

# Função para ajustar a imagem de fundo ao redimensionar a janela
def ajustar_imagem(event):
    nova_largura = max(1, event.width)  # Garante que largura seja pelo menos 1
    nova_altura = max(1, event.height)  # Garante que altura seja pelo menos 1
    imagem_redimensionada = original_bg_image.resize((nova_largura, nova_altura))
    bg_image._light_image = imagem_redimensionada  # Atualiza a imagem interna
    bg_label.configure(image=bg_image)

# Vincula o evento de redimensionamento à função
app.bind("<Configure>", ajustar_imagem)

# Outros widgets sobre o fundo
logo_image = CTkImage(light_image=Image.open("imagens/logo_login_icon.png"), size=(100, 100))
logo_label = ctk.CTkLabel(app, image=logo_image, text="",fg_color='black')
logo_label.place(relx=0.5, rely=0.3, anchor="center")

# Inicia a aplicação
app.mainloop()