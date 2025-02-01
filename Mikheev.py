
def Mikheev(message, bot, types):
    chat_id = message.chat.id
    keyboard = types.InlineKeyboardMarkup()
    button_meme = types.InlineKeyboardButton(text="Мемы", callback_data='meme')
    button_joke = types.InlineKeyboardButton(text="Шутки", callback_data='joke')
    keyboard.add(button_meme, button_joke)
    bot.send_message(chat_id, 'Сделай правильный выбор:', reply_markup=keyboard)

def answer(call, bot, types):
    chat_id = call.chat.id
    keyboard = types.InlineKeyboardMarkup()

    if call.data == 'meme':
        meme_btn = types.InlineKeyboardButton(text="Мемы", url='https://gorbilet.com/blog/news/o-chinazes-top-15-memov-2024-goda')
        keyboard.add(meme_btn)
        bot.send_message(chat_id, 'Отборные мемы:', keyboard)
    elif call.data == 'joke':
        joke_btn = types.InlineKeyboardButton(text="Шутки", url='https://www.maximonline.ru/entertainment/luchshie-anekdoty-pro-pensionerov-i-pensiyu-id556196/')
        keyboard.add(joke_btn)
        bot.send_message(chat_id, 'Ответ для пенсионеров:', keyboard)

