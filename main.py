from tkinter import ttk, Tk, Canvas

from main_screen import MainScreen
from condition_screen import ConditionScreen
from start_screen import StartScreen
from base_screen import BaseScreen
from sim_screen import SimScreen
from sim_input_screen import SimInputScreen

win = Tk()
win.geometry("1920x1080")
can = Canvas(width=1920, height=1080)

base = BaseScreen(win)
cond = ConditionScreen(win)
sim = SimScreen(win, can)
sim_inp = SimInputScreen(win, can)
menu = MainScreen(win, cond, sim, sim_inp)
start = StartScreen(win, menu)

cond.add_main_screen(menu)
sim_inp.add_main_to_sim_screen(menu)

win.bind("<space>", start.destroy_start_screen)

win.mainloop()
