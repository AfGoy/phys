from tkinter import ttk, Tk, Canvas

from main_screen import MainScreen
from condition_screen import ConditionScreen
from start_screen import StartScreen
from base_screen import BaseScreen
from sim_screen import SimScreen

win = Tk()
win.geometry("1920x1080")
can = Canvas(width=1920, height=1080)

base = BaseScreen(win)
cond = ConditionScreen(win)
sim = SimScreen(win, can)
menu = MainScreen(win, cond, sim)
start = StartScreen(win, menu)


win.bind("<space>", start.destroy_start_screen)

# win.bind("<Escape>", escape_handler)

win.mainloop()
