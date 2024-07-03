import flet as ft
import telebot
import qrcode
from io import BytesIO

def main(page: ft.Page):
    ft.title = 'qr-bot'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def close_bs(e):
        bs.open = False
        bs.update()

    bs = ft.BottomSheet(
        ft.Container(
            ft.Column(
                [
                    ft.Text("       Бот запущен!"),
                    ft.ElevatedButton("        Понятно        ", on_click=close_bs),
                ],
                tight=True, alignment=ft.alignment.center
            ),
            padding=50,
        ),
        open=False,
    )
    page.overlay.append(bs),

    def bot(e):
        bs.open = True
        bs.update()
        
        bot = telebot.TeleBot('TOKEN')

        @bot.message_handler(commands=['start'])
        def start_message(message):
            name = str(message.chat.first_name)
            bot.send_message(message.chat.id,
                             f'Здравствуйте, {name}, я ваш бот по созданию qr-кодов! \n\nНапишите для создания стандртного qr-кода - /qr "ссылка".\n\nНапишите для создания qr с разными цветами - /qrc "цвет фигур на английском языке" "цвет заливки на английском языке" "ссылка".')

        @bot.message_handler(commands=['qr'])
        def generate_qr(message):
            try:
                link = message.text.replace('/qr ', '')
                qr = qrcode.QRCode(
                    version=1,
                    box_size=10,
                    border=5
                )
                qr.add_data(link)
                qr.make(fit=True)
                qr_img = qr.make_image(fill_color="black", back_color="white")

                pil_img = qr_img.get_image()

                resized_image = pil_img.resize((300, 300))

                buffer = BytesIO()
                resized_image.save(buffer, format='PNG')
                buffer.seek(0)

                bot.send_photo(message.chat.id, photo=buffer)

            except Exception as e:
                bot.reply_to(message, 'Пожалуйста, отправьте ваш запрос правильно!')

        @bot.message_handler(commands=['qrc'])
        def generate_qrc(message):
            try:
                link = message.text.replace('/qrc ', '')
                inf = link.split()
                back_c = str(inf[0])
                fill_c = str(inf[1])
                link = str(inf[2])

                qr = qrcode.QRCode(
                    version=1,
                    box_size=10,
                    border=5
                )
                qr.add_data(link)
                qr.make(fit=True)
                qr_img = qr.make_image(fill_color=fill_c, back_color=back_c)

                pil_img = qr_img.get_image()

                resized_image = pil_img.resize((300, 300))

                buffer = BytesIO()
                resized_image.save(buffer, format='PNG')
                buffer.seek(0)

                bot.send_photo(message.chat.id, photo=buffer)

            except Exception as e:
                bot.reply_to(message, 'Пожалуйста, отправьте ваш запрос правильно!')

        @bot.message_handler(content_types=['text'])
        def talk(message):
            bot.reply_to(message, 'Пожалуйста, отправьте ваш запрос правильно!')

        bot.polling()

    btn = ft.ElevatedButton(text='Запустить', on_click=bot, width=page.window_width/3, height=page.window_height/4)

    page.add(btn)

ft.app(target=main)
