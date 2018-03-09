from tkinter import Tk, E
import tkinter.ttk as ttk
from Views import TabWindow, AppWindow, add_weight, create_tab
from Models import Case
import openpyxl

FILE_PATH = "C:\\Users\\Justin Kudela\\Desktop\\"

TAB_DICT = {'Manual Votes': 0, 'Scroll Votes': 1}

root = Tk()
root.geometry("1050x620")
root.title("Jurisdictional Voter")
add_weight(root)
application = AppWindow(root, TAB_DICT)

jur_list = openpyxl.load_workbook(FILE_PATH + 'Jur_list.xlsx')
sheet = jur_list['Sheet1']
print(sheet['A2'].value)
print(sheet.max_row)

case_one = Case()

create_tab(application, 'Manual Votes', case_one)



root.mainloop()
