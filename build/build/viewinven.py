from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Toplevel, StringVar
from tkinter.ttk import Combobox
import sqlite3
from tkinter import ttk, Listbox, Scrollbar


class InventoryWindow(Toplevel):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\paule\OneDrive\Desktop\build\build\assets\frame0")
        
        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)
        
        self.geometry("800x500")
        self.configure(bg="#F6F6F6")

        self.title("VIEW INVENTORY")       


        self.canvas = Canvas(
            self,
            bg="#BEBAB4",
            height=500,
            width=800,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        

        
        self.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        self.categ_sort = Button(
            self.canvas,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat")
        self.categ_sort.place(x=555.0, y=445.0, width=225.0, height=43.0)

             



        self.button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        self.delete_button = Button(
            self.canvas,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat")
        self.delete_button.place(x=19.0,y=445.0,width=225.0,height=43.0)
        



        self.canvas.create_text(
            16.0,
            28.0,
            anchor="nw",
            text="VIEWING ALL INVENTORY",
            fill="#000000",
            font=("Manjari Regular", 20 * -1)
        )

        
        self.search_var = StringVar()
        self.search_entry = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            textvariable=self.search_var
        )
        self.search_entry.place(x=461, y=21, width=300, height=30)
        
        importance_values = fetch_importance_values()

        self.importance_combobox = Combobox(
            self.canvas,
            values=importance_values,  # options for importance
            state="readonly",  # make the combobox read-only
        )
        self.importance_combobox.place(
            x=287,  # x-coordinate
            y=445,  # y-coordinate
            width=200,
            height=43
        )
        self.importance_combobox.set("Select Importance")





        self.mainloop()

def fetch_importance_values():
    conn = sqlite3.connect('Inventory.db')
    cursor = conn.cursor()
    cursor.execute('SELECT importance FROM Inventory')
    values = [item[0] for item in cursor.fetchall()]
    conn.close()
    return values
