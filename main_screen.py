import tkinter

from base_screen import BaseScreen
from consts import FONT_TITLE, MENU_TITLE
from funcs import *


class MainScreen(BaseScreen):
    MENU_BUTTONS = {"anchor_": "center", "padx_": 10, "pady_": 30, "ipadx_": 50, "ipady_": 40}

    def __init__(self, win, cond, math, sim, sim_input, help):
        super().__init__(win)
        self.cond = cond
        self.math = math
        self.sim = sim
        self.sim.main = self
        self.sim_input = sim_input
        self.help = help
        self.init_main()

    def init_main(self):
        self.add_button("Условие", command_=lambda: [self.clear_screen(), self.cond.render_screen(), write_name_screen("COND")])
        self.add_button("Мат. решение", command_=lambda: [self.clear_screen(), self.math.render_screen(), write_name_screen("MATH")])
        self.add_button("Демонстрация", command_=lambda: [self.clear_screen(), self.sim.init_sim(), write_name_screen("SIM")])
        self.add_button("Краткое условие", command_=lambda: [self.clear_screen(), self.sim_input.init_sim(), write_name_screen("SIM_INPUT")])
        self.add_button("Помощь", command_=lambda: [self.clear_screen(), self.help.render_screen(), write_name_screen("HLP")])
        self.add_text(title="title", w=200, font_=FONT_TITLE, bg_="white", fg_="black", text_=MENU_TITLE)


    def render_buttons(self, padx_=10, pady_=30, ipadx_=50, ipady_=40, anchor_="center", buttons=None):
        buttons_to_render = buttons if buttons else self.buttons
        for btn in buttons_to_render:
            if anchor_:
                btn.pack(anchor=anchor_, padx=padx_, pady=pady_, ipadx=ipadx_, ipady=ipady_)
            else:
                btn.pack(padx=padx_, pady=pady_)

    def render_texts(self):
        self.render_text_by_name(pady_=(15, 15), title="title")