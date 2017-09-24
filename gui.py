from tkinter import *


class GUI:
    def __init__(self):
        # Makes main window widget and gives it a title.
        self.mainWindow = Tk()
        self.mainWindow.wm_title("FourPlusOne's Encyclopedia")

        # Retrieves the current screen's width and height.
        # Fractions of these values are used to determine
        # the size of the main window.
        windowWidth = self.mainWindow.winfo_screenwidth() / 4
        windowHeight = self.mainWindow.winfo_screenheight() * .6
        self.mainWindow.geometry("%dx%d" % (windowWidth, windowHeight))

        # Sets up the checkboxes in their own frame.
        self.checkboxFrame = Frame(self.mainWindow)
        self.cboxValue1 = IntVar()
        self.cboxValue2 = IntVar()
        self.cboxValue3 = IntVar()

        self.checkbox1 = Checkbutton(self.checkboxFrame, text = "Wikipedia", variable = self.cboxValue1)
        self.checkbox2 = Checkbutton(self.checkboxFrame, text="not", variable=self.cboxValue2)
        self.checkbox3 = Checkbutton(self.checkboxFrame, text="sure", variable=self.cboxValue3)
        self.checkbox1.pack()
        self.checkbox2.pack()
        self.checkbox3.pack()
        self.checkboxFrame.pack()

        self.searchFrame = Frame(self.mainWindow)
        self.searchButton = Button(self.searchFrame, text ="Search:",
                                           command = runSearch)
        self.searchButton.pack()
        self.searchFrame.pack()


        mainloop()


def runSearch():
    print("searching...")





# Helpful resources:
    # setting window size
    # https://www.daniweb.com/programming/software-development/threads/322818/tkinter-window-size