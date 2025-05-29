import os
from tkinter import ttk, Tk, Canvas

from main_screen import MainScreen
from condition_screen import ConditionScreen
from math_screen import MathScreen
from start_screen import StartScreen
from base_screen import BaseScreen
from help_screen import HelpScreen
from funcs import *


win = Tk()
win.geometry("1920x1080")
can = Canvas(width=1920, height=1080)

base = BaseScreen(win)
cond = ConditionScreen(win)
math = MathScreen(win)
sim = SimScreen(win, can)
sim_inp = SimInputScreen(win, can)
help = HelpScreen(win)
menu = MainScreen(win, cond, math, sim, sim_inp, help)
start = StartScreen(win, menu)

cond.add_main_screen(menu)
sim_inp.add_main_to_sim_screen(menu)

win.bind("<space>", lambda e: [start.destroy_start_screen(), write_name_screen("MENU")])
win.bind("<Escape>", lambda e: [escape_handler(can=can, MAIN=menu, COND=cond, SIM=sim, SIM_INPUT=sim_inp, MATH=math, HELP=help)])
win.bind("<Return>", lambda e: [enter_handler(SIM=sim, SIM_INPUT=sim_inp)])

win.mainloop()

os.remove(FILENAME)
