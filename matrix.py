import customtkinter as ctk
import tkinter as tk
import importlib.util

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class MatrixEditorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Editor de Matriz")
        self.geometry("500x500")

        # Cargar valores iniciales desde el archivo Laberinto.py
        self.load_labyrinth()

        # Etiquetas y entradas para el tamaño de la matriz
        self.rows_label = ctk.CTkLabel(self, text="Número de filas:")
        self.rows_label.pack(pady=5)
        self.rows_entry = ctk.CTkEntry(self, placeholder_text="Ejemplo: 5")
        self.rows_entry.pack(pady=5)

        self.cols_label = ctk.CTkLabel(self, text="Número de columnas:")
        self.cols_label.pack(pady=5)
        self.cols_entry = ctk.CTkEntry(self, placeholder_text="Ejemplo: 5")
        self.cols_entry.pack(pady=5)

        # Botón para actualizar el tamaño de la matriz
        self.update_button = ctk.CTkButton(self, text="Actualizar Matriz", command=self.update_matrix_size)
        self.update_button.pack(pady=10)

        # Botón para editar la matriz
        self.edit_button = ctk.CTkButton(self, text="Editar Matriz", command=self.open_matrix_editor)
        self.edit_button.pack(pady=10)

        # Botones para seleccionar el ratón y el queso
        self.select_raton_button = ctk.CTkButton(self, text="Seleccionar Ratón", command=self.set_raton)
        self.select_raton_button.pack(pady=10)

        self.select_queso_button = ctk.CTkButton(self, text="Seleccionar Queso", command=self.set_queso)
        self.select_queso_button.pack(pady=10)

        # Botón para guardar la matriz
        self.save_button = ctk.CTkButton(self, text="Guardar Matriz", command=self.save_matrix_to_file)
        self.save_button.pack(pady=10)

    def load_labyrinth(self):
        """Carga la matriz y las posiciones del ratón y queso desde el archivo Laberinto.py."""
        try:
            spec = importlib.util.spec_from_file_location("Laberinto", "Laberinto.py")
            lab_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(lab_module)

            self.matrix = lab_module.laberinto
            self.raton = lab_module.raton
            self.queso = lab_module.queso
        except (FileNotFoundError, AttributeError):
            self.matrix = [[0 for _ in range(5)] for _ in range(5)]  # Matriz predeterminada (5x5)
            self.raton = None
            self.queso = None

    def update_matrix_size(self):
        """Actualiza el tamaño de la matriz según las entradas."""
        try:
            rows = int(self.rows_entry.get())
            cols = int(self.cols_entry.get())
            if rows > 0 and cols > 0:
                self.matrix = [[0 for _ in range(cols)] for _ in range(rows)]
                ctk.CTkMessagebox.show_info("Éxito", f"Tamaño de la matriz actualizado a {cols}x{rows}.")
            else:
                ctk.CTkMessagebox.show_error("Error", "Las dimensiones deben ser mayores a 0.")
        except ValueError:
            ctk.CTkMessagebox.show_error("Error", "Por favor ingresa valores numéricos válidos.")

    def open_matrix_editor(self):
        """Abre una ventana emergente para editar la matriz."""
        editor = MatrixEditorPopup(self, self.matrix)
        editor.grab_set()

    def set_raton(self):
        """Abre una ventana para seleccionar la posición del ratón."""
        selector = RatonQuesoPopup(self, self.matrix, mode="raton")
        selector.grab_set()

    def set_queso(self):
        """Abre una ventana para seleccionar la posición del queso."""
        selector = RatonQuesoPopup(self, self.matrix, mode="queso")
        selector.grab_set()

    def save_matrix_to_file(self):
        """Guarda la matriz y las posiciones en el archivo Laberinto.py."""
        try:
            with open("Laberinto.py", "w") as file:
                file.write("# Archivo generado automáticamente\n")
                file.write("laberinto = [\n")
                for row in self.matrix:
                    file.write(f"    {row},\n")
                file.write("]\n")
                if self.raton is not None:
                    file.write(f"raton = {self.raton}\n")
                if self.queso is not None:
                    file.write(f"queso = {self.queso}\n")
            ctk.CTkMessagebox.show_info("Guardado", "La matriz y las posiciones se han guardado en 'Laberinto.py'.")
        except Exception as e:
            ctk.CTkMessagebox.show_error("Error", f"No se pudo guardar la matriz: {str(e)}")


