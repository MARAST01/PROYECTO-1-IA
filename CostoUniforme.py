from arbol import Nodo  # Importamos la clase Nodo
from Laberinto import laberinto,queso  # Importamos el laberinto

def calcular_costo_acumulado(nodo, costo_actual=0):
    """
    Calcula el costo acumulado desde la raíz hasta un nodo.
    """
    return costo_actual + nodo.costo  # Suma el costo del nodo actual al acumulado (acumula los costos)

def obtener_hojas_con_costos(nodo, costo_acumulado=0):
    """
    Obtiene todas las hojas del árbol y sus costos acumulados.
    """
    hojas = []  #Lista donde se almacenarán nodos hoja junto con sus costos.
    costo_actual = calcular_costo_acumulado(nodo, costo_acumulado) #Llama a "calcular_costo_acumulado" para obtener el costo desde la raíz hasta el nodo actual.

    if not nodo.hijos:  # Si nodo.hijos está vacío, es un nodo hoja. 
        hojas.append((nodo, costo_actual)) # así que se agrega a la lista "hojas" con su costo acumulado.
    else:
        for hijo in nodo.hijos: # Si tiene hijos, se llama recursivamente para cada hijo.
            hojas.extend(obtener_hojas_con_costos(hijo, costo_actual))
    return hojas # Retorna la lista de hojas con sus costos acumulados.

def obtener_movimientos_validos(pos_actual):
    """
    Devuelve los movimientos válidos desde una posición actual en el laberinto.
    """
    movimientos = [] #Lista para almacenar posiciones válidas.
    x, y = pos_actual #Obtiene las coordenadas de la posición actual.

    posibilidades = [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]  # Arriba, Derecha, Abajo, Izquierda

    for nx, ny in posibilidades:
        if 0 <= nx < len(laberinto[0]) and 0 <= ny < len(laberinto):  # Comprueba si (nx, ny) está dentro de los límites del laberinto.
            if laberinto[ny][nx] == 0:  # Verifica que la celda sea espacio libre (0)
                movimientos.append((nx, ny))
    return movimientos

def costo_uniforme(arbol):
    """
    Expande el nodo hoja con menor costo acumulado y actualiza el árbol.
    Si el nodo a expandir tiene las coordenadas del queso, retorna True (meta alcanzada).
    """
    # Llama a obtener_hojas_con_costos para listar hojas y sus costos acumulados.
    hojas_con_costos = obtener_hojas_con_costos(arbol)

    # El nodo hoja con el costo acumulado más bajo usando min
    nodo_a_expandir, _ = min(hojas_con_costos, key=lambda x: x[1]) #key=lambda x: x[1] asegura que min busque el nodo con el menor costo acumulado

    # Obtener la posición del nodo a expandir
    pos_actual = eval(nodo_a_expandir.valor)  # Convertir el string "(x, y)" a una tupla (x, y)

    # Verificar si el nodo actual tiene las mismas coordenadas que el queso
    if pos_actual == queso:
        return arbol, True  # Si es el queso, retornar el árbol y meta como True

    # Obtener movimientos válidos desde la posición actual
    movimientos = obtener_movimientos_validos(pos_actual)

    # Expandir el nodo añadiendo hijos
    for mov in movimientos:
        nuevo_nodo = Nodo(str(mov), max([nodo.id for nodo, _ in hojas_con_costos]) + 1, 1) # Crea un nuevo nodo para cada movimiento.
        nuevo_nodo.costo = 1  # Suponemos que cada movimiento tiene un costo de 1 (costo uniforme)
        nodo_a_expandir.agregar_hijo(nuevo_nodo) #Lo agrega como hijo del nodo a expandir.

    return arbol, False  # Si no es el queso, retornar el árbol y meta como False