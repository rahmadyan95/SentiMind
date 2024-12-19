import customtkinter as ctk

class GoogleApiScrapperView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = ctk.CTkLabel(self, text="Google API Scrapper View", font=("Arial", 24))
        label.pack(pady=20, padx=20)
