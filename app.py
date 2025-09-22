from tkinter import filedialog

import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.set_window_center()
        self.title("Yeet Organizer")

        self.path_entry = customtkinter.CTkEntry(self, state="disabled")
        self.path_entry.pack(padx=20, pady=20)

        self.path_button = customtkinter.CTkButton(
            self, text="Select folder", command=self.select_path
        )
        self.path_button.pack(padx=20, pady=20)

    def select_path(self):
        path_selected = filedialog.askdirectory()

        if path_selected:
            self.path_entry.delete(0, "end")
            self.path_entry.insert(0, path_selected)

    def set_window_center(self):
        window_height = 600
        window_width = 500
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")


if __name__ == "__main__":
    app = App()
    app.mainloop()
