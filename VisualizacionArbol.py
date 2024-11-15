import networkx as nx
import matplotlib.pyplot as plt
import time

class VisualizacionArbol:
    def __init__(self):
        self.grafo = nx.DiGraph()
        self.posiciones = {}
        self.nivel = {}
        self.nodos_unicos = {}
        self.fig, self.ax = plt.subplots(figsize=(12, 8))
        self.separacion_nivel = 2
        self.espacio_hojas = 2
        self.pos_x = 0

    def agregar_nodo(self, nodo, padre=None):
        # Crear un identificador único interno para cada nodo
        if nodo not in self.nodos_unicos:
            self.nodos_unicos[nodo] = []
        nodo_real = (nodo[0], nodo[1], len(self.nodos_unicos[nodo]))
        self.nodos_unicos[nodo].append(nodo_real)
        self.grafo.add_node(nodo_real, label=str(nodo))

        if padre is not None:
            padre_real = [n for n in self.nodos_unicos.get(padre, [])]
            if not padre_real:
                raise KeyError(f"El nodo padre {padre} no existe en el grafo.")
            padre_real = padre_real[-1]
            self.grafo.add_edge(padre_real, nodo_real)
            self.nivel[nodo_real] = self.nivel[padre_real] + 1
        else:
            self.nivel[nodo_real] = 0  # Nodo raíz

    def _calcular_posiciones(self):
        self.pos_x = 0
        nodos_ordenados = list(nx.topological_sort(self.grafo))

        # Primera pasada: asignar posiciones a las hojas
        for nodo in nodos_ordenados:
            hijos = list(self.grafo.successors(nodo))
            if not hijos:  # Nodo hoja
                self.posiciones[nodo] = (self.pos_x, -self.nivel[nodo] * self.separacion_nivel)
                self.pos_x += self.espacio_hojas

        # Segunda pasada: calcular posiciones de nodos internos
        for nodo in reversed(nodos_ordenados):
            hijos = list(self.grafo.successors(nodo))
            if hijos:  # Nodo interno
                if all(hijo in self.posiciones for hijo in hijos):
                    x_min = min(self.posiciones[hijo][0] for hijo in hijos)
                    x_max = max(self.posiciones[hijo][0] for hijo in hijos)
                    self.posiciones[nodo] = ((x_min + x_max) / 2, -self.nivel[nodo] * self.separacion_nivel)
                else:
                    raise KeyError(f"No todos los hijos del nodo {nodo} tienen posición calculada.")

    def _dibujar_grafico(self):
        self.ax.clear()
        labels = nx.get_node_attributes(self.grafo, 'label')
        nx.draw(
            self.grafo,
            pos=self.posiciones,
            labels=labels,
            with_labels=True,
            node_size=2000,
            node_color="lightblue",
            edgecolors="black",
            font_size=10,
            font_weight="bold",
            arrows=True,
            arrowsize=15,
            ax=self.ax
        )
        self.ax.set_title("Representación del Árbol", fontsize=14)
        plt.draw()
        plt.pause(0.001)

    def finalizar(self):
        self._calcular_posiciones()
        self._dibujar_grafico()
        plt.show()


# Prueba del árbol con nodos repetidos
visualizador = VisualizacionArbol()
visualizador.agregar_nodo((0, 2))  # Nodo raíz
visualizador.agregar_nodo((0,1), (0,2))  # Primer hijo
visualizador.agregar_nodo((0,3), (0,2))  # Segundo hijo
visualizador.agregar_nodo((1,3), (0,1))  # Hijo del nodo (0, 1)
visualizador.agregar_nodo((1,0), (0,3))  # Hijo del nodo (0, 3)
visualizador.agregar_nodo((2,3), (0,3))  # Hijo del nodo (0, 3)
visualizador.agregar_nodo((2,0), (1,0))  # Hijo del nodo (1, 0)
visualizador.agregar_nodo((2,2), (1,0))  # Hijo del nodo (1, 0)
visualizador.agregar_nodo((3,0), (2,2))  # Hijo del nodo (2, 2)
visualizador.agregar_nodo((1,3), (2,3))  # Repetición del nodo (1, 3) como hijo de (0, 1)
visualizador.agregar_nodo((3,2), (2,2))  # Hijo repetido del nodo (2, 2)
visualizador.agregar_nodo((3,1), (2,0))  # Hijo del nodo (2, 0)
visualizador.agregar_nodo((1,3), (2,3))  # Repetición del nodo (1, 3) como hijo del nodo (2, 3)
visualizador.agregar_nodo((3,1), (1,3))  # Hijo del nodo (3, 2)

visualizador.finalizar()
