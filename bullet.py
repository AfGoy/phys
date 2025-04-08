import tkinter
from tkinter import ttk, Tk
from time import *
from PIL import ImageTk, Image

from consts import *

class Bullet:
    def __init__(self, win, can):
        self.win = win
        self.can = can

    def bullet_fly(self, t):
        # for t in range(0, 10000):
        #     tt = t / 10000
        x = (Vb + Vp) * t
        y = (1080 - h) + (g*t**2) * 0.5
        print(x, y)
        blt = self.can.create_oval(x + 5, y + 5, x - 5, y - 5)
        self.can.update()