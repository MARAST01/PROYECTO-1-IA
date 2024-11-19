from arbol import Nodo  # Importamos la clase Nodo
from Laberinto import laberinto, queso  # Importamos el laberinto y la posición del queso


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


def obtener_nodo_hoja_mas_profundo_limite(nodo, limite):
    """
    Obtiene el nodo hoja más profundo dentro del límite de profundidad usando una pila.
    """
    pila = [(nodo, 0)]  # Pila con tuplas de (nodo, profundidad)
    hojas = []

    while pila:
        actual, profundidad = pila.pop()

        if profundidad < limite:  # Solo procesar nodos dentro del límite
            if not actual.hijos:  # Si es hoja
                hojas.append((actual, profundidad))
            else:
                # Iterar sobre los hijos en orden inverso para priorizar los más a la izquierda
                for hijo in reversed(actual.hijos):
                    pila.append((hijo, profundidad + 1))

    # Si hay hojas, devolver la más profunda dentro del límite
    if hojas:
        return max(hojas, key=lambda x: x[1])[0]  # Retorna solo el nodo

    return None  # Si no hay hojas dentro del límite


def profundidad_limitada(arbol, limite,idn):
    """
    Expande el nodo hoja más profundo dentro del límite de profundidad y actualiza el árbol.
    Si el nodo a expandir tiene las coordenadas del queso, retorna True (meta alcanzada).
    """
    # Obtener la hoja más profunda dentro del límite
    nodo_a_expandir = obtener_nodo_hoja_mas_profundo_limite(arbol, limite)
 
    if nodo_a_expandir is None:
        # Si no hay nodos dentro del límite para expandir
        return arbol, False

    # Obtener la posición del nodo a expandir
    pos_actual = eval(nodo_a_expandir.valor)  # Convertir el string "(x, y)" a una tupla

    # Verificar si el nodo actual tiene las mismas coordenadas que el queso
    if pos_actual == queso:
        return arbol, True  # Si es el queso, retornar el árbol y meta como True

    # Obtener movimientos válidos desde la posición actual
    movimientos = obtener_movimientos_validos(pos_actual)

    # Expandir el nodo añadiendo hijos
    for i, mov in enumerate(movimientos, start=1):
        nuevo_nodo = Nodo(
            valor=str(mov),  # La posición como string
            id=idn+i,  # Generar un nuevo ID único basado en el ID más alto
            costo=1,  # Suponemos que cada movimiento tiene un costo de 1
            padre=nodo_a_expandir  # Establecer el nodo padre
        )
        nodo_a_expandir.agregar_hijo(nuevo_nodo) # Añadir el nuevo nodo como hijo

    return arbol, False  # Si no es el queso, retornar el árbol y meta como False

