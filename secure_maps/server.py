import threading
import time
import flet as ft
import flet.map as ft_map

def main(page: ft.Page):
    marker_layer_ref = ft.Ref[ft_map.MarkerLayer]()


    def update_map():
        coordinates = []
        with open('markers.txt', 'r') as file:
            for line in file:
                if line.strip():  # Проверка на пустую строку
                    try:
                        lat, lon, name = line.strip().split(',')
                        lat = float(lat)
                        lon = float(lon)
                        coordinates.append((lat, lon, name))
                    except ValueError:
                        print(f"Невозможно преобразовать строку в числа: {line.strip()}")

        marker_layer_ref.current.markers.clear()
        for lat, lon, name in coordinates:
            marker_layer_ref.current.markers.append(
                ft_map.Marker(
                    content=ft.Icon(
                        ft.icons.LOCATION_ON, color=ft.cupertino_colors.DESTRUCTIVE_RED, tooltip=name
                    ),
                    coordinates=ft_map.MapLatitudeLongitude(lat, lon)
                )
            )
        page.update()

    def show_messages():
        with open('messages.txt', 'r') as file:
            messages = file.readlines()

        for message in messages:
            if message.strip():
                text = ft.Container(
                    content=ft.Text(message.strip(), color=ft.colors.WHITE),
                    bgcolor=ft.colors.RED_600,
                    border_radius=10,
                    alignment=ft.alignment.center,
                    width=180,
                    height=80
                )
                page.overlay.append(
                    ft.Container(
                        content=text,
                        alignment=ft.alignment.center,
                        bottom=10,
                        left=0,
                        right=0,
                        padding=ft.padding.all(10),
                    )
                )
                page.update()  # Обновляем страницу безопасно
                time.sleep(5)
                page.overlay.clear()
                page.overlay.clear()
                page.update()  # Обновляем страницу для удаления сообщения

        with open('messages.txt', 'w') as file:
            file.write('')

    def periodic_load():
        while True:
            update_map()
            time.sleep(10)

    def load_messages_periodically():
        while True:
            show_messages()
            time.sleep(10)  # Задержка между загрузками сообщений

    page.add(
        ft_map.Map(
            expand=True,
            configuration=ft_map.MapConfiguration(
                initial_center=ft_map.MapLatitudeLongitude(15, 10),
                initial_zoom=4.2,
                min_zoom=2.0,
                interaction_configuration=ft_map.MapInteractionConfiguration(
                    flags=ft_map.MapInteractiveFlag.ALL
                ),
                on_init=lambda e: print(f"Initialized Map"),
            ),
            layers=[
                ft_map.TileLayer(
                    url_template="https://tile.openstreetmap.org/{z}/{x}/{y}.png",
                    on_image_error=lambda e: print("TileLayer Error"),
                ),
                ft_map.MarkerLayer(
                    ref=marker_layer_ref,
                    markers=[
                        ft_map.Marker(
                            content=ft.Icon(ft.icons.LOCATION_ON),
                            coordinates=ft_map.MapLatitudeLongitude(30, 15),
                        ),
                        ft_map.Marker(
                            content=ft.Icon(ft.icons.LOCATION_ON),
                            coordinates=ft_map.MapLatitudeLongitude(10, 10),
                        ),
                        ft_map.Marker(
                            content=ft.Icon(ft.icons.LOCATION_ON),
                            coordinates=ft_map.MapLatitudeLongitude(25, 45),
                        ),
                    ],
                ),
            ],
        ),
    )

    threading.Thread(target=periodic_load).start()
    threading.Thread(target=load_messages_periodically).start()

ft.app(target=main, port=159, view=None)
