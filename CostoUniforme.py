import heapq
from VisualizacionArbol import visualizacionArbol
from Movimientos import movimientoValido, desplazamiento

def costoUniforme(laberinto, raton, queso):
    visualizacion = visualizacionArbol()
    cola_prioridad = [(0, raton)]
    costo_minimo = {raton: 0}
    
    while cola_prioridad:
        costo_actual, raton = heapq.heappop(cola_prioridad)
        visualizacion.agregar_nodo(raton)  # Agregar el nodo actual al árbol visual
        
        if raton == queso:
            print(f"Encontrado el queso en {raton} con costo {costo_actual}")
            visualizacion.finalizar()
            return
        
        columna, fila = raton
        for movimiento, (dc, df) in desplazamiento.items():
            nueva_pos = (columna + dc, fila + df)
            nuevo_costo = costo_actual + 1
            
            if movimientoValido(laberinto, nueva_pos) and (nueva_pos not in costo_minimo or nuevo_costo < costo_minimo[nueva_pos]):
                costo_minimo[nueva_pos] = nuevo_costo
                heapq.heappush(cola_prioridad, (nuevo_costo, nueva_pos))
                visualizacion.agregar_nodo(nueva_pos, padre=raton)  # Agregar el nodo y conectar al padre
    
    visualizacion.finalizar()
