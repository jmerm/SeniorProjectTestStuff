from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo('Window Title', 'Monkeys can live up to 300 years')

answer = tkinter.messagebox.askquestion('question 1', 'Do you like silley faced?')

if answer == 'yes':
    print(":^)")

root.mainloop()