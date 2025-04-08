import tkinter
from tkinter import ttk, Tk
from time import *
from PIL import ImageTk, Image

from consts import *

class Trg:
    def __init__(self, win, can):
        self.can = can
        self.win = win

    def trg_fly(self, t):
        # for t in range(0, 10000):
        #     tt = t / 10000
        x = L
        y = (1080 - H) + Vt
        trg = self.can.create_rectangle(x + 20, y + 20, x - 20, y - 20)
        self.can.update()