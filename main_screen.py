from tkinter import ttk

from consts import HELPTEXT
from base_screen import BaseScreen


class MainScreen(BaseScreen):
    MENU_BUTTONS = {"anchor_": "center", "padx_": 10, "pady_": 30, "ipadx_": 50, "ipady_": 40}

    def __init__(self, win, cond, sim, sim_input):
        super().__init__(win)
        self.cond = cond
        self.sim = sim
        self.sim.main = self
        self.sim_input = sim_input
        self.init_main()

    def init_main(self):
        self.add_button("Условие", command_=lambda: [self.clear_screen(), self.cond.render_screen()])
        self.add_button("Мат. решение")
        self.add_button("Демонстрация", command_=lambda: [self.clear_screen(), self.sim.init_sim()])
        self.add_button("Краткое условие", command_=lambda: [self.clear_screen(), self.sim_input.init_sim()])
        self.add_button("Помощь", command_=lambda: [self.clear_screen(),
                                                    self.add_text(1000, "white", "black", "hlp", HELPTEXT),
                                                    self.render_text_by_name(10, 10, "hlp")])

    def render_buttons(self, padx_=10, pady_=30, ipadx_=50, ipady_=40, anchor_="center", buttons=None):
        buttons_to_render = buttons if buttons else self.buttons
        for btn in buttons_to_render:
            if anchor_:
                btn.pack(anchor=anchor_, padx=padx_, pady=pady_, ipadx=ipadx_, ipady=ipady_)
            else:
                btn.pack(padx=padx_, pady=pady_)
