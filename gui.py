import tkinter


class GUI:
    def __init__(self):
        self.mainWindow = tkinter.Tk()
        self.mainWindow.wm_title("FourPlusOne's Encyclopedia")
        windowWidth = self.mainWindow.winfo_screenwidth() / 4
        windowHeight = self.mainWindow.winfo_screenheight() * .6
        self.mainWindow.geometry("%dx%d" % (windowWidth, windowHeight))

        self.checkboxFrame = tkinter.Frame(self.mainWindow)
        self.searchFrame = tkinter.Frame(self.mainWindow)
        self.searchButton = tkinter.Button(self.searchFrame, text ="Search:",
                                           command = runSearch)
        self.searchButton.pack()
        self.searchFrame.pack()


        tkinter.mainloop()


def runSearch():
    print("searching...")





# Helpful resources:
    # setting window size
    # https://www.daniweb.com/programming/software-development/threads/322818/tkinter-window-size