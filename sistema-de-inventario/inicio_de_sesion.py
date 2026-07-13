# Programa de Inicio de Sesion

import customtkinter 
from tkinter import messagebox
from imagen_logo import logo
from pantalla_principal_ import principal_keepit


customtkinter.set_appearance_mode("light") 
customtkinter.set_default_color_theme("blue")  

# colores que voy a usar en todo el programa

color_fondo = "#121212"
color_celeste = "#00BFFE"
color_gris = "#E0E0E0"

archivo_usuarios = "usuarios.txt"

ventana = customtkinter.CTk()
ventana.title("KeepIt")
ventana.geometry("1060x650")
ventana.configure(bg=color_fondo)
ventana.resizable(True, True)

# esta funcion sirve para limpiar todo lo que hay en la pantalla

def limpiar_pantalla():

    for widget in ventana.winfo_children():

        widget.destroy()


# PANTALLA DE LOGIN 

def pantalla_login():

    limpiar_pantalla()

    #PARTE DE DISEÑO.
    
    login_card = customtkinter.CTkFrame(ventana, width=340, height=400, corner_radius=15, bg_color=color_gris, fg_color="white", border_width=1)
    login_card.pack(pady=40, padx=40, fill="both", expand=True)
    login_card.pack_propagate(False) 
    
    titulo = customtkinter.CTkLabel(login_card, text="Iniciar Sesión", font=("Segoe UI", 30, "bold"), bg_color="transparent", text_color=color_celeste)
    titulo.pack(pady=(45, 5))
    
    imagen_logo = customtkinter.CTkLabel(login_card, image=logo, text="")
    imagen_logo.pack(pady=(5, 30))
    
    #LABELS E INPUTS.

    label_user = customtkinter.CTkLabel(login_card, text="Usuario:", font=("Segoe UI", 14), bg_color="transparent", text_color=color_fondo)
    label_user.pack(pady=5)

    entry_user = customtkinter.CTkEntry(login_card, font=("Segoe UI", 14), width= 250, height= 40, placeholder_text="Ingrese su usuario")
    entry_user.pack(pady=5)

    label_pass = customtkinter.CTkLabel(login_card, text="Contraseña:", font=("Segoe UI", 14), bg_color="transparent", text_color=color_fondo)
    label_pass.pack(pady=5)

    entry_pass = customtkinter.CTkEntry(login_card, font=("Segoe UI", 14),width= 250, height= 40, show="*", placeholder_text="Ingrese su contraseña")
    entry_pass.pack(pady=5)

    # funcion para revisar si el usuario existe en el archivo

    def verificar_login():

        usuario = entry_user.get()
        clave = entry_pass.get()

        if usuario == "" or clave == "":

            messagebox.showwarning("Aviso", "Tienes que llenar los dos campos")

            return

        encontrado = False

        try:

            archivo = open(archivo_usuarios, "r", encoding="utf-8")
            lineas = archivo.readlines()

            archivo.close()

        except FileNotFoundError:

            lineas = []

        # aqui uso un bucle para recorrer cada linea del archivo

        for linea in lineas:

            linea = linea.strip()
            datos = linea.split(",")

            if len(datos) == 2:

                user_guardado = datos[0]
                pass_guardado = datos[1]

                if usuario == user_guardado and clave == pass_guardado:

                    encontrado = True

                    break

        # condicional para saber si encontro el usuario o no

        if encontrado == True:

            pantalla_bienvenida(usuario)

        else:

            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    boton_login = customtkinter.CTkButton(login_card, text="Entrar", font=("Segoe UI", 14, "bold"), bg_color=color_gris, fg_color=color_celeste, width= 250, height= 40, command=verificar_login)
    boton_login.pack(pady=20)

    boton_registrar = customtkinter.CTkButton(login_card, text="Crear cuenta", font=("Segoe UI", 14, "bold"), bg_color=color_celeste, fg_color="transparent", width= 250, height= 40, command=pantalla_registro)
    boton_registrar.pack(pady=5)


# PANTALLA DE REGISTRO

