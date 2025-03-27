import telebot
from datetime import datetime

# Substitua pelo token do seu bot
BOT_TOKEN = '7661763397:AAGoy9dFnqrcBKx-DSCNdF9xJgguv5zVVZg'
CHAT_ID = '7854524030'

bot = telebot.TeleBot(BOT_TOKEN)

# Função para enviar a solicitação de cadastro
def enviar_solicitacao(email):
    agora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    mensagem = (
        f"Solicitação de cadastro recebida:\n\n"
        f"E-mail: {email}\n"
        f"Data/Hora: {agora}\n\n"
        f"Responda com:\n/sim - Para autorizar\n/nao - Para recusar"
    )
    try:
        bot.send_message(CHAT_ID, mensagem)
        print("Mensagem de solicitação enviada com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar mensagem de solicitação: {e}")

# Comando para autorizar cadastro
@bot.message_handler(commands=['sim'])
def autorizar(mensagem):
    bot.reply_to(mensagem, "Cadastro autorizado! Atualizando sistema...")
    # Aqui você pode adicionar lógica para sinalizar o sistema principal

# Comando para recusar cadastro
@bot.message_handler(commands=['nao'])
def recusar(mensagem):
    bot.reply_to(mensagem, "Solicitação recusada.")

# Mantém o bot ativo
def iniciar_bot():
    print("Bot do Telegram iniciado.")
    bot.polling()

# Exemplo de teste para enviar a solicitação
if __name__ == '__main__':
    enviar_solicitacao("teste@exemplo.com")
    iniciar_bot()


""" import telebot
print('Tesntando telebot')
from datetime import datetime

# Substitua pelo token do seu bot
BOT_TOKEN = '7661763397:AAGoy9dFnqrcBKx-DSCNdF9xJgguv5zVVZg'
CHAT_ID = '7854524030'

bot = telebot.TeleBot(BOT_TOKEN)

# Mensagem para solicitação de cadastro
def enviar_solicitacao(email):
    agora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    mensagem = (
        f"Solicitação de cadastro recebida:\n\n"
        f"E-mail: {email}\n"
        f"Data/Hora: {agora}\n\n"
        f"Responda com:\n/sim - Para autorizar\n/não - Para recusar"
    )
    bot.send_message(CHAT_ID, mensagem)

# Comando para autorizar cadastro
@bot.message_handler(commands=['sim'])
def autorizar(mensagem):
    bot.reply_to(mensagem, "Cadastro autorizado! Atualizando sistema...")
    # Aqui você pode adicionar lógica para sinalizar o sistema principal

# Comando para recusar cadastro
@bot.message_handler(commands=['não'])
def recusar(mensagem):
    bot.reply_to(mensagem, "Solicitação recusada.")

# Mantém o bot ativo
def iniciar_bot():
    print("Bot do Telegram iniciado.")
    bot.polling()

# Exemplo de teste
if __name__ == '__main__':
    iniciar_bot() """