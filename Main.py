from tkinter import Tk, E
import tkinter.ttk as ttk
from Views import TabWindow, AppWindow, add_weight, create_tab
from Models import Case
import openpyxl

FILE_PATH = "C:\\Users\\Justin Kudela\\Desktop\\"

TAB_DICT = {'Voting': 0, 'Results': 1}

root = Tk()
root.geometry("1050x620")
root.title("Jurisdictional Voter")
add_weight(root)
application = AppWindow(root, TAB_DICT)

jur_list = openpyxl.load_workbook(FILE_PATH + 'Jur_list.xlsx')
sheet = jur_list['Sheet1']
row = 2
scroll_list = []
while row <= sheet.max_row:
    scroll_list.append(sheet['A' + str(row)].value)
    row +=1

print(scroll_list)
case_one = Case()

create_tab(application, 'Voting', case_one)



root.mainloop()
