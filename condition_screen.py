from tkinter import ttk, Tk

from base_screen import BaseScreen
from consts import TEXT1


class ConditionScreen(BaseScreen):
    def __init__(self, win):
        super().__init__(win)
        self.cond_init()

    def cond_init(self):
        self.add_text(1000, "white", "black", "cond", TEXT1)
        self.add_image("ill", "44i.png")

    def render_screen(self):
        self.render_text_by_name(10, 10, "cond")
        self.render_image_by_name("ill", 10, 10)

    def add_main_screen(self, main):
        self.main = main
        self.win.bind("<Escape>", self.escape_handler)

    def escape_handler(self, e):
        self.clear_screen()  # Очищаем экран
        self.main.clear_screen()
        self.main.init_main()
        self.cond_init()
        self.main.render_buttons(buttons=self.main.buttons)  # Упаковываем
