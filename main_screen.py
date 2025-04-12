import tkinter
from tkinter import ttk, Tk, PhotoImage
from PIL import Image, ImageTk

from consts import TEXT1, HELPTEXT
from base_screen import BaseScreen
from condition_screen import ConditionScreen
from sim_screen import SimScreen


class MainScreen(BaseScreen):
    MENU_BUTTONS = {"anchor_": "center", "padx_": 10, "pady_": 30, "ipadx_": 50, "ipady_":40}

    def __init__(self, win, cond, sim):
        super().__init__(win)
        self.cond = cond
        self.sim = sim
        self.init_main()
        # self.render_buttons(**MainScreen.MENU_BUTTONS)

    def init_main(self):
        self.add_button("Условие", command_=lambda: [self.clear_screen(), self.cond.render_screen()])
        self.add_button("Мат. решение")
        self.add_button("Демонстрация", command_=lambda: [self.clear_screen(), self.sim.init_sim()])
        self.add_button("Краткое условие")
        self.add_button("Помощь", command_=lambda: [self.clear_screen(),
                                                    self.add_text(1000, "white", "black", "hlp", HELPTEXT),
                                                    self.render_text_by_name(10, 10, "hlp")])

    def render_buttons(self, padx_, pady_, ipadx_, ipady_, anchor_=None):
        for btn in self.buttons:
            if anchor_:
                btn.pack(anchor=anchor_, padx=padx_, pady=pady_, ipadx=ipadx_, ipady=ipady_)
            else:
                btn.pack(padx=padx_, pady=pady_)

    def esc_btn(self):
        self.esc = ttk.Button(self.win, text="Выход", command=lambda:
        [self.clear_screen(), self.render_buttons(**MainScreen.MENU_BUTTONS)])
        self.esc.pack(padx=1, pady=1)
