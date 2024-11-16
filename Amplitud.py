from collections import deque
from VisualizacionArbol import VisualizacionArbol  # Visualización del árbol (asegúrate de implementarla)
from Movimientos import movimientoValido  # Comprueba si un movimiento es válido

def preferenteAmplitud(laberinto, raton, queso):
    visualizacion = VisualizacionArbol()  # Creamos la visualización del árbol
    cola = deque([raton])  # Cola para BFS, iniciamos con la posición del ratón
    visitados = set([raton])  # Usamos un conjunto para registrar posiciones visitadas
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
        if raton == (3,2):
            print(f"¡Encontrado el queso en {raton}! ")
            visualizacion.finalizar()  # Finalizamos la visualización
            return
        
        columna, fila = raton
        # Orden de exploración de los 4 movimientos: antihorario (izquierda, abajo, derecha, arriba)
        movimientos = [
            ('izquierda', (0, -1)),
            ('abajo', (1, 0)),
            ('derecha', (0, 1)),
            ('arriba', (-1, 0))
        ]
        
        # Probar cada movimiento en el orden deseado
        for movimiento, (dc, df) in movimientos:
            nueva_pos = (columna + dc, fila + df)
            if movimientoValido(laberinto, nueva_pos) and nueva_pos not in visitados:
                cola.append(nueva_pos)
                visitados.add(nueva_pos)
                padres[nueva_pos] = raton  # Guardamos el padre de la nueva posición
    
    print("No se encontró el queso en el laberinto.")
    visualizacion.finalizar()  # Finalizamos la visualización si no se encuentra el queso
