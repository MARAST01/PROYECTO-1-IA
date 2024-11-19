import random
import matplotlib.pyplot as plt
import networkx as nx
from arbol import Nodo
from CostoUniforme import costo_uniforme
from Profundidad import preferente_por_profundidad
from Avara import busqueda_avara
from Amplitud import amplitud
from LimitadaProfundidad import profundidad_limitada
from Laberinto import raton  # Importamos las coordenadas iniciales


def contar_nodos(raiz):
    if raiz is None:
        return 0
    # Contar el nodo actual
    total = 1  
    # Recorrer los hijos y sumar sus nodos
    for hijo in raiz.hijos:
        total += contar_nodos(hijo)
    return total


def hojas_misma_profundidad(nodo):
    def dfs(nodo, profundidad, profundidades):
        # Si el nodo no tiene hijos, es una hoja
        if not nodo.hijos:
            profundidades.add(profundidad)
            # Si hay más de un nivel de profundidad, no pueden estar al mismo nivel
            if len(profundidades) > 1:
                return False
        else:
            # Recorrer los hijos del nodo
            for hijo in nodo.hijos:
                if not dfs(hijo, profundidad + 1, profundidades):
                    return False
        return True
    
    # Usamos un conjunto para almacenar las profundidades únicas
    profundidades = set()
    return dfs(nodo, 0, profundidades)


G = nx.DiGraph()
# Inicializar el árbol con el nodo raíz en la posición del ratón
arbol = Nodo("coordenadas", 1, 0)  # "coordenadas" es un string para identificar el nodo

# Establecer la posición inicial del ratón
arbol.valor = str(raton)  # Asignamos la posición del ratón al nodo raíz
"""
arbol = Nodo("(0,2)", 1, 0)  # Nodo raíz con coordenada (0, 2), id=1 y costo=0

# Crear los h"ijos del nodo raíz
hijo1 = Nodo("(0,1)", 1, 5)  # Primer hijo con coordenada (1, 2), id=2 y costo=5
hijo2 = Nodo("(0,3)", 1, 6)  # Segundo hijo con coordenada (0, 3), id=3 y costo=6


hijo1.agregar_hijo(Nodo("(0,2)", 2, 3))  # Agregar un hijo al primer hijo
#hijo1.agregar_hijo(Nodo("(0,0)", 3, 4))  # Agregar otro hijo al primer hijo
# Agregar los hijos al nodo raíz
arbol.agregar_hijo(hijo1)
arbol.agregar_hijo(hijo2)

#"""

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

idn = 0  # ID para los nodos
limite = 4  # Límite de profundidad para la búsqueda limitada
numero_expansion = 1
def altura_arbol(nodo):
    """
    Calcula la altura de un árbol recursivamente.
    
    :param nodo: Nodo raíz del árbol.
    :return: Altura del árbol (profundidad máxima desde la raíz hasta una hoja).
    """
    if not nodo.hijos:  # Si el nodo no tiene hijos, es una hoja
        return 1
    else:
        # La altura es 1 (este nodo) más la mayor altura entre sus hijos
        return 1 + max(altura_arbol(hijo) for hijo in nodo.hijos)


# Función para ejecutar la expansión
def ejecutar_expansion():
    global meta, arbol,idn,limite
    # Crear una lista de controles (0 a 5)
    #controles_disponibles = [0, 1, 2, 3, 4, 5]
    #control = random.choice(controles_disponibles)
    #controles_disponibles.remove(control)


    # Mientras no se alcance la meta (queso), seguir expandiendo el árbol
    while not meta: #and controles_disponibles:
        idn = contar_nodos(arbol)
        # Control aleatorio para decidir qué estrategia usar
        control = 4 # Esto puede ser ajustado si decides incorporar aleatoriedad
        #control = random.randint(0, 5)

        # Variable para guardar el árbol actual y el nuevo árbol
        arbol_actual = arbol
        arbol_nuevo = None

        if control == 0:
            arbol_nuevo, meta = costo_uniforme(arbol_actual,idn)  # Expande el árbol una ve
            print ("costo uniforme")
            dibujar_arbol()
        elif control == 1:
            arbol_nuevo, meta = preferente_por_profundidad(arbol_actual,idn)
            print("profundidad")
            dibujar_arbol()
        elif control == 2:
            arbol_nuevo, meta = busqueda_avara(arbol_actual,idn)
            print("avara")
            dibujar_arbol()
        elif control == 3:
            arbol_nuevo, meta = amplitud(arbol_actual,idn)
            print("amplitud")
            dibujar_arbol()
        #limitada por profundidad
        elif control == 4:
            arbol_nuevo, meta = profundidad_limitada(arbol_actual,limite,idn)
            print("limitada")
            dibujar_arbol()
            
        elif control == 6:
            print("limitada")
            for i in range(0, limite ):
                arbol_nuevo, meta = preferente_por_profundidad(arbol_actual,idn)
                print("prof")
                arbol = arbol_nuevo
                idn = contar_nodos(arbol)
                dibujar_arbol()
                if meta:
                    print("¡Meta alcanzada!")
                    break
            terminar = False
            while not terminar:
                arbol_nuevo, meta = amplitud(arbol_actual,idn)
                print("ampl")
                arbol = arbol_nuevo
                idn = contar_nodos(arbol)
                dibujar_arbol()
                terminar = hojas_misma_profundidad(arbol)
                if meta:
                    break
        #profundidad iterativa
        elif control == 5:
            print("iterativa")
            for i in range(0, limite ):
                arbol_nuevo, meta = preferente_por_profundidad(arbol_actual,idn)
                print("prof")
                arbol = arbol_nuevo
                idn = contar_nodos(arbol)
                dibujar_arbol()
                terminar = False
                while not terminar:
                    arbol_nuevo, meta = amplitud(arbol_actual,idn)
                    print("ampl")
                    arbol = arbol_nuevo
                    idn = contar_nodos(arbol)
                    dibujar_arbol()
                    terminar = hojas_misma_profundidad(arbol)
                    if meta:
                        break
                if meta:
                    print("¡Meta alcanzada!")
                    break
            
        
                
            
            
        arbol = arbol_nuevo

        # Sobrescribir el árbol anterior con el nuevo
        

        # Si se alcanzó la meta, salir del bucle
        if meta:
            print("¡Meta alcanzada!")
            break
        # Si se agotaron los controles y no se alcanzó la meta
    if not meta:
        print("No se alcanzó la meta y no quedan estrategias disponibles.")

# Ejecutar la expansión del árbol
ejecutar_expansion()
### dibujar_arbol(arbol, arbol_nuevo)
### organizar la funcion dibujar arbol para el color, tenemos el arbol viejo y el arbol nuevo.