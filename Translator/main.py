import flet as ft
from deep_translator import GoogleTranslator

def main(page: ft.Page):
    page.title = 'Translator'
    page.scroll = True
    page.window_width = 350

    def translate_from(e):
        translated_text = GoogleTranslator(source='auto', target=row1.controls[0].content.value).translate(row_for_translate.controls[0].value)
        row_for_translate.controls[2].content = ft.Text(str(translated_text), selectable=True)
        page.update(row_for_translate)

    def translate_to(e):
        translated_text = GoogleTranslator(source=row1.controls[0].content.value, target=row1.controls[2].content.value).translate(row_for_translate.controls[0].value)
        row_for_translate.controls[2].content = ft.Text(str(translated_text), selectable=True, text_align=ft.alignment.center)
        page.update(row_for_translate)

    row1 = ft.Row(
        controls=[
            ft.Container(
                content=ft.TextField(width=page.window_width/7, height=page.window_height/8/1.5),
                alignment=ft.alignment.center,
                width=page.window_width/5,
                height=page.window_height/8,
                border_radius=10,
                bgcolor=ft.colors.GREY_800,
            ),
            ft.Container(
                content=ft.Text(' To ', size=page.window_width/15)
            ),
            ft.Container(
                content=ft.TextField(width=page.window_width / 7, height=page.window_height / 8 / 1.5),
                alignment=ft.alignment.center,
                width=page.window_width / 5,
                height=page.window_height / 8,
                border_radius=10,
                bgcolor=ft.colors.GREY_800,
            ),
        ], alignment=ft.MainAxisAlignment.CENTER
    )

    interval = ft.Text(' ', size=page.window_height/40)

    row_for_translate = ft.Row(
        controls=[
            ft.TextField(
                label='Text',
                width=page.window_width/3,
                min_lines=5,
                multiline=True,
                border_radius=10
            ),
            ft.Text('    ', size=page.window_width/40),
            ft.Container(
                content=ft.Text(''),
                width=page.window_width/3,
                height=page.window_height/4.7,
                border_radius=10,
                bgcolor=ft.colors.GREY_800,
                alignment=ft.alignment.center,
            )
        ], alignment=ft.MainAxisAlignment.CENTER
    )

    interval2 = ft.Text(' ', size=page.window_height/35)

    btn = ft.Row(
        controls=[
            ft.Container(
                content=ft.ElevatedButton(text='Translate from', width=page.window_width / 2.5, height=page.window_height / 8, on_click=translate_from),
            ),
            ft.Container(
                content=ft.ElevatedButton(text='Translate to', width=page.window_width / 2.5, height=page.window_height / 8, on_click=translate_to),
            ),
        ], alignment=ft.MainAxisAlignment.CENTER
    )

    page.add(row1, interval, row_for_translate, interval2, btn)



ft.app(target=main)
