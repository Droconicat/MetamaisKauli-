import tkinter as tk
from tkinter import*
from random import randrange

#-  -   -   -   -   -   -   -   -   -   -   Vērtības

R_value = 1

#-  -   -   -   -   -   -   -   -   -   -   Funkcijas

def on_button1_press(TEXT):
    global R_value    
    R_value = randrange(1, 13)
    TEXT.configure(text="Rats uzrulēja: "+str(R_value))
    print(R_value)
    
    
def on_button2_press(text1, text2):
    global R_value
    N1, N2 = randrange(1, 7), randrange(1, 7)
    text2.configure(text = "Tu uzmeti: "+str(N1)+" un "+str(N2))
    print(N1, N2, R_value)
    if int(R_value) <= int(N1+N2) :
        text1.configure(text = "Tu vinēji!", fg="lawn green")
    else:
        text1.configure(text = "Tu zaudēji!", fg="orange red")

#-  -   -   -   -   -   -   -   -   -   -   programmas logs

App_Window = Tk()
App_Window.title("Metamais kauliņš2")
App_Window.geometry("500x800")
App_Window.resizable(False, False) 


#-  -   -   -   -   -   -   -   -   -   -   programmas widgets


FRAME = tk.Frame(App_Window)
FRAME.pack()

Button1 = tk.Button(FRAME, text="Griezst ratu", cursor="hand2", bg="lightgrey", fg="purple", font=("Arial", 12))
Button1.grid(column=0, row=0, pady = 10)

Text1 = tk.Label(FRAME, text = "Rats uzrulēja: 1", font=("Arial", 12, "bold"))
Text1.grid(column=0, row=1, pady = 10)

Image = tk.PhotoImage(file = "BILDES/Roulette_Rats(1).png")

BILDE1 = tk.Label(FRAME, image=Image)
BILDE1.grid(column=0, row=3, pady = 10)

#   -  -   -   -   -

Button2 = tk.Button(FRAME, text = "Mest kauliņus", cursor="hand2", bg="lightgrey", fg="purple", font=("Arial", 12))
Button2.grid(column=0, row=4, pady = 10)

Text2 = tk.Label(FRAME, text = "Tu uzmeti: 1 un 1", font=("Arial", 12, "bold"))
Text2.grid(column=0, row=5, pady = 10)

Image2 = tk.PhotoImage(file = "BILDES/Kaulins.png")
BILDE2 = tk.Label(FRAME, image=Image2)
BILDE2.grid(column=0, row=6, pady = 10)

Text3 = tk.Label(FRAME, text = "", fg = "white", bg="grey35", height=3, width=30, font=("Arial", 20, "bold"))
Text3.grid(column=0, row=7, pady = 10)

#-  -   -   -   -   -   -   -   -   -   -   Pogu loģiku

Button1.configure(command = lambda widgets=Text1: on_button1_press(widgets))
Button2.configure(command = lambda widget=Text3: on_button2_press(widget, Text2))

#-  -   -   -   -   -   Start Loop

App_Window.mainloop()