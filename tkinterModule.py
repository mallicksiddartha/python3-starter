from tkinter import *
from PIL import Image, ImageTk

class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master

        self.init_window()

    def init_window(self):
        self.master.title("This title should show in the window top.")
        self.pack(fill = BOTH, expand = 1)
        quitButton = Button(self, text="Quit", command=self.client_exit)
        quitButton.place(x=0, y=0)

        customMenu = Menu(self.master)
        self.master.config(menu=customMenu)
        file = Menu(customMenu, tearoff = 0)
        file.add_command(label='Exit', command =self.client_exit)
        customMenu.add_cascade(label='File', menu=file)

        edit = Menu(customMenu, tearoff = 0)
        edit.add_command(label='Show Image', command = self.showImage)
        edit.add_command(label='Show Text', command = self.showText)
        customMenu.add_cascade(label = 'Edit', menu = edit)

    def client_exit(self):
        exit()

    def showImage(self):
        load = Image.open('F:\Siddartha\Photo\dimpahar.jpg')
        render = ImageTk.PhotoImage(load)
        loadedImage = Label(self, image = render)
        loadedImage.image = render
        loadedImage.place(x = 0, y = 0)

    def showText(self):
        viewedText = Label(self, text = 'Found reasons behind dark fantasy biscuit.')
        viewedText.pack()

root = Tk()
root.geometry("300x400")
app = Window(root)
root.mainloop()

