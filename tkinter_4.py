#Zadanie 1
#Napisz program, który wykorzystuje
#widgety Canvas i Scale. Na Canvas powinno być
#narysowane koło, a dzięki Scale można zmieniać
#jego rozmiar (promień).

from tkinter import *

x1, y1, x2, y2 = 350, 100, 250, 200

def zoomer(event):
    canvas.coords(co, x1+v.get(), y1-v.get(), x2-v.get(), y2+v.get())

root = Tk()
root.geometry("640x360")
root.title("The green oval of hell")

v = DoubleVar()
scale = Scale(root, length=640, variable=v, from_=-50, to=75, orient=HORIZONTAL, command=zoomer)
scale.pack(side=BOTTOM)

canvas = Canvas(root, width=640, height=360)
co = canvas.create_oval(x1, y1, x2, y2, fill="green")
canvas.pack()

root.mainloop()