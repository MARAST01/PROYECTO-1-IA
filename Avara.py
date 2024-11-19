from arbol import Nodo  # Importamos la clase Nodo
from Laberinto import laberinto, queso  # Importamos el laberinto

def obtener_hojas_con_heuristica(nodo):
    """
    Obtiene todas las hojas del árbol junto con su valor de heurística.
    """
    hojas = []

    if not nodo.hijos:  # Si es una hoja
        hojas.append((nodo, nodo.heuristica))
    else:
        for hijo in nodo.hijos:
            hojas.extend(obtener_hojas_con_heuristica(hijo))
    return hojas

def obtener_movimientos_validos(pos_actual):
    """
    Devuelve los movimientos válidos desde una posición actual en el laberinto.
    """
    movimientos = []
    x, y = pos_actual

    posibilidades = [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]  # Arriba, Derecha, Abajo, Izquierda

    for nx, ny in posibilidades:
        if 0 <= nx < len(laberinto[0]) and 0 <= ny < len(laberinto):  # Dentro de los límites
            if laberinto[ny][nx] == 0:  # Espacio libre
                movimientos.append((nx, ny))
    return movimientos

def calcular_heuristica(pos_actual, meta):
    """
    Calcula la heurística basada en la distancia de Manhattan entre la posición actual y la meta.
    """
    x1, y1 = pos_actual
    x2, y2 = meta
    return abs(x1 - x2) + abs(y1 - y2)  # Distancia de Manhattan

def busqueda_avara(arbol,idn):
    """
    Expande el nodo hoja con menor heurística y actualiza el árbol.
    Si el nodo a expandir tiene las coordenadas del queso, retorna True (meta alcanzada).
    """
    # Obtener todas las hojas con sus valores de heurística
    hojas_con_heuristica = obtener_hojas_con_heuristica(arbol)

    # Encontrar la hoja con menor heurística
    nodo_a_expandir, _ = min(hojas_con_heuristica, key=lambda x: x[1])

    # Obtener la posición del nodo a expandir
    pos_actual = eval(nodo_a_expandir.valor)  # Convertir el string "(x, y)" a una tupla

    # Verificar si el nodo actual tiene las mismas coordenadas que el queso
    if pos_actual == queso:
        return arbol, True  # Si es el queso, retornar el árbol y meta como True

    # Obtener movimientos válidos desde la posición actual
    movimientos = obtener_movimientos_validos(pos_actual)

    # Expandir el nodo añadiendo hijos
    for i, mov in enumerate(movimientos):
        heuristica = calcular_heuristica(mov, queso)
        nuevo_nodo = Nodo(str(mov), idn+i+1, costo=1, heuristica=heuristica)
        nodo_a_expandir.agregar_hijo(nuevo_nodo)

    return arbol, False  # Si no es el queso, retornar el árbol y meta como False
