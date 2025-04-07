import tkinter
from tkinter import ttk, Tk
from time import *
from PIL import ImageTk, Image

from main_screen import MainScreen
from condition_screen import ConditionScreen
from start_screen import StartScreen
from base_screen import BaseScreen

win = Tk()
win.geometry("1920x1080")

base = BaseScreen(win)
cond = ConditionScreen(win)
menu = MainScreen(win, cond)
start = StartScreen(win, menu)

def escape_handler(e):
    base.clear_screen()
    menu.render_buttons(padx_=10, pady_=30, ipadx_=50, ipady_=40, anchor_="center")


win.bind("<space>", start.destroy_start_screen)
win.bind("<Escape>", escape_handler)

win.mainloop()
