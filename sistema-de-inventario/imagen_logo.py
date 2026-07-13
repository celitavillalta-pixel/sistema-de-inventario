
from PIL import Image
import customtkinter
from pathlib import Path

# Obtener ruta dinámica del logo
ruta_logo = Path(__file__).parent / "logo.png"

# Si el logo existe, usarlo; si no, crear un placeholder
try:
    logo = customtkinter.CTkImage(light_image=Image.open(str(ruta_logo)), size=(180, 75))
except (FileNotFoundError, IOError):
    # Crear una imagen placeholder si no existe
    placeholder = Image.new("RGB", (180, 75), color=(0, 191, 254))
    logo = customtkinter.CTkImage(light_image=placeholder, size=(180, 75))  
