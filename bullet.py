import tkinter
from tkinter import ttk, Tk
from time import *
from PIL import ImageTk, Image

from consts import *


class Bullet:
    def __init__(self, win, can):
        self.win = win
        self.can = can
        self.x_start = 60
        self.y_start = SCR_HGHT - h
        self.blt = self.can.create_oval(self.x_start + 5, self.y_start + 5, self.x_start, self.y_start, fill="black")

    def bullet_fly(self, t):
        delta_x = (Vb + Vp) * t
        delta_y = (g * t ** 2) * 0.5

        self.blt = self.can.create_oval(self.x_start + delta_x + 5, self.y_start + delta_y, self.x_start + delta_x,
                                        self.y_start + delta_y+5, fill="black")

        self.can.update()
        return self.blt

