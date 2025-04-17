import tkinter
from tkinter import ttk
from PIL import Image, ImageTk


class BaseScreen:

    def __init__(self, win):
        self.win = win
        self.buttons = []
        self.texts = {}
        self.photos = {}
        self.labels = []

    def add_button(self, text_, command_=None):
        self.buttons.append(ttk.Button(self.win, text=text_, command=command_))

    def get_buttons(self):
        return self.buttons

    def add_text(self, w, bg_, fg_, title, text_, font_=("Arial", 15, "bold")):
        self.texts[title] = tkinter.Message(self.win, width=w, font=font_, bg=bg_, fg=fg_, text=text_)

    def render_text_by_name(self, padx_, pady_, title):
        self.texts[title].pack(padx=padx_, pady=pady_)

    def add_image(self, name, path):
        pil_image = Image.open(path)
        self.photos[name] = ImageTk.PhotoImage(pil_image)

    def render_image_by_name(self, name, padx_, pady_):
        lb = tkinter.Label(self.win, image=self.photos[name])
        lb.pack(padx=padx_, pady=pady_)
        self.labels.append(lb)

    def clear_screen(self, e=None):
        for el1 in self.buttons:
            el1.destroy()
        for el2 in self.texts.values():
            el2.destroy()
        for el3 in self.labels:
            el3.destroy()
        self.buttons.clear()
        self.texts.clear()
        self.labels.clear()


