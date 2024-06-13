import flet as ft
from pytube import YouTube
import os

def main(page = ft.Page):
    def download_video_from_youtube(e):
        try:
            url = str(enter.value)
            yt = YouTube(url)
            video = yt.streams.filter(progressive=True, file_extension='mp4').first()
            video.download()
            file_name = video.default_filename
            os.startfile(file_name)  # Для Windows
            # Для MacOS можно использовать subprocess.Popen(["open", file_name])
        except Exception as e:
            pass

    page.title = 'Downloader'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    enter = ft.TextField(
            width=500,
            height=100,
            label='Link'
    )

    btn = ft.ElevatedButton(
            text='Download',
            on_click=download_video_from_youtube,
            width=250,
            height=50,
        )


    page.add(enter,btn)

ft.app(target=main)
