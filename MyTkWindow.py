from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import chardet
import numpy as np
from matplotlib.widgets import Slider, Button
from tkinter import *

# ------------- IMPORTED CLASSES FOR GUI -----------------

from DataSelect import *
from FileSelect import SideBar
from Graphing import *

# ------------- IMPORTED FUNCTIONS -----------------

import CSV_reader as read
import Graphing as graph


class MyTkWindow:
    def __init__(self):
        # ------------- BASIC APP LAYOUT -----------------
        
        # Makes the window
        self.root = Tk() 

        # Sets the size of the window equal to the screen 
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Setting some stylistic elements for the GUI and making it dynamic for use by all computers
        self.style = ttk.Style()
        self.style.configure("Blue.TFrame", background='#c0a98e')# we can use these style elements to make things colourful
        self.root.geometry(f"{screen_width}x{screen_height}")
        self.root.title("How the Fucj do I code")
        self.root.config(background="#d2e7ca")
        
		# ------------- FILE SELECTION SIDE BAR -----------------
        
        self.frame = ttk.Frame(self.root, padding="20", style="Blue.TFrame")
        self.frame.pack(fill=tk.Y, expand=False, side=tk.LEFT)
        side_bar = SideBar(self.root, self.frame, self.on_file_selected_callback)

        # self.root.tk_setPalette(background='#FFD700')  # Set the background color to gold

        # # Create a custom style
        self.root.style = ttk.Style()
        self.root.style.configure('Custom.TFrame', background='#FFD700')

        # temp code, this can be done directly in the command for a button
        def d():
            all_files = side_bar.get_all_filepaths()
            print(all_files)

        def c():
            df = read.get_dataframes(self, side_bar.get_all_filepaths())
            print(df)

        def e():
            file = side_bar.get_all_filepaths()
            print(file)
            print(read.get_headers(self, file))

        # ------------- DATA SELCTION AREA ----------------------

        # data_select = Dropdown(self.root)
        # data_select = Dropdown(self.root)

        self.button_frame = ttk.Frame(self.root, padding ="10")
        self.button_frame.pack(fill=tk.Y, expand=False, side=tk.LEFT)

        drop_down = DropDownSelect(self.root,self.button_frame,side_bar)

    def on_file_selected_callback(self):
        print("File selected in SideBar")

    def start(self):
        self.root.mainloop()  # Start monitoring and updating the GUI
	

class MyDataProcessor:
    def __init__(self, master, column_names):
        self.master = master
        self.column_names = column_names

        self.label = ttk.Label(master, text="Select an option:")
        self.label.pack()

        self.selected_option = tk.StringVar()
        self.dropdown_menu = ttk.Combobox(master, textvariable=self.selected_option, values=self.column_names)
        self.dropdown_menu.pack()

    def get_selected_option(self):
        return self.selected_option.get()



        # self.open_button = ttk.Button(
        #     self.button_frame,
        #     text='Open Files',
        #     command=d
        # )
        # self.open_button.pack(side=tk.LEFT)

        # self.open_button = ttk.Button(
        #     self.button_frame,
        #     text='coloum headers',
        #     command=e
        # )
        # self.open_button.pack(side=tk.LEFT)



        # self.open_button = ttk.Button(
        #     self.button_frame,
        #     text='print data',
        #     command=c
        # )
        # self.open_button.pack(side=tk.LEFT)