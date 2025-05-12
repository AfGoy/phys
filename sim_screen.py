from time import *
from tkinter import ttk, Tk, Canvas

from plane import Plane
from bullet import Bullet
from trg import Trg

from base_screen import BaseScreen
from consts import H, IS_COLLISION, IS_NOT_COLLISION, CONDITION, TIME_STEP


class SimScreen(BaseScreen):
    IS_SIM = False

    def __init__(self, win, can):
        super().__init__(win)
        self.can = can
        self.objs_del = []
        self.create_obj()
        self.result_text_id = None

    def create_obj(self):
        self.pln = Plane(self.win, self.can)
        self.blt = Bullet(self.win, self.can)
        self.trg = Trg(self.win, self.can, H)

    def init_sim(self):
        if hasattr(self, 'result_text_id'):
            self.can.itemconfig(self.result_text_id, state='hidden')
        self.clear_objects(*self.objs_del)
        self.add_text(1000, "white", "black", "cond_sim", CONDITION)
        self.render_text_by_name(10, 10, "cond_sim")
        self.create_obj()
        self.can.pack()
        for obj in [self.pln, self.pln, self.trg]:
            self.objs_del.append(obj.fly(0))

    def start_sim(self):
        self.can.delete("all")
        SimScreen.IS_SIM = True

        objs = [self.pln, self.blt, self.trg]
        hit_target = False

        for t in range(0, 10000):
            if not SimScreen.IS_SIM:
                break
            else:
                self.objs_del = []
                for obj in objs:
                    self.objs_del.append(obj.fly(t / 1000))

                if "trg" in self.__dict__ and "blt" in self.__dict__:
                    if self.blt.is_collide(self.trg):
                        hit_target = True
                        SimScreen.IS_SIM = False
                        break

                    if self.blt.x > self.trg.x + 15 or self.blt.x > self.can.winfo_width() or \
                            self.blt.y < 0 or self.blt.y > self.can.winfo_height():
                        SimScreen.IS_SIM = False
                        break

            self.clear_objects(*self.objs_del)
            sleep(TIME_STEP)

        self.show_result(hit_target)
        self.win.mainloop()

    def show_result(self, hit):
        if hasattr(self, 'result_text_id'):
            self.can.itemconfig(self.result_text_id, state='hidden')

        self.result_text_id = self.can.create_text(
            self.can.winfo_width() // 2, 100,
            text=IS_COLLISION,
            fill="green",
            font=('Helvetica', 16, 'bold'),
            anchor="center"
        )
        self.can.itemconfig(self.result_text_id, state='normal')


    def render_screen(self, text):
        self.render_text_by_name(10, 10, "hlp")

    def clear_objects(self, *args):
        for obj_del in args:
            self.can.delete(obj_del)

