import customtkinter as ctk
from views.GoogleAPIScrapperView import GoogleApiScrapperView
from views.MainPageView import MainPageView

import customtkinter as ctk
from views.MainPageView import MainPageView
from  views.GoogleAPIScrapperView import GoogleApiScrapperView  # Import the missing view
from views.TokopediaScrapperView import TokopediaScrapperView

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Your App")
        self.geometry("1200x800")

        # Dictionary to hold frames
        self.frames = {}

        container = ctk.CTkFrame(self)
        container.pack(fill="both", expand=True)

        # Register all frames here
        for F in (MainPageView, GoogleApiScrapperView,TokopediaScrapperView):  # Add GoogleApiScrapperView here
            frame = F(container, self)
            self.frames[F.__name__] = frame  # Use class name as the key
            frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.show_frame('TokopediaScrapperView')  # Start with MainPageView

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()



if __name__ == '__main__' :
    app = App()
    app.title('Sentimind')
    app.geometry("1350x788")
    app._set_appearance_mode("light")
    app.resizable(False,False)
    app.mainloop()