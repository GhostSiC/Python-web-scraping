from tkinter import Tk, Button


class gui_class:
    def __init__(self):
        self.root = Tk()
        self.root.title("GhostSiC Apk")
        self.root.geometry("1200x800")


        self.create_button()
        self.engine()


    def engine(self):
        self.root.mainloop()

    def create_button(self):
        self.refresh_button = Button(self.root, text="Refresh", width=8)
        self.refresh_button.pack()

        #self.refresh_button.config(command=lambda: click_action(click_button))