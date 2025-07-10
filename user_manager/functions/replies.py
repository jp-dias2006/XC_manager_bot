from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove

# mensagem_regras = ("Antes de te adicionar em nosso grupo preciso te informar como funciona nossas regras")

def start_msg(nome_usuario):
    saudacao = f"Olá <b>{nome_usuario}</b>, Seja muito bem vindo(a) ao bot do grupo <b>X CANTOS OFICIAL ⛳🏆</b>"
    texto_regras = "Antes de te adicionar em nosso grupo preciso te informar como funcionam nossas regras."
    keyboard = [
        [InlineKeyboardButton("Concordo em ver as regras", callback_data="ver_regras")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return saudacao, texto_regras, reply_markup

def rules_msg():
    regras = [
        "1. Respeite todos os membros do grupo.",
        "2. Não compartilhe conteúdo ilegal ou ofensivo.",
        "3. Evite spam e mensagens repetitivas."
    ]
    return regras

def regra_1_keyboard():
    texto = "📋 **Regra 1:**\n\nRespeite todos os membros do grupo.\n\nEsta é a base da nossa comunidade. Trate todos com cortesia e educação."
    keyboard = [["OK, entendi"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    return texto, reply_markup

def regra_2_keyboard():
    texto = "🚫 **Regra 2:**\n\nNão compartilhe conteúdo ilegal ou ofensivo.\n\nMantenha o ambiente limpo e adequado para todos."
    keyboard = [["OK, entendi"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    return texto, reply_markup

def regra_3_keyboard():
    texto = "💬 **Regra 3:**\n\nEvite spam e mensagens repetitivas.\n\nQualidade é melhor que quantidade. Pense antes de enviar."
    keyboard = [["OK, entendi"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    return texto, reply_markup

# ===== FUNÇÕES INLINE ORIGINAIS (COMENTADAS PARA BACKUP) =====
"""
def regra_1():
    texto = "📋 **Regra 1:**\n\nRespeite todos os membros do grupo.\n\nEsta é a base da nossa comunidade. Trate todos com cortesia e educação."
    keyboard = [
        [InlineKeyboardButton("OK, entendido", callback_data="regra_2")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return texto, reply_markup

def regra_2():
    texto = "🚫 **Regra 2:**\n\nNão compartilhe conteúdo ilegal ou ofensivo.\n\nMantenha o ambiente limpo e adequado para todos."
    keyboard = [
        [InlineKeyboardButton("OK, entendido", callback_data="regra_3")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return texto, reply_markup

def regra_3():
    texto = "💬 **Regra 3:**\n\nEvite spam e mensagens repetitivas.\n\nQualidade é melhor que quantidade. Pense antes de enviar."
    keyboard = [
        [InlineKeyboardButton("OK, entendido", callback_data="regras_concluidas")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return texto, reply_markup
"""

def get_regra_individual(numero_regra):
    regras_funcoes = {
        0: regra_1_keyboard,
        1: regra_2_keyboard,
        2: regra_3_keyboard
    }
    
    if numero_regra in regras_funcoes:
        return regras_funcoes[numero_regra]()
    
    return None, None

def mensagem_regras_concluidas():
    texto = "✅ Perfeito! Você leu e concordou com todas as regras. Agora você pode ser adicionado ao grupo!"
    keyboard = [
        [InlineKeyboardButton("🔒 Entrar no Canal Privado", url="https://t.me/+0F0bHJ0vvKRkYjVh")],
        [InlineKeyboardButton("💬 Falar com Suporte", url="https://t.me/SuporteXCantos")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return texto, reply_markup
