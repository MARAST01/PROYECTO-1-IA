from arbol import Nodo
from Laberinto import laberinto, queso  # Importamos el laberinto

def obtener_movimientos_validos(pos_actual):
    """
    Devuelve los movimientos válidos desde una posición actual en el laberinto,
    en el orden de arriba, derecha, abajo, izquierda.
    """
    movimientos = []
    x, y = pos_actual

    # Posibilidades en el orden: arriba, derecha, abajo, izquierda
    posibilidades = [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]  # Arriba, Derecha, Abajo, Izquierda

    # Filtramos las posibilidades que están dentro de los límites y son espacios libres
    for nx, ny in posibilidades:
        if 0 <= nx < len(laberinto[0]) and 0 <= ny < len(laberinto):  # Dentro de los límites
            if laberinto[ny][nx] == 0:  # Espacio libre
                movimientos.append((nx, ny))

    return movimientos

def profundidad(arbol):
    """
    Realiza un movimiento de búsqueda en profundidad para encontrar el queso en el laberinto.
    Devuelve el árbol y True si encuentra el queso, de lo contrario False.
    """
    # Si el nodo actual tiene las coordenadas del queso, hemos encontrado la meta
    if eval(arbol.valor) == queso:
        return arbol, True

    # Obtener los movimientos válidos desde la posición actual
    movimientos = obtener_movimientos_validos(eval(arbol.valor))

    # Si no hay movimientos válidos, retornar el árbol con False
    if not movimientos:
        return arbol, False

    # Expandir el nodo más a la izquierda (el primero en la lista de movimientos)
    mov = movimientos[0]

    # Crear el nuevo nodo hijo con la nueva posición
    nuevo_nodo = Nodo(str(mov), len(arbol.hijos) + 1, 1)
    arbol.agregar_hijo(nuevo_nodo)  # Agregarlo como hijo del nodo actual

    # Verificar si es el queso
    if eval(nuevo_nodo.valor) == queso:
        return arbol, True  # Si es el queso, retornar el árbol y True

    # Si no es queso, expandir el nodo con los movimientos: arriba, derecha, abajo, izquierda
    movimientos_nuevo_nodo = obtener_movimientos_validos(mov)

    for mov_hijo in movimientos_nuevo_nodo:
        # Crear nuevos nodos hijos en el orden deseado: arriba, derecha, abajo, izquierda
        nuevo_nodo_hijo = Nodo(str(mov_hijo), len(nuevo_nodo.hijos) + 1, 1)
        nuevo_nodo.agregar_hijo(nuevo_nodo_hijo)

    # Retornar el árbol con False si no se encontró el queso
    return arbol, False
