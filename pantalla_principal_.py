
import customtkinter
import tkinter as tk 
from imagen_logo import logo
from pantalla_registro_de_produc import registrar_producto 

def principal_keepit(ventana, limpiar_pantalla):
    #espicifcaciones de customtkinter.
    
    limpiar_pantalla()  

    customtkinter.set_appearance_mode("light")  # Modos: "System" (predeterminado), "Dark", "Light"
    customtkinter.set_default_color_theme("blue")  # Temas: "blue" (predeterminado), "green", "dark-blue"
    

    tarjeta_pantalla_principal = customtkinter.CTkFrame(master=ventana, fg_color="white", corner_radius=15)
    tarjeta_pantalla_principal.pack(pady=40, padx=40, fill="both", expand=True)

    #Labels. 
    #logo
    logo_label = customtkinter.CTkLabel(
        master = tarjeta_pantalla_principal,
        image = logo,
        text = ""
    )
    logo_label.pack(pady = 20, padx = 20) 


    ventana.configure(bg_color = "#E0E0E0") 

    #Botones 

    boton_1= customtkinter.CTkButton(
        master=tarjeta_pantalla_principal, 
        text = "Ingresar Producto",
        font= ("Segoe UI", 15, "bold"),
        bg_color="#E0E0E0", 
        fg_color="#00BFFE", 
        width= 250,
        height= 40,
        command=lambda: registrar_producto(tarjeta_pantalla_principal, limpiar_pantalla, logo_label, boton_1, boton_2, boton_3)
        )
    boton_1.pack(pady=20)

    boton_2= customtkinter.CTkButton(
        master=tarjeta_pantalla_principal, 
        text = "Mostrar Inventario", 
        font= ("Segoe UI", 15, "bold"), 
        bg_color= "#E0E0E0",
        fg_color= "#00BFFE",
        width= 250,
        height= 40
        )
    boton_2.pack(pady=20)  

    boton_3 = customtkinter.CTkButton(
        master=tarjeta_pantalla_principal, 
        text = "Eliminar Productos", 
        font = ("Segoe UI", 15, "bold"), 
        bg_color = "#E0E0E0", 
        fg_color = "#00BFFE",
        width = 250,
        height = 40
        )
    boton_3.pack(pady= 20) 
    



    ventana.mainloop()
