from tkinter import filedialog

import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.set_window_center()
        self.resizable(False, False)
        self.title("Yeet Organizer")

        self.path_button = customtkinter.CTkButton(
            self, text="Select folder", command=self.select_path
        )
        self.path_button.grid(row=0, column=0, padx=(10, 2), pady=20)
        self.path_entry = customtkinter.CTkEntry(self, state="disabled", width=300)
        self.path_entry.grid(row=0, column=1, padx=(3, 20), pady=20, sticky="ew")

        self.select_label = customtkinter.CTkLabel(self, text="Select a filetype")
        self.select_label.grid(row=1, column=0, padx=(3, 10), pady=20)

        self.selection = customtkinter.CTkOptionMenu(
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
        self.selection.grid(row=1, column=1, padx=(10, 2), pady=20, sticky="w")

    def select_path(self):
        path_selected = filedialog.askdirectory()

        if path_selected:
            self.path_entry.configure(state="normal")
            self.path_entry.delete(0, "end")
            self.path_entry.insert(0, path_selected)
            self.path_entry.configure(state="disabled")

    def set_window_center(self):
        window_height = 250
        window_width = 500
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")


if __name__ == "__main__":
    app = App()
    app.mainloop()
