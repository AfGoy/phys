import tkinter
from tkinter import ttk, Tk
from time import *
from PIL import ImageTk, Image

from consts import *


class Trg:
    def __init__(self, win, can):
        self.can = can
        self.win = win
        self.x_start = L
        self.y_start = SCR_HGHT - H
        self.trg = self.can.create_rectangle(self.x_start + 10, self.y_start + 10, self.x_start, self.y_start,
                                             fill="black")

    def trg_fly(self, t):
        delta_y = Vt * t
        self.trg = self.can.create_rectangle(self.x_start + 10, self.y_start + 10 + delta_y, self.x_start,
                                             self.y_start + delta_y,
                                             fill="black")
        self.can.update()
        return self.trg
