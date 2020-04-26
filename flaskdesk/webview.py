from ctypes import *
import os
from sys import platform
from threading import Thread
import socket
extensions = {
    "linux": "so"
}
lib = cdll.LoadLibrary(os.path.abspath(
    f"libs/{platform}/libwebview.{extensions[platform]}"))


def open_webview(title, width, height, url):
    webv = lib.fd_create_webview(c_char_p(title.encode(
        'utf-8')), width, height, c_char_p(url.encode('utf-8')))


class FlaskDeskApp:
    def __init__(self, app, title="Flask Application", width=720, height=540):
        self.app = app
        self.title = title
        self.width = width
        self.height = height
        self.choose_port()

    def choose_port(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('localhost', 0))
        port = sock.getsockname()[1]
        sock.close()
        self.port = port
        self.url = f"http://127.0.0.1:{port}"

    def run_flask(self):
        self.app.run(port=self.port)

    def run_webview(self):
        open_webview(self.title, self.width, self.height, self.url)

    def run(self):
        flask_thread = Thread(target=self.run_flask)
        ui_thread = Thread(target=self.run_webview)
        flask_thread.setDaemon(True)
        flask_thread.start()

        ui_thread.start()
        ui_thread.join()
