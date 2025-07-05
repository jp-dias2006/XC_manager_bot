import os
import sys
from dotenv import load_dotenv
import logging
from telegram import Update
from telegram.ext import ContextTypes
from . import chat_messages
from dotenv import load_dotenv

msg_admin = chat_messages.START_MESSAGE_ADMIN
msg_start = chat_messages.START_MESSAGE_VIP
msg_info = chat_messages.INFO_MESSAGE

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

if logger.hasHandlers():
    logger.handlers.clear()

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.INFO)
stdout_handler.addFilter(lambda record: record.levelno < logging.WARNING)
stdout_handler.setFormatter(formatter)

stderr_handler = logging.StreamHandler(sys.stderr)
stderr_handler.setLevel(logging.WARNING)
stderr_handler.setFormatter(formatter)

logger.addHandler(stdout_handler)
logger.addHandler(stderr_handler)

load_dotenv()
ADMIN = os.getenv('MANAGER_ID')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    user = update.effective_user

    if user.id == int(ADMIN):
        await update.message.reply_text(msg_admin)
        logger.info(f"Usuário administrador iniciou o bot: id={user.id}, nome={user.full_name}")

    else:
        await update.message.reply_text(msg_start)
        logger.info(f"Usuário iniciou o bot: id={user.id}, nome={user.full_name}")

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(msg_info)
    