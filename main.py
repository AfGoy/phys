import os
from tkinter import ttk, Tk, Canvas

from main_screen import MainScreen
from condition_screen import ConditionScreen
from math_screen import MathScreen
from start_screen import StartScreen
from base_screen import BaseScreen
from sim_screen import SimScreen
from sim_input_screen import SimInputScreen
from funcs import *


def escape_handler(**kwargs):
    name_screen = read_name_screen()
    if name_screen == "COND":
        write_name_screen("MENU")
        kwargs["COND"].clear_screen()
        kwargs["MAIN"].clear_screen()
        kwargs["MAIN"].init_main()
        kwargs["COND"].cond_init()
        kwargs["MAIN"].render_buttons(buttons=kwargs["MAIN"].buttons)
    elif name_screen == "MATH":
        write_name_screen("MENU")
        kwargs["MATH"].clear_screen()
        kwargs["MAIN"].clear_screen()
        kwargs["MAIN"].init_main()
        kwargs["MATH"].math_init()
        kwargs["MAIN"].render_buttons(buttons=kwargs["MAIN"].buttons)
    elif name_screen == "SIM":
        write_name_screen("MENU")
        kwargs["SIM"].clear_screen()
        kwargs["MAIN"].clear_screen()
        SimScreen.IS_SIM = False
        kwargs["SIM"].can.pack_forget()
        kwargs["SIM"].pln.init_cords()
        kwargs["SIM"].blt.init_cords()
        kwargs["SIM"].trg.init_cords()
        kwargs["MAIN"].init_main()
        kwargs["MAIN"].render_buttons(buttons=kwargs["MAIN"].buttons)
    elif name_screen == "SIM_INPUT":
        write_name_screen("MENU")
        kwargs["SIM_INPUT"].clear_screen()
        kwargs["MAIN"].clear_screen()
        SimInputScreen.IS_SIM = False
        kwargs["SIM_INPUT"].can.pack_forget()
        kwargs["SIM_INPUT"].pln.init_cords()
        kwargs["SIM_INPUT"].blt.init_cords()
        kwargs["SIM_INPUT"].entry_.destroy()
        del kwargs["SIM_INPUT"].trg
        kwargs["MAIN"].init_main()
        kwargs["MAIN"].render_buttons(buttons=kwargs["MAIN"].buttons)



win = Tk()
win.geometry("1920x1080")
can = Canvas(width=1920, height=1080)

base = BaseScreen(win)
cond = ConditionScreen(win)
math = MathScreen(win)
sim = SimScreen(win, can)
sim_inp = SimInputScreen(win, can)
menu = MainScreen(win, cond, math, sim, sim_inp)
start = StartScreen(win, menu)
cond.add_main_screen(menu)
sim_inp.add_main_to_sim_screen(menu)

win.bind("<space>", lambda e: [start.destroy_start_screen(), write_name_screen("MENU")])
win.bind("<Escape>", lambda e: [escape_handler(MAIN=menu, COND=cond, SIM=sim, SIM_INPUT=sim_inp, MATH=math)])

win.mainloop()

os.remove(FILENAME)
