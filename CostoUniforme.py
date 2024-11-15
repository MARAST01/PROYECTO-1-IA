import heapq
from VisualizacionArbol import VisualizacionArbol  # Asegúrate de que la importación sea correcta
from Movimientos import movimientoValido, desplazamiento

def costoUniforme(laberinto, raton, queso):
    visualizacion = VisualizacionArbol()
    cola_prioridad = [(0, raton)]  # Cola de prioridad con (costo, posición)
    costo_minimo = {raton: 0}  # Costo mínimo para llegar a cada posición
    padres = {raton: None}  # Seguimiento del padre de cada nodo

    while cola_prioridad:
        costo_actual, posicion_actual = heapq.heappop(cola_prioridad)

        # Siempre agregamos el nodo a la visualización, incluso si ya fue visualizado antes
        if padres[posicion_actual] is not None:
            visualizacion.agregar_nodo(posicion_actual, padre=padres[posicion_actual])
        else:
            visualizacion.agregar_nodo(posicion_actual)  # Nodo raíz

        # Verificar si se encontró el queso
        if posicion_actual == queso:
            print(f"¡Encontrado el queso en {posicion_actual} con costo {costo_actual}!")
            visualizacion.finalizar()
            return

        # Expandir los vecinos del nodo actual
        columna, fila = posicion_actual
        for movimiento, (dc, df) in desplazamiento.items():
            nueva_pos = (columna + dc, fila + df)
            nuevo_costo = costo_actual + 1

            # Verificar si el movimiento es válido y si mejora el costo mínimo
            if movimientoValido(laberinto, nueva_pos) and (
                nueva_pos not in costo_minimo or nuevo_costo < costo_minimo[nueva_pos]
            ):
                costo_minimo[nueva_pos] = nuevo_costo

                # Actualizamos el padre en cada nuevo camino encontrado
                padres[nueva_pos] = posicion_actual  # Conectar siempre al nodo actual como padre

                # Empujamos la nueva posición a la cola de prioridad
                heapq.heappush(cola_prioridad, (nuevo_costo, nueva_pos))

    print("No se encontró el queso en el laberinto.")
    visualizacion.finalizar()
