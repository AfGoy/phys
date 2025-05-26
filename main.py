import os
from tkinter import ttk, Tk, Canvas

from main_screen import MainScreen
from condition_screen import ConditionScreen
from math_screen import MathScreen
from start_screen import StartScreen
from base_screen import BaseScreen
from sim_screen import SimScreen
from sim_input_screen import SimInputScreen
from help_screen import HelpScreen
from funcs import *


def escape_handler(**kwargs):
    name_screen = read_name_screen()
    if name_screen == "COND":
        write_name_screen("MENU")
        kwargs["COND"].clear_screen()
        kwargs["MAIN"].clear_screen()
        kwargs["MAIN"].init_main()
        kwargs["COND"].cond_init()
        kwargs["MAIN"].render_texts()
        kwargs["MAIN"].render_buttons(buttons=kwargs["MAIN"].buttons)
    elif name_screen == "MATH":
        write_name_screen("MENU")
        kwargs["MATH"].clear_screen()
        kwargs["MAIN"].clear_screen()
        kwargs["MAIN"].init_main()
        kwargs["MATH"].math_init()
        kwargs["MAIN"].render_texts()
        kwargs["MAIN"].render_buttons(buttons=kwargs["MAIN"].buttons)
    elif name_screen == "SIM":
        write_name_screen("MENU")
        kwargs["SIM"].clear_screen()
        SimScreen.IS_SIM = False
        kwargs["SIM"].clear_objects(*kwargs["SIM"].objs_del)
        kwargs["SIM"].can.pack_forget()
        del kwargs["SIM"].pln
        del kwargs["SIM"].blt
        del kwargs["SIM"].trg
        can.itemconfig(kwargs["SIM"].result_text_id, state='hidden')
        del kwargs["SIM"].result_text_id
        kwargs["MAIN"].init_main()
        kwargs["MAIN"].render_texts()
        kwargs["MAIN"].render_buttons(buttons=kwargs["MAIN"].buttons)
    elif name_screen == "SIM_INPUT":
        write_name_screen("MENU")
        kwargs["SIM_INPUT"].clear_screen()
        SimInputScreen.IS_SIM = False
        kwargs["SIM_INPUT"].clear_objects(*kwargs["SIM_INPUT"].objs_del)
        kwargs["SIM_INPUT"].can.pack_forget()
        kwargs["SIM_INPUT"].entry_.destroy()
        kwargs["SIM_INPUT"].can.delete(kwargs["SIM_INPUT"].line)
        del kwargs["SIM_INPUT"].pln
        del kwargs["SIM_INPUT"].blt
        del kwargs["SIM_INPUT"].trg
        can.itemconfig(kwargs["SIM_INPUT"].result_text_id, state='hidden')
        del kwargs["SIM_INPUT"].result_text_id
        kwargs["MAIN"].init_main()
        kwargs["MAIN"].render_texts()
        kwargs["MAIN"].render_buttons(buttons=kwargs["MAIN"].buttons)
    elif name_screen == "HLP":
        write_name_screen("MENU")
        kwargs["HELP"].clear_screen()
        kwargs["MAIN"].clear_screen()
        kwargs["MAIN"].init_main()
        kwargs["HELP"].help_init()
        kwargs["MAIN"].render_texts()
        kwargs["MAIN"].render_buttons(buttons=kwargs["MAIN"].buttons)


def enter_handler(**kwargs):
    name_screen = read_name_screen()
    if name_screen == "SIM":
        kwargs["SIM"].start_sim()
    elif name_screen == "SIM_INPUT" and kwargs["SIM_INPUT"].entry_.get() != "":
        kwargs["SIM_INPUT"].start_sim()


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
win.bind("<Escape>", lambda e: [escape_handler(MAIN=menu, COND=cond, SIM=sim, SIM_INPUT=sim_inp, MATH=math, HELP=help)])
win.bind("<Return>", lambda e: [enter_handler(SIM=sim, SIM_INPUT=sim_inp)])

win.mainloop()

os.remove(FILENAME)
