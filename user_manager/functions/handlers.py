from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    print(f"Usuário iniciou o bot: id={user.id}, nome={user.full_name}")
    await update.message.reply_text('Bem-vindo ao grupo VIP!')

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Gostaria de saber mais sobre o grupo VIP?')
