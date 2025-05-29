from consts import *


class Trg:
    def __init__(self, win, can, H_):
        self.H = H_
        self.can = can
        self.win = win
        self.y_start = (SCR_HGHT - self.H + OFFSET_Y)
        self.x = L + x0
        self.y = self.y_start
        self.trg = self.can.create_rectangle(self.x + 10, self.y_start + 10, self.x, self.y_start,
                                             fill="black")

    def fly(self, t):
        delta_y = Vt * t * KY**0.5
        self.y = self.y_start + delta_y
        self.trg = self.can.create_rectangle(self.x + SIZE_TRG, self.y + SIZE_TRG, self.x,
                                             self.y,
                                             fill="black")

        self.can.update()
        return self.trg

    def is_collide_ground(self):
        if COORDS_GROUND[1] - 1 < self.y + SIZE_TRG < COORDS_GROUND[1] + 1:
            return True
        return False
