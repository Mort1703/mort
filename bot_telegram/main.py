#---------------------------------------------------------------------------



import telebot

from telebot import types



#---------------------------------------------------------------------------



bot = telebot.TeleBot('Ваш токен: ')
 
@bot.message_handler(commands=['start'])



#---------------------------------------------------------------------------



def welcome(message):
    sti = open('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
 
    # keyboard (Создание кнопок и приветствие)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("📋 Информация 📋")
    item2 = types.KeyboardButton("💎 О да, я хочу быть в топе! 💎")
    item3 = types.KeyboardButton("💻 Разработчики 💻")
 
    markup.add(item1, item2, item3)
 
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, помогу тебе ворваться в хип-хоп!".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
 
@bot.message_handler(content_types=['text'])



#---------------------------------------------------------------------------



def lalala(message):
    if message.chat.type == 'private':
        if message.text == '💎 О да, я хочу быть в топе! 💎':
 
 			# keyboard (Создание кнопок под текстом)
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("💸 Напишите крутой бит! 💸", callback_data='1')
            item2 = types.InlineKeyboardButton("⚡ Сделайте текст! ⚡", callback_data='2')
            item3 = types.InlineKeyboardButton("🎧 Сведите на высшем уровне! 🎧", callback_data='3')
            item4 = types.InlineKeyboardButton("🌟 Напишите трек! 🌟", callback_data='4')
 
            markup.add(item1, item2, item3, item4)
 
            bot.send_message(message.chat.id, 'Что вам нужно?', reply_markup=markup)

        # elif message.text == ' '
        elif message.text == "📋 Информация 📋":
            bot.send_message(message.chat.id, " 📃 Мы работаем в сфере создания треков уже 4 года." +
                " Наша профессиональная команда готова помочь вам с любыми музыкальными трудностями, мы обладаем лучшей аппаратурой для выполнений всех" + 
                " задач в сфере музыкального продюсирования. Наши услуги дают возможность максимально индивидуализировать продукт под себя.")

        elif message.text == "💻 Разработчики 💻":
            bot.send_message(message.chat.id, '🤖 Данный бот был разработан <b>LimeGeeg Corporation™️</b> & <b>Cat️</b>, || <b>YouTube: LimeGeeg️</b>', parse_mode='html')


        else:
            bot.send_message(message.chat.id, 'По другим вопросам пишите сюда → @mafioznik_mihail_zubenk')



#---------------------------------------------------------------------------



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:

        	# keyboard (Работа с кнопками под текстом)
            if call.data == '1':
                bot.send_message(call.message.chat.id, '💥 Пишите сюда → @mafioznik_mihail_zubenk')
            elif call.data == '2':
                bot.send_message(call.message.chat.id, '💥 Пишите сюда → @mafioznik_mihail_zubenk')
            elif call.data == '3':
                bot.send_message(call.message.chat.id, '💥 Пишите сюда → @mafioznik_mihail_zubenk')
            elif call.data == '4':
                bot.send_message(call.message.chat.id, '💥 Пишите сюда → @mafioznik_mihail_zubenk')
 
            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Спасибо за оброщение! 😘",
                reply_markup=None)
 
            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="Пишите, всегда поможем!")
 
    except Exception as e:
        print(repr(e))
 


#---------------------------------------------------------------------------


# Старт
bot.polling(none_stop=True)



#---------------------------------------------------------------------------