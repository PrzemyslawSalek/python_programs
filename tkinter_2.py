from tkinter import *

root=Tk()

scroll=Scrollbar(root)
textArea=Text(root, height=10, width =50)

scroll.pack(side=RIGHT, fill=Y)
textArea.pack(side=LEFT, fill=Y)

scroll.config(command=textArea.yview)
textArea.config(yscrollcommand=scroll.set)

file = open("plik1.txt")

textArea.insert(END, file.read())

e1=Entry(root)
e1.pack()

def save():
    f2 = open(e1.get(), "wt")
    f2.write(textArea.get("1.0", "end-1c"))
    f2.close()

b1=Button(root, text ='Save', command=lambda :save()).pack()

mainloop()