def pomacckibidi(message, bot, types):
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_id = types.KeyboardButton("id")
    btn_usr = types.KeyboardButton("usr")
    markup_reply.add(btn_id, btn_usr)
    id = message.from_user.id
    bot.send_message(message.chat.id, f"твой id: {id}")
