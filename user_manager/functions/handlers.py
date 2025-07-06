import os
import sys
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from . import replies
from dotenv import load_dotenv

# Define messages and menus

admin_msg = replies.START_MESSAGE_ADMIN
start_msg = replies.START_MESSAGE_VIP
info_msg = replies.INFO_MESSAGE

info_menu = replies.info_menu
sub_menu = replies.sub_menu

# Create a logger for the handlers module

logger = logging.getLogger("Handlers")
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

# Get the admin ID from environment variables

ADMIN = os.getenv('MANAGER_ID')

# Start command handler

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    user = update.effective_user

    if user.id == int(ADMIN):
        await update.message.reply_text(admin_msg)

        logger.info(f"Administrador: {user.full_name}, iniciou o bot")

    else:
        await update.message.reply_text(start_msg)

        logger.info(f"Usuário iniciou o bot: id={user.id}, nome={user.full_name}")  

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        info_msg,
        reply_markup=info_menu()
    )

async def sub(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "Suporte":
        suporte_username = "diaslemes"
        suporte_link = f"https://t.me/{suporte_username}"
        keyboard = [
            [InlineKeyboardButton("Falar com o Suporte", url=suporte_link)]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(
            "Clique no botão abaixo para falar diretamente com o suporte humano:",
            reply_markup=reply_markup
        )
    elif text == "Assinaturas":
        await update.message.reply_text(
            "Escolha uma opção de assinatura:",
            reply_markup=sub_menu()
        )
    elif text == "Voltar":
        await info(update, context)
        
    else:
        await update.message.reply_text(
            "Opção inválida. Por favor, escolha uma opção válida."
        )

