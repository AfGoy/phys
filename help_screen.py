from base_screen import BaseScreen
from consts import *


class HelpScreen(BaseScreen):
    def __init__(self, win):
        super().__init__(win)
        self.help_init()

    def help_init(self):
        self.add_text(1000, "white", "black", "hlp", HELPTEXT)
        self.add_text(title="title", w=200, font_=FONT_TITLE, bg_="white", fg_="black", text_=HLP_TITLE)

    def render_screen(self):
        self.render_text_by_name(pady_=(15, 15), title="title")
        self.render_text_by_name(10, 10, "hlp")

    def add_main_screen(self, main):
        self.main = main
