import os
import sys
import logging
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackQueryHandler
from dotenv import load_dotenv
from datetime import datetime, timezone
from . import db
from . import replies

save_user = db.save_user
user_exists = db.user_exists

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

# Start command

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    nome_usuario = user.first_name
    saudacao, texto_regras, reply_markup = replies.start_msg(nome_usuario)
    await asyncio.sleep(1)
    await update.message.reply_text(saudacao, parse_mode="HTML")
    await asyncio.sleep(2)
    await update.message.reply_text(texto_regras, reply_markup=reply_markup)

async def rules(update: Update, context: ContextTypes.DEFAULT_TYPE):
    regras = replies.rules_msg()
    await update.message.reply_text(regras, parse_mode="HTML")

# ===== CÓDIGO INLINE BUTTONS (COMENTADO PARA BACKUP) =====
"""
async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # Confirma o clique do botão
    
    if query.data == "ver_regras":
        # Usuário clicou para ver as regras - mostra a primeira regra
        regra_texto, reply_markup = replies.regra_1()
        await query.message.reply_text(
            text=regra_texto,
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )
    
    elif query.data == "regra_2":
        # Remove o botão da mensagem anterior e mostra confirmação
        await query.edit_message_text(
            text=query.message.text + "\n\n✅ OK, entendido"
        )
        # Mostra a segunda regra
        regra_texto, reply_markup = replies.regra_2()
        await query.message.reply_text(
            text=regra_texto,
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )
    
    elif query.data == "regra_3":
        # Remove o botão da mensagem anterior e mostra confirmação
        await query.edit_message_text(
            text=query.message.text + "\n\n✅ OK, entendido"
        )
        # Mostra a terceira regra
        regra_texto, reply_markup = replies.regra_3()
        await query.message.reply_text(
            text=regra_texto,
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )
    
    elif query.data == "regras_concluidas":
        # Remove o botão da mensagem anterior e mostra confirmação
        await query.edit_message_text(
            text=query.message.text + "\n\n✅ OK, entendido"
        )
        # Usuário terminou de ler todas as regras
        texto_final, reply_markup = replies.mensagem_regras_concluidas()
        await query.message.reply_text(text=texto_final, reply_markup=reply_markup)
"""

# ===== NOVO CÓDIGO COM KEYBOARD BUTTONS =====

# Dicionário para controlar o estado de cada usuário
user_states = {}

async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler apenas para o botão inline inicial 'ver_regras'"""
    query = update.callback_query
    await query.answer()
    
    if query.data == "ver_regras":
        user_id = query.from_user.id
        user_states[user_id] = "aguardando_regra_1"
        
        # Mostra a primeira regra com keyboard button
        regra_texto, reply_markup = replies.regra_1_keyboard()
        await query.message.reply_text(
            text=regra_texto,
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )

async def handle_keyboard_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para processar mensagens do teclado personalizado"""
    user_id = update.effective_user.id
    message_text = update.message.text
    
    # Verifica se o usuário está no fluxo de regras
    if user_id not in user_states:
        return
    
    current_state = user_states[user_id]
    
    if current_state == "aguardando_regra_1" and message_text == "OK, entendi":
        # Usuário confirmou regra 1
        user_states[user_id] = "aguardando_regra_2"
        regra_texto, reply_markup = replies.regra_2_keyboard()
        await update.message.reply_text(
            text=regra_texto,
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )
    
    elif current_state == "aguardando_regra_2" and message_text == "OK, entendi":
        # Usuário confirmou regra 2
        user_states[user_id] = "aguardando_regra_3"
        regra_texto, reply_markup = replies.regra_3_keyboard()
        await update.message.reply_text(
            text=regra_texto,
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )
    
    elif current_state == "aguardando_regra_3" and message_text == "OK, entendi":
        # Usuário confirmou regra 3 - finaliza o processo
        del user_states[user_id]  # Remove o estado do usuário
        texto_final, reply_markup = replies.mensagem_regras_concluidas()
        await update.message.reply_text(
            text=texto_final, 
            reply_markup=reply_markup
        )
    
    elif current_state.startswith("aguardando_regra"):
        # Usuário enviou mensagem incorreta durante o fluxo de regras
        await update.message.reply_text(
            "⚠️ Por favor, clique no botão correspondente à regra atual para continuar."
        )
