import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from pandas import DataFrame
import os

import CSV_reader as read

# How to invoke SideBar as a class
# First you need to create a frame which will position the sidebar in the GUI.
# After that you create an instance of the Class and assign it to a variable name you must pass in the 
# the parameters self, root, and the frame you just created

# example
# this creates the frame the side bar will go inside
# self.frame = ttk.Frame(self.root, padding="20", style="Blue.TFrame")
# self.frame.pack(fill=tk.Y, expand=False, side=tk.LEFT)

# this will call an instance of the side_bar class that can be accesed later
# side_bar = SideBar(self.root, self.frame)

# get_all_files(self) returns all the selected file names
# get_dataframe(self, files) returns cleaned data frames, you can pass in an array of files or a signle file in an array 
# get_headers(self, files) returns the headers of for the dataframe for the filenames given

class SideBar:

    file_paths: list[str] = []
    file_paths: list[str] = []

    def __init__(self, root: tk.Tk, frame: tk.Frame, on_file_selected_callback):   #the __init__ method is called known as a constructor method it is automaticall invoked when you create an instance of the class it is in
 
        self.label = tk.Label(frame, text="Selected Files:", fg="purple")
        self.label.pack()
        
        self.button_frame = ttk.Frame(frame)
        self.button_frame.pack()
        
        self.file_list = tk.Listbox(frame, selectbackground="yellow")
        self.file_list.pack(fill=tk.Y, expand=True, side=tk.TOP, padx=10, pady=10)
        
        self.open_button = ttk.Button(
            self.button_frame,
            text='Open Files',
            command=self.select_files
        )
        self.open_button.pack(side=tk.LEFT)

        self.on_file_selected_callback = on_file_selected_callback

    def on_file_selected(self):
        event = tk.Event()
        self.on_file_selected_callback()
                
        
    def select_files(self):
        selected_files = []
        column_names = []

        filetypes = (
            ('CSV', '*.csv'),
            ('All files', '*.*')
        )

        filenames = fd.askopenfilenames(
            title='Open files',
            initialdir='/',
            filetypes=filetypes)

        # this creates a pop up dialog showing you what files were added(annoying)
        # showinfo(
        #     title='Selected Files',
        #     message=filenames
        # )

        selected_files.extend(filenames)
        SideBar.file_paths.extend(filenames)
        self.on_file_selected()

        def display_filenames(self, selected_files):
            self.file_list.delete(0, tk.END)
            for filename in selected_files:
                base_filename = os.path.basename(filename)
                self.file_list.insert(tk.END, base_filename)

        display_filenames(self, selected_files)



     # returns all files selected
    def get_all_files(self):
        all_files = [self.file_list.get(idx) for idx in range(self.file_list.size())]
        return all_files
    
    def get_all_filepaths(self):
        return SideBar.file_paths
    
    
        

