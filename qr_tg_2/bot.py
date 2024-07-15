import telebot
from telebot import types
import json
import flet as ft
import threading

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    bot = None
    bot_thread = None

    def bot_def(e):
        page.snack_bar = ft.SnackBar(ft.Text("Бот запустился!", color=ft.colors.LIGHT_BLUE_ACCENT_700), bgcolor=ft.colors.BLACK54)
        nonlocal bot, bot_thread
        TOKEN = token_input.value
        bot = telebot.TeleBot(TOKEN)

        # Удаление вебхука перед началом опроса
        bot.remove_webhook()

        @bot.message_handler(commands=['start'])
        def send_welcome(message):
            bot.send_message(message.chat.id, 'Здравствуйте, это бот для создания QR-кодов! \n\nОтправьте /reg "имя" "пароль" для регистрации аккаунта.\n\nЕсли у вас появились проблемы - /help', reply_markup=webAppKeyboard())

        def webAppKeyboard():
            keyboard = types.ReplyKeyboardMarkup(row_width=1)
            webAppTest = types.WebAppInfo(url_input.value)
            one_butt = types.KeyboardButton(text="Открыть приложение", web_app=webAppTest)
            keyboard.add(one_butt)
            return keyboard

        @bot.message_handler(commands=['reg'])
        def register_user(message):
            try:
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
                    bot.send_message(message.chat.id, 'У вас есть аккаунт!')
                    for user in data:
                        if user.get('chat_id') == chat_id:
                            bot.send_message(message.chat.id, f'Ваша информация:\nИмя: {user.get("name")}\nПароль: {user.get("password")}')

                elif answer == 'No2':
                    bot.reply_to(message, 'Такое имя занято!')

                else:
                    data.append({
                        "name": name,
                        "password": password,
                        "chat_id": chat_id
                    })
                    bot.reply_to(message, 'Сохранено!')

                with open(filename, 'w') as file:
                    json.dump(data, file, indent=4)

            except:
                bot.reply_to(message, 'Отправьте вашу информацию правильно!')

        @bot.message_handler(commands=['help'])
        def send_help(message):
            bot.send_message(message.chat.id, f'Если у вас возникли проблемы с приложением, то посетите сайт {url_input.value}.')

        @bot.message_handler(func=lambda message: True)
        def echo_all(message):
            bot.reply_to(message, "Простите, я не понимаю!")

        bot_thread = threading.Thread(target=bot.polling)
        bot_thread.start()

    def stop_bot(e):
        nonlocal bot, bot_thread
        if bot:
            bot.stop_polling()
            bot_thread.join()
            bot = None
            bot_thread = None
            page.snack_bar = ft.SnackBar(ft.Text("Бот остановлен!", color=ft.colors.LIGHT_BLUE_ACCENT_700), bgcolor=ft.colors.BLACK54)
            page.snack_bar.open = True
            page.update()

    token_input = ft.TextField(label='Токен')
    url_input = ft.TextField(label='Ссылка')
    start_btn = ft.ElevatedButton(text='Старт', on_click=bot_def)
    stop_btn = ft.ElevatedButton(text='Остановить бота', on_click=stop_bot)

    page.add(token_input, url_input, ft.Row([start_btn, stop_btn],alignment=ft.MainAxisAlignment.CENTER))

if __name__ == '__main__':
    ft.app(target=main)
