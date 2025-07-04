import sys
import os
import asyncio
import logging
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram.error import Conflict
from dotenv import load_dotenv
from user_manager.funcions.handlers import start

# Configuração básica de logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Adiciona a raiz do projeto ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

load_dotenv()
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    """Loga os erros causados por Updates."""
    logger.error("Exception while handling an update:", exc_info=context.error)


def register_handlers(app):
    app.add_handler(CommandHandler('start', start))

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Adiciona o error handler
    app.add_error_handler(error_handler)

    register_handlers(app)
    logger.info('Bot está rodando...')
    try:
        # drop_pending_updates evita conflitos com instâncias anteriores
        app.run_polling(drop_pending_updates=True)
    except Conflict:
        logger.warning('Conflito detectado: outra instância de polling já está em execução.')
    except Exception as e:
        logger.critical(f'Ocorreu um erro fatal que encerrou o bot: {e}')

if __name__ == '__main__':
    main()
