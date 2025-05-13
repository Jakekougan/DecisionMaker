import tkinter as tk
from tkinter import *
import tkinter.ttk
import deci_maker
import deci_UI as dui

r = Tk()
r.geometry("350x350")
r.attributes('-fullscreen', True)

screen_text = "Welcome to the Selector!\n Select your Mode!"
parent_message = tk.Message(r,text=screen_text)


but1 = tkinter.ttk.Button(r, text="Decision Maker", command=dui.create_top_level)
but2 = tkinter.ttk.Button(r, text="Eliminator")
but_exit = tkinter.ttk.Button(r, text="Exit", command=r.destroy)

parent_message.pack(pady=10)

but1.pack(pady=10)
but2.pack(pady=10)
but_exit.pack(pady=25)


tkinter.mainloop()