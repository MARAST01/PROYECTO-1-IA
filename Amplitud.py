from collections import deque
from Movimientos import desplazamiento, movimientoValido

def preferenteAmplitud(laberinto, raton, queso):
    cola = deque([raton])
    visitados = [raton]
    
    while cola:
        raton = cola.popleft()  # Sacamos el primer elemento de la cola
        if raton == queso:
            print(f"Encontrado el queso en {raton}")
            break
        
        columna, fila = raton
        # Probamos los 4 movimientos posibles
        for movimiento, (dc, df) in desplazamiento.items():
            nueva_pos = (columna + dc, fila + df)
            if movimientoValido(laberinto, nueva_pos) and nueva_pos not in visitados:
                cola.append(nueva_pos)
                visitados.append(nueva_pos)
        
        print(f"Visitados: {visitados}")