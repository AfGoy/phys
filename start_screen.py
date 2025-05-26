from base_screen import BaseScreen
from main_screen import MainScreen

from consts import MENU_TITLE


class StartScreen(BaseScreen):

    def __init__(self, win, main):
        super().__init__(win)
        self.main = main
        self.add_image("startscr", "startscr.png")
        self.render_image_by_name("startscr", 0, 0)

    def destroy_start_screen(self):
        self.clear_screen()
        self.main.render_text_by_name(pady_=(15, 15), title="title")
        self.main.render_buttons(**MainScreen.MENU_BUTTONS)
