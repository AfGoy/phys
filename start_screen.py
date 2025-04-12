import tkinter
from tkinter import ttk, Tk
from time import *
from PIL import ImageTk, Image

from base_screen import BaseScreen


class StartScreen(BaseScreen):
    MENU_BUTTONS = {"anchor_": "center", "padx_": 10, "pady_": 30, "ipadx_": 50, "ipady_": 40}

    def __init__(self, win, main):
        super().__init__(win)
        self.main = main
        self.add_image("startscr", "startscr.png")
        self.render_image_by_name("startscr", 0, 0)

    def destroy_start_screen(self, e):
        self.clear_screen()
        self.main.render_buttons(**StartScreen.MENU_BUTTONS)
