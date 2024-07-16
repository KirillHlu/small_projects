import socket
import threading
import flet as ft
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('IP', 159))

log_file = "chat_log.txt"

def main(page: ft.Page):
    def receive_messages(sock, message_list):
        while True:
            try:
                message = sock.recv(1024).decode('utf-8')
                if not message:
                    break
                message_list.controls.append(ft.Text(message))
                page.update()
            except:
                sock.close()
                break

    def send_message(e):
        message = message_input.value
        message_input.value = ""
        sock.send(message.encode('utf-8'))
        message_list.controls.append(ft.Text(f"You: {message}"))
        page.update()

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

    threading.Thread(target=receive_messages, args=(sock, message_list)).start()
    threading.Thread(target=periodic_load).start()

ft.app(target=main, port=159, view=None)
