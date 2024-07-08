import telebot
from telebot import types
import json

TOKEN = 'TOKEN'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Hello, this is your bot for qr-code! \n\n Send /reg "password" for create account.', reply_markup=webAppKeyboard())

def webAppKeyboard():  
    keyboard = types.ReplyKeyboardMarkup(row_width=1)  
    webAppTest = types.WebAppInfo(
        "SITE")  
    one_butt = types.KeyboardButton(text="Open app", web_app=webAppTest)  
    keyboard.add(one_butt) 
    return keyboard

@bot.message_handler(commands=['reg'])
def send_welcome(message):
    filename = 'users.json'
    data = []

    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            if not isinstance(data, list):
                data = []
    except FileNotFoundError:
        pass

    name = message.text.split()[1]
    password = message.text.split()[2]
    chat_id = message.chat.id

    answer = 'Yes'

    for user in data:
        if user.get('chat_id') == chat_id:
            answer = 'No'

    for user in data:
        if user.get('name') == name:
            answer = 'No2'

    if answer == 'No':
        bot.send_message(message.chat.id, 'You have an account!')
        for user in data:
            if user.get('chat_id') == chat_id:
                bot.send_message(message.chat.id, f'Your data:\nName: {user.get("name")}\nPassword: {user.get("password")}')

    elif answer == 'No2':
        bot.reply_to(message, 'This name is busy!')

    else:
        data.append({
            "name": name,
            "password": password,
            "chat_id": chat_id
        })
        bot.reply_to(message, 'Successful!')


    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Sorry, i don't understand!")

bot.polling()
