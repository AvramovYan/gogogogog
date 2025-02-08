import telebot
from telebot import types
from Mikheev import Mikheev, answer
bot = telebot.TeleBot("7024653639:AAFxfsxImjJSj-mtkNEeuIdnu8I6OftepbI")
@bot.message_handler(commands=["help","start"])
def info(message):
    bot.send_message(message.chat.id,"startlox")

@bot.message_handler(commands=['mikheev'])
def memes(message):
    Mikheev(message, bot, types)

@bot.callback_query_handler(func=lambda call: True)
def show_meme_or_joke(call):
    if call.message:
        answer(call, bot, types)

