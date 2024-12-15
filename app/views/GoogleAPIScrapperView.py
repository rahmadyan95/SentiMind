import customtkinter as ctk

class GoogleApiScrapperView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = ctk.CTkLabel(self, text="This is Page 1")
        label.pack(pady=20, padx=20)



