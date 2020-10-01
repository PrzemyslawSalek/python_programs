#Zadanie 1
#Napisz program składający się z dwóch
#button’ów: ‚+’ i ‚-’. Po wciśnięciu +/- program
#zwiększa/zmniejsza wartość zmiennej ‚licznik’
#(jej wartość początkowa to 0) o wartość
#zmiennej ‚krok’ (wartość początkowa to 1).
#Wartości zmiennych ‚licznik’ i ‚krok’
#powinny być wyświetlane w oknie głównym w
#postaci label'ów.

#Zadanie 2
#Zmodyfikuj zadanie 1. Dodaj widget 'Entry',
#w którym wpisuje się początkową wartość
#zmiennej ‚licznik’. Przypisanie nowej wartości
#odbywa się przez kliknięcie dodatkowego
#button’u.

#Zadanie 3
#Zmodyfikuj zadanie 2. Dodaj trzy
#radiobutton’y, które zmieniają wartości zmiennej
#‚krok’ na 1, 3 lub 10.

#Zadanie 4
#Zmodyfikuj zadanie 3. Dodaj kolory tła do
#radiobutton’ów (red, green, blue). Kolor
#button’ów ‚+’ i ‚-’ powinien być zgodny z tłem
#wybranego radiobutton’a.

#Zadanie 5
#Zmodyfikuj zadanie 4. Po przekroczeniu
#zakresu (-20,20) przez zmienną ‚licznik’ powinno
#wyświetlić się okno z komunikatem:
#"Przekroczono zakres".

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