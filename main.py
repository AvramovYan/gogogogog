
import telebot
from telebot import types
from teacher import teacher
bot = telebot.TeleBot("7024653639:AAFxfsxImjJSj-mtkNEeuIdnu8I6OftepbI")
@bot.message_handler(commands=["help","start"])
def info(message):
    bot.send_message(message.chat.id,"startlox")


@bot.message_handler(commands=["teacher"])
def teach(message):
    teacher(message, bot, types)






bot.infinity_poling()