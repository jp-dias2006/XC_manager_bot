import pytest
from telegram import Update, Message, User as TgUser
from usr_bot.bot.handlers import start

class DummyMessage:
    def __init__(self):
        self.text = None
    async def reply_text(self, text):
        self.text = text

class DummyUpdate:
    def __init__(self):
        self.message = DummyMessage()

import asyncio

def test_start():
    update = DummyUpdate()
    context = None
    asyncio.run(start(update, context))
    assert update.message.text == 'Bem-vindo ao grupo VIP!'
