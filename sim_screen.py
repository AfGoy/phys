from time import *
from tkinter import ttk, Tk, Canvas

from plane import Plane
from bullet import Bullet
from trg import Trg

from base_screen import BaseScreen
from main_screen import MainScreen
from consts import H


class SimScreen(BaseScreen):
    IS_SIM = False

    def __init__(self, win, can):
        super().__init__(win)
        self.can = can
        self.objs_del = []
        self.pln = Plane(self.win, self.can)
        self.blt = Bullet(self.win, self.can)
        self.trg = Trg(self.win, self.can, H)

    def init_sim(self):
        self.clear_objects(*self.objs_del)
        self.can.pack()
        for obj in [self.pln, self.pln, self.trg]:
            self.objs_del.append(obj.fly(0))

    def start_sim(self):
        self.can.delete("all")
        SimScreen.IS_SIM = True

        objs = [self.pln, self.blt, self.trg]
        for t in range(0, 10000):
            if not SimScreen.IS_SIM:
                break

            self.objs_del = []
            for obj in objs:
                self.objs_del.append(obj.fly(t / 1000))

            if self.blt.is_collide(self.trg):
                break

            self.clear_objects(*self.objs_del)

            sleep(0.01)

        self.win.mainloop()

    def clear_objects(self, *args):
        for obj_del in args:
            self.can.delete(obj_del)

