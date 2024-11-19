import customtkinter as ctk
import subprocess

# Configuración inicial
ctk.set_appearance_mode("Dark")  # Modos: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Colores: "blue", "green", "dark-blue"

# Crear ventana principal
app = ctk.CTk()
app.title("Laberinto uwu")
app.geometry("400x600")  # Tamaño de la ventana

# Variables globales para almacenar los valores ingresados
valor_expansion = None
valor_limite_profundidad = None
valor_limite_amplitud = None
valor_limite_iterativa = None

# Título
title_label = ctk.CTkLabel(app, text="Laberinto", font=("Arial", 20, "bold"))
title_label.pack(pady=10)

# Etiquetas y entradas
labelExpansion = ctk.CTkLabel(app, text="Expansión:", font=("Arial", 14))
labelExpansion.pack(pady=5)
numeroExpansion = ctk.CTkEntry(app, placeholder_text="Introduce un número")
numeroExpansion.pack(pady=5, padx=20)

labelLimiteProfundidad = ctk.CTkLabel(app, text="Profundidad Limitada:", font=("Arial", 14))
labelLimiteProfundidad.pack(pady=5)
LimiteProfundiad = ctk.CTkEntry(app, placeholder_text="Introduce un número")
LimiteProfundiad.pack(pady=5, padx=20)

labelLimiteAmplitud = ctk.CTkLabel(app, text="Profundidad Limitada Amplitud:", font=("Arial", 14))
labelLimiteAmplitud.pack(pady=5)
LimiteProfundiadLimiAmpli = ctk.CTkEntry(app, placeholder_text="Introduce un número")
LimiteProfundiadLimiAmpli.pack(pady=5, padx=20)

labelLimiteIterativa = ctk.CTkLabel(app, text="Límite Iterativa:", font=("Arial", 14))
labelLimiteIterativa.pack(pady=5)
Limiteiterativa = ctk.CTkEntry(app, placeholder_text="Introduce un número")
Limiteiterativa.pack(pady=5, padx=20)

# Función para guardar los valores ingresados
def guardar_valores():
    global valor_expansion, valor_limite_profundidad, valor_limite_amplitud, valor_limite_iterativa
    valor_expansion = numeroExpansion.get()
    valor_limite_profundidad = LimiteProfundiad.get()
    valor_limite_amplitud = LimiteProfundiadLimiAmpli.get()
    valor_limite_iterativa = Limiteiterativa.get()
    ctk.CTkMessagebox(title="Guardado", message="Valores guardados correctamente.")

# Función para ejecutar el script en un archivo separado
def ejecutarventanamatrix():
    try:
        subprocess.run(["python", "matrix.py"], check=True)
        ctk.CTkMessagebox(title="Éxito", message="El script se ejecutó correctamente.")
    except subprocess.CalledProcessError as e:
        ctk.CTkMessagebox(title="Error", message=f"Error al ejecutar el script:\n{e}")

# Botón para guardar los valores ingresados
boton_guardar = ctk.CTkButton(app, text="Guardar", command=guardar_valores)
boton_guardar.pack(pady=10)

# Botón para ejecutar el script
modificarmatriz = ctk.CTkButton(app, text="Modificar laberinto", command=ejecutarventanamatrix)
modificarmatriz.pack(pady=20)

boton_ejecutar= ctk.CTkButton(app, text="Ejecutar", command="printholamundo")
boton_ejecutar.pack(pady=20)

# Ejecutar aplicación
app.mainloop()
