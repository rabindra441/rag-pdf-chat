#
import flet as ft
import time
import threading
import datetime

def main(page: ft.Page):
    page.title = "Digital Clock"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    clock_text = ft.Text(
        value="00:00:00",
        size=64,
        weight=ft.FontWeight.BOLD,
    )
    page.add(clock_text)

    def update_clock():
        while True:
            now = time.time()                     # 1. syscall -> float
            formatted = datetime.datetime.fromtimestamp(now).strftime("%H:%M:%S")
            clock_text.value = formatted           # 2. mutate Python object (just a string in memory)
            page.update()                          # 3. send a diff to the Flutter engine
            time.sleep(1)

    threading.Thread(target=update_clock, daemon=True).start()

ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8550, host="0.0.0.0")