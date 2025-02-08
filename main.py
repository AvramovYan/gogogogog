

import telebot


from vadim import Vadim
from telebot import types
from Mikheev import Mikheev, answer

admins = [2073232860]


bot = telebot.TeleBot("7024653639:AAFxfsxImjJSj-mtkNEeuIdnu8I6OftepbI")
@bot.message_handler(commands=["help","start"])
def info(message):



@bot.message_handler(commands=["whatch"])
def lala(message):
    lalala(message, bot, types)

@bot.message_handler(content_types=["text"])
def kors(message):
    korsak(message, bot, types)
    user_id = message.chat.id
    if user_id in admins:
        bot.send_message(message.chat.id, "ты че АДМИН?!?!?!?")
    else:
        bot.send_message(message.chat.id,"startlox")

@bot.message_handler(commands=['mikheev'])
def memes(message):
    Mikheev(message, bot, types)

@bot.callback_query_handler(func=lambda call: True)
def show_meme_or_joke(call):
    if call.message:
        answer(call, bot, types)



@bot.message_handler(commands=["Vadim"])
def Vadim (message):
    vadim(message, bot, types)

