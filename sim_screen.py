import tkinter
from tkinter import ttk, Tk, Canvas
from time import *
from PIL import ImageTk, Image

from plane import Plane
from bullet import Bullet
from trg import Trg

import tkinter
from tkinter import ttk, Tk, PhotoImage
from PIL import Image, ImageTk

from base_screen import BaseScreen


class SimScreen(BaseScreen):

    def __init__(self, win, can):
        super().__init__(win)
        self.can = can
        self.pln = Plane(win, can)
        self.blt = Bullet(win, can)
        self.trg = Trg(win, can)

        # self.add_image()

    def init_sim(self):
        # TODO:
        # Добавить изображение
        self.can.pack()
        self.can.delete(self.pln.pln)
        self.can.delete(self.blt.blt)
        self.can.delete(self.trg.trg)
        self.start_sim()

    def start_sim(self):
        objs = [self.pln, self.blt, self.trg]
        for t in range(0, 10000):

            objs_del = []
            for obj in objs:
                objs_del.append(obj.fly(t / 1000))

            if self.blt.is_collide(self.trg):
                break

            for obj_del in objs_del:
                self.can.delete(obj_del)

            sleep(0.01)

        self.win.mainloop()
