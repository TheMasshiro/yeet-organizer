import os
import tkinter
from tkinter import filedialog, messagebox

import customtkinter as ctk

from main import organize


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Yeet Organizer")
        self.set_window_center(450, 220)
        self.resizable(False, False)
        ctk.set_appearance_mode("light")

        self.after(
            201,
            lambda: self.iconphoto(
                True,
                tkinter.PhotoImage(
                    file=os.path.join(os.getcwd(), "assets", "icon.png")
                ),
            ),
        )

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        self.path_button = ctk.CTkButton(
            self, text="Select folder", command=self.select_path
        )
        self.path_button.grid(row=0, column=0, padx=(15, 5), pady=20, sticky="w")

        self.path_entry = ctk.CTkEntry(self, state="disabled")
        self.path_entry.grid(row=0, column=1, padx=(5, 15), pady=20, sticky="ew")

        self.select_label = ctk.CTkLabel(self, text="Select a filetype:")
        self.select_label.grid(row=1, column=0, padx=(15, 5), pady=(0, 20), sticky="w")

        self.selection = ctk.CTkOptionMenu(
            self,
            values=[
                "all",
                "archives",
                "backups",
                "code",
                "configs",
                "databases",
                "documents",
                "ebooks",
                "executables",
                "fonts",
                "images",
                "installers",
                "music",
                "powerpoints",
                "publishers",
                "spreadsheets",
                "subtitles",
                "system files",
                "text files",
                "videos",
                "3d models",
            ],
        )
        self.selection.grid(row=1, column=1, padx=(5, 15), pady=(0, 20), sticky="w")

        self.confirm_button = ctk.CTkButton(
            self, text="Yeet", command=self.open_dialogbox
        )
        self.confirm_button.grid(row=2, column=1, padx=(5, 15), pady=40, sticky="w")

    def open_dialogbox(self):
        folder = self.path_entry.get()
        filetype = self.selection.get()

        if not folder:
            messagebox.showwarning("Missing Folder", "Please select a folder first.")
            return

        confirm = messagebox.askyesno(
            "Confirm Action",
            f"Organize the folder:\n{folder}\n\nWith filetype filter: {filetype}?\n\nContinue?",
        )

        if confirm:
            organize(folder, filetype)
            messagebox.showinfo(
                "Success", "Your files have been organized successfully!"
            )
        else:
            messagebox.showwarning("Cancelled", "Process was cancelled.")

    def select_path(self):
        path_selected = filedialog.askdirectory()
        if path_selected:
            self.path_entry.configure(state="normal")
            self.path_entry.delete(0, "end")
            self.path_entry.insert(0, path_selected)
            self.path_entry.configure(state="disabled")

    def set_window_center(self, width, height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.geometry(f"{width}x{height}+{x}+{y}")


if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    app = App()
    app.mainloop()
