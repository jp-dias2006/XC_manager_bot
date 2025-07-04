import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram.error import Conflict
from dotenv import load_dotenv
from user_manager.funcions.handlers import start

load_dotenv()
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

def register_handlers(app):
    app.add_handler(CommandHandler('start', start))

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    register_handlers(app)
    print('Bot está rodando...')
    try:
        # drop_pending_updates evita conflitos com instâncias anteriores
        app.run_polling(drop_pending_updates=True)
    except Conflict:
        print('Conflito detectado: outra instância de polling já está em execução.')

if __name__ == '__main__':
    main()
