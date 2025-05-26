from base_screen import BaseScreen
from consts import *


class MathScreen(BaseScreen):
    def __init__(self, win):
        super().__init__(win)
        self.math_init()

    def math_init(self):
        self.add_image("mth", "12.png")
        self.add_text(title="title", w=400, font_=FONT_TITLE, bg_="white", fg_="black", text_=MATH_TITLE)

    def render_screen(self):
        self.render_text_by_name(pady_=(15, 15), title="title")
        self.render_image_by_name("mth", 10, 10)

    def add_main_screen(self, main):
        self.main = main