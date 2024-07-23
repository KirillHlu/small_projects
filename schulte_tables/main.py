import flet as ft
import random

def main(page: ft.Page):
    page.scroll = True
    page.add(ft.Text(" ", size=100))

    for i in range(10):
        numbers = []
        for j in range(5):
            row = ft.Row(controls=[], alignment=ft.MainAxisAlignment.CENTER)
            for h in range(5):
                cnt = 0
                while cnt == 0:
                    num = random.randint(1,25)
                    if num in numbers:
                        pass
                    else:
                        numbers.append(num)
                        cnt = 1
                        row.controls.append(
                            ft.Container(
                                content=ft.Text(f"{num}", color=ft.colors.BLACK, weight=ft.FontWeight.W_900, theme_style=ft.TextThemeStyle.TITLE_MEDIUM, size=21),
                                bgcolor=ft.colors.WHITE,
                                border_radius=0.1,
                                width=50,
                                height=50,
                                alignment=ft.alignment.center
                            )
                        )
            page.add(row)
        page.add(ft.Text(" ", size=100))

        print(numbers)



ft.app(target=main)
