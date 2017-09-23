import tkinter


class GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.wm_title("FourPlusOne's Encyclopedia")
        self.search_frame = tkinter.Frame(self.main_window)
        self.search_button = tkinter.Button(self.search_frame, text = "Search:",
                                            command = runSearch)
        self.search_button.pack()
        self.search_frame.pack()
        tkinter.mainloop()


def runSearch():
    print("searching...")
