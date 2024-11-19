from arbol import Nodo  # Importamos la clase Nodo
from Laberinto import laberinto, queso  # Importamos el laberinto

def obtener_nodo_hoja_mas_profundo(nodo):
    """
    Obtiene el nodo hoja más profundo utilizando una pila para simular un recorrido en profundidad,
    con prioridad al nodo más a la izquierda.
    """
    pila = [(nodo, 0)]  # Pila con tuplas de (nodo, profundidad)
    hojas = []

    while pila:
        actual, profundidad = pila.pop()

        if not actual.hijos:  # Si es hoja
            hojas.append((actual, profundidad))
        else:
            # Iterar sobre los hijos en orden inverso para priorizar los más a la izquierda
            for hijo in reversed(actual.hijos):
                pila.append((hijo, profundidad + 1))

    # Encontrar la hoja con mayor profundidad (preferencia por la última en la pila)
    hoja_mas_profunda = max(hojas, key=lambda x: x[1])
    return hoja_mas_profunda[0]  # Retorna solo el nodo

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

def preferente_por_profundidad(arbol,idn):
    """
    Expande el nodo hoja más profundo y actualiza el árbol.
    Si el nodo a expandir tiene las coordenadas del queso, retorna True (meta alcanzada).
    """
    # Obtener la hoja más profunda
    nodo_a_expandir = obtener_nodo_hoja_mas_profundo(arbol)

    # Obtener la posición del nodo a expandir
    pos_actual = eval(nodo_a_expandir.valor)  # Convertir el string "(x, y)" a una tupla

    # Verificar si el nodo actual tiene las mismas coordenadas que el queso
    if pos_actual == queso:
        return arbol, True  # Si es el queso, retornar el árbol y meta como True

    # Obtener movimientos válidos desde la posición actual
    movimientos = obtener_movimientos_validos(pos_actual)

    # Expandir el nodo añadiendo hijos
    for i,mov in enumerate(movimientos):
        nuevo_nodo = Nodo(str(mov), idn+1+i, 1)
        nuevo_nodo.costo = 1  # Suponemos que cada movimiento tiene un costo de 1
        nodo_a_expandir.agregar_hijo(nuevo_nodo)

    return arbol, False  # Si no es el queso, retornar el árbol y meta como False
