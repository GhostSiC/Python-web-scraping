import tkinter
from io import BytesIO
from typing import io

from tkinter import *

from web_sub import WebClass, Anime

from PIL import Image, ImageTk

class GuiClass:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("GhostSiC Apk")
        self.root.geometry("1200x800")



        self.create_button()
        self.engine()

    def engine(self):
        self.root.mainloop()

    def create_button(self):
        self.nav = tkinter.Frame(master = self.root, height=50, bg="red")
        self.nav.grid_propagate(False)
        self.nav.pack(fill=tkinter.X, side=tkinter.TOP)

        self.anime_box = tkinter.Frame(master=self.root,height=600, bg="blue")
        self.anime_box.pack(fill=tkinter.BOTH, side=tkinter.TOP, expand=True)

        self.refresh_button = tkinter.Button(master=self.nav, text="Get Anime", width=8)
        self.refresh_button.pack()

        self.refresh_button.config(command=lambda: self.get_anime())

    def get_anime(self):
        web = WebClass("https://subsplease.org")
        self.anime_list = web.get_anime_by_name()

        self.anime_frame_each = []

        for i in self.anime_list:
            frame = tkinter.Frame(master=self.anime_box, height=50, bg="green")
            frame.pack(fill=tkinter.BOTH, side=tkinter.TOP, expand=True, padx=10, pady=10)

            img = ImageTk.PhotoImage(Image.open(BytesIO(i.raw_data_img)))



            label1 = tkinter.Label(frame, image=img)
            label1.photo = img
            label1.pack(side=tkinter.LEFT)

            name_label = tkinter.Label(frame, text=i.name, font=30, fg="blue")
            name_label.pack()

            self.anime_frame_each.append(frame)

        web.close_brw()