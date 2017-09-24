import tkinter


class GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.wm_title("FourPlusOne's Encyclopedia")
        windowWidth = self.main_window.winfo_screenwidth()
        windowHeight = self.main_window.winfo_screenheight()
        self.main_window.geometry("%dx%d" % (windowWidth / 4, windowHeight * .6))

        self.search_frame = tkinter.Frame(self.main_window)
        self.search_button = tkinter.Button(self.search_frame, text = "Search:",
                                            command = runSearch)
        self.search_button.pack()
        self.search_frame.pack()


        tkinter.mainloop()


def runSearch():
    print("searching...")





# Helpful resources:
    # setting window size
    # https://www.daniweb.com/programming/software-development/threads/322818/tkinter-window-size