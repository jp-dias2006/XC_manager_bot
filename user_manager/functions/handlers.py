import os
from telegram import Update
from telegram.ext import ContextTypes
from . import chat_messages

msg_admin = chat_messages.START_MESSAGE_ADMIN
msg_start = chat_messages.START_MESSAGE_VIP
msg_info = chat_messages.INFO_MESSAGE

ADMIN = os.getenv('MANAGER_ID')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    user = update.effective_user

    if user.id == int(ADMIN):
        await update.message.reply_text(msg_admin)
        print(f"O admin {user.full_name}, iniciou o bot")

    else:
        await update.message.reply_text(msg_start)
        print(f"Usuário iniciou o bot: id={user.id}, nome={user.full_name}")

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(msg_info)
    