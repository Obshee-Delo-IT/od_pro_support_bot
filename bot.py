import telebot
from telebot.types import BotCommand, WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = '****' # create token through https://t.me/BotFather

bot = telebot.TeleBot(TOKEN)

bot.set_my_commands(
    commands=[
        BotCommand(command='/help', description='FAQ'),
        BotCommand(command='/start', description='Старт'),
        BotCommand(command='/webform', description='Написать обращение')
    ]
)

@bot.message_handler(commands=['start','Start'])
def comand_hendler(message):
    bot.send_message(message.chat.id, '''🌟 Привет! 🌟

Это служба помощи и заботы участников конкурса «Общее дело-ПРО»!

Здесь вы можете задать любой вопрос, касающийся нашей деятельности и конкурса.

💬 Напишите свой вопрос, и мы постараемся ответить на него максимально быстро. Для этого вам необходимо нажать в левом нижнем углу «Меню» — «Написать обращение», и ввести ваш вопрос.''')

@bot.message_handler(commands=['help', 'Help', 'FAQ', 'faq'])
def help_handler(message):
    bot.send_message(message.chat.id, '''
💬 Нажмите в левом нижнем углу кнопку «Меню», затем «Написать обращение», и введите ваш вопрос в открывшуюся форму обращения.
Пишите свой вопрос только через эту форму. Сообщения, отправленные просто в бот, никто не увидит. Пользуйтесь командами бота.''')

@bot.message_handler(commands=['webForm', 'webform'])
def start_web_form(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Форма обращения', web_app=WebAppInfo(url='https://forms.yandex.ru/u/653a3e6ee010db2c10cf9912/')))
    bot.send_message(message.chat.id, 'Нажми на кнопку снизу сообщения', reply_markup=markup)

bot.infinity_polling()
