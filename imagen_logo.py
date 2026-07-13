import os 
import customtkinter as ctk 
from PIL import Image
 

ruta = os.path.dirname(__file__)
ruta_final = os.path.join(ruta, "assets", "logo (1).png")
logo = ctk.CTkImage(
    light_image=Image.open(ruta_final),
    dark_image=Image.open(ruta_final),
    size=(180, 75))