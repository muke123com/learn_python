from tkinter import *
class Main(Frame):
    def __init__(self, master=None):
        if(master != None):
            master = Tk()
            master.title("学习")
        super().__init__(master)
        self.button = {
            'bg': "#f5f5f5",
            'fg': "#333333",
        }

        self.pack()
        self.start()
        self.mainloop()
        pass


    def start(self):
        leftLabel = Label(self)
        leftLabel["bg"] = "#eeeeee"

        leftTitle = Label(leftLabel)
        leftTitle["text"] = "Test"
        leftTitle["width"] = 30
        leftTitle.pack()

        item = StringVar()
        leftList = Listbox(leftLabel, listvariable=item)
        item.set(["aaa", "bbb", "ccc", "ddd", "eee"])
        leftList["width"] = 26
        leftList.bind('<Button-1>', self.list_click)
        leftList.pack()

        rightLabel = Label(self)
        rightLabel["width"] = 90
        rightLabel["bg"] = "#aaa"

        self.rightNote = Label(rightLabel)
        self.rightNote["text"] = "空"
        self.rightNote.pack()

        leftLabel.pack(side="left")
        rightLabel.pack(side="right", fill=Y)
        pass


    def list_click(self, e):

        pass