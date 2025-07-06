from telegram import ReplyKeyboardMarkup

START_MESSAGE_ADMIN = "Você é o administrador do grupo VIP!"

START_MESSAGE_VIP = (
    "Olá! Seja bem-vindo ao vip!\n"
    "Para mais informações, use /info.")

INFO_MESSAGE = "Qual é a sua dúvida? \n"

def info_menu():
    keyboard = [
        ["Assinaturas", "Suporte"],
        ["Como jogar?"],
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def sub_menu():
    keyboard = [
        ["Assinatura mensal: R$ 60"],
        ["Assinatura Trimestral: R$ 120"],
        ["Voltar"]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
