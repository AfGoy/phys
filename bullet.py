from consts import *


class Bullet:
    def __init__(self, win, can):
        self.win = win
        self.can = can
        self.x_start = 60 + x0
        self.y_start = (SCR_HGHT - h + OFFSET_Y)
        self.x = self.x_start
        self.y = self.y_start
        self.blt = self.can.create_oval(self.x_start + 5, self.y_start + 5, self.x_start, self.y_start, fill="black")

    def fly(self, t):
        delta_x = (Vb + Vp) * t
        delta_y = (g * t ** 2) * 0.5

        self.x = self.x_start + delta_x
        self.y = self.y_start + delta_y * KY
        self.blt = self.can.create_oval(self.x + 5, self.y, self.x,
                                        self.y + 5, fill="black")

        self.can.update()
        return self.blt

    def is_collide(self, trg):
        if trg.x - 8 <= self.x <= trg.x + 5 and trg.y - 8 <= self.y <= trg.y + 8:
            return True
        return False


