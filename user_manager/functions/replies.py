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
        "1. Mansagem 1",
        "2. Mansagem 2",
        "3. Mansagem 3"
        "4. Mansagem 4"
        "5. Mansagem 5"
    ]
    return regras

def regra_1_keyboard():
    texto = (
        "<b>⛳ | Plataforma e Modalidade:</b>\n\n"
        "• Operamos apenas dentro da <b>BET365</b>.\n\n"
        "• Nosso foco é exclusivamente na modalidade <b>Mais de 0.5 Escanteios nos Próximos 10 Minutos</b>.\n\n"
    )
    
    keyboard = [["OK, entendi ✅"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    return texto, reply_markup

def regra_2_keyboard():
    texto = (
        "<b>📊 | Metodologia e Entradas</b>\n\n"
        "• Nossas entradas são baseadas em análises pré-jogo e, <b>principalmente em leituras de jogo ao vivo</b>. Não contamos com a sorte.\n\n"
        "• Nossa metodologia tem 2 etapas simples: \n\n"
        "<b>1️⃣. Etapa</b>\n"
        "Entramos com 1,5% da banca para que ocorra +0.5 escanteios nos próximos 10 minutos.\n\n" 
        "<b>2️⃣. Etapa</b>\n"
        "Se após 8:30 min ainda não houver resultado, ativamos a proteção:\n"
        "Como proteção, uma nova entrada com <b>4,5%</b> da banca para +0.5 escanteios nos 10 min seguintes.\n\n"
        "<b>Exemplo prático na imagem acima ⬆️:</b> \n\n"

        #"1ª entrada 1,5% : <b>10 aos 20 min.</b>\n\n"
        #"Proteção ativa ao chegar no <b>minuto 18:30</b>\n\n"
        # "1ª entrada 4,5% : <b>20 aos 30 min</b>."
        
    )
    keyboard = [["OK, entendi ✅"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    return texto, reply_markup

def regra_3_keyboard():
    texto = (
        "<b>emoji | titulo:</b>\n\n"
        "• descrição 1.\n\n"
        "• descrição 2.\n\n"
        "• descrição 3.\n\n"
    )
    keyboard = [["OK, entendi ✅"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    return texto, reply_markup

def regra_4_keyboard():
    texto = (
        "<b>⛳ | Plataforma e Modalidade:</b>\n\n"
        "• Operamos apenas dentro da <b>BET365</b>.\n\n"
        "• Nosso foco é exclusivamente na modalidade <b>Mais de 0.5 Escanteios nos Próximos 10 Minutos</b>.\n\n"
    )
    keyboard = [["OK, entendi ✅"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    return texto, reply_markup

def regra_5_keyboard():
    texto = (
        "**🎯 Plataforma e Modalidade:**\n\n"
        "• Todas as nossas operações são realizadas exclusivamente na Bet365.\n"
        "• Jogamos na modalidade Mais de 0,5 escanteios nos próximos 10 minutos.\n"
        "• Nosso ciclo de operação vai do início ao fim de cada mês 💰"
    )
    keyboard = [["OK, entendi ✅"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    return texto, reply_markup

def get_regra_individual(numero_regra):
    regras_funcoes = {
        0: regra_1_keyboard,
        1: regra_2_keyboard,
        2: regra_3_keyboard,
        3: regra_4_keyboard,
        4: regra_5_keyboard
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
