from collections import deque
from VisualizacionArbol import VisualizacionArbol  # Asegúrate de que la importación sea correcta
from Movimientos import desplazamiento, movimientoValido

def preferenteAmplitud(laberinto, raton, queso):
    visualizacion = VisualizacionArbol()  # Creamos la visualización del árbol
    cola = deque([raton])
    visitados = [raton]
    padres = {raton: None}  # Diccionario para llevar el seguimiento de los padres de cada nodo

    while cola:
        raton = cola.popleft()  # Sacamos el primer elemento de la cola
        
        # Añadir el nodo actual a la visualización
        if padres[raton] is None:  # Nodo raíz
            visualizacion.agregar_nodo(raton)
        else:
            # Añadimos el nodo con su respectivo padre
            visualizacion.agregar_nodo(raton, padre=padres[raton])

        # Verificar si hemos llegado al queso
        if raton == queso:
            print(f"¡Encontrado el queso en {raton}!")
            visualizacion.finalizar()  # Finalizamos la visualización
            return
        
        columna, fila = raton
        # Probamos los 4 movimientos posibles
        for movimiento, (dc, df) in desplazamiento.items():
            nueva_pos = (columna + dc, fila + df)
            if movimientoValido(laberinto, nueva_pos) and nueva_pos not in visitados:
                cola.append(nueva_pos)
                visitados.append(nueva_pos)
                padres[nueva_pos] = raton  # Guardamos el padre de la nueva posición
        
        print(f"Visitados: {visitados}")
    
    print("No se encontró el queso en el laberinto.")
    visualizacion.finalizar()  # Finalizamos la visualización si no se encuentra el queso
