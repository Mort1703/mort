

import telebot

bot = telebot.TeleBot("5206328525:AAE9CtEWt07iDr41kNiO2u34UPTSMkckBaE")

@bot.message_handler(commands=["start", "help"])



def send_welcome(message):
	bot.reply_to(message, "Привет, как ты?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()