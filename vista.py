import customtkinter as ctk
import subprocess
import main

# Configuración inicial
ctk.set_appearance_mode("Dark")  # Modos: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Colores: "blue", "green", "dark-blue"

# Crear ventana principal
app = ctk.CTk()
app.title("Laberinto uwu")
app.geometry("400x400")  # Tamaño de la ventana

# Variables globales para almacenar los valores ingresados
valor_expansion = None
valor_limite_profundidad = None

# Título
title_label = ctk.CTkLabel(app, text="Laberinto", font=("Arial", 20, "bold"))
title_label.pack(pady=10)

# Etiquetas y entradas
labelExpansion = ctk.CTkLabel(app, text="Expansión:", font=("Arial", 14))
labelExpansion.pack(pady=5)
numeroExpansion = ctk.CTkEntry(app, placeholder_text="Introduce un número")
numeroExpansion.pack(pady=5, padx=20)

labelLimiteProfundidad = ctk.CTkLabel(app, text="Límite profundidad:", font=("Arial", 14))
labelLimiteProfundidad.pack(pady=5)
LimiteProfundiad = ctk.CTkEntry(app, placeholder_text="Introduce un número")
LimiteProfundiad.pack(pady=5, padx=20)

# Función para guardar los valores ingresados
def guardar_valores():
    global valor_expansion, valor_limite_profundidad
    try:
        # Convertir los valores ingresados a enteros
        valor_expansion = int(numeroExpansion.get())
        valor_limite_profundidad = int(LimiteProfundiad.get())
        
  

        ctk.CTkMessagebox(title="Guardado", message="Valores guardados correctamente.")
    except ValueError:
        ctk.CTkMessagebox(title="Error", message="Por favor, introduce valores numéricos válidos.")

# Función para ejecutar el script en un archivo separado
def ejecutarventanamatrix():
    try:
        subprocess.run(["python", "matrix.py"], check=True)
        ctk.CTkMessagebox(title="Éxito", message="El script se ejecutó correctamente.")
    except subprocess.CalledProcessError as e:
        ctk.CTkMessagebox(title="Error", message=f"Error al ejecutar el script:\n{e}")

# Función para ejecutar la función `ejecutar_expansion` en main
def ejecutar_expansion_main():
    if valor_expansion is not None and valor_limite_profundidad is not None:
        main.ejecutar_expansion(valor_limite_profundidad, valor_expansion)
        ctk.CTkMessagebox(title="Éxito", message="La función ejecutar_expansion se ejecutó correctamente.")
    else:
        ctk.CTkMessagebox(title="Error", message="Por favor, guarda los valores primero.")

# Botón para guardar los valores ingresados
boton_guardar = ctk.CTkButton(app, text="Guardar", command=guardar_valores)
boton_guardar.pack(pady=10)

# Botón para ejecutar el script
modificarmatriz = ctk.CTkButton(app, text="Modificar laberinto", command=ejecutarventanamatrix)
modificarmatriz.pack(pady=20)

# Botón para ejecutar la función en main
boton_ejecutar = ctk.CTkButton(app, text="Ejecutar", command=ejecutar_expansion_main)
boton_ejecutar.pack(pady=20)

# Ejecutar aplicación
app.mainloop()
