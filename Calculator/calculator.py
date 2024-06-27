import flet as ft
from flet import theme

def main(page: ft.page):
    page.title = 'Calculator'
    page.theme = theme.Theme(color_scheme_seed="dark")
    page.window_width = 450
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    values = []
    list1 = []
    list2 = []
    list3 = []

    def add_value(e, btn_text):
        values.append(btn_text)
        text = ''
        for value in values:
            text += f'{value}'
        output.controls[0].content = ft.Text(text, selectable=True)
        page.update()

    def clear(e):
        del values[:]
        output.controls[0].content = ft.Text('')
        page.update()

    def submit(e):
        text = ''
        for value in values:
           text += f'{value}'
        output.controls[0].content = ft.Text(eval(text), selectable=True)
        page.update()

    for i in range(1,4):
        btn = ft.ElevatedButton(text=f'{i}', width=page.window_width / 5, height=page.window_height / 13,
                                on_click=lambda e, value=i: add_value(e, str(value)))
        list1.append(btn)
    list1.append(ft.ElevatedButton(text=f'+', width=page.window_width / 5, height=page.window_height / 13,
                            on_click=lambda e, value='+': add_value(e, str(value))))

    for i in range(4,7):
        btn = ft.ElevatedButton(text=f'{i}', width=page.window_width / 5, height=page.window_height / 13,
                                on_click=lambda e, value=i: add_value(e, str(value)))
        list2.append(btn)
    list2.append(ft.ElevatedButton(text=f'-', width=page.window_width / 5, height=page.window_height / 13,
                                   on_click=lambda e, value='-': add_value(e, str(value))))

    for i in range(7,10):
        btn = ft.ElevatedButton(text=f'{i}', width=page.window_width / 5, height=page.window_height / 13,
                                on_click=lambda e, value=i: add_value(e, str(value)))
        list3.append(btn)
    list3.append(ft.ElevatedButton(text=f'*', width=page.window_width / 5, height=page.window_height / 13,
                                   on_click=lambda e, value='*': add_value(e, str(value))))

    output = ft.Row(
        controls=[
            ft.Container(
                content=ft.Text(f'', selectable=True),
                width=page.window_width/1.2,
                height=page.window_height/10,
                bgcolor=ft.colors.GREY_800,
                border_radius=10,
                alignment=ft.alignment.center
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    row1 = ft.Row(
        controls=list1,
        alignment=ft.MainAxisAlignment.CENTER
    )

    row2 = ft.Row(
        controls=list2,
        alignment=ft.MainAxisAlignment.CENTER
    )

    row3 = ft.Row(
        controls=list3,
        alignment=ft.MainAxisAlignment.CENTER
    )

    other_btn1 = ft.Row(
        controls=[
            ft.ElevatedButton(text=f'{0}', width=page.window_width / 5, height=page.window_height / 13,
                              on_click=lambda e, value=0: add_value(e, str(value))),
            ft.ElevatedButton(text=f'(', width=page.window_width / 5, height=page.window_height / 13,
                              on_click=lambda e, value='(': add_value(e, str(value))),
            ft.ElevatedButton(text=f')', width=page.window_width / 5, height=page.window_height / 13,
                              on_click=lambda e, value=')': add_value(e, str(value))),
            ft.ElevatedButton(text=f'/', width=page.window_width / 5, height=page.window_height / 13,
                              on_click=lambda e, value='/': add_value(e, str(value))),
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    other_btn2 = ft.Row(
        controls=[
            ft.ElevatedButton(text='Ok', width=page.window_width / 3.5, height=page.window_height / 13,
                              on_click=submit),
            ft.ElevatedButton(text='C', width=page.window_width / 3.5, height=page.window_height / 13,
                              on_click=clear)
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    page.add(output, row1, row2, row3, other_btn1, other_btn2)

ft.app(target=main)