def pantalla_registro():

    limpiar_pantalla()
    
    registrar_card = customtkinter.CTkFrame(ventana, width=340, height=400, corner_radius=15, bg_color=color_gris, fg_color="white", border_width=1)
    registrar_card.pack(pady=40, padx=40, fill="both", expand=True)
    registrar_card.pack_propagate(False)
    

    titulo = customtkinter.CTkLabel(registrar_card, text="Crear Cuenta", font=("Segoe UI", 30, "bold"), bg_color="transparent", text_color=color_celeste)
    titulo.pack(pady=50)

    label_user = customtkinter.CTkLabel(registrar_card, text="Nuevo usuario:", font=("Segoe UI", 14), bg_color="transparent", text_color=color_fondo)
    label_user.pack(pady=5)

    entry_user = customtkinter.CTkEntry(registrar_card, font=("Segoe UI", 14), placeholder_text="Ingrese su nuevo usuario", width= 250, height= 40) 
    entry_user.pack(pady=5)

    label_pass = customtkinter.CTkLabel(registrar_card, text="Nueva contraseña:", font=("Segoe UI", 14), bg_color="transparent", text_color=color_fondo)
    label_pass.pack(pady=5)

    entry_pass = customtkinter.CTkEntry(registrar_card, font=("Segoe UI", 14), placeholder_text="Ingrese su nueva contraseña", width= 250, height= 40, show="*")
    entry_pass.pack(pady=5)

    def guardar_usuario():

        usuario_nuevo = entry_user.get()
        clave_nueva = entry_pass.get()

        if usuario_nuevo == "" or clave_nueva == "":

            messagebox.showwarning("Aviso", "Llena los dos campos porfa")

            return

        # reviso con un bucle si el usuario ya existe antes de guardarlo

        try:

            archivo = open(archivo_usuarios, "r", encoding="utf-8")
            lineas = archivo.readlines()

            archivo.close()

        except FileNotFoundError:

            lineas = []

        ya_existe = False

        for linea in lineas:

            linea = linea.strip()
            datos = linea.split(",")

            if len(datos) == 2:

                if datos[0] == usuario_nuevo:

                    ya_existe = True

        if ya_existe == True:

            messagebox.showerror("Error", "Ese usuario ya existe, elige otro")

        else:

            archivo = open(archivo_usuarios, "a", encoding="utf-8")
            archivo.write(usuario_nuevo + "," + clave_nueva + "\n")

            archivo.close()

            messagebox.showinfo("Listo", "Cuenta creada, ya puedes iniciar sesión")

            pantalla_login()

    boton_guardar = customtkinter.CTkButton(registrar_card, text="Registrarse", font=("Segoe UI", 14, "bold"), bg_color=color_gris, fg_color=color_celeste, width= 250, height= 40, command=guardar_usuario)
    boton_guardar.pack(pady=20)

    boton_volver = customtkinter.CTkButton(registrar_card, text="Volver", font=("Segoe UI", 14, "bold"), bg_color=color_gris, fg_color=color_celeste, width= 250, height= 40, command=pantalla_login)
    boton_volver.pack(pady=5)


# PANTALLA DE BIENVENIDA (cuando ya iniciaste sesion)

def pantalla_bienvenida(nombre_usuario):

    limpiar_pantalla()
    
    #Diseño.
    
    welcome_card = customtkinter.CTkFrame(ventana, width=340, height=400, corner_radius=15, bg_color=color_gris, fg_color="white", border_width=1)
    welcome_card.pack(pady=40, padx=40, fill="both", expand=True)
    welcome_card.pack_propagate(False)

    titulo = customtkinter.CTkLabel(welcome_card, text="¡Bienvenido/a " + nombre_usuario + "!", font=("Segoe UI", 28, "bold"), bg_color="transparent", text_color=color_celeste)
    titulo.pack(pady=100)

    mensaje = customtkinter.CTkLabel(welcome_card, text="Iniciaste sesión correctamente\n y tus credenciales han sido guardadas", font=("Segoe UI", 14, "bold"), bg_color="transparent", text_color=color_fondo)
    mensaje.pack(pady=20)

    boton_entendido = customtkinter.CTkButton(welcome_card, text="Entendido", font=("Segoe UI", 14, "bold"), bg_color=color_gris, fg_color=color_celeste, width= 250, height= 40, command=lambda: principal_keepit(ventana, limpiar_pantalla))
    boton_entendido.pack(pady=50)



# aqui empieza el programa, mostrando primero el login

pantalla_login()

ventana.mainloop()
