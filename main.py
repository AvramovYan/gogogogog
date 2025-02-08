admins = [2073232860]
import telebot
bot = telebot.TeleBot("7024653639:AAFxfsxImjJSj-mtkNEeuIdnu8I6OftepbI")
@bot.message_handler(commands=["help","start"])
def info(message):
    user_id = message.chat.id
    if user_id in admins:
        bot.send_message(message.chat.id, "ты че АДМИН?!?!?!?")
    else:
        bot.send_message(message.chat.id,"startlox")
