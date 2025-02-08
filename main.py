
import telebot

bot = telebot.TeleBot("7024653639:AAFxfsxImjJSj-mtkNEeuIdnu8I6OftepbI")
@bot.message_handler(commands=["help","start"])
def info(message):
    bot.send_message(message.chat.id,"startlox")


@bot.message_handler(commands=["whatch"])
def lala(message):
    lalala(message, bot, types)

@bot.message_handler(content_types=["text"])
def kors(message):
    korsak(message, bot, types)