from tkinter import Frame, Menu, W, E, Label, Entry, Radiobutton, Checkbutton, \
    Button, Text, WORD, END
import tkinter.ttk as ttk
import tkinter as tk
from functools import partial

"""Constants"""
BTN_WIDTH = 20
BTN_STYLE = "Blue.TButton"
HEADING_FONT = "Times 12 bold"
HEADING_WIDTH = 30
SUBHEADING_FONT = "Times 8"
PREVIEW_FIELD_FONT = "Times 9"
"""End Constants"""

def add_weight(widget):
    rows = 0
    while rows < 50:
        widget.rowconfigure(rows, weight=1)
        widget.columnconfigure(rows, weight=1)
        rows += 1
    return None

def add_button_left(master, button_name, button_command):
    button = ttk.Button(master, text=button_name, command=button_command, width=BTN_WIDTH, style=BTN_STYLE)
    button.grid(row=master.row_cursor, column=master.col_cursor, sticky=W, padx=10, pady=3)
    master.row_cursor += 1
    return button

def add_heading(master, heading):
    heading = ttk.Label(master, text=heading, width=HEADING_WIDTH, font=HEADING_FONT)
    heading.grid(row=master.row_cursor, column=master.col_cursor, columnspan=2,
            sticky=W, pady=10, padx=5)
    master.row_cursor += 1

def print_vote(model):
    print(model.vote.get())


def create_tab(application, tab_name, model):
    """A generic tab for multiple templates with a preview window."""
    tab = application.app_tab_dict[tab_name]
    add_heading(tab, 'Case Number')
    entry = Entry(tab, width=20)
    entry.grid(row=tab.row_cursor, column=tab.col_cursor, pady=5)
    tab.row_cursor += 1
    decline_button = Radiobutton(tab, text="Decline", variable=model.vote, value=1)
    decline_button.grid(row=tab.row_cursor, column=tab.col_cursor, sticky=W)
    accept_button = Radiobutton(tab, text="Accept", variable=model.vote, value=2)
    accept_button.grid(row=tab.row_cursor+1, column=tab.col_cursor, sticky=W)
    hold_button = Radiobutton(tab, text="Hold", variable=model.vote, value=3)
    hold_button.grid(row=tab.row_cursor+2, column=tab.col_cursor, sticky=W)
    notpart_button = Radiobutton(tab, text="Not Participating", variable=model.vote, value=4)
    notpart_button.grid(row=tab.row_cursor+3, column=tab.col_cursor, sticky=W)
    tab.row_cursor += 4
    vote_button = add_button_left(tab, "Submit Vote", partial(print_vote, model))

class AppWindow(ttk.Frame):
    """The main application window."""
    def __init__(self, master, tabs_dict):
        self.tab_dict = tabs_dict
        self.app_tab_dict = {}
        self.master = master
        self.notebook = ttk.Notebook(self.master)
        self.notebook.grid(row=1, column=0, columnspan=50, sticky='NESW')
        self.set_style()
        # self.menu = AppMenu(self.master) #Menu can be added back later
        for key, value in self.tab_dict.items():
            self.tab = TabWindow(self.notebook)
            self.notebook.add(self.tab, text=key)
            self.app_tab_dict[key] = self.tab

    def set_style(self):
        """Sets the style for objects on the application. Can add new styles in
        this method and they will apply to entire application."""
        self.style = ttk.Style()
        self.style.configure('Blue.TButton', font='helvetica 8', foreground='blue', padding=5)


# class AppMenu(ttk.Frame):
#     """The menu widget for the main application."""
#     def __init__(self, master):
#         ttk.Frame.__init__(self, master)
#         self.menu = Menu(self.master)


class TabWindow(ttk.Frame):
    """A class view object for creating tab windows on the main application. """
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.master = master
        self.row_cursor = 0
        self.col_cursor = 0

    def set_col_cursor(self, column):
        self.col_cursor = column

    def set_row_cursor(self, row):
        self.row_cursor = row
