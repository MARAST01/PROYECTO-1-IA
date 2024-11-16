import networkx as nx
import matplotlib.pyplot as plt
#from CostoUniforme import costo_uniforme

class Nodo:
    def __init__(self, valor, id,costo):
        self.valor = valor
        self.id = id  # Atributo único
        self.costo = costo  # Costo asociado al nodo
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)
"""
# Crear el árbol (ahora con id en cada nodo)
raiz = Nodo("A", 1)  # Nivel 0

# Nivel 1
nodo_b = Nodo("B", 2)
nodo_c = Nodo("C", 3)
nodo_d = Nodo("D", 4)
nodo_e = Nodo("E", 5)

# Nivel 2 (hijos de B, máximo 4 hijos)
nodo_f = Nodo("F", 6)
nodo_g = Nodo("G", 7)
nodo_h = Nodo("A", 8)
nodo_i = Nodo("I", 9)

# Nivel 2 (hijos de C)
nodo_j = Nodo("J", 10)
nodo_k = Nodo("A", 11)
nodo_l = Nodo("L", 12)
nodo_m = Nodo("M", 13)

# Nivel 3 (hijos de F)
nodo_n = Nodo("N", 14)
nodo_o = Nodo("A", 15)

# Nivel 3 (hijos de G)
nodo_p = Nodo("A", 16)

# Nivel 3 (hijos de H)
nodo_q = Nodo("Q", 17)
nodo_r = Nodo("M", 18)

# Nivel 4 (hijos de P)
nodo_s = Nodo("S", 19)

# Construcción del árbol
raiz.agregar_hijo(nodo_b)
raiz.agregar_hijo(nodo_c)
raiz.agregar_hijo(nodo_d)
raiz.agregar_hijo(nodo_e)

nodo_b.agregar_hijo(nodo_f)
nodo_b.agregar_hijo(nodo_g)
nodo_b.agregar_hijo(nodo_h)
nodo_b.agregar_hijo(nodo_i)

nodo_c.agregar_hijo(nodo_j)
nodo_c.agregar_hijo(nodo_k)
nodo_c.agregar_hijo(nodo_l)
nodo_c.agregar_hijo(nodo_m)

nodo_f.agregar_hijo(nodo_n)
nodo_f.agregar_hijo(nodo_o)

nodo_g.agregar_hijo(nodo_p)

nodo_h.agregar_hijo(nodo_q)
nodo_h.agregar_hijo(nodo_r)

nodo_p.agregar_hijo(nodo_s)
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


raiz = Nodo("(0,2)", 1,0)  
arbol = costo_uniforme(raiz)
# Asignar posiciones a los nodos comenzando desde la raíz
pos = {}
agregar_aristas(arbol)
asignar_posiciones(arbol, pos)
"""
asignar_posiciones(raiz, pos)

"""

# Dibujar el grafo con posiciones jerárquicas
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_size=1000, node_color="skyblue", font_size=10, font_weight="bold", arrows=True)
plt.title("Árbol Jerárquico Representado con NetworkX")
plt.show()
