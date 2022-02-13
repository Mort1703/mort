import telebot

from telebot import types  



bot = telebot.TeleBot('5206328525:AAE9CtEWt07iDr41kNiO2u34UPTSMkckBaE')

@bot.message_handler(commands=['start'])



#Приветствие бота со стикером 
def welcome(message):
	sti =  open('static/welcome.webp' , 'rb')
	bot.send_stiker(message.chat.id, sti)

#Кнопочки для бота
	markup = typees.ReplyKeyBoardMarkup(resiza_keyboard = True)
	item1 = types.keyboardButton('Информация')
	item2 = types.keyboardButton('Что я могу делать')
	iten3 = types.keyboardButton('Разработчик')

	markup.add(item1, item2, iten3)

	bot.send_message(message.chat.id, "welcome to the club buddy".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)


@bot.message_handler(contect_types = ['text'])

	


def lalala(message):

	if message.chat.types == 'privet':

		if message.text == 'Что я могу делать':
			bot.send_message(message.chat.id,"Все что я умею это глотать слюну")
			bot.send_message(message.chat.id, 'Что вам нужно ?', reply_markup=markup)

 		elif message.text == 'Разработчик':
 			bot.send_message(message.chat.id, 'Привет, я морт пытаюсь тут на говнокодить. Может быть Сережка похвалит')

 		elif message.text == "Информация":
 			bot.send_message(message.chat.id, 'Пока еще не придумал')


 	except Exception as e:
 		print(repr(e))


bot.polling(none_stop=True)
