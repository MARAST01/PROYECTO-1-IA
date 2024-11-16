<<<<<<< HEAD
from collections import deque
from VisualizacionArbol import VisualizacionArbol  # Visualización del árbol (asegúrate de implementarla)
from Movimientos import movimientoValido  # Comprueba si un movimiento es válido

def preferenteAmplitud(laberinto, raton, queso):
    visualizacion = VisualizacionArbol()  # Creamos la visualización del árbol
    cola = deque([raton])  # Cola para BFS, iniciamos con la posición del ratón
    visitados = set([raton])  # Usamos un conjunto para registrar posiciones visitadas
    padres = {raton: None}  # Diccionario para llevar el seguimiento de los padres de cada nodo
=======
from arbol import Nodo  # Importamos la clase Nodo
from Laberinto import laberinto  # Importamos el laberinto
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque  # Para manejar la cola de nodos

# Contador global para asignar identificadores únicos
contador_id = 1
>>>>>>> 7df7d07964fe293c0b7bd663fc26e5567cec48a5

def obtener_movimientos_validos(pos_actual):
    """
    Devuelve los movimientos válidos desde una posición actual en el laberinto.
    """
    movimientos = []
    x, y = pos_actual
    posibilidades = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]  # Arriba, Derecha, Abajo, Izquierda

<<<<<<< HEAD
        # Verificar si hemos llegado al queso
        if raton == (3,2):
            print(f"¡Encontrado el queso en {raton}! ")
            visualizacion.finalizar()  # Finalizamos la visualización
            return
        
        columna, fila = raton
        # Orden de exploración de los 4 movimientos: antihorario (izquierda, abajo, derecha, arriba)
        movimientos = [
            ('izquierda', (0, -1)),
            ('abajo', (1, 0)),
            ('derecha', (0, 1)),
            ('arriba', (-1, 0))
        ]
        
        # Probar cada movimiento en el orden deseado
        for movimiento, (dc, df) in movimientos:
            nueva_pos = (columna + dc, fila + df)
            if movimientoValido(laberinto, nueva_pos) and nueva_pos not in visitados:
                cola.append(nueva_pos)
                visitados.add(nueva_pos)
                padres[nueva_pos] = raton  # Guardamos el padre de la nueva posición
    
    print("No se encontró el queso en el laberinto.")
    visualizacion.finalizar()  # Finalizamos la visualización si no se encuentra el queso
=======
    for nx, ny in posibilidades:
        if 0 <= nx < len(laberinto[0]) and 0 <= ny < len(laberinto):  # Dentro de los límites
            if laberinto[ny][nx] == 0:  # Espacio libre
                movimientos.append((nx, ny))
    return movimientos

def busqueda_amplitud_iterativa(arbol, cola, visitados):
    """
    Expande un nodo a la vez usando Búsqueda en Amplitud.
    """
    global contador_id

    if not cola:
        cola.append(arbol)  # Inicia con la raíz si la cola está vacía

    # Tomar el nodo más antiguo de la cola
    nodo_actual = cola.popleft()
    pos_actual = eval(nodo_actual.valor)  # Convertir el string "(x, y)" a una tupla

    # Evitar ciclos revisando si ya fue visitado
    if nodo_actual.valor in visitados:
        return arbol

    visitados.add(nodo_actual.valor)

    # Obtener movimientos válidos desde la posición actual
    movimientos = obtener_movimientos_validos(pos_actual)

    # Expandir el nodo añadiendo hijos
    for mov in movimientos:
        if str(mov) not in visitados:
            nuevo_nodo = Nodo(str(mov), contador_id, 1)  # Asignar un identificador único
            contador_id += 1  # Incrementar el contador global
            nodo_actual.agregar_hijo(nuevo_nodo)
            cola.append(nuevo_nodo)  # Añadir a la cola para futuras expansiones

    return arbol

# Crear el grafo dirigido
G = nx.DiGraph()

# Función para agregar nodos y aristas
def agregar_aristas(nodo):
    for hijo in nodo.hijos:
        G.add_edge(f"{nodo.valor} ({nodo.id})", f"{hijo.valor} ({hijo.id})")
        agregar_aristas(hijo)

# Función para asignar posiciones a los nodos de forma jerárquica
def asignar_posiciones(nodo, pos, x=0, y=0, layer=1):
    pos[f"{nodo.valor} ({nodo.id})"] = (x, y)
    numhijos = len(nodo.hijos)
    factor = [[0], [-0.5, 0.5], [-1, 0, 1], [-1, -0.3, 0.3, 1]]
    for i, hijo in enumerate(nodo.hijos):
        y1 = (y - 1) * -1
        x1 = x + (factor[numhijos - 1][i]) / (y1 * y1)
        asignar_posiciones(hijo, pos, x1, y - 1, layer + 1)

# Crear el árbol inicial con el nodo raíz
arbol = Nodo("(0,2)", contador_id, 0)
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

    # Limpiar la figura anterior
    plt.clf()

    # Dibujar el grafo con posiciones jerárquicas
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color="skyblue", font_size=10, font_weight="bold", arrows=True)
    plt.title(f"Árbol Jerárquico Expansión {(_ + 1)}")
    plt.show()
>>>>>>> 7df7d07964fe293c0b7bd663fc26e5567cec48a5
