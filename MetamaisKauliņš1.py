import tkinter as tk
from tkinter import*
from random import randrange

#-  -   -   -   -   -   -   -   -   -   -   Vērtības
SB_value = 1

#-  -   -   -   -   -   -   -   -   -   -   Funkcijas

def on_spinbox_change(sb):
    global SB_value    
    SB_value = sb.get()
    print(SB_value)
    
def on_button_press(text1, text2):
    global SB_value
    N = randrange(1, 7)
    text2.configure(text = "Tu uzmeti: "+str(N))
    print(N, SB_value)
    if int(N) == int(SB_value):
        text1.configure(text = "Tu vinēji!", fg="green")
    else:
        text1.configure(text = "Tu zaudēji!", fg="red")

#-  -   -   -   -   -   -   -   -   -   -   programmas logs
App_Window = Tk()
App_Window.title("Metamais kauliņš1")
App_Window.geometry("800x400")
App_Window.resizable(False, False) 


#-  -   -   -   -   -   -   -   -   -   -   programmas widgets
FRAME = tk.Frame(App_Window)
FRAME.pack()

SB = tk.Spinbox(FRAME, from_=1, to=6, cursor="hand2", relief="sunken", bg="lightgrey", fg="blue", font=("Arial", 12))
SB.configure(command = lambda widget=SB: on_spinbox_change(widget))
SB.grid(column=0, row=1, pady = 10)

TEKSTS1 = tk.Label(FRAME, text = "Ievadiet skaitli te ko tu domā uzmetīsi no kauliņa: ", font=("Arial", 12, "bold"))
TEKSTS1.grid(column=0, row=0, pady = 10)

TEKSTS2 = tk.Label(FRAME, text = "", font=("Arial", 12, "bold"))
TEKSTS2.grid(column=0, row=4, pady = 10)

TEKSTS3 = tk.Label(FRAME, text = "Tu uzmeti: ", font=("Arial", 12, "bold"))
TEKSTS3.grid(column=0, row=2, pady = 10)

BUTTON = tk.Button(FRAME, text = "Mest kauliņu", bg="grey40", height=5, width=15
, font=("Arial", 20, "bold")
, command = lambda widget=TEKSTS2: on_button_press(widget, TEKSTS3))
BUTTON.grid(column=0, row=3, pady = 10)

#-  -   -   -   -   -   Start Loop
App_Window.mainloop()