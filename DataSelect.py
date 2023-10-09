import tkinter as tk
from tkinter import ttk
import CSV_reader as read
from FileSelect import SideBar


# I want this to create two drop down menus, 
class DropDownSelect:

    file_names: list[str] = []
    file_paths: list[str] = []

    def __init__(self, root: tk.Tk, frame: tk.Frame, side_bar: SideBar):

        self.sidebar = side_bar
        self.sidebar.on_file_selected_callback = self.on_file_selected

        self.selected_file = tk.StringVar()
        self.selected_header = tk.StringVar()

        self.side_bar = side_bar

        self.label = tk.Label(frame, text="Drop Down:", fg="purple")
        self.label.pack()

        # Create a Combobox for files
        self.dropdown_menu_file = ttk.Combobox(frame, textvariable=self.selected_file, values=[])
        self.dropdown_menu_file.pack()

        # Create a Combobox for headers (initially empty, to be updated)
        self.dropdown_menu_headers = ttk.Combobox(frame, textvariable=self.selected_header, values=[])
        self.dropdown_menu_headers.pack()

        # Bind the event to update the files when the dropdown menu is clicked
        self.dropdown_menu_file.bind("<<ComboboxSelected>>", print("selected"))

        # Update the files initially
        # self.update_files()

   # This is a call back from the file selector, when a new file is selected this method is called 
    def on_file_selected(self, side_bar):
        # This method will be called when a file is selected in the sidebar
        print("File selected in Sidebar: Data select")
        updated_file_names = self.side_bar.get_all_files(self)

        # Update the values in the first drop-down menu
        self.dropdown_menu_file['values'] = updated_file_names




        # def dropdown_value_1():
        #     return selected_file.get()

        # def dropdown_value_2():
        #     return selected_header.get()

        # def update_dropdownfiles():
        #     files = side_bar.get_all_files()

        # def updates_dropdownheaders():
        #     return 