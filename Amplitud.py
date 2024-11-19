from collections import deque
from arbol import Nodo  # Importamos la clase Nodo
from Laberinto import laberinto, queso  # Importamos el laberinto y la posición del queso

# Contador global para generar IDs únicos



def obtener_movimientos_validos(pos_actual):
    """
    Devuelve los movimientos válidos desde una posición actual en el laberinto.
    """
    movimientos = []
    x, y = pos_actual

    # Definir los posibles movimientos: Arriba, Derecha, Abajo, Izquierda
    posibilidades = [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]

    for nx, ny in posibilidades:
        if 0 <= nx < len(laberinto[0]) and 0 <= ny < len(laberinto):  # Dentro de los límites
            if laberinto[ny][nx] == 0:  # Espacio libre
                movimientos.append((nx, ny))
    return movimientos

def es_meta(pos_actual):
    """
    Verifica si una posición actual es la meta (el queso).
    """
    return pos_actual == queso

def amplitud(arbol,idn):
    """
    Expande un solo nodo según la lógica de búsqueda preferente por amplitud.
    Si el nodo expandido tiene las coordenadas del queso, retorna el árbol y True (meta alcanzada).
    Si no, retorna el árbol y False.
    """
    # Crear una cola temporal para buscar el siguiente nodo a expandir
    cola = deque([arbol])  # Inicialmente, el nodo raíz está en la cola

    # Realizar un recorrido por nivel para encontrar el siguiente nodo no expandido
    while cola:
        nodo_a_expandir = cola.popleft()

        # Verificar si el nodo actual es la meta
        pos_actual = eval(nodo_a_expandir.valor)  # Convertir el string "(x, y)" a una tupla
        if es_meta(pos_actual):
            return arbol, True  # Meta alcanzada

        # Si el nodo ya tiene hijos, agregar los hijos a la cola
        if nodo_a_expandir.hijos:
            cola.extend(nodo_a_expandir.hijos)
        else:
            # Nodo encontrado para expandir
            movimientos = obtener_movimientos_validos(pos_actual)

            # Crear hijos para cada movimiento válido
            for i, mov in enumerate(movimientos):
                nuevo_nodo = Nodo(
                    valor=str(mov),  # La posición como string
                    id=idn+i+1,  # Generar un nuevo ID único
                    costo=nodo_a_expandir.costo + 1,  # Incrementar el costo
                    padre=nodo_a_expandir  # Establecer el nodo padre
                )
                nodo_a_expandir.agregar_hijo(nuevo_nodo)  # Añadir el nuevo nodo como hijo

            return arbol, False  # Nodo expandido, retornar el árbol y meta como False

    return arbol, False  # Si no hay más nodos para expandir, retornar el árbol y meta como False
