from base_screen import BaseScreen
from main_screen import MainScreen


class StartScreen(BaseScreen):

    def __init__(self, win, main):
        super().__init__(win)
        self.main = main
        self.add_image("startscr", "startscr.png")
        self.render_image_by_name("startscr", 0, 0)

    def destroy_start_screen(self, e):
        print(1)
        self.clear_screen()
        self.main.render_buttons(**MainScreen.MENU_BUTTONS)
