from tkinter import ttk, Tk

from base_screen import BaseScreen
# from main_screen import MainScreen
from consts import TEXT1


class ConditionScreen(BaseScreen):
    def __init__(self, win):
        super().__init__(win)
        self.add_text(1000, "white", "black", "cond", TEXT1)
        self.add_image("ill", "44i.png")

    def render_screen(self):
        # MainScreen.esc_btn()
        self.render_text_by_name(10, 10, "cond")
        self.render_image_by_name("ill", 10, 10)
