from arbol import Nodo  # Importamos la clase Nodo
from Laberinto import laberinto,queso,raton  # Importamos el laberinto
import networkx as nx
import matplotlib.pyplot as plt
import random

def calcular_costo_acumulado(nodo, costo_actual=0):
    """
    Calcula el costo acumulado desde la raíz hasta un nodo.
    """
    return costo_actual + nodo.costo  # Suma el costo del nodo actual al acumulado

def obtener_hojas_con_costos(nodo, costo_acumulado=0):
    """
    Obtiene todas las hojas del árbol y sus costos acumulados.
    """
    hojas = []
    costo_actual = calcular_costo_acumulado(nodo, costo_acumulado)

    if not nodo.hijos:  # Si es una hoja
        hojas.append((nodo, costo_actual))
    else:
        for hijo in nodo.hijos:
            hojas.extend(obtener_hojas_con_costos(hijo, costo_actual))
    return hojas

def obtener_movimientos_validos(pos_actual):
    """
    Devuelve los movimientos válidos desde una posición actual en el laberinto.
    """
    movimientos = []
    x, y = pos_actual

    posibilidades = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]  # Arriba, Abajo, Izquierda, Derecha

    for nx, ny in posibilidades:
        if 0 <= nx < len(laberinto[0]) and 0 <= ny < len(laberinto):  # Dentro de los límites
            if laberinto[ny][nx] == 0:  # Espacio libre
                movimientos.append((nx, ny))
    return movimientos

def costo_uniforme(arbol):
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
    for mov in movimientos:
        nuevo_nodo = Nodo(str(mov), max([nodo.id for nodo, _ in hojas_con_costos]) + 1, 1)
        nuevo_nodo.costo = 1  # Suponemos que cada movimiento tiene un costo de 1
        nodo_a_expandir.agregar_hijo(nuevo_nodo)

    return arbol, False  # Si no es el queso, retornar el árbol y meta como False
"""
# Crear el grafo dirigido
G = nx.DiGraph()

# Función para agregar nodos y aristas
def agregar_aristas(nodo):
    for hijo in nodo.hijos:
        #G.add_edge(nodo.valor, hijo.valor)
        G.add_edge(f"{nodo.valor} ({nodo.id})", f"{hijo.valor} ({hijo.id})")
        agregar_aristas(hijo)



    
    
# Función para asignar posiciones a los nodos de forma jerárquica
def asignar_posiciones(nodo, pos, x=0, y=0, layer=1):
    pos[f"{nodo.valor} ({nodo.id})"] = (x, y)
    numhijos = len(nodo.hijos)
    #factor = [0,0,-0.5,0.5,-1,0,1, -1, -0.5,0.5,1]
    factor = [[0],[-0.5,0.5],[-1,0,1],[-1,-0.3,0.3,1]]
    for i, hijo in enumerate(nodo.hijos):
        #asignar_posiciones(hijo, pos, x + i - (numhijos/2), y - 1, layer + 1)
        y1=(y-1)*-1
        x1 = x+(factor[numhijos-1][i])/(y1*y1)
        asignar_posiciones(hijo, pos, x1, y - 1, layer + 1)

coordenadas = raton
arbol = Nodo("coordenadas", 1,0)  
for _ in range(6): # while meta is False:
    arbol,meta = costo_uniforme(arbol)  # Expande el árbol una vez
    # Asignar posiciones a los nodos comenzando desde la raíz
    pos = {}
    agregar_aristas(arbol)
    asignar_posiciones(arbol, pos)

    # Limpiar la figura anterior
    plt.clf()
    # Dibujar el grafo con posiciones jerárquicas
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color="skyblue", font_size=10, font_weight="bold", arrows=True)
    plt.title(f"Árbol Jerárquico Expansión {(_ + 1)}")
    plt.show()

# Expande el árbol tres veces y dibuja en cada paso
for _ in range(6): # while meta is False:
    control = random.randint(0, 5)
    if control == 0:
        arbol,meta = costo_uniforme(arbol)  # Expande el árbol una vez
        # Asignar posiciones a los nodos comenzando desde la raíz
        pos = {}
        agregar_aristas(arbol)
        asignar_posiciones(arbol, pos)
        
        # Limpiar la figura anterior
        plt.clf()

        # Dibujar el grafo con posiciones jerárquicas
        plt.figure(figsize=(8, 6))
        nx.draw(G, pos, with_labels=True, node_size=1000, node_color="skyblue", font_size=10, font_weight="bold", arrows=True)
        plt.title(f"Árbol Jerárquico Expansión {(_ + 1)}")
        plt.show()
        
        
        
    if control == 1:
        arbol = ffff(arbol)
    arbol = costo_uniforme(arbol)  # Expande el árbol una vez

 """   
