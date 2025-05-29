from consts import FILENAME
from sim_screen import SimScreen
from sim_input_screen import SimInputScreen


def write_name_screen(name):
    with open(FILENAME, "w", encoding="utf-8") as f:
        f.write(name)


def read_name_screen():
    with open(FILENAME, "r", encoding="utf-8") as f:
        return f.read().strip()


#TODO:
# Сделать проверки через словарь
# {"COND": func_cond ...}
# image to path with dir

def escape_handler(can, **kwargs):
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