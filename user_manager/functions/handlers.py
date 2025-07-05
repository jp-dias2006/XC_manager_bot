from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    print(f"Usuário iniciou o bot: id={user.id}, nome={user.full_name}")

    if user.id == 7520921378:
        await update.message.reply_text
        ("""
        Bem vindo ao grupo Vip!.
        Para mais informações, use o comando /info.

        """)
    elif user.id == 1302885619:
        await update.message.reply_text('Você é o administrador do grupo VIP!')

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('informalção 1\ninformalção 2\ninformalção 3.')
