from tkinter import *
import tkinter
from tkinter import messagebox

import WikipediaAPI


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

        # Makes list of checkbox labels. Additional attributes can
        # be added later if needed.
        checkboxSourceList = [["Wikipedia"], ["not"], ["sure"]]

        # Loops through list creating each checkbox and packing it.
        for x in range(len(checkboxSourceList)):
            cbox = Checkbutton(self.checkboxFrame, text=checkboxSourceList[x][0], variable=checkboxSourceList[x])
            #packing
            cbox.pack(padx=5,pady=0, side=LEFT)
        self.checkboxFrame.pack()

        # Sets up the search frame with button and text box.
        self.searchFrame = Frame(self.mainWindow)
        self.searchButton = Button(self.searchFrame, text ="Search:", command = self.runSearch)
        self.searchTextbox = Entry(self.searchFrame, width=40)

        #packs textbox, button, and frame
        self.searchTextbox.pack(side=LEFT, padx=0, pady=0)
        self.searchButton.pack(side=LEFT, padx=5, pady=0)
        self.searchFrame.pack()

        # Sets up the listbox widget.
        self.listFrame = Frame(self.mainWindow)
        self.resultsListbox = Listbox(self.listFrame, width=50, height =20)
        self.resultsListbox.pack()
        self.listFrame.pack()

        # Keeps window active.
        mainloop()


    def runSearch(self):
        search_word = self.searchTextbox.get()

        #checks to make sure that input has been entered into the textbox
        if search_word == "":
            tkinter.messagebox.showinfo("Error", "Please enter a word to search.")
            self.searchTextbox.delete(0, "end")

        #checks to make sure there are no spaces in the input entered
        else:
            if hasSpaces(search_word) == True:
                tkinter.messagebox.showinfo("Error", "Please enter only one word. Spaces are not allowed.")

            #checks to make sure only letters are being typed being input
            else:
                search_word = "".join(search_word.split())

                if search_word.isalpha():
                    print("Searching")

                    #clear all search
                    self.resultsListbox.delete(0, END)

                    getSearchResults(WikipediaAPI.getSearchResults(search_word), self.resultsListbox)

                else:
                    tkinter.messagebox.showinfo("Error", "Please type only letters.")
                    self.searchTextbox.delete(0, "end")

#returns list of search results (Only one word)
def getSearchResults(search_list, listbox):
    results = []
    for i in search_list:
        if hasSpaces(i) == False:
            results.append(i)
    addToListBox(results, listbox)

# Add provided string to listbox. END indicates
# to append to the end.
def addToListBox(list, listbox):
    for i in list:
        listbox.insert(END, i)

        summary = WikipediaAPI.getSummary(i)
        total_lines= len(summary)/50

        if total_lines < 1.0:
            listbox.insert(END, WikipediaAPI.getSummary(i))
        else:
            listbox.insert(END,summary[:50])
            listbox.insert(END, summary[50:100])

#checks for spaces
def hasSpaces(check_word):
    if " " in check_word:
        return True
    else:
        return False

    # Helpful resources:
    # setting window size:
    # https://www.daniweb.com/programming/software-development/threads/322818/tkinter-window-size
    # adding widgets in a loop:
    # https://stackoverflow.com/questions/8536518/how-do-i-create-multiple-checkboxes-from-a-list-in-a-for-loop-in-python-tkinter
    #https://stackoverflow.com/questions/26987222/checking-whitespace-in-a-string-python
    #https://docs.python.org/3/library/stdtypes.html