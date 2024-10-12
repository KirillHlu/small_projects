from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


class MoonBrowser:

    def __init__(self):
        self.window = QWidget()

        self.window.setWindowFlags(Qt.FramelessWindowHint)


        # Установка заголовка окна
        self.window.setWindowTitle("IWDI Browser")

        # Установка стилей
        self.window.setStyleSheet("""
            border-radius: 15px;
            background-color: #000000;  
            border: 2px solid #444444;  
            width: 400px;
            height: 350px; /* Цвет рамки */
        """)

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        # Поле ввода URL
        self.input_url = QTextEdit()
        self.input_url.setMaximumHeight(30)
        self.input_url.setStyleSheet(
            "background-color: #373737; color: #fff; font-weight: 900; border: 2px solid #373737;")

        # Кнопка поиска
        self.search_btn = QPushButton("Search")
        self.search_btn.setMaximumHeight(30)
        self.search_btn.setStyleSheet(
            "background-color: #141414; color: #fff; font-weight: 900; width: 70px; border: 2px solid #000;")

        # Кнопка "Назад"
        self.back_btn = QPushButton("<")
        self.back_btn.setMaximumHeight(30)
        self.back_btn.setStyleSheet(
            "background-color: #212121; color: #fff; font-weight: 900; width: 30px; border: 2px solid #212121;")

        # Кнопка "Вперед"
        self.forward_btn = QPushButton(">")
        self.forward_btn.setMaximumHeight(30)
        self.forward_btn.setStyleSheet(
            "background-color: #212121; color: #fff; font-weight: 900; width: 30px; border: 2px solid #212121;")

        # Кнопка "Обновить"
        self.reload_btn = QPushButton("@")
        self.reload_btn.setMaximumHeight(30)
        self.reload_btn.setStyleSheet(
            "background-color: #212121; color: #fff; font-weight: 900; width: 30px; border: 2px solid #212121;")

        # Кнопка меню
        self.menu = QPushButton("≡")
        self.menu.setMaximumHeight(30)
        self.menu.setStyleSheet(
            "background-color: #212121; color: #fff; font-weight: 900; width: 30px; border: 2px solid #212121;")

        # Кнопка "Закрыть"
        self.close_btn = QPushButton("X")
        self.close_btn.setMaximumHeight(30)
        self.close_btn.setStyleSheet(
            "background-color: #000000; color: #fff; font-weight: 900; width: 30px; border: 2px solid #000000;")
        self.close_btn.clicked.connect(self.close_application)

        # Кнопка "Свернуть"
        self.minimize_btn = QPushButton("_")
        self.minimize_btn.setMaximumHeight(30)
        self.minimize_btn.setStyleSheet(
            "background-color: #000000; color: #fff; font-weight: 900; width: 30px; border: 2px solid #000000;")
        self.minimize_btn.clicked.connect(self.window.showMinimized)

        # Кнопка "Развернуть на весь экран"
        self.maximize_btn = QPushButton("⬜")
        self.maximize_btn.setMaximumHeight(30)
        self.maximize_btn.setStyleSheet(
            "background-color: #000000; color: #fff; font-weight: 900; width: 30px; border: 2px solid #000000;")
        self.maximize_btn.clicked.connect(self.toggle_fullscreen)

        # Добавление кнопок в горизонтальный layout
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)
        self.horizontal.addWidget(self.reload_btn)
        self.horizontal.addWidget(self.input_url)
        self.horizontal.addWidget(self.search_btn)
        self.horizontal.addWidget(self.menu)
        self.horizontal.addWidget(self.minimize_btn)  # Кнопка "Свернуть"
        self.horizontal.addWidget(self.maximize_btn)  # Кнопка "Развернуть на весь экран"

        self.horizontal.addWidget(self.close_btn)  # Кнопка "Закрыть"

        # Объявляем браузер
        self.browser = QWebEngineView()

        # Подключаем кнопки
        self.search_btn.clicked.connect(lambda: self.navigate(self.input_url.toPlainText()))
        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)
        self.reload_btn.clicked.connect(self.browser.reload)

        # Добавление горизонтального layout и браузера в основной layout
        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        # Открываем начальную страницу
        self.browser.setUrl(QUrl("http://google.com"))

        # Устанавливаем основной layout
        self.window.setLayout(self.layout)

        # Параметры для управления движением мыши
        self.mouse_press = False
        self.old_pos = None
        self.window.mousePressEvent = self.mousePressEvent
        self.window.mouseMoveEvent = self.mouseMoveEvent
        self.window.mouseReleaseEvent = self.mouseReleaseEvent

        self.window.show()

    def close_application(self):
        self.window.close()

    def navigate(self, url):
        if not url.startswith("http"):
            url = "http://" + url
            self.input_url.setText(url)
        self.browser.setUrl(QUrl(url))

    def toggle_fullscreen(self):
        if self.window.isFullScreen():
            self.window.setWindowState(
                self.window.windowState() & ~Qt.WindowFullScreen)  # Выход из полноэкранного режима
        else:
            self.window.setWindowState(self.window.windowState() | Qt.WindowFullScreen)  # Вход в полноэкранный режим

    def mousePressEvent(self, event):
        self.mouse_press = True
        self.old_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        if self.mouse_press:
            delta = event.globalPos() - self.old_pos
            self.window.move(self.window.x() + delta.x(), self.window.y() + delta.y())
            self.old_pos = event.globalPos()

    def mouseReleaseEvent(self, event):
        self.mouse_press = False

app = QApplication([])
window = MoonBrowser()
app.exec_()
