import tkinter as tk
from tkinter import *
import tkinter.ttk
import deci_maker

d = deci_maker.Decisions()


def create_top_level():
    top = Toplevel()
    top.geometry("350x350")
    top.attributes('-fullscreen', True)

    label = Label(top, text="Got a tough choice to make huh? \n Well enter your options below and I maybe can help!")
    input = tkinter.ttk.Entry(top)

    entry = input.get()
    submit = tkinter.ttk.Entry(top, text="Add", command=lambda:submit(entry))

    close = tkinter.ttk.Button(top, text="Close", command=top.destroy)
    label.pack_configure(pady=15)
    input.pack(pady=20)
    close.pack(pady=25)
    top.mainloop()

def submit(txt):
    d.new(txt)




