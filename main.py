
import telebot
from vadim import Vadim
bot = telebot.TeleBot("7024653639:AAFxfsxImjJSj-mtkNEeuIdnu8I6OftepbI")
@bot.message_handler(commands=["help","start"])
def info(message):
    bot.send_message(message.chat.id,"startlox")



@bot.message_handler(commands=["Vadim"])
def Vadim (message):
    vadim(message, bot, types)