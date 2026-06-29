import tkinter as tk 
from tkinter import *
from pantalla_registro_de_produc import registrar_producto 
 

#tamaños de la pantalla en general. 

screen = tk.Tk()
screen.title("Sistema de inventario.")
screen.geometry("700x500")
screen.resizable(True, True)

#Labels. 

label_principal = tk.Label(screen, text= "INVENTARIO", font= ("Helvetica", 25, "bold"), bg= "#E0E0E0") 
label_principal.pack(pady= 20) 

screen.config(bg = "#E0E0E0") 

#Botones 

boton_1= tk.Button(screen, text = "Ingresar Producto", width=20, height=2, font= ("Times New Roman", 15), bg= "#00BFFE", fg= "Black", command = registrar_producto)
boton_1.pack(pady=20)

boton_2= tk.Button(screen, text = "Mostrar Inventario", width=20, height=2, font= ("Times New Roman", 15), bg= "#00BFFE", fg= "Black")
boton_2.pack(pady=20)  

boton_3 = tk.Button(screen, text = "Eliminar Productos", width=20, height=2, font = ("Times New Roman", 15), bg = "#00BFFE", fg = "Black")
boton_3.pack(pady= 20) 



screen.mainloop()
