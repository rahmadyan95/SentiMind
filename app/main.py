import customtkinter as ctk
from views.GoogleAPIScrapperView import GoogleApiScrapperView
from views.MainPageView import MainPageView

class tkinterApp(ctk.CTk):
    def __init__(self,*args, **kwargs):
        
        super().__init__(*args, **kwargs)
        container = ctk.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (MainPageView,GoogleApiScrapperView):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPageView)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


if __name__ == '__main__' :
    app = tkinterApp()
    app.title('Sentimind')
    app.geometry("1350x788")
    app._set_appearance_mode("light")
    app.resizable(False,False)
    app.mainloop()