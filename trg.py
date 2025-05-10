import tkinter
from tkinter import ttk, Tk
from time import *
from PIL import ImageTk, Image

from consts import *


class Trg:
    def __init__(self, win, can, H_):
        self.H = H
        self.can = can
        self.win = win
        self.y_start = (SCR_HGHT - self.H) * KY
        self.x = L + x0
        self.y = self.y_start
        self.trg = self.can.create_rectangle(self.x + 10, self.y_start + 10, self.x, self.y_start,
                                             fill="black")

    def fly(self, t):
        delta_y = Vt * t * KY
        self.y = self.y_start + delta_y
        self.trg = self.can.create_rectangle(self.x + 10, self.y + 10, self.x,
                                             self.y,
                                             fill="black")
        self.can.update()
        return self.trg

    def init_cords(self):
        self.y_start = (SCR_HGHT - self.H) * KY
        self.x = L + x0
