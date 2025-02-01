import random



def vadim(message, bot, types):
    num = random.randint(1, 5)
    bot.send_message(message.chat.id, f"Я загадал число, :{num}!")
