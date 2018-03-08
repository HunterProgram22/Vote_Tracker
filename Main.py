from tkinter import Tk, E
import tkinter.ttk as ttk
from Models import Case

TAB_DICT = {'Vote Entry': 0, 'Entered Votes': 1,}


def add_weight(widget):
    rows = 0
    while rows < 50:
        widget.rowconfigure(rows, weight=1)
        widget.columnconfigure(rows, weight=1)
        rows += 1
    return None

root = Tk()
root.geometry("1050x620")
root.title("Jurisdictional Voter")
add_weight(root)





root.mainloop()
