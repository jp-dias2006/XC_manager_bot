import sys
import os
import logging
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler
from telegram.error import Conflict
from functions.handlers import start, callback_handler, handle_keyboard_messages
from dotenv import load_dotenv

# Cria um logger específico para este módulo
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO) # Define o nível mínimo de log a ser capturado

# Remove handlers existentes para evitar duplicação de logs
if logger.hasHandlers():
    logger.handlers.clear()

# Formato do log
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Handler para logs de nível INFO e DEBUG (saída padrão - stdout)
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.INFO)
stdout_handler.addFilter(lambda record: record.levelno < logging.WARNING) # Apenas logs abaixo de WARNING
stdout_handler.setFormatter(formatter)

# Handler para logs de nível WARNING, ERROR, CRITICAL (saída de erro - stderr)
stderr_handler = logging.StreamHandler(sys.stderr)
stderr_handler.setLevel(logging.WARNING) # Apenas logs a partir de WARNING
stderr_handler.setFormatter(formatter)

# Adiciona os handlers ao logger
logger.addHandler(stdout_handler)
logger.addHandler(stderr_handler)

# Adiciona a raiz do projeto ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

load_dotenv()
TOKEN = os.getenv('USER_BOT_TOKEN')

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    """Loga os erros causados por Updates."""
    logger.error("Exception while handling an update:", exc_info=context.error)

def register_handlers(app):
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CallbackQueryHandler(callback_handler))
    # Handler para mensagens do teclado personalizado
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_keyboard_messages))
    # app.add_handler(CommandHandler('info', info))

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
