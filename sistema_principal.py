from tkinter import Tk
import tkinter as tk
import os
import customtkinter as ctk
from PIL import Image
import platform
from os import system
system('cls')

class App(tk.Tk):  # Herdando de Tk para criar a interface
    def __init__(self):
        super().__init__()
        self.pastaApp = os.path.dirname(__file__)
        self.subpasta_imagens = os.path.join(self.pastaApp, "imagens")
        self.verificar_tamanho_tela()
        self.title("Janela Maximizada com Frames")
        self.setup_frames()
        self.setup_widgets()
        self.frame_visivel_home = False  # Variável de controle para o estado do Frame Home
        self.frame_visivel_config = False # Variavel de controle para o estado do Frame Config
        self.frame_visivel_menu = False # Variavel de controle para o estado do Frame Menu

    def verificar_tamanho_tela(self):
        '''Configura a janela para se ajustar ao tamanho da tela.'''
        # Obtém a resolução da tela
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Configura o tamanho da janela
        self.geometry(f"{screen_width}x{screen_height}")
        
        # Maximiza dependendo do sistema operacional
        if platform.system() == "Windows":
            self.state('zoomed')  # Maximizar no Windows
        else:
            self.attributes('-fullscreen', True)  # Maximizar em macOS ou Linux

    def setup_frames(self):
        '''Configura os frames principais da interface.'''
        # Frame principal
        self.frame_principal = tk.Frame(self, bg="#ffffff")
        self.frame_principal.pack(side="top", fill="both", expand=True)

        # Frame esquerdo
        self.frame_esquerdo = tk.Frame(self.frame_principal, bg="#969aa2", width=70)
        self.frame_esquerdo.pack(side="left", fill="y")

        # Frame direito
        self.frame_direito = tk.Frame(self.frame_principal, bg="#ffffff", width=400)
        self.frame_direito.pack(side="right", fill="both", expand=True)

    def setup_widgets(self):
        '''Adiciona os widgets à interface.'''
        # Imagem de fundo no frame direito
        img_logo_path = os.path.join(self.subpasta_imagens, "background_image_logo.gif")
        img_logo = tk.PhotoImage(file=img_logo_path)
        self.l_logo = tk.Label(
            self.frame_direito,
            image=img_logo,
            bg="#ffffff",
            highlightthickness=2,
            highlightbackground="#ffffff",
            highlightcolor="#ffffff",
        )
        self.l_logo.image = img_logo  # Evita que a imagem seja coletada pelo garbage collector
        self.l_logo.pack(side="left", pady=10, padx=(50, 0))

        '''Criando o CTkFrame como contêiner para a página inicial'''
        self.label_home_frame = ctk.CTkFrame(
            self.frame_direito,
            fg_color="#969aa2",
            corner_radius=10
        )
        self.label_home_frame.place(x=10, y=220)
        self.label_home_frame.place_forget()

        # Configuração do layout para os botões
        for i in range(3):  # Até 3 colunas
            self.label_home_frame.grid_columnconfigure(i, weight=1, uniform="col")

        '''Cria um frame contendo os botões das Configurações.'''
        self.label_config_frame = ctk.CTkFrame(
            self.frame_direito,
            fg_color="#969aa2",
            corner_radius=10,
        )
        self.label_config_frame.place(x=10, y=120)
        self.label_config_frame.place_forget()

        # Configuração do layout para os botões
        for i in range(2):  # Até 2 colunas
            self.label_config_frame.grid_columnconfigure(i, weight=1, uniform="col")

        '''Cria um frame contendo os botões do Menu.'''
        self.label_menu_frame = ctk.CTkFrame(
            self.frame_direito,
            fg_color="#969aa2",
            corner_radius=10,
        )
        self.label_menu_frame.place(x=10, y=220)
        self.label_menu_frame.place_forget()

        # Configuração do layout para os botões
        for i in range(2):  # Até 2 colunas
            self.label_menu_frame.grid_columnconfigure(i, weight=1, uniform="col")

        '''Label do Título da Página Inicial'''
        self.label_titulo = ctk.CTkLabel(
            self.label_home_frame,
            text="Página Inicial:",
            font=("DM Sans", 30, "bold"),
            text_color="white",
        )
        # Centraliza o título acima dos botões
        self.label_titulo.grid(row=0, column=0, columnspan=3, pady=(10, 20),padx=(20,0), sticky='w')

        '''Label do Título das Configurações'''
        self.title_label = ctk.CTkLabel(
            self.label_config_frame,
            text="Configurações:",
            font=("DM Sans", 30, "bold"),
            text_color="white",
        )
        # Centralizando o título acima dos botões
        self.title_label.grid(row=0, column=0, columnspan=3, pady=(10, 20),padx=(20,0), sticky="w")

        '''Label do Título do Menu'''
        self.title_label = ctk.CTkLabel(
            self.label_menu_frame,
            text="Menu:",
            font=("DM Sans", 30, "bold"),
            text_color="white",
        )
        # Centralizando o título acima dos botões
        self.title_label.grid(row=0, column=0, columnspan=3, pady=(10, 20),padx=(20,0), sticky="w")

        # Configura os botões laterais
        self.add_side_buttons()

        # Adiciona os botões no label dinâmico: Página Inicial
        self.add_label_buttons()

        # Adicionando os botões no Label dinâmico: Configurações
        self.setup_config_frame()

        # Adicionando os botões no Label dinâmico: Configurações
        self.setup_menu_frame()



    def setup_menu_frame(self):
        # Informações dos botões
        button_info = {
            "Funções Administrativas": "funcoes_admins_icon.png",
            "Acessos e Ferramentas": "acessos_ferramentas_icon.png",
            "Configurações do sistema": "config_system_icon.png",
            "Gerenciamento e Informações": "gerenciamento_informacoes_icon.png",
            "Opções relacionadas à conta do Usuário": "config_user_aconout_icon.png",
            "Açõs Rápidas": "acoes_rapidas_icon.png",
            "Fechar Sistema": "close_system_icon.png",
        }

        # Criação dos botões em grid
        for index, (name, icon_file) in enumerate(button_info.items()):
            icon_path = os.path.join(self.subpasta_imagens, icon_file)
            icon = ctk.CTkImage(Image.open(icon_path), size=(50, 50))
            button = ctk.CTkButton(
                self.label_menu_frame,
                text=name,
                image=icon,
                compound="top",
                width=180,
                height=40,
                fg_color="#969aa2",
                hover_color="#65686d",
                text_color="white",
                font=("DM Sans", 14,"bold"),
                corner_radius=10,
                command=lambda t=name: print(f"{t} pressionado!"),
            )
            row = (index // 2) + 1  # Ajusta para começar da linha 1
            col = index % 2  # Determina a coluna
            button.grid(row=row, column=col, padx=20, pady=10, sticky="nsew")

    def setup_config_frame(self):
        # Informações dos botões
        button_texts = [
            "Perfil do usuário",
            "Configuração de idioma/tema",
            "Notificações",
            "segurança e privacidade",
            "Horário e Ponto",
            "Acesso a Documentos",
            "Suporte e Ajuda",
            "Acessibilidade",
        ]

        # Criando os botões organizados em grid
        for index, text in enumerate(button_texts):
            button = ctk.CTkButton(
                self.label_config_frame,
                text=text,
                width=180,
                height=40,
                fg_color="#969aa2",
                hover_color="#65686d",
                text_color="white",
                font=("DM Sans", 14,"bold"),
                corner_radius=10,
                command=lambda t=text: print(f"{t} pressionado!"),
            )
            row = (index // 2) + 1  # Ajusta para começar da linha 1
            col = index % 2  # Determina a coluna
            button.grid(row=row, column=col, padx=20, pady=10, sticky="nsew")

    # Adicionando os botões ao Frame dinâmico da página inicial
    def add_label_buttons(self):
        '''Adiciona botões dentro do frame dinâmico.'''
        buttons_info = {
            "Clientes": "cliente_icon.png",
            "Fornecedores": "fornecedores_icon.png",
            "Produtos/Serviços": "prod.serv_icon.png",
            "Transportadora": "transportadora_icon.png",
            "Compras": "compras_icon.png",
            "Arquivos fiscais": "arquivosfiscais_icon.png",
            "Faturamento": "faturamentos_icon.png",
            "Relatórios": "relatorio_icon.png",
            "NFS - e": "nfse_icon.png",
        }

        # Criação dos botões em grid
        for index, (name, icon_file) in enumerate(buttons_info.items()):
            icon_path = os.path.join(self.subpasta_imagens, icon_file)
            icon = ctk.CTkImage(Image.open(icon_path), size=(50, 50))

            button = ctk.CTkButton(
                self.label_home_frame,
                text=name,
                image=icon,
                compound="top",
                fg_color="#969aa2",
                hover_color="#65686d",
                text_color="white",
                font=("DM Sans", 14, 'bold'),
                command=lambda name=name: print(f"{name} pressionado!"),  # Exemplo de comando
            )

            # Coloca os botões em uma grade
            row = (index // 3) + 1  # Começa na linha 1 (linha 0 é o título)
            col = index % 3  # Determina a coluna
            button.grid(row=row, column=col, padx=20, pady=10, sticky="nsew")

    # Adicionando os botões do menu lateral
    def add_side_buttons(self):
        '''Adiciona os botões no frame esquerdo.'''
        icons = {
            "menu": "menu_icon.png",
            "home": "home_icon.png",
            "config": "config_icon.png",
            "save": "save_icon.png",
            "qrcode": "qrcode_icon.png",
            "backup": "backup_icon.png",
        }
        for name, icon_file in icons.items():
            self.add_button(icon_file, name)

    def add_button(self, icon_file, name):
        '''Adiciona um botão com ícone ao frame esquerdo.'''
        icon_path = os.path.join(self.subpasta_imagens, icon_file)
        icon = ctk.CTkImage(Image.open(icon_path), size=(70, 70))
        
        # Definir as cores de foco e fundo
        foco_color = "#182745" if name == "menu" else "#65686d"
        fundo_color = "#182745" if name == "menu" else "#969aa2"

        # Ajustar o padding para o botão de backup
        eixo = (0, 0) if name == "backup" else (0, 40)

        # Define a lógica para cada botão
        if name == "menu":
            button_command = self.open_menu
        elif name == "home":
            button_command = self.open_home_page
        elif name == "config":
            button_command = self.open_config
        elif name == "save":
            button_command = self.save_data
        elif name == "qrcode":
            button_command = self.generate_qrcode
        elif name == "backup":
            button_command = self.run_backup
        else:
            button_command = None  # Botão sem ação

        button = ctk.CTkButton(
            self.frame_esquerdo,
            text="",
            image=icon,
            compound="top",
            corner_radius=0,
            hover_color=foco_color,
            fg_color=fundo_color,
            width=70,
            command=button_command,
        )
        button.pack(pady=eixo, side="top", fill="x")

    # Função para esconder/mostrar o frame da página inicial
    def open_home_page(self):
        '''Alterna a visibilidade do frame dinâmico da página inicial.'''
        # Verifica se o frame atual já está visível
        if self.frame_visivel_home:
            # Se sim, apenas fecha ele
            self.label_home_frame.place_forget()
            self.frame_visivel_home = False
        else:
            # Fecha outros frames e exibe o atual
            self.close_all_dynamic_frames()
            self.label_home_frame.place(x=10, y=220)
            self.frame_visivel_home = True

    # Função para esconder/mostrar o frame das configurações
    def open_config(self):
        '''Alterna a visibilidade do frame dinâmico das configurações.'''
        # Verifica se o frame atual já está visível
        if self.frame_visivel_config:
            # Se sim, apenas fecha ele
            self.label_config_frame.place_forget()
            self.frame_visivel_config = False
        else:
            # Fecha outros frames e exibe o atual
            self.close_all_dynamic_frames()
            self.label_config_frame.place(x=10, y=220)
            self.frame_visivel_config = True

    # Função para esconder/mostrar o frame das configurações
    def open_menu(self):
        '''Alterna a visibilidade do frame dinâmico das configurações.'''
        # Verifica se o frame atual já está visível
        if self.frame_visivel_menu:
            # Se sim, apenas fecha ele
            self.label_menu_frame.place_forget()
            self.frame_visivel_menu = False
        else:
            # Fecha outros frames e exibe o atual
            self.close_all_dynamic_frames()
            self.label_menu_frame.place(x=10, y=120)
            self.frame_visivel_menu = True

    def close_all_dynamic_frames(self):
        '''Fecha todos os frames dinâmicos.'''
        # Oculta o frame da Página Inicial
        if self.frame_visivel_home:
            self.label_home_frame.place_forget()
            self.frame_visivel_home = False

        # Oculta o frame das Configurações
        if self.frame_visivel_config:
            self.label_config_frame.place_forget()
            self.frame_visivel_config = False

        # Oculta o frame do Menu
        if self.frame_visivel_menu:
            self.label_menu_frame.place_forget()
            self.frame_visivel_menu = False

    def save_data(self):
        pass

    def generate_qrcode(self):
        pass

    def run_backup(self):
        pass


# Inicializando o app
if __name__ == "__main__":
    app = App()
    app.mainloop()