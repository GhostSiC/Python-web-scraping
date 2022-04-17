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

        index = []
        index_x = 0
        index_y = 0

        for i in self.anime_list:
            frame_box = tkinter.Frame(master=self.anime_box, height=50, bg="green")
            #frame_box.pack(fill=tkinter.BOTH, side=tkinter.TOP, expand=True, padx=10, pady=10)
            frame_box.grid(row=index_x, column=index_y)

            frame_label = tkinter.Frame(master=frame_box, bg="green")
            #frame_label.pack(fill=tkinter.BOTH, side=tkinter.TOP, expand=True, padx=10, pady=10)


            img = ImageTk.PhotoImage(Image.open(BytesIO(i.raw_data_img)))

            label_img = tkinter.Label(frame_box, image=img)
            label_img.photo = img

            name_label = tkinter.Label(frame_label, text=i.name, font=30, fg="blue")
            desc_label = tkinter.Label(frame_label, text=i.desc, font=30, fg="blue")

            label_img.grid(row=0, column=0)
            frame_label.grid(row=0, column=1)


            name_label.grid(row=0, column=0)
            desc_label.grid(row=1, column=0)

            #label_img.pack(side=tkinter.LEFT)
            #name_label.pack(side=tkinter.TOP)
            #desc_label.pack(side=tkinter.TOP)


            self.anime_frame_each.append(frame_box)

            index_y += 1

            if (index_y % 2 == 0):
                index_x += 1
                index_y = 0

        web.close_brw()