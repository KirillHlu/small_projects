import flet as ft
import json
import time

with open('train.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Check the loaded data
print(data)

count = len(data) // 2


def main(page: ft.Page):
    page.scroll = True
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 600
    page.window_height = 500

    for i in range(count):
        page.clean()
        question = data.get(f'question{i}', 'Question not found')
        page.add(ft.Text(question))  # Make sure the question contains Russian characters
        answer_from_user = ft.TextField(width=500, label='Answer')
        page.add(answer_from_user)

        while answer_from_user.value.lower() != f"{data.get(f'answer{i}', '').lower()}":
            pass

        right = ft.Row(
            controls=[
                ft.Container(
                    content=ft.Text('Correct!!!', size=50),
                    bgcolor='#4CCD77',
                    border_radius=20,
                    width=500,
                    height=300,
                    alignment=ft.alignment.center
                )
            ], alignment=ft.MainAxisAlignment.CENTER
        )

        end = ft.Row(
            controls=[
                ft.Container(
                    content=ft.Text('This is the end of the test, you did great!', size=50),
                    bgcolor='#4CCD77',
                    border_radius=20,
                    width=500,
                    height=300,
                    alignment=ft.alignment.center
                )
            ], alignment=ft.MainAxisAlignment.CENTER
        )

        if i + 1 != count:
            page.add(right)
            time.sleep(1)

        else:
            page.add(end)


ft.app(main)
