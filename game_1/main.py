import flet as ft
import random
import time

def main(page: ft.Page):
    numbers2 = []
    wrongs = []
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    def check(e):
        if e.control.data in numbers:
            e.control.bgcolor=ft.colors.GREEN
            numbers2.append(e.control.data)
            page.update()
        else:
            e.control.bgcolor=ft.colors.RED
            numbers2.append(e.control.data)
            wrongs.append(e.control.data)
            page.update()

        if len(wrongs) == 3:
            wrongs.clear()
            page.clean()
            page.add(ft.Text('Game over'))
            time.sleep(3)
            page.clean()
            numbers2.clear()
            numbers.clear()
            for j in range(5):
                row = ft.Row(controls=[], alignment=ft.MainAxisAlignment.CENTER)
                for h in range(5):
                    cnt = 0
                    while cnt == 0:
                        num = random.randint(1, 25)
                        if num in numbers:
                            pass
                        else:
                            numbers.append(num)
                            cnt = 1
                            square = ft.Container(
                                data=num,
                                on_click=check,
                                bgcolor=ft.colors.WHITE,
                                border_radius=10,
                                width=100,
                                height=100
                            )

                            row.controls.append(square)

                page.add(row)

            print(numbers)

            while len(numbers) != 20:
                try:
                    num = random.randint(1, 25)
                    if num in numbers:
                        numbers.pop(num)
                except IndexError:
                    pass
            print(numbers)


        if len(numbers2) == 25:
            page.clean()
            numbers2.clear()
            numbers.clear()
            for j in range(5):
                row = ft.Row(controls=[], alignment=ft.MainAxisAlignment.CENTER)
                for h in range(5):
                    cnt = 0
                    while cnt == 0:
                        num = random.randint(1, 25)
                        if num in numbers:
                            pass
                        else:
                            numbers.append(num)
                            cnt = 1
                            square = ft.Container(
                                data=num,
                                on_click=check,
                                bgcolor=ft.colors.WHITE,
                                border_radius=10,
                                width=100,
                                height=100
                            )

                            row.controls.append(square)

                page.add(row)

            print(numbers)

            while len(numbers) != 22:
                try:
                    num = random.randint(1, 25)
                    if num in numbers:
                        numbers.pop(num)
                except IndexError:
                    pass
            print(numbers)


    numbers = []
    for j in range(5):
        row = ft.Row(controls=[], alignment=ft.MainAxisAlignment.CENTER)
        for h in range(5):
            cnt = 0
            while cnt == 0:
                num = random.randint(1, 25)
                if num in numbers:
                    pass
                else:
                    numbers.append(num)
                    cnt = 1
                    square = ft.Container(
                        data=num,
                        on_click=check,
                        bgcolor=ft.colors.WHITE,
                        border_radius=10,
                        width=100,
                        height=100
                    )

                    row.controls.append(square)

        page.add(row)

    print(numbers)

    while len(numbers) != 20:
        try:
            num = random.randint(1, 25)
            if num in numbers:
                numbers.pop(num)
        except IndexError:
            pass
    print(numbers)


ft.app(target=main)
