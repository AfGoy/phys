from tkinter import ttk, NW
from time import *

from plane import Plane
from bullet import Bullet
from trg import Trg

from base_screen import BaseScreen
from consts import IS_COLLISION, IS_NOT_COLLISION, CONDITION, TIME_STEP


class SimInputScreen(BaseScreen):
    MENU_BUTTONS = {"anchor_": "center", "padx_": 10, "pady_": 30, "ipadx_": 50, "ipady_": 40}
    IS_SIM = False

    def __init__(self, win, can):
        super().__init__(win)
        self.can = can
        self.win = win
        self.objs_del = []
        self.pln = Plane(win, can)
        self.blt = Bullet(win, can)
        self.trg = None
        self.entry_ = None
        self.result_text_id = None
        self.can.create_rectangle(0, 500, 10000, 501, fill="black")

    @staticmethod
    def validate_number(input_):
        return input_.isdigit() or input_ == ""

    def init_sim(self):
        self.can.create_rectangle(0, 500, 10000, 501, fill="black")
        if hasattr(self, 'result_text_id'):
            self.can.delete(self.result_text_id)
        self.pln = Plane(self.win, self.can)
        self.blt = Bullet(self.win, self.can)
        self.add_text(1000, "white", "black", "cond_sim_", CONDITION)
        self.render_text_by_name(10, 10, "cond_sim_")
        self.add_text(1000, "white", "black", "h_", "H (В метрах) = ")
        self.render_text_by_name(10, 120, "h_")

        self.trg = None
        if hasattr(self, 'result_text_id'):
            self.can.itemconfig(self.result_text_id, state='hidden')
        else:
            self.result_text_id = None
        self.clear_objects(*self.objs_del)
        self.can.pack()
        self.entry_ = ttk.Entry(validate="key", validatecommand=(self.win.register(SimInputScreen.validate_number), '%P'))
        self.entry_.place(x=1050, y=325)
        self.entry_.focus_set()
        for obj in [self.pln, self.pln, self.trg]:
            if obj is not None:
                self.objs_del.append(obj.fly(0))

    def start_sim(self):
        self.can.delete("all")
        SimInputScreen.IS_SIM = True
        self.trg = Trg(self.win, self.can, int(self.entry_.get()))
        self.can.delete("all")
        self.can.create_rectangle(0, 500, 10000, 501, fill="black")

        objs = [self.pln, self.blt, self.trg]
        hit_target = False

        for t in range(0, 10000):
            if not SimInputScreen.IS_SIM:
                break
            else:
                for obj in objs:
                    self.objs_del.append(obj.fly(t / 1000))

                if "trg" in self.__dict__ and "blt" in self.__dict__:
                    if self.blt.is_collide(self.trg):
                        hit_target = True
                        SimInputScreen.IS_SIM = False
                        break

                    if self.blt.x > self.trg.x + 15 or self.blt.x > self.can.winfo_width() or \
                            self.blt.y < 0 or self.blt.y > self.can.winfo_height():
                        SimInputScreen.IS_SIM = False
                        break

            self.clear_objects(*self.objs_del)
            sleep(TIME_STEP)

        self.show_result(hit_target)
        self.win.mainloop()

    def add_main_to_sim_screen(self, main):
        self.main = main

    def show_result(self, hit):
        if hasattr(self, 'result_text_id'):
            self.can.itemconfig(self.result_text_id, state='hidden')

        if hit:
            text = IS_COLLISION
            color = "green"
        else:
            text = IS_NOT_COLLISION
            color = "red"

        self.result_text_id = self.can.create_text(
            self.can.winfo_width() // 2, 100,
            text=text,
            fill=color,
            font=('Helvetica', 16, 'bold'),
            anchor="center"
        )
        if hasattr(self, 'result_text_id'):
            self.can.itemconfig(self.result_text_id, state='normal')

    def clear_objects(self, *args):
        for obj_del in args:
            self.can.delete(obj_del)
