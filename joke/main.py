import flet as ft
from flet_core import theme
import webbrowser
from tkinter import messagebox
import cv2

def main(page: ft.Page):
    page.title = "Хомячок"
    page.theme = theme.Theme(color_scheme_seed="dark")
    page.window_width = 500

    cnt = 0

    def show_webcam(mirror=False):
        cam = cv2.VideoCapture(0)
        while True:
            ret_val, img = cam.read()
            if mirror:
                img = cv2.flip(img, 1)
            cv2.imshow('SHAVEL SILA PERSIK MAGILA', img)
            if cv2.waitKey(1) == 27:
                break  # esc to quit
        cv2.destroyAllWindows()

    def counter(e):
        page.clean()

        nonlocal cnt
        cnt += 1

        score = ft.Row(
            [
                ft.Container(
                    content=ft.Text(f"MLSTR COINS: {cnt}", color='black', size=20),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.YELLOW_800,
                    width=280,
                    height=150,
                    border_radius=10,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

        page.add(MLSTR, score)

    def open(e):
        messagebox.showwarning('Urgent notification!',
                               'Ваша система находится под угрозой! \nError: Замечена натовская программа от Меллстроя!')
        for i in range(1):
            webbrowser.open('https://www.youtube.com/watch?v=jev32jC59ck')
            webbrowser.open('https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Favatars.mds.yandex.net%2Fget-mpic%2F5268049%2Fimg_id1813142962720858471.jpeg%2Forig&lr=64&pos=0&rpt=simage&text=%D1%89%D0%B5%D0%B0%D0%B2%D0%B5%D0%BB%D1%8C')
            webbrowser.open('https://images.app.goo.gl/L8idRCm43XsHcUL2A')
            webbrowser.open('https://images.app.goo.gl/MoadHUXEZhWxDUhWA')
            webbrowser.open('https://images.app.goo.gl/EW5Mw4HpPadJ1Ydb9')
            webbrowser.open('https://images.app.goo.gl/xLoJfdU6W3KgGc4y5')
            webbrowser.open('https://images.app.goo.gl/A8bispmWmUY6nXGV8')
            webbrowser.open('https://youtu.be/FKDRkPDIe_o?si=oKc3ZHb9wNBb9IAa')
            webbrowser.open('https://youtu.be/Wwn7LiKN-Nk?si=xGNIrqfL3zLeKR43')

        messagebox.showerror('Notification from Mellstroy', 'Жди докс, жди сват и спортиков')
        show_webcam(mirror=True)

    MLSTR = ft.Row(
        [
            ft.Container(
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                width=350,
                height=350,
                border_radius=50,
                image_src='https://i.postimg.cc/cJ4drdMn/msg1392167370-50829.jpg',
                on_click=counter,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    score = ft.Row(
        [
            ft.Container(
                content=ft.Text(f"MLSTR COINS: ?", color='black', size=20),
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.YELLOW_800,
                width=280,
                height=150,
                border_radius=10,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    row1 = ft.Row(
        [
            ft.Text(' ', size=100)
        ]
    )

    row2= ft.Row(
        [
            ft.ElevatedButton(text="ВЫВЕЗТИ МИЛИАРДЫ НЕ СКАМ !!!", width=300, height=200, on_click=open)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    def navigate(e):
        index = page.navigation_bar.selected_index
        page.clean()

        if index == 0:
            page.add(MLSTR, score)
            page.update()

        elif index == 1:
            page.add(row1, row2)

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(label='ТЫКАТЬ ХОМЯКА', icon=ft.icons.HOUSE),
            ft.NavigationDestination(label='ВЫВЕСТИ МИЛИАРДЫ', icon=ft.icons.MONEY_SHARP),
        ], on_change=navigate
    )

    page.add(MLSTR, score)

ft.app(main)
