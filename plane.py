import tkinter
from tkinter import ttk, Tk
from time import *
from PIL import ImageTk, Image

from consts import *


class Plane:

    def __init__(self, win, can):
        self.win = win
        self.can = can
        self.x_start = 60 + x0
        self.y_start = SCR_HGHT - 30 - h
        self.pln = self.can.create_rectangle(self.x_start + 60, self.y_start + 40, self.x_start, self.y_start,
                                             fill="black")

    def fly(self, t):
        delta_x = Vp * t
        self.pln = self.can.create_rectangle(self.x_start + delta_x + 60, self.y_start + 40, self.x_start + delta_x,
                                             self.y_start,
                                             fill="black")
        self.can.update()
        return self.pln
