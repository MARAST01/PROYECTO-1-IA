from arbol import Nodo  # Importamos la clase Nodo
from Laberinto import laberinto, queso  # Importamos el laberinto

def calcular_costo_acumulado(nodo):
    """
    Calcula el costo acumulado desde la raíz hasta un nodo.
    """
    if nodo.padre is None:  # Si es la raíz, el costo es su propio costo
        return nodo.costo
    else:
        return calcular_costo_acumulado(nodo.padre) + nodo.costo

def obtener_hojas_con_costos(nodo):
    """
    Obtiene todas las hojas del árbol y sus costos acumulados.
    """
    hojas = []

    if not nodo.hijos:  # Si es una hoja
        hojas.append((nodo, calcular_costo_acumulado(nodo)))
    else:
        for hijo in nodo.hijos:
            hojas.extend(obtener_hojas_con_costos(hijo))
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

def costo_uniforme(arbol,idn):
    """
    Expande el nodo hoja con menor costo acumulado y actualiza el árbol.
    Si el nodo a expandir tiene las coordenadas del queso, retorna True (meta alcanzada).
    """
    # Obtener todas las hojas con sus costos acumulados
    hojas_con_costos = obtener_hojas_con_costos(arbol)

    # Encontrar la hoja con menor costo acumulado
    nodo_a_expandir, _ = min(hojas_con_costos, key=lambda x: x[1])

    # Obtener la posición del nodo a expandir
    pos_actual = eval(nodo_a_expandir.valor)  # Convertir el string "(x, y)" a una tupla

    # Verificar si el nodo actual tiene las mismas coordenadas que el queso
    if pos_actual == queso:
        return arbol, True  # Si es el queso, retornar el árbol y meta como True

    # Obtener movimientos válidos desde la posición actual
    movimientos = obtener_movimientos_validos(pos_actual)

    # Expandir el nodo añadiendo hijos
    for i, mov in enumerate(movimientos):
        nuevo_nodo = Nodo(str(mov), idn + i+1, 1)
        nuevo_nodo.costo = nodo_a_expandir.costo + 1  # Costo del padre + 1
        nuevo_nodo.padre = nodo_a_expandir  # Establecer el nodo padre
        nodo_a_expandir.agregar_hijo(nuevo_nodo)

    return arbol, False  # Si no es el queso, retornar el árbol y meta como False
