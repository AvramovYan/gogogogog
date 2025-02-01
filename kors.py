
def kors(message, bot, types):
    if "привет" == message.text:
        bot.send_message(message.chat.id, "привет")
    else:
        bot.send_message(message.chat.id, "...")
    if "пока" == message.text:
        bot.send_message(message.chat.id, "пока")
    else:
        bot.send_message(message.chat.id, "...")

def lala(message, bot, types):
    markup_inline = types.InlineKeyboardMarkup()
    btn_f = InlineKeyboardButton(text = 'фильмец', url='https://www.kinopoisk.ru/')
    markup_inline.add(btn_f)
    bot.send_message(message.chat.id, "ща открою", reply_markup=markup_inline)


