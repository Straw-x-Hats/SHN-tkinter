import tkinter
import tkinter.messagebox
import customtkinter
import os
from PIL import Image

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("ImageX")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # load images
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Assets")
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image.png")), size=(20, 20))

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="ImageX", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.uploadbutton = customtkinter.CTkButton(self.sidebar_frame, text="Upload", image=self.image_icon_image, compound="right")
        self.uploadbutton.grid(row=2, column=0, padx=20, pady=10)

        self.removebg = customtkinter.CTkButton(self.sidebar_frame, text="RemoveBG", image=self.image_icon_image, compound="right")
        self.removebg.grid(row=3, column=0, padx=20, pady=10)

        self.blur = customtkinter.CTkButton(self.sidebar_frame, text="Blur Image", image=self.image_icon_image, compound="right")
        self.blur.grid(row=4, column=0, padx=20, pady=10)

        self.grayscale = customtkinter.CTkButton(self.sidebar_frame, text="Gray Scale", image=self.image_icon_image, compound="right")
        self.grayscale.grid(row=5, column=0, padx=20, pady=10)

        self.invert = customtkinter.CTkButton(self.sidebar_frame, text="Invert", image=self.image_icon_image, compound="right")
        self.invert.grid(row=6, column=0, padx=20, pady=10)



if __name__ == "__main__":
    app = App()
    app.mainloop()