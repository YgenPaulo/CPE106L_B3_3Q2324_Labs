from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
import database
from database import create_table, delete_item, fetch_items, insert_item, id_exist, update_item
from Main import ItemManager
from Main import main
from tkinter.ttk import *
from tkinter import *
from build import viewinven
import sqlite3


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\paule\OneDrive\Desktop\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("500x500")
window.configure(bg = "#F6F6F6")

window.title("PERSONAL INVENTORY MANAGEMENT SYSTEM")





def close():
    window.destroy()


def view_inven():
    view_inven_window = viewinven.InventoryWindow(master=window)
    window.withdraw()  # Hide the main window
    view_inven_window.mainloop()  # Start the mainloop of the viewinven window
    window.deiconify()  # Show the main window again after viewinven window is closed


#creates the window
canvas = Canvas(
    window,
    bg = "#F6F6F6",
    height = 500,
    width = 500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    
)

canvas.place(x = 0, y = 0)




image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    250.0,
    35.0,
    image=image_image_1
)

canvas.create_text(
    20.0,
    19.0,
    anchor="nw",
    text="PERSONAL INVENTORY MANAGEMENT\nSYSTEM",
    fill="#5F5135",
    font=("JosefinSansRoman Regular", 23 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
addItem = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=print("hello world add"),
    relief="flat"
)
addItem.place(
    x=63.0,
    y=361.0,
    width=171.0,
    height=42.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
view_inventory = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=view_inven,
    relief="flat"
)
view_inventory.place(
    x=251.0,
    y=361.0,
    width=174.0,
    height=42.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
edit_button = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command=print("hello"),

)
edit_button.place(
    x=63.0,
    y=421.0,
    width=171.0,
    height=42.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
close_button = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=close,
    relief="flat"
)
close_button.place(
    x=251.0,
    y=420.0,
    width=174.0,
    height=42.0
)

canvas.create_text(
    63.0,
    123.0,
    anchor="nw",
    text="ITEM NO.:",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    194.0,
    237.0,
    anchor="nw",
    text="IMPORTANCE:",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    63.0,
    237.0,
    anchor="nw",
    text="ITEM QTY:",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    63.0,
    180.0,
    anchor="nw",
    text="ITEM NAME:",
    fill="#000000",
    font=("Inter", 12 * -1)
)

qty = Entry(
    bd=0,
    bg="#D9D9D9",
   fg="#000716",
  highlightthickness=0
)
qty.place(
    x=63.0,
    y=260.0,
    width=117.0,
    height=28.0
)

#entry_2 = Entry(
#    bd=0,
#    bg="#D9D9D9",
#    fg="#000716",
#    highlightthickness=0
#)
#entry_2.place(
#    x=194.0,
#    y=260.0,
#    width=101.0,
#    height=28.0
#) make new combobox
importance_values = ["Low", "Medium", "High"]
importance_combobox = Combobox(
    window,
    values=importance_values,
    state="readonly",

)
importance_combobox.place(
    x=194.0,
    y=260.0,
    width=101.0,
    height=28.0
)

canvas.create_text(
    323.0,
    237.0,
    anchor="nw",
    text="CATEGORY",
    fill="#000000",
    font=("Inter", 12 * -1)
)

category = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
category.place(
    x=323.0,
    y=260.0,
    width=101.0,
    height=28.0
)

ItemNo = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
ItemNo.place(
    x=63.0,
    y=142.0,
    width=362.0,
    height=27.0
)

itemName = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
itemName.place(
    x=63.0,
    y=199.0,
    width=362.0,
    height=27.0
)


window.resizable(False, False)
window.mainloop()
