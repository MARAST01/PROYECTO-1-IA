desplazamiento = {
    'derecha': (1, 0),
    'izquierda': (-1, 0),
    'arriba': (0, -1),
    'abajo': (0, 1)
}

def movimientoValido(laberinto, nueva_pos):
    """ Verifica si el movimiento es dentro del laberinto y si no hay obstáculo """
    columna, fila = nueva_pos
    return 0 <= columna < len(laberinto[0]) and 0 <= fila < len(laberinto) and laberinto[fila][columna] != 1 