class MatrixEditorPopup(ctk.CTkToplevel):
    def __init__(self, parent, matrix):
        super().__init__(parent)
        self.title("Editor de Matriz")
        self.geometry("600x400")

        self.parent = parent
        self.matrix = matrix
        self.buttons = []

        self.create_matrix_grid()
        save_button = ctk.CTkButton(self, text="Guardar Cambios", command=self.save_changes)
        save_button.pack(pady=10)

    def create_matrix_grid(self):
        """Crea una cuadrícula de botones para la matriz."""
        for widget in self.winfo_children():
            widget.destroy()

        self.buttons = []
        for i, row in enumerate(self.matrix):
            button_row = []
            for j, value in enumerate(row):
                btn = ctk.CTkButton(
                    self,
                    text=str(value),
                    width=40,
                    height=40,
                    command=lambda i=i, j=j: self.toggle_cell(i, j),
                )
                btn.grid(row=i, column=j, padx=2, pady=2)
                button_row.append(btn)
            self.buttons.append(button_row)

    def toggle_cell(self, i, j):
        """Alterna el valor de una celda entre 0 y 1."""
        self.matrix[i][j] = 1 if self.matrix[i][j] == 0 else 0
        self.buttons[i][j].configure(text=str(self.matrix[i][j]))

    def save_changes(self):
        """Guarda los cambios en la matriz y cierra el editor."""
        self.parent.matrix = self.matrix
        ctk.CTkMessagebox.show_info("Guardado", "Los cambios en la matriz han sido guardados.")
        self.destroy()


class RatonQuesoPopup(ctk.CTkToplevel):
    def __init__(self, parent, matrix, mode):
        super().__init__(parent)
        self.title(f"Seleccionar {'Ratón' if mode == 'raton' else 'Queso'}")
        self.geometry("600x400")

        self.parent = parent
        self.matrix = matrix
        self.mode = mode  # Modo: "raton" o "queso"

        self.grid_frame = ctk.CTkFrame(self)
        self.grid_frame.pack(pady=10)

        self.create_selection_grid()

    def create_selection_grid(self):
        """Crea una cuadrícula para seleccionar las posiciones del ratón o el queso."""
        for j, row in enumerate(self.matrix):
            for i, _ in enumerate(row):  # Iterar como columna, fila
                btn = ctk.CTkButton(
                    self.grid_frame,
                    text=f"({i},{j})",
                    width=40,
                    height=40,
                    command=lambda i=i, j=j: self.select_position(i, j),
                )
                btn.grid(row=j, column=i, padx=2, pady=2)

    def select_position(self, i, j):
        """Selecciona la posición del ratón o del queso y cambia el color."""
        if self.mode == "raton":
            self.parent.raton = (i, j)  # Guardar como columna, fila
            ctk.CTkMessagebox.show_info("Seleccionado", f"Ratón seleccionado en ({i}, {j}).")
            self.matrix[j][i] = 2  # Código opcional para indicar el ratón
        elif self.mode == "queso":
            self.parent.queso = (i, j)  # Guardar como columna, fila
            ctk.CTkMessagebox.show_info("Seleccionado", f"Queso seleccionado en ({i}, {j}).")
            self.matrix[j][i] = 3  # Código opcional para indicar el queso
        self.destroy()


if __name__ == "__main__":
    app = MatrixEditorApp()
    app.mainloop()
