import telebot
import random

bot = telebot.TeleBot("")
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
        bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
        bot.reply_to(message, "Привет! Как дела?")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
        bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['help'])
def send_bye(message):
        bot.reply_to(message, "Вот все команды:(/hello,/bye,/random_answer)")

@bot.message_handler(commands=['random_answer'])
def send_random_answer(message):
        random_answer= {
                "Да"
                "Нет"
                "Возможно частично"
        }
        bot.send_message(message.chat.id, f"вот твой случайный ответ"+{message.chat.id})

@bot.message_handler(commands=['animals'])
def send_mem(message):
    image = random.choice(os.listdir('animals'))
    with open(f'animals/{image}', 'rb') as f:
        bot.send_photo(message.chat.id, f)
    
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
        bot.reply_to(message, message.text)
    

bot.polling()

