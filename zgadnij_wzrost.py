#Troll

from tkinter import *

def main():
    global root
    root = Tk()
    root.title('Ile masz wzrostu?')
    root.geometry('320x180')
    root.resizable(False, False)
    sign = Label(root, text='@p_salek')
    sign.place(x=265, y=160)

def start():
    l1.destroy()
    b1.destroy()
    second_v()

def first_v():
    global l1, b1
    l1 = Label(root, text='Zadamy ci kilka osobistych pytań\n na podstawie których podamy twój wzrost.')
    l1.place(x=40, y=40)
    b1 = Button(root, text='Start', command=lambda: start())
    b1.place(x=140, y=110)

def get(event):
    global name
    name = e1.get()
    print(name)
    e1.delete(0, END)
    third_v()

def second_v():
    global lq, e1
    lq = Label(root, text='Jak masz na imię?')
    lq.place(relx=0.5, rely=0.3, anchor=CENTER)
    e1 = Entry(root, width='40')
    e1.place(x=40, y=90)
    e1.bind('<Return>', get)

def get2(event):
    global tmp
    tmp = e1.get()
    print(tmp)
    e1.destroy()
    lq.destroy()
    fourth_v()

def third_v():
    lq.config(text='Witaj ' + name + '!\n Może od razu przejdźmy do rzeczy!\n Ile masz wzrostu?')
    e1.bind('<Return>', get2)

def fourth_v():
    lq = Label(root, text='Chyba już wiemy wystarczająco!\nCzy twój wzrost to: ' + tmp + '?')
    lq.place(relx=0.5, rely=0.4, anchor=CENTER)

main()
first_v()
root.mainloop()