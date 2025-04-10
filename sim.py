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
can.delete(pln.pln)
blt = Bullet(win, can)
can.delete(blt.blt)
trg = Trg(win, can)
can.delete(trg.trg)

for t in range(0, 10000):
    tt = t / 1000
    pln_ = pln.fly(tt)
    blt_ = blt.bullet_fly(tt)
    trg_ = trg.trg_fly(tt)
    can.delete(pln_)
    can.delete(blt_)
    can.delete(trg_)
    sleep(0.01)

win.mainloop()
