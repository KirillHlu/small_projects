import flet as ft
import time
import threading  

log_file = "chat_log.txt"

def main(page: ft.Page):
    page.scroll = True
    def send_message(e):
        message = message_input.value
        message_input.value = ""
        with open(log_file, "a") as f:
            f.write(f"{message}\n")
        load_messages()

    def load_messages():
        try:
            with open(log_file, "r") as f:
                messages = f.readlines()
                message_list.controls.clear()
                for message in messages:
                    message_list.controls.append(ft.Text(message.strip()))
                page.update()
        except FileNotFoundError:
            pass

    def periodic_load():
        while True:
            load_messages()
            time.sleep(1)

    message_list = ft.Column()
    message_input = ft.TextField(hint_text="Enter your message", on_submit=send_message)

    page.add(
        ft.Text("Chat Client", size=20),
        message_list,
        message_input,
        ft.ElevatedButton(text="Send", on_click=send_message)
    )

    threading.Thread(target=periodic_load).start()

ft.app(target=main, port=159, view=None)
