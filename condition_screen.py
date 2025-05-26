from base_screen import BaseScreen
from consts import *


class ConditionScreen(BaseScreen):
    def __init__(self, win):
        super().__init__(win)
        self.cond_init()

    def cond_init(self):
        self.add_text(1000, "white", "black", "cond", TEXT1)
        self.add_text(1000, "white", "black", "cond", TEXT1)
        self.add_text(title="title", w=200, font_=FONT_TITLE, bg_="white", fg_="black", text_=COND_TITLE)
        self.add_image("ill", "44i.png")

    def render_screen(self):
        self.render_text_by_name(pady_=(15, 15), title="title")
        self.render_text_by_name(10, 10, "cond")
        self.render_text_by_name(pady_=(15, 15), title="title")
        self.render_image_by_name("ill", 10, 10)

    def add_main_screen(self, main):
        self.main = main