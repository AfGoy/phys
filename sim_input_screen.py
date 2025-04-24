import tkinter
from tkinter import ttk, Tk, Canvas, NW
from time import *
from PIL import ImageTk, Image

from main_screen import MainScreen
from plane import Plane
from bullet import Bullet
from trg import Trg

from base_screen import BaseScreen
from consts import FONT, HELPTEXT, KX, KY


class SimInputScreen(BaseScreen):
    MENU_BUTTONS = {"anchor_": "center", "padx_": 10, "pady_": 30, "ipadx_": 50, "ipady_": 40}

    def __init__(self, win, can):
        super().__init__(win)
        self.can = can
        self.win = win
        self.pln = Plane(win, can)
        self.blt = Bullet(win, can)
        self.trg = None
        self.entry_ = None

    def init_sim(self):
        self.can.place(x=150, y=0)
        self.entry_ = ttk.Entry()
        self.entry_.place(x=5, y=300, anchor=NW)
        self.win.bind("<Return>", self.start_sim)

    def start_sim(self):
        self.trg = Trg(self.win, self.can, int(self.entry_.get()))
        self.can.delete("all")

        objs = [self.pln, self.blt, self.trg]
        for t in range(0, 10000):

            objs_del = []
            for obj in objs:
                objs_del.append(obj.fly(t / 1000))

            if self.blt.is_collide(self.trg):
                break

            self.clear_objects(*objs_del)

            sleep(0.01)

        self.win.mainloop()

    def add_main_to_sim_screen(self, main):
        self.main = main

    def clear_objects(self, *args):
        for obj_del in args:
            self.can.delete(obj_del)
