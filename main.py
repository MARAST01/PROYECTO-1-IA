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





#GRAFOOOO
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


    
def asignar_posiciones(nodo, pos, colores, x=0, y=0, layer=1):
    """
    Asigna posiciones jerárquicas a los nodos de un árbol y crea un diccionario de colores.
    
    :param nodo: Nodo actual que se está procesando.
    :param pos: Diccionario para almacenar las posiciones de los nodos.
    :param colores: Diccionario para almacenar los colores de los nodos.
    :param x: Coordenada X del nodo actual.
    :param y: Coordenada Y del nodo actual.
    :param layer: Capa (nivel) del nodo actual en el árbol.
    """
    # Formatear el nombre del nodo para usarlo como clave en las posiciones y colores
    nodo_key = f"{nodo.valor}\n{nodo.heuristica}\n({nodo.id})"
    pos[nodo_key] = (x, y)

    # Asignar color inicial (skyblue) a todos los nodos
    colores[nodo_key] = "skyblue"

    # Factor de espaciado horizontal basado en el número de hijos
    numhijos = len(nodo.hijos)
    factor = [[0], [-0.5, 0.5], [-1, 0, 1], [-1, -0.3, 0.3, 1]]

    for i, hijo in enumerate(nodo.hijos):
        y1 = (y - 1) * -1  # Invertir para mantener lógica visual
        x1 = x + (factor[numhijos - 1][i]) / (y1 * y1)  # Calcular la posición del hijo
        asignar_posiciones(hijo, pos, colores, x1, y - 1, layer + 1)

    # Al final de la asignación, identificar el nodo con el ID más grande
    max_id = max(int(key.split("(")[-1].strip(")")) for key in colores.keys())
    for key in colores.keys():
        if f"({max_id})" in key:
            colores[key] = "turquoise"  # Pintar de verde el nodo con el ID más grande

        
def dibujar_arbol(titulo):
    """
    Dibuja el árbol con sus nodos y aristas, mostrando las posiciones jerárquicas.
    
    :param titulo: Título a mostrar en la ventana del gráfico.
    """
    # Asignar posiciones a los nodos comenzando desde la raíz
    pos = {}
    colores = {}  # Diccionario para almacenar colores de los nodos

    agregar_aristas(arbol)
    asignar_posiciones(arbol, pos, colores)  # Pasar también el diccionario de colores

    # Coordenadas del nodo raíz (asumimos que el nodo raíz está en 0,0)
    raiz = list(pos.keys())[0]  # Suponiendo que el primer nodo en `pos` es la raíz
    x_raiz, y_raiz = pos[raiz]

    # Dibujar el grafo con posiciones jerárquicas
    plt.figure(figsize=(8, 6))
    
    nx.draw(
        G, pos, with_labels=True,
        node_size=1000, node_color=[colores[nodo] for nodo in G.nodes],  # Usar los colores del diccionario
        font_size=10, font_weight="bold", arrows=True
    )

    # Agregar el título 4 unidades arriba del nodo raíz
    plt.text(x_raiz, y_raiz - 1, titulo, fontsize=12, ha='center', va='center', fontweight='bold')

    # Mostrar el gráfico
    plt.show()



# Inicializar la variable meta como False
meta = False

idn = 1  # ID para los nodos
limite = 2  # Límite de profundidad para la búsqueda limitada
numero_expansion = 2
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
    controles_disponibles = [0, 1, 2, 3, 4, 5]
    


    # Mientras no se alcance la meta (queso), seguir expandiendo el árbol
    while not meta and controles_disponibles:
        # Control aleatorio para decidir qué estrategia usar
        #control = 1 # Esto puede ser ajustado si decides incorporar aleatoriedad
        #control = random.randint(0, 1)
        control = random.choice(controles_disponibles)
        #control = controles_disponibles[0]
        controles_disponibles.remove(control)

        # Variable para guardar el árbol actual y el nuevo árbol
        arbol_actual = arbol
        arbol_nuevo = None

        if control == 0:
            for i in range(0,numero_expansion):
                arbol_nuevo, meta = costo_uniforme(arbol_actual,idn)  # Expande el árbol una ve
                print ("costo uniforme")
                dibujar_arbol("costo uniforme")
                idn = contar_nodos(arbol)
        elif control == 1:
            for i in range(0,numero_expansion):
                arbol_nuevo, meta = preferente_por_profundidad(arbol_actual,idn)
                print("profundidad")
                dibujar_arbol("profundidad")
                idn = contar_nodos(arbol)
        elif control == 2:
            for i in range(0,numero_expansion):
                arbol_nuevo, meta = busqueda_avara(arbol_actual,idn)
                print("avara")
                dibujar_arbol("avara")
                idn = contar_nodos(arbol)
        elif control == 3:
            for i in range(0,numero_expansion):
                arbol_nuevo, meta = amplitud(arbol_actual,idn)
                print("amplitud")
                dibujar_arbol("amplitud")
                idn = contar_nodos(arbol)
        #limitada por profundidad
        elif control == 4:
            for i in range(0,numero_expansion):
                arbol_nuevo, meta = profundidad_limitada(arbol_actual,limite,idn)
                print("limitada")
                dibujar_arbol("limitada por profundidad")
                idn = contar_nodos(arbol)
        #profundidad iterativa
        elif control == 5:
            limite_iter = limite
            for i in range(0,numero_expansion):
                arbol_nuevo, meta = profundidad_limitada(arbol_actual,limite_iter,idn)
                print("iterativa")
                dibujar_arbol("profundizacion iterativa")
                idn = contar_nodos(arbol)
                limite_iter+=1
               
        arbol = arbol_nuevo        

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