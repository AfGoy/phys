import tkinter
from tkinter import ttk, Tk, Canvas
from time import *
from PIL import ImageTk, Image

from plane import Plane
from bullet import Bullet
from trg import Trg

win = Tk()
win.geometry("1920x1080")
can = Canvas(width=1920, height=1080)
can.pack()

pln = Plane(win, can)
blt = Bullet(win, can)
trg = Trg(win, can)

for t in range(0, 10000):
    tt = t / 10000
    pln.fly(tt)
    blt.bullet_fly(tt)
    trg.trg_fly(tt)
    # can.delete("ALL")
    can.update()



win.mainloop()