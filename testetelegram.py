from os import system
import customtkinter as ctk
from tkinter import *
from PIL import Image
from customtkinter import CTkImage
import os
import openpyxl
import pathlib  # Para manipular arquivos Excel
from openpyxl import load_workbook, Workbook
from tkinter import messagebox
from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import asyncio


system('cls')  # Limpa o terminal

# Caminho da pasta
pastaApp = os.path.dirname(__file__)

# Configuração Telegram
TELEGRAM_TOKEN = "your token"
CHAT_ID = "your chat id" # Para obter o chat_id, envie uma mensagem para o bot e acesse https://api.telegram.org/bot<seu_token>/getUpdates

bot = Bot(token=TELEGRAM_TOKEN)


async def testar_bot():
    try:
        # Envia uma mensagem de teste para o seu chat no Telegram de forma assíncrona
        await bot.send_message(chat_id=CHAT_ID, text="com todo respeito")
        print("Mensagem enviada com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")

# Chama a função de teste de forma assíncrona
asyncio.run(testar_bot())
