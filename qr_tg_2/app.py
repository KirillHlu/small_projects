import flet as ft
import qrcode
from io import BytesIO
import base64
import json
import telebot

TOKEN = input('Токен: ')
PORT = input('Порт: ')

def image_to_link(image_path):
    with open(image_path, "rb") as img_file:
        encoded_image = base64.b64encode(img_file.read()).decode("utf-8")
        image_link = "data:image/jpg;base64," + encoded_image
    return image_link

def main(page: ft.Page):
    page.scroll = True
    page.theme = ft.Theme(
        color_scheme_seed=ft.colors.BLUE_ACCENT_700,
    )

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def close_bs(e):
        name = input_name.value
        password = input_password.value

        with open('users.json', 'r') as file:
            data = json.load(file)

        for user in data:
            if user.get('name') == name:
                if password == user.get('password'):
                    qr = qrcode.QRCode(
                        version=1,
                        box_size=10,
                        border=5
                    )
                    qr.add_data(row1.controls[0].value)
                    qr.make(fit=True)
                    qr_img = qr.make_image(fill_color=row3.controls[0].value, back_color=row2.controls[0].value)

                    resized_image = qr_img.resize((300, 300))

                    buffer = BytesIO()
                    resized_image.save(buffer, format='PNG')
                    buffer.seek(0)

                    bot = telebot.TeleBot(TOKEN)

                    chat_id = user.get('chat_id')
                    photo_url = buffer

                    bot.send_photo(chat_id, photo_url, caption=f"Текст: '{row1.controls[0].value}'")

        bs.open = False
        bs.update()
        page.update()


    def save(e):
        generate(e)
        bs.open = True
        bs.update()


    def generate(e):
        background1 = row2.controls[0].value
        fill_c = row3.controls[0].value

        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5
        )

        qr.add_data(row1.controls[0].value)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color=fill_c, back_color=background1)

        resized_image = qr_img.resize((300, 300))

        buffer = BytesIO()
        resized_image.save(buffer, format='PNG')
        buffer.seek(0)
        img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        qr_image.controls[0].image_src = f'data:image/png;base64,{img_base64}'
        qr_image.controls[0].content = ft.Text('')

        page.update()

    input_name = ft.TextField(label='Имя')
    input_password = ft.TextField(label='Пароль')

    bs = ft.BottomSheet(
        ft.Container(
            ft.Column(
                [
                    input_name,
                    input_password,
                    ft.ElevatedButton("Отправить", on_click=close_bs),
                ],
                tight=True, alignment=ft.MainAxisAlignment.CENTER
            ),
            padding=50,
        ),
        open=False,
    )
    page.overlay.append(bs)

    row1 = ft.Row(
        controls=[
            ft.TextField(label='Текст', expand=True, width=300),
            ft.ElevatedButton(text='Создать', on_click=generate)
        ], alignment=ft.MainAxisAlignment.CENTER
    )

    row2 = ft.Row(
        controls=[
            ft.Dropdown(
                width=100,
                expand=True,
                label='Фон',
                options=[
                    ft.dropdown.Option("Red"),
                    ft.dropdown.Option("Green"),
                    ft.dropdown.Option("Blue"),
                    ft.dropdown.Option("Yellow"),
                    ft.dropdown.Option("Orange"),
                    ft.dropdown.Option("Purple"),
                    ft.dropdown.Option("Pink"),
                    ft.dropdown.Option("Black"),
                    ft.dropdown.Option("White"),
                    ft.dropdown.Option("Brown"),
                    ft.dropdown.Option("Gray"),
                ], alignment=ft.alignment.center
            ),
        ], alignment=ft.MainAxisAlignment.CENTER
    )

    row3 = ft.Row(
        controls=[
            ft.Dropdown(
                width=100,
                expand=True,
                label='Фигуры',
                options=[
                    ft.dropdown.Option("Red"),
                    ft.dropdown.Option("Green"),
                    ft.dropdown.Option("Blue"),
                    ft.dropdown.Option("Yellow"),
                    ft.dropdown.Option("Orange"),
                    ft.dropdown.Option("Purple"),
                    ft.dropdown.Option("Pink"),
                    ft.dropdown.Option("Black"),
                    ft.dropdown.Option("White"),
                    ft.dropdown.Option("Brown"),
                    ft.dropdown.Option("Gray"),
                ],
                alignment=ft.alignment.center
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    qr_image = ft.Row(
        controls=
        [
            ft.Container(
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                width=350,
                height=350,
                image_src=f'',
                content=ft.Text('Ваше изображение будет здесь', color=ft.colors.BLUE_ACCENT_100)
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    btn_save = ft.ElevatedButton(text='Сохранить', on_click=save)

    page.add(row1, row2, row3, qr_image, btn_save)


if __name__ == "__main__":
    ft.app(target=main, view=None, port=PORT)
