from time import *

from plane import Plane
from bullet import Bullet
from trg import Trg

from base_screen import BaseScreen
from main_screen import MainScreen
from consts import H


class SimScreen(BaseScreen):

    def __init__(self, win, can):
        super().__init__(win)
        self.can = can
        self.pln = Plane(win, can)
        self.blt = Bullet(win, can)
        self.trg = Trg(win, can, H)

    def init_sim(self):
        self.can.pack()
        self.win.bind("<Return>", self.start_sim)

    def start_sim(self, e):
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

    def clear_objects(self, *args):
        for obj_del in args:
            self.can.delete(obj_del)

