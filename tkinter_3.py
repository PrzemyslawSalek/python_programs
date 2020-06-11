from tkinter import *

def paint(event):
    w.create_oval(event.x-5, event.y-5, event.x+5, event.y+5, fill="black")

master = Tk()

w = Canvas(master, width=500, height=150)
w.pack(expand=YES, fill=BOTH)
w.bind("<ButtonPress-1>", paint)

def clear(event):
    w.delete(ALL)

master.bind("d", clear)

mainloop()