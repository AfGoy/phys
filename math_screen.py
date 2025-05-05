from base_screen import BaseScreen


class MathScreen(BaseScreen):
    def __init__(self, win):
        super().__init__(win)
        self.math_init()

    def math_init(self):
        self.add_image("mth", "12.png")

    def render_screen(self):
        self.render_image_by_name("mth", 10, 10)

    def add_main_screen(self, main):
        self.main = main