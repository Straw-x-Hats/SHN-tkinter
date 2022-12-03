import tkinter
import tkinter.messagebox
import customtkinter
import os
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("ImageX")
        self.geometry(f"{1100}x{580}")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Assets")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "imagex.png")), size=(26, 26))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image.png")), size=(20, 20))
        self.removebg_icon = customtkinter.CTkImage(Image.open(os.path.join(image_path, "removebg.png")), size=(20, 20))
        self.blur_icon = customtkinter.CTkImage(Image.open(os.path.join(image_path, "blur.png")), size=(20, 20))
        self.greyscale_icon = customtkinter.CTkImage(Image.open(os.path.join(image_path, "color.png")), size=(20, 20))
        self.invert_icon = customtkinter.CTkImage(Image.open(os.path.join(image_path, "invert.png")), size=(20, 20))
        self.random = customtkinter.CTkImage(Image.open(os.path.join(image_path, "random.jpg")), size=(500, 350))

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="ImageX",image=self.logo_image,
                                                             compound="left",  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 25))

        self.uploadbutton = customtkinter.CTkButton(self.sidebar_frame, text="Upload", image=self.image_icon_image, compound="right")
        self.uploadbutton.grid(row=2, column=0, padx=20, pady=(10, 125))

        self.removebg = customtkinter.CTkButton(self.sidebar_frame, text="RemoveBG", image=self.removebg_icon, compound="right")
        self.removebg.grid(row=3, column=0, padx=20, pady=10)

        self.blur = customtkinter.CTkButton(self.sidebar_frame, text="Blur Image", image=self.blur_icon, compound="right")
        self.blur.grid(row=4, column=0, padx=20, pady=10)

        self.grayscale = customtkinter.CTkButton(self.sidebar_frame, text="Gray Scale", image=self.greyscale_icon, compound="right")
        self.grayscale.grid(row=5, column=0, padx=20, pady=10)

        self.invert = customtkinter.CTkButton(self.sidebar_frame, text="Invert Image", image=self.invert_icon, compound="right")
        self.invert.grid(row=6, column=0, padx=20, pady=10)

        # HOme
        self.Home = customtkinter.CTkFrame(self, corner_radius=0)
        self.Home.grid(row=0, column=1)

        # Random Image Updated
        self.random_image = customtkinter.CTkLabel(self.Home, text="", image=self.random)
        self.random_image.grid(row=0, column=0, padx=20, pady=10)



if __name__ == "__main__":
    app = App()
    app.mainloop()