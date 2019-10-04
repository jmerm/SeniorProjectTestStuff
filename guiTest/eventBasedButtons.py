from tkinter import *
#binding a function to a widget
root = Tk()

def printName(event):
    print("Hello my name is John")

button_1 = Button(root, text="Print my name")
button_1.bind("<Button-1>", printName)
button_1.pack()

root.mainloop()