import os
import shutil
import subprocess
import tkinter as tk
from tkinter import ttk

class BiosStyleTreeGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("BIOS-Style Tree GUI")
        self.geometry("800x600")

        # Set BIOS-like colors
        self.configure(bg='#000000')
        self.listbox_bg_color = '#000000'
        self.listbox_fg_color = '#00FF00'
        self.entry_bg_color = '#000000'
        self.entry_fg_color = '#00FF00'
        self.button_bg_color = '#000000'
        self.button_fg_color = '#00FF00'
        self.label_bg_color = '#000000'
        self.label_fg_color = '#FFFFFF'

        # Font configuration
        font = ('Courier', 14)  # You can adjust the font size here

        # Create Listbox for directory structure
        self.listbox = tk.Listbox(self, bg=self.listbox_bg_color, fg=self.listbox_fg_color, selectbackground='#002200', selectforeground=self.listbox_fg_color, font=font)
        self.listbox.pack(expand=tk.YES, fill=tk.BOTH)
        self.listbox.bind("<Up>", self.move_up)
        self.listbox.bind("<Down>", self.move_down)
        self.listbox.bind("<Return>", self.enter_directory)

        # Create Entry for command input
        self.command_entry = tk.Entry(self, bg=self.entry_bg_color, fg=self.entry_fg_color, font=font)
        self.command_entry.pack(pady=10, padx=10, fill=tk.X)
        self.command_entry.bind("<Return>", self.execute_command)

        # Create Refresh Button
        refresh_button = tk.Button(self, text="Refresh", command=self.refresh_listbox, bg=self.button_bg_color, fg=self.button_fg_color, font=font)
        refresh_button.pack(pady=5)

        # Create Label for current directory display
        self.current_directory_label = tk.Label(self, text="Current Directory: " + os.getcwd(), bg=self.label_bg_color, fg=self.label_fg_color, font=font)
        self.current_directory_label.pack(side=tk.BOTTOM, fill=tk.X)

        # Initialize the listbox with the current directory
        self.refresh_listbox()

    def refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        with os.scandir(os.getcwd()) as entries:
            for entry in entries:
                self.listbox.insert(tk.END, entry.name)

        # Update the current directory label
        self.current_directory_label.config(text="Current Directory: " + os.getcwd())

    def move_up(self, event):
        current_selection = self.listbox.curselection()
        if current_selection:
            self.listbox.selection_clear(current_selection[0])
            self.listbox.selection_set(current_selection[0] - 1)
            self.listbox.see(current_selection[0] - 1)

    def move_down(self, event):
        current_selection = self.listbox.curselection()
        if current_selection:
            self.listbox.selection_clear(current_selection[0])
            self.listbox.selection_set(current_selection[0] + 1)
            self.listbox.see(current_selection[0] + 1)

    def enter_directory(self, event):
        current_selection = self.listbox.curselection()
        if current_selection:
            selected_item = self.listbox.get(current_selection[0])
            if os.path.isdir(selected_item):
                os.chdir(selected_item)
                self.refresh_listbox()

    def execute_command(self, event):
        command = self.command_entry.get()
        if command:
            try:
                subprocess.run(command, shell=True)
            except Exception as e:
                print(f"An error occurred: {e}")

        self.refresh_listbox()  # Refresh the listbox after executing the command
        self.command_entry.delete(0, tk.END)

if __name__ == "__main__":
    app = BiosStyleTreeGUI()
    app.mainloop()



