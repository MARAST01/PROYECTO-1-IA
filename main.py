import random
import matplotlib.pyplot as plt
import networkx as nx
from arbol import Nodo
from CostoUniforme import costo_uniforme
from Profundidad import preferente_por_profundidad
from Avara import busqueda_avara
from Laberinto import raton  # Importamos las coordenadas iniciales

G = nx.DiGraph()
# Inicializar el árbol con el nodo raíz en la posición del ratón
arbol = Nodo("coordenadas", 1, 0)  # "coordenadas" es un string para identificar el nodo

# Establecer la posición inicial del ratón
arbol.valor = str(raton)  # Asignamos la posición del ratón al nodo raíz



# Función para agregar nodos y aristas
def agregar_aristas(nodo):
    for hijo in nodo.hijos:
        #G.add_edge(nodo.valor, hijo.valor)
        G.add_edge(f"{nodo.valor}\n{nodo.heuristica}\n({nodo.id})", f"{hijo.valor}\n{hijo.heuristica}\n({hijo.id})")
        agregar_aristas(hijo)



    
    
# Función para asignar posiciones a los nodos de forma jerárquica
def asignar_posiciones(nodo, pos, x=0, y=0, layer=1):
    pos[f"{nodo.valor}\n{nodo.heuristica}\n({nodo.id})"] = (x, y)
    numhijos = len(nodo.hijos)
    #factor = [0,0,-0.5,0.5,-1,0,1, -1, -0.5,0.5,1]
    factor = [[0],[-0.5,0.5],[-1,0,1],[-1,-0.3,0.3,1]]
    for i, hijo in enumerate(nodo.hijos):
        #asignar_posiciones(hijo, pos, x + i - (numhijos/2), y - 1, layer + 1)
        y1=(y-1)*-1
        x1 = x+(factor[numhijos-1][i])/(y1*y1)
        asignar_posiciones(hijo, pos, x1, y - 1, layer + 1)
def dibujar_arbol():
    """
    Dibuja el árbol con sus nodos y aristas, mostrando las posiciones jerárquicas.
    
    :param arbol: El árbol que se va a dibujar.
    """
    # Asignar posiciones a los nodos comenzando desde la raíz
    pos = {}
    agregar_aristas(arbol)
    asignar_posiciones(arbol, pos)

    # Dibujar el grafo con posiciones jerárquicas
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color="skyblue", font_size=10, font_weight="bold", arrows=True)
    plt.title(f"Árbol Jerárquico Expansión")
    plt.show()

# Inicializar la variable meta como False
meta = False



# Función para ejecutar la expansión
def ejecutar_expansion():
    global meta, arbol

    # Mientras no se alcance la meta (queso), seguir expandiendo el árbol
    while not meta:
        # Control aleatorio para decidir qué estrategia usar
        control = 2  # Esto puede ser ajustado si decides incorporar aleatoriedad

        # Variable para guardar el árbol actual y el nuevo árbol
        arbol_actual = arbol
        arbol_nuevo = None

        if control == 0:
            arbol_nuevo, meta = costo_uniforme(arbol_actual)  # Expande el árbol una vez
        elif control == 1:
            arbol_nuevo, meta = preferente_por_profundidad(arbol_actual)
        elif control == 2:
            arbol_nuevo, meta = busqueda_avara(arbol_actual)

        # Dibujar el árbol (ya sea el actual o el nuevo, dependiendo de tu implementación)
        dibujar_arbol()

        # Sobrescribir el árbol anterior con el nuevo
        arbol = arbol_nuevo

        # Si se alcanzó la meta, salir del bucle
        if meta:
            break

# Ejecutar la expansión del árbol
ejecutar_expansion()
### dibujar_arbol(arbol, arbol_nuevo)
### organizar la funcion dibujar arbol para el color, tenemos el arbol viejo y el arbol nuevo.