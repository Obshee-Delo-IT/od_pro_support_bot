import telebot
from telebot.types import BotCommand, WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = '5666097861:AAGqniTTfeDc7rxh6hIoTtMMl83uoH2shi4'

bot = telebot.TeleBot(  TOKEN)

bot.set_my_commands(
    commands=[
        BotCommand(command='/help', description='FAQ'),
        BotCommand(command='/start', description='Старт'),
        BotCommand(command='/webform', description='Веб форма')
    ]
)

@bot.message_handler(commands=['start','Start'])
def comand_hendler(message):
    bot.send_message(message.chat.id, 'Привет тут ты можешь заполнить форму, для навигации используй меню слева снизу экрана')

@bot.message_handler(commands=['/help', '/Help', '/FAQ', '/faq'])
def help_handler(message):
    bot.send_message(message.chat.id, 'Тут будет FAQ по боту')

@bot.message_handler(commands=['webForm', 'webform'])
def start_web_form(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Веб форма', web_app=WebAppInfo(url='https://forms.yandex.ru/u/653a3e6ee010db2c10cf9912/')))
    bot.send_message(message.chat.id, 'Нажми на кнопку снизу сообщения', reply_markup=markup)

bot.infinity_polling()