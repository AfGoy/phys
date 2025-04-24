import os
from tkinter import ttk, Tk, Canvas

from main_screen import MainScreen
from condition_screen import ConditionScreen
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
    elif name_screen == "SIM":
        write_name_screen("MENU")
        kwargs["SIM"].clear_screen()
        kwargs["MAIN"].clear_screen()
        kwargs["SIM"].can.destroy()
        kwargs["MAIN"].init_main()
        # TODO:
        # Бой холсту!
        #
        # kwargs["SIM"].init_sim()
        kwargs["MAIN"].render_buttons(buttons=kwargs["MAIN"].buttons)


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

win.bind("<space>", lambda e: [start.destroy_start_screen(), write_name_screen("MENU")])
win.bind("<Escape>", lambda e: [escape_handler(MAIN=menu, COND=cond, SIM=sim)])

win.mainloop()

os.remove(FILENAME)
