from collections import deque
from arbol import Nodo  # Importamos la clase Nodo
from Laberinto import laberinto, queso  # Importamos el laberinto y la posición del queso

# Contador global para generar IDs únicos
contador_id = 0

def generar_id():
    """
    Genera un ID único incremental.
    """
    global contador_id
    contador_id += 1
    return contador_id

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

def amplitud(arbol):
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
            for mov in movimientos:
                nuevo_nodo = Nodo(
                    valor=str(mov),  # La posición como string
                    id=generar_id(),  # Generar un nuevo ID único
                    costo=nodo_a_expandir.costo + 1,  # Incrementar el costo
                    padre=nodo_a_expandir  # Establecer el nodo padre
                )
                nodo_a_expandir.agregar_hijo(nuevo_nodo)  # Añadir el nuevo nodo como hijo

            return arbol, False  # Nodo expandido, retornar el árbol y meta como False

<<<<<<< HEAD
# Crear el grafo dirigido
G = nx.DiGraph()

# Función para agregar nodos y aristas
def agregar_aristas(nodo):
    for hijo in nodo.hijos:
        # Conexión padre -> hijo
        G.add_edge(f"{nodo.valor} ({nodo.id})", f"{hijo.valor} ({hijo.id})")
        # Conexión hijo -> padre para permitir la representación bidireccional
        G.add_edge(f"{hijo.valor} ({hijo.id})", f"{nodo.valor} ({nodo.id})")
        agregar_aristas(hijo)

# Función para asignar posiciones a los nodos de forma jerárquica
def asignar_posiciones(nodo, pos, x=0, y=0, layer=1):
    pos[f"{nodo.valor} ({nodo.id})"] = (x, y)
    numhijos = len(nodo.hijos)
    factor = [[0], [-0.5, 0.5], [-1, 0, 1], [-1, -0.3, 0.3, 1]]  # Ajusta según el número de hijos
    for i, hijo in enumerate(nodo.hijos):
        y1 = (y - 1) * -1
        x1 = x + (factor[numhijos - 1][i]) / (y1 * y1)
        asignar_posiciones(hijo, pos, x1, y - 1, layer + 1)

# Crear el árbol inicial con el nodo raíz
arbol = Nodo((0, 2), contador_id, 0)  # El valor ahora es una tupla (x, y)
contador_id += 1  # Incrementar el contador para el siguiente nodo
cola = deque()  # Cola para la expansión
visitados = set()  # Conjunto de nodos visitados

# Expande el árbol iterativamente y dibuja en cada paso
for _ in range(10):
    arbol = busqueda_amplitud_iterativa(arbol, cola, visitados)  # Expande un nodo

    # Asignar posiciones a los nodos comenzando desde la raíz
    pos = {}
    G.clear()
    agregar_aristas(arbol)
    asignar_posiciones(arbol, pos)


    # Dibujar el grafo con posiciones jerárquicas
    plt.figure(figsize=(10, 8))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=1000,
        node_color="skyblue",
        font_size=10,
        font_weight="bold",
        arrows=True,
    )
    plt.title(f"Árbol Jerárquico Expansión {(_ + 1)}")
    plt.show()
=======
    return arbol, False  # Si no hay más nodos para expandir, retornar el árbol y meta como False
>>>>>>> a08b1411af3e41058b757865f1f31880a719cabe
