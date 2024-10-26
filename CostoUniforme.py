import heapq
from Movimientos import desplazamiento, movimientoValido

def costoUniforme(laberinto, raton, queso):
    # Cola de prioridad para almacenar (costo acumulado, posición actual)
    cola_prioridad = [(0, raton)]
    # Diccionario para almacenar los costos mínimos para llegar a cada nodo
    costo_minimo = {raton: 0}
    
    while cola_prioridad:
        # Extraemos el nodo con el costo acumulado más bajo
        costo_actual, raton = heapq.heappop(cola_prioridad)
        
        if raton == queso:
            print(f"Encontrado el queso en {raton} con costo {costo_actual}")
            return
        
        columna, fila = raton
        # Probamos los 4 movimientos posibles
        for movimiento, (dc, df) in desplazamiento.items():
            nueva_pos = (columna + dc, fila + df)
            nuevo_costo = costo_actual + 1  # Supongamos que cada movimiento tiene costo 1
            
            # Solo agregamos la nueva posición si es válida y tiene un menor costo acumulado
            if movimientoValido(laberinto, nueva_pos) and (nueva_pos not in costo_minimo or nuevo_costo < costo_minimo[nueva_pos]):
                costo_minimo[nueva_pos] = nuevo_costo
                heapq.heappush(cola_prioridad, (nuevo_costo, nueva_pos))
        
        print(f"Costos acumulados: {costo_minimo}")

