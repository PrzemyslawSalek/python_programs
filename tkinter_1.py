import tkinter.messagebox
from tkinter import *

licznik = 0
krok = 1

def add(label):
    global licznik
    if(licznik+krok > 20):
            tkinter.messagebox.showinfo("Blad!", "Przekroczono zakres!")
    else:
        licznik += krok
        label.config(text="Licznik: " + str(licznik))

def sub(label):
    global  licznik
    if(licznik-krok < -20):
            tkinter.messagebox.showinfo("Blad!", "Przekroczono zakres!")
    else:
        licznik -= krok
        label.config(text="Licznik: " + str(licznik))

def show_entry_fields():
    global licznik, l1
    licznik = int(e1.get())
    l1.config(text="Licznik: " + str(licznik))

master=Tk()
master.geometry('250x140')

e1=Entry(master)
e1.place(x = 15, y = 90)

l1 = Label(master, text="Licznik: " + str(licznik))
l1.place(x = 25, y = 0)
l2 = Label(master, text="Krok: " + str(krok))
l2.place(x = 90, y = 0)

Button(master, text='Zmien licznik', command=show_entry_fields).place(x = 40, y = 55)

b1=Button(master, text ='+', command=lambda: add(l1), bg='red')
b1.place(x = 55, y = 25)

b2=Button(master, text='-', command=lambda: sub(l1), bg='red')
b2.place(x = 90, y = 25)

def krokc(v):
    global krok, b1, b2
    krok = v.get()
    if(krok == 1):
        b1.config(bg='red')
        b2.config(bg='red')
    elif(krok == 3):
        b1.config(bg='green')
        b2.config(bg='green')
    else:
        b1.config(bg='blue')
        b2.config(bg='blue')
    l2.config(text="Krok: " + str(krok))

v = IntVar()
Radiobutton(master, text="Krok: 1", variable=v, command=lambda: krokc(v) , value=1, bg='red').place(x = 165, y = 0)
Radiobutton(master, text="Krok: 3", variable=v, command=lambda: krokc(v) , value=3, bg='green').place(x = 165, y = 30)
Radiobutton(master, text="Krok: 10", variable=v, command=lambda: krokc(v) , value=10, bg='blue').place(x = 165, y = 60)


master.mainloop()