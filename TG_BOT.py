#DEFAULT IMPORT (start)
import os
os.system('cls')
print("please wait . . .")

#MAIN IMPORT
import knowledge_base
from telebot import types, TeleBot as tocken
from dotenv import load_dotenv, find_dotenv

# Token
load_dotenv(find_dotenv())
bot = tocken(os.getenv('TOKEN'))

# Start bot
@bot.message_handler(commands=['start'])
def start(message):
    send_welcome(message)

@bot.message_handler(func=lambda message: True)

# Check condition
def handle_message(message):
    user_input = message.text
    output_for_tag = "Кажется такого нет. Вы можете написать нам на почту, чтобы мы добавили этот тег: (почта)"
    print("\n User say: ", user_input)

    if ("<" in user_input) and (">" in user_input):
        tag = user_input.strip()
        answer = knowledge_base.find_answer(tag)
        if answer is not None:
            bot.send_message(message.chat.id, answer)
            print("\n Bot say: ", answer)
        else:
            bot.send_message(message.chat.id, output_for_tag)
            print("\n Bot say: ", output_for_tag)

    elif user_input == 'Информация о боте':
        handle_bot_info(message)
    elif user_input == 'Пока':
        handle_stop(message)

# Check info
def handle_bot_info(message):
    bot.send_message(message.chat.id, "Этот бот находит тег и выводит его определение.")
    print("\n Bot say: ", "Этот бот находит тег и выводит его определение.")

# Condition bye
def handle_stop(message):
    bot.send_message(message.chat.id, "До свидания!")
    print("\n Bot say: ", "До свидания!")


def send_welcome(message):
    # Keyboard for info buttons
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Информация о боте', 'Пока']])
    bot.send_message(message.chat.id, 'Привет! Чем я могу помочь?', reply_markup=keyboard)

os.system('cls')
print("bot started )")

bot.polling(none_stop=True)

os.system('cls')
print("bot ended.